import json
import logging
from typing import (
    Any, 
    Dict, 
    List, 
    Optional, 
    Type, 
    TypeVar, 
    Union, 
    Generator,
    AsyncGenerator,
    cast,
    Generic,
    Literal
)
from pydantic import BaseModel

from ..utils import clean_params, extract_items_from_response

T = TypeVar("T", bound="LitecardResource")
ModelT = TypeVar("ModelT", bound=BaseModel)

logger = logging.getLogger(__name__)

class PaginatedResponse(Generic[T]):
    """
    Generic container for paginated API responses from Litecard.
    
    Supports both offset/limit and cursor-based pagination.
    """
    
    def __init__(self, 
                items: List[T], 
                # Offset/limit pagination
                offset: Optional[int] = None,
                limit: Optional[int] = None,
                total_count: Optional[int] = None,
                # Cursor-based pagination  
                next_cursor: Optional[str] = None,
                previous_cursor: Optional[str] = None,
                has_more: bool = False):
        self.items = items
        # Offset/limit pagination
        self.offset = offset
        self.limit = limit
        self.total_count = total_count
        # Cursor-based pagination
        self.next_cursor = next_cursor
        self.previous_cursor = previous_cursor
        self.has_more = has_more
        
    def __len__(self) -> int:
        return len(self.items)
        
    def __iter__(self):
        return iter(self.items)
        
    def __getitem__(self, index):
        return self.items[index]
    
    @property
    def next_offset(self) -> Optional[int]:
        """Get the next offset for offset-based pagination."""
        if self.offset is not None and self.limit is not None and self.has_more:
            return self.offset + self.limit
        return None
    
    @property
    def previous_offset(self) -> Optional[int]:
        """Get the previous offset for offset-based pagination."""
        if self.offset is not None and self.limit is not None and self.offset > 0:
            return max(0, self.offset - self.limit)
        return None


