"""
Card resource for the Litecard API.
"""

from typing import Dict, Any, List, Union, Optional
from .base import LitecardResource, PaginatedResponse
from ..models_ import (
    Card as CardModel,
    CardStatus,
    PrivateSignUpRequest,
    SignUpResponse,
    SignUpOptions,
    BaseCardPayload,
    TemplateOverridesV1,
)
from ..request_types import (
    CreateCardRequest,
    UpdateCardRequest,
    SetCardStatusRequest,
    CreateCardAndTemplateRequest,
    GenerateBusinessCardRequest,
    SuccessResponse,
    CardQueryParams,
)


class Card(LitecardResource):
    """
    Card resource for managing digital wallet cards.
    """
    
    endpoint = "card"
    model_class = CardModel
    
    def create_card(
        self,
        template_id: str,
        card_payload: BaseCardPayload,
        tier: Optional[str] = None,
        options: Optional[SignUpOptions] = None,
        template_overrides: Optional[TemplateOverridesV1] = None
    ) -> SignUpResponse:
        """
        Create a new card.
        
        Args:
            template_id: ID of the template to use
            card_payload: Card data (email, phone, custom fields, etc.)
            tier: Optional tier for multi-tiered templates
            options: Optional card creation options (e.g., emailInvitationEnabled=True)
            template_overrides: Optional template overrides for custom locations, images, etc.
            
        Returns:
            Card creation response with card details
            
        Example:
            ```python
            from litecard.models_ import BaseCardPayload, SignUpOptions
            
            # Create card payload
            card_payload = BaseCardPayload(
                email="user@example.com",
                phone="+1234567890",
                firstName="John",
                lastName="Doe"
            )
            
            # Create options
            options = SignUpOptions(
                emailInvitationEnabled=True,
                smsInvitationEnabled=False
            )
            
            # Create card
            response = card_resource.create_card(
                template_id="template_123",
                card_payload=card_payload,
                options=options
            )
            ```
        """
        if not hasattr(self._client, '_make_request_sync'):
            raise TypeError("This method requires a synchronous client")
        
        request_data: CreateCardRequest = {
            "templateId": template_id,
            "cardPayload": card_payload.model_dump(exclude_none=True)
        }
        
        if options:
            request_data["options"] = options.model_dump(exclude_none=True)
        
        if tier:
            request_data["tier"] = tier
            
        if template_overrides:
            request_data["templateOverrides"] = template_overrides.model_dump(exclude_none=True)

        response = self._client._make_request_sync(
            "POST",
            self._build_url(),
            json_data=request_data
        )
        
        return SignUpResponse(**response)
    
    def update_card(
        self, 
        card_id: str,
        card_payload: Optional[BaseCardPayload] = None,
        sync_static_fields: Optional[bool] = None,
        tier: Optional[str] = None,
        template_overrides: Optional[TemplateOverridesV1] = None
    ) -> SuccessResponse:
        """
        Update an existing card.
        
        Args:
            card_id: Card ID to update
            card_payload: Updated card data (optional)
            sync_static_fields: Flag to sync static fields
            tier: Optional tier for multi-tiered templates
            template_overrides: Optional template overrides for custom locations, images, etc.
            
        Returns:
            Update response
            
        Example:
            ```python
            from litecard.models_ import BaseCardPayload
            
            # Update card data
            updated_payload = BaseCardPayload(
                email="newemail@example.com",
                phone="+0987654321"
            )
            
            response = card_resource.update_card(
                card_id="card_123",
                card_payload=updated_payload,
                sync_static_fields=True
            )
            ```
        """
        if not hasattr(self._client, '_make_request_sync'):
            raise TypeError("This method requires a synchronous client")
        
        request_data: UpdateCardRequest = {
            "cardId": card_id
        }
        
        if card_payload:
            request_data["cardPayload"] = card_payload.model_dump(exclude_none=True)
        
        if sync_static_fields is not None:
            request_data["syncStaticFields"] = sync_static_fields
        
        if tier:
            request_data["tier"] = tier
            
        if template_overrides:
            request_data["templateOverrides"] = template_overrides.model_dump(exclude_none=True)
        
        response = self._client._make_request_sync(
            "PATCH",
            self._build_url(),
            json_data=request_data
        )
        
        return response
    
    def set_card_status(
        self, 
        card_id: str, 
        status: CardStatus
    ) -> SuccessResponse:
        """
        Set card status (ACTIVE, INACTIVE, DELETED).
        
        Args:
            card_id: Card ID
            status: New status from CardStatus enum
            
        Returns:
            Success response
            
        Example:
            ```python
            from litecard.models_ import CardStatus
            
            response = card_resource.set_card_status(
                card_id="card_123",
                status=CardStatus.INACTIVE
            )
            ```
        """
        if not hasattr(self._client, '_make_request_sync'):
            raise TypeError("This method requires a synchronous client")
        
        request_data: SetCardStatusRequest = {
            "cardId": card_id, 
            "status": status.value
        }
        
        url = self._build_url(suffix="status")
        response = self._client._make_request_sync(
            "POST",
            url,
            json_data=request_data
        )
        
        return response
    
    def get_card(self, card_id: str) -> CardModel:
        """
        Get a card by ID.
        
        Args:
            card_id: Card ID
            
        Returns:
            Card instance
        """
        return self.get(card_id)
    
    def list_cards_by_template(
        self,
        template_id: str,
        limit: int = 10,
        next_token: Optional[str] = None,
        paginated: bool = False
    ) -> Union[List[CardModel], PaginatedResponse[CardModel]]:
        """
        Get cards by template ID.
        
        Args:
            template_id: Template ID
            limit: Maximum number of cards to return
            next_token: Token for pagination
            paginated: Return PaginatedResponse instead of list
            
        Returns:
            List of cards or paginated response
            
        Example:
            ```python
            # Get first 20 cards for a template
            cards = card_resource.list_cards_by_template(
                template_id="template_123",
                limit=20
            )
            
            # Get paginated response
            paginated_cards = card_resource.list_cards_by_template(
                template_id="template_123",
                limit=10,
                paginated=True
            )
            ```
        """
        if not hasattr(self._client, '_make_request_sync'):
            raise TypeError("This method requires a synchronous client")
        
        params: CardQueryParams = {"templateId": template_id}
        if limit is not None:
            params["limit"] = limit
        if next_token:
            params["next"] = next_token
        
        url = f"/api/v1/card/template/{template_id}"
        return self.list(url=url, paginated=paginated, **params)
    
    def create_card_and_template(
        self,
        template_payload: Dict[str, Any],
        card_payload: BaseCardPayload,
        options: Optional[SignUpOptions] = None
    ) -> SignUpResponse:
        """
        Create both card and template in one request.
        
        Args:
            template_payload: Template configuration
            card_payload: Card data
            options: Optional card creation options
            
        Returns:
            Response with both template and card details
            
        Example:
            ```python
            from litecard.models_ import BaseCardPayload, SignUpOptions
            
            template_config = {
                "name": "My Template",
                "description": "Template description",
                "businessName": "My Business",
                # ... other template fields
            }
            
            card_data = BaseCardPayload(
                email="user@example.com",
                firstName="John",
                lastName="Doe"
            )
            
            response = card_resource.create_card_and_template(
                template_payload=template_config,
                card_payload=card_data
            )
            ```
        """
        if not hasattr(self._client, '_make_request_sync'):
            raise TypeError("This method requires a synchronous client")
        
        request_data: CreateCardAndTemplateRequest = {
            "templatePayload": template_payload,
            "cardPayload": card_payload.model_dump(exclude_none=True)
        }
        
        if options:
            request_data["options"] = options.model_dump(exclude_none=True)
        
        url = self._build_url(suffix="template")
        response = self._client._make_request_sync(
            "POST",
            url,
            json_data=request_data
        )
        
        return SignUpResponse(**response)
    
    def generate_business_card(
        self,
        template_id: str,
        card_payload: BaseCardPayload,
        business_card: Dict[str, Any],
        options: Optional[SignUpOptions] = None
    ) -> SignUpResponse:
        """
        Generate a business card.
        
        Args:
            template_id: Template ID
            card_payload: Card data
            business_card: Business card specific data
            options: Optional card creation options
            
        Returns:
            Card creation response
            
        Example:
            ```python
            from litecard.models_ import BaseCardPayload
            
            card_data = BaseCardPayload(
                email="john@company.com",
                firstName="John",
                lastName="Doe"
            )
            
            business_info = {
                "jobTitle": "Software Engineer",
                "company": "Tech Corp",
                "website": "https://techcorp.com"
            }
            
            response = card_resource.generate_business_card(
                template_id="template_123",
                card_payload=card_data,
                business_card=business_info
            )
            ```
        """
        if not hasattr(self._client, '_make_request_sync'):
            raise TypeError("This method requires a synchronous client")
        
        request_data: GenerateBusinessCardRequest = {
            "templateId": template_id,
            "cardPayload": card_payload.model_dump(exclude_none=True),
            "businessCard": business_card
        }
        
        if options:
            request_data["options"] = options.model_dump(exclude_none=True)
        
        url = "/api/v1/card/business"
        response = self._client._make_request_sync(
            "POST",
            url,
            json_data=request_data
        )
        
        return SignUpResponse(**response)
    
    # Async methods
    
    async def create_card_async(
        self,
        template_id: str,
        card_payload: BaseCardPayload,
        tier: Optional[str] = None,
        options: Optional[SignUpOptions] = None,
        template_overrides: Optional[TemplateOverridesV1] = None
    ) -> SignUpResponse:
        """
        Create a new card asynchronously.
        
        Args:
            template_id: ID of the template to use
            card_payload: Card data (email, phone, custom fields, etc.)
            tier: Optional tier for multi-tiered templates
            options: Optional card creation options
            template_overrides: Optional template overrides
            
        Returns:
            Card creation response with card details
        """
        if not hasattr(self._client, '_make_request_async'):
            raise TypeError("This method requires an asynchronous client")
        
        request_data: CreateCardRequest = {
            "templateId": template_id,
            "cardPayload": card_payload.model_dump(exclude_none=True)
        }
        
        if options:
            request_data["options"] = options.model_dump(exclude_none=True)
        
        if tier:
            request_data["tier"] = tier
            
        if template_overrides:
            request_data["templateOverrides"] = template_overrides.model_dump(exclude_none=True)
        
        response = await self._client._make_request_async(
            "POST",
            self._build_url(),
            json_data=request_data
        )
        
        return SignUpResponse(**response)
    
    async def update_card_async(
        self,
        card_id: str,
        card_payload: Optional[BaseCardPayload] = None,
        sync_static_fields: Optional[bool] = None,
        tier: Optional[str] = None,
        template_overrides: Optional[TemplateOverridesV1] = None
    ) -> SuccessResponse:
        """
        Update an existing card asynchronously.
        
        Args:
            card_id: Card ID to update
            card_payload: Updated card data (optional)
            sync_static_fields: Flag to sync static fields
            tier: Optional tier for multi-tiered templates
            template_overrides: Optional template overrides
            
        Returns:
            Update response
        """
        if not hasattr(self._client, '_make_request_async'):
            raise TypeError("This method requires an asynchronous client")
        
        request_data: UpdateCardRequest = {
            "cardId": card_id
        }
        
        if card_payload:
            request_data["cardPayload"] = card_payload.model_dump(exclude_none=True)
        
        if sync_static_fields is not None:
            request_data["syncStaticFields"] = sync_static_fields
        
        if tier:
            request_data["tier"] = tier
            
        if template_overrides:
            request_data["templateOverrides"] = template_overrides.model_dump(exclude_none=True)
        
        response = await self._client._make_request_async(
            "PATCH",
            self._build_url(),
            json_data=request_data
        )
        
        return response
    
    async def set_card_status_async(
        self, 
        card_id: str, 
        status: CardStatus
    ) -> SuccessResponse:
        """
        Set card status asynchronously.
        
        Args:
            card_id: Card ID
            status: New status from CardStatus enum
            
        Returns:
            Success response
        """
        if not hasattr(self._client, '_make_request_async'):
            raise TypeError("This method requires an asynchronous client")
        
        request_data: SetCardStatusRequest = {
            "cardId": card_id, 
            "status": status.value
        }
        
        url = self._build_url(suffix="status")
        response = await self._client._make_request_async(
            "POST",
            url,
            json_data=request_data
        )
        
        return response
    
    async def get_card_async(self, card_id: str) -> CardModel:
        """Get a card by ID asynchronously."""
        return await self.get_async(card_id)
    
    async def list_cards_by_template_async(
        self,
        template_id: str,
        limit: Optional[int] = None,
        next_token: Optional[str] = None,
        paginated: bool = False
    ) -> Union[List[CardModel], PaginatedResponse[CardModel]]:
        """Get cards by template ID asynchronously."""
        if not hasattr(self._client, '_make_request_async'):
            raise TypeError("This method requires an asynchronous client")
        
        params: CardQueryParams = {"templateId": template_id}
        if limit is not None:
            params["limit"] = limit
        if next_token:
            params["next"] = next_token
        
        url = f"/api/v1/card/template/{template_id}"
        return await self.list_async(url=url, paginated=paginated, **params)
    
    async def create_card_and_template_async(
        self,
        template_payload: Dict[str, Any],
        card_payload: BaseCardPayload,
        options: Optional[SignUpOptions] = None
    ) -> SignUpResponse:
        """Create both card and template in one request asynchronously."""
        if not hasattr(self._client, '_make_request_async'):
            raise TypeError("This method requires an asynchronous client")
        
        request_data: CreateCardAndTemplateRequest = {
            "templatePayload": template_payload,
            "cardPayload": card_payload.model_dump(exclude_none=True)
        }
        
        if options:
            request_data["options"] = options.model_dump(exclude_none=True)
        
        url = self._build_url(suffix="template")
        response = await self._client._make_request_async(
            "POST",
            url,
            json_data=request_data
        )
        
        return SignUpResponse(**response)
    
    async def generate_business_card_async(
        self,
        template_id: str,
        card_payload: BaseCardPayload,
        business_card: Dict[str, Any],
        options: Optional[SignUpOptions] = None
    ) -> SignUpResponse:
        """Generate a business card asynchronously."""
        if not hasattr(self._client, '_make_request_async'):
            raise TypeError("This method requires an asynchronous client")
        
        request_data: GenerateBusinessCardRequest = {
            "templateId": template_id,
            "cardPayload": card_payload.model_dump(exclude_none=True),
            "businessCard": business_card
        }
        
        if options:
            request_data["options"] = options.model_dump(exclude_none=True)
        
        url = "/api/v1/card/business"
        response = await self._client._make_request_async(
            "POST",
            url,
            json_data=request_data
        )
        
        return SignUpResponse(**response)