class LitecardResource:
    """
    Base class for all Litecard API resources.
    
    This class represents both individual resources and collections of resources.
    When initialized with data, it represents a specific resource instance.
    When used without data, it represents the collection.
    """
    
    endpoint: str = ""
    model_class: Optional[Type[BaseModel]] = None
    
    def __init__(
        self,
        *,
        client: Any,  # LitecardClient or LitecardAsyncClient
        data: Optional[Dict[str, Any]] = None,
        parent: Optional["LitecardResource"] = None,
        parent_path: Optional[str] = None,
    ) -> None:
        self._client = client
        self._data: Dict[str, Any] = data or {}
        self._parent = parent
        self._parent_path = parent_path
        self._model: Optional[BaseModel] = None
        
        # Initialize model if data and model_class are provided
        if data and self.model_class:
            try:
                self._model = self.model_class(**data)
            except Exception:
                # If model creation fails, continue without it
                pass
    
    def __getattr__(self, name: str) -> Any:
        # First try to get from the model
        if self._model and hasattr(self._model, name):
            return getattr(self._model, name)
            
        # Then try to get from the data dictionary
        if name in self._data:
            return self._data[name]
            
        raise AttributeError(f"'{self.__class__.__name__}' has no attribute '{name}'")
        
    def __repr__(self) -> str:
        identifier = self.get_identifier()
        if identifier:
            return f"<{self.__class__.__name__} {identifier}>"
        return f"<{self.__class__.__name__} collection>"
    
    def get_identifier(self) -> Optional[str]:
        """Get the identifier for this resource."""
        # Try common identifier fields
        for field in ['id', 'uuid', 'resource_id', 'identifier']:
            value = self._data.get(field)
            if value:
                return str(value)
        return None
        
    def is_instance(self) -> bool:
        """Check if this represents a specific resource instance (vs collection manager)."""
        return bool(self._data and self.get_identifier())
        
    def _validate_data(self) -> bool:
        """Debugging function, to check if data is valid, against its assigned model class"""
        if self._data and self.model_class:
            try:
                self.model_class(**self._data)
                return True
            except Exception as e:
                logger.info(f"Data validation failed: {e}", exc_info=e)
                return False
        return False
        
    def _require_instance(self) -> str:
        """Ensure this is a resource instance and return its identifier."""
        if not self.is_instance():
            raise ValueError(f"This method requires a {self.__class__.__name__} instance, not a collection manager")
        identifier = self.get_identifier()
        if not identifier:
            raise ValueError(f"Could not determine identifier for {self.__class__.__name__} instance")
        return identifier
        
    @classmethod
    def get_endpoint(cls) -> str:
        """Get the API endpoint for this resource."""
        return cls.endpoint
        
    def _build_url(self, resource_id: Optional[str] = None, suffix: str = "") -> str:
        """Build a URL path for this resource."""
        if self._parent_path:
            base = f"{self._parent_path}/{self.get_endpoint()}"
        else:
            base = f"/v1/{self.get_endpoint()}"
            
        url = base
        if resource_id is not None:
            url = f"{url}/{resource_id}"
        if suffix:
            url = f"{url}/{suffix}"
            
        return url
        
    def _prepare_request_params(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """Prepare parameters for an API request."""
        return clean_params(params)
        
    def _prepare_request_data(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Convert data for an API request."""
        if hasattr(data, "model_dump") and isinstance(data, BaseModel):
            # It's a Pydantic model
            return data.model_dump(by_alias=True, exclude_none=True)
        return data

    def _create_instance(self: T, data: Dict[str, Any], instance_cls: Optional[Type[T]] = None) -> T:
        """Create a new instance of this resource with the given data."""
        instance_cls = instance_cls or self.__class__
        return instance_cls(client=self._client, data=data, parent_path=self._parent_path)

    def _extract_pagination_data(self, response: Union[List[Dict[str, Any]], Dict[str, Any]], params: Dict[str, Any]) -> Dict[str, Any]:
        """Extract pagination information from a response."""
        pagination_data = {}
        
        # Handle offset/limit pagination
        if 'offset' in params or 'limit' in params:
            pagination_data['offset'] = params.get('offset', 0)
            pagination_data['limit'] = params.get('limit', 50)
            
            if isinstance(response, dict):
                pagination_data['total_count'] = response.get('total_count') or response.get('total')
                items_count = len(extract_items_from_response(response))
                pagination_data['has_more'] = items_count >= pagination_data['limit']
            else:
                pagination_data['total_count'] = len(response)
                pagination_data['has_more'] = len(response) >= pagination_data['limit']
        
        # Handle cursor-based pagination
        if isinstance(response, dict):
            if 'next_cursor' in response:
                pagination_data['next_cursor'] = response['next_cursor']
            if 'previous_cursor' in response:
                pagination_data['previous_cursor'] = response['previous_cursor']
            if 'has_more' in response:
                pagination_data['has_more'] = response['has_more']
        
        return pagination_data
        
    def _extract_items(self, response: Any) -> List[Dict[str, Any]]:
        """Extract items from a response."""
        return extract_items_from_response(response)
        
    def to_dict(self, mode: Literal['json', 'python'] = 'python') -> Dict[str, Any]:
        """Convert the resource instance to a dictionary."""
        if self._model:
            return self._model.model_dump(mode=mode, by_alias=True, exclude_none=False)
        return self._data.copy()
        
    # Synchronous methods
    
    def __call__(self: T, resource_id: Optional[str] = None, **params) -> Union[T, List[T], PaginatedResponse[T]]:
        """
        If a resource_id is provided, fetch a single resource by ID.
        Otherwise, list resources based on the provided parameters.
        """
        if resource_id is not None:
            return self.get(resource_id)
        return self.list(**params)
        
    def get(self: T, resource_id: str) -> T:
        """Get a single resource by ID."""
        if not hasattr(self._client, '_make_request_sync'):
            raise TypeError("This method requires a synchronous client")
        
        url = self._build_url(resource_id)
        response = self._client._make_request_sync("GET", url)
        
        return self._create_instance(response)
        
    def list(
        self: T,
        url: Optional[str] = None,
        paginated: bool = False,
        **params
    ) -> Union[List[T], PaginatedResponse[T]]:
        """
        List resources matching the given parameters.
        
        Args:
            paginated: If True, return a PaginatedResponse object instead of a list
            **params: Filter parameters for the request (offset, limit, cursor, etc.)
        
        Returns:
            Either a list of resource instances or a PaginatedResponse object
        """
        if not hasattr(self._client, '_make_request_sync'):
            raise TypeError("This method requires a synchronous client")
            
        url = url or self._build_url()
        prepared_params = self._prepare_request_params(params)
        response = self._client._make_request_sync("GET", url, params=prepared_params)
        
        # Extract items and pagination data
        items = self._extract_items(response)
        instances = [self._create_instance(item) for item in items]
        
        if paginated:
            pagination_data = self._extract_pagination_data(response, prepared_params)
            return PaginatedResponse(
                items=instances,
                offset=pagination_data.get('offset'),
                limit=pagination_data.get('limit'),
                total_count=pagination_data.get('total_count'),
                next_cursor=pagination_data.get('next_cursor'),
                previous_cursor=pagination_data.get('previous_cursor'),
                has_more=pagination_data.get('has_more', False)
            )
        
        return instances
        
    def create(self: T, data: Dict[str, Any]) -> T:
        """Create a new resource."""
        if not hasattr(self._client, '_make_request_sync'):
            raise TypeError("This method requires a synchronous client")
            
        url = self._build_url()
        prepared_data = self._prepare_request_data(data)
        response = self._client._make_request_sync("POST", url, json_data=prepared_data)
        
        return self._create_instance(response)
        
    def update(self: T, resource_id: str, data: Dict[str, Any]) -> T:
        """Update an existing resource."""
        if not hasattr(self._client, '_make_request_sync'):
            raise TypeError("This method requires a synchronous client")
            
        url = self._build_url(resource_id)
        prepared_data = self._prepare_request_data(data)
        response = self._client._make_request_sync("PUT", url, json_data=prepared_data)
        
        # Litecard typically returns the updated resource
        return self._create_instance(response)
        
    def delete(self, resource_id: str) -> None:
        """Delete a resource."""
        if not hasattr(self._client, '_make_request_sync'):
            raise TypeError("This method requires a synchronous client")
            
        url = self._build_url(resource_id)
        self._client._make_request_sync("DELETE", url)

    def paginate(self: T, url: Optional[str] = None, **params) -> Generator[T, None, None]:
        """
        Generator that yields all resources matching the given parameters.
        
        Supports both offset/limit and cursor-based pagination.
        
        Args:
            **params: Filter parameters for the request
            
        Yields:
            Resource instances one at a time
        """
        if not hasattr(self._client, '_make_request_sync'):
            raise TypeError("This method requires a synchronous client")
        
        # Determine pagination type
        use_cursor = 'cursor' in params
        
        if use_cursor:
            # Cursor-based pagination
            cursor = params.get('cursor')
            while True:
                if cursor:
                    params['cursor'] = cursor
                
                page_response = self.list(url=url, paginated=True, **params)
                
                if not isinstance(page_response, PaginatedResponse):
                    raise TypeError(f"Expected PaginatedResponse, got {type(page_response)}")
                
                if not page_response.items:
                    break
                    
                for item in page_response.items:
                    yield item
                    
                if not page_response.has_more or not page_response.next_cursor:
                    break
                    
                cursor = page_response.next_cursor
        else:
            # Offset/limit pagination
            offset = params.get("offset", 0)
            limit = params.get("limit", 50)
            
            while True:
                params["offset"] = offset
                params["limit"] = limit
                
                page_response = self.list(url=url, paginated=True, **params)
                
                if not isinstance(page_response, PaginatedResponse):
                    raise TypeError(f"Expected PaginatedResponse, got {type(page_response)}")
                
                if not page_response.items:
                    break
                    
                for item in page_response.items:
                    yield item
                    
                if not page_response.has_more:
                    break
                    
                offset += limit
        
    # Asynchronous methods
    
    async def get_async(self: T, resource_id: str) -> T:
        """Get a single resource by ID asynchronously."""
        if not hasattr(self._client, '_make_request_async'):
            raise TypeError("This method requires an asynchronous client")
        
        url = self._build_url(resource_id)
        response = await self._client._make_request_async("GET", url)
        
        return self._create_instance(response)

    async def list_async(
        self: T, 
        url: Optional[str] = None,
        paginated: bool = False, 
        **params
    ) -> Union[List[T], PaginatedResponse[T]]:
        """
        List resources matching the given parameters asynchronously.
        
        Args:
            paginated: If True, return a PaginatedResponse object instead of a list
            **params: Filter parameters for the request
        
        Returns:
            Either a list of resource instances or a PaginatedResponse object
        """
        if not hasattr(self._client, '_make_request_async'):
            raise TypeError("This method requires an asynchronous client")

        url = url or self._build_url()
        prepared_params = self._prepare_request_params(params)
        response = await self._client._make_request_async("GET", url, params=prepared_params)
        
        # Extract items and pagination data
        items = self._extract_items(response)
        instances = [self._create_instance(item) for item in items]
        
        if paginated:
            pagination_data = self._extract_pagination_data(response, prepared_params)
            return PaginatedResponse(
                items=instances,
                offset=pagination_data.get('offset'),
                limit=pagination_data.get('limit'),
                total_count=pagination_data.get('total_count'),
                next_cursor=pagination_data.get('next_cursor'),
                previous_cursor=pagination_data.get('previous_cursor'),
                has_more=pagination_data.get('has_more', False)
            )
        
        return instances
        
    async def create_async(self: T, data: Dict[str, Any]) -> T:
        """Create a new resource asynchronously."""
        if not hasattr(self._client, '_make_request_async'):
            raise TypeError("This method requires an asynchronous client")
            
        url = self._build_url()
        prepared_data = self._prepare_request_data(data)
        response = await self._client._make_request_async("POST", url, json_data=prepared_data)
        
        return self._create_instance(response)
        
    async def update_async(self: T, resource_id: str, data: Dict[str, Any]) -> T:
        """Update an existing resource asynchronously."""
        if not hasattr(self._client, '_make_request_async'):
            raise TypeError("This method requires an asynchronous client")
            
        url = self._build_url(resource_id)
        prepared_data = self._prepare_request_data(data)
        response = await self._client._make_request_async("PUT", url, json_data=prepared_data)
        
        return self._create_instance(response)
        
    async def delete_async(self, resource_id: str) -> None:
        """Delete a resource asynchronously."""
        if not hasattr(self._client, '_make_request_async'):
            raise TypeError("This method requires an asynchronous client")
            
        url = self._build_url(resource_id)
        await self._client._make_request_async("DELETE", url)

    async def paginate_async(self: T, url: Optional[str] = None, **params) -> AsyncGenerator[T, None]:
        """
        Async generator that yields all resources matching the given parameters.
        
        Supports both offset/limit and cursor-based pagination.
        
        Args:
            **params: Filter parameters for the request
            
        Yields:
            Resource instances one at a time
        """
        if not hasattr(self._client, '_make_request_async'):
            raise TypeError("This method requires an asynchronous client")
        
        # Determine pagination type
        use_cursor = 'cursor' in params
        
        if use_cursor:
            # Cursor-based pagination
            cursor = params.get('cursor')
            while True:
                if cursor:
                    params['cursor'] = cursor
                
                page_response = await self.list_async(url=url, paginated=True, **params)
                
                if not isinstance(page_response, PaginatedResponse):
                    raise TypeError(f"Expected PaginatedResponse, got {type(page_response)}")
                
                if not page_response.items:
                    break
                    
                for item in page_response.items:
                    yield item
                    
                if not page_response.has_more or not page_response.next_cursor:
                    break
                    
                cursor = page_response.next_cursor
        else:
            # Offset/limit pagination
            offset = params.get("offset", 0)
            limit = params.get("limit", 50)
            
            while True:
                params["offset"] = offset
                params["limit"] = limit

                page_response = await self.list_async(url=url, paginated=True, **params)

                if not isinstance(page_response, PaginatedResponse):
                    raise TypeError(f"Expected PaginatedResponse, got {type(page_response)}")

                if not page_response.items:
                    break
                    
                for item in page_response.items:
                    yield item
                    
                if not page_response.has_more:
                    break
                    
                offset += limit
