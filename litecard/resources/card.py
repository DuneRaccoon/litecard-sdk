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


class Card(LitecardResource):
    """
    Card resource for managing digital wallet cards.
    """
    
    endpoint = "card"
    model_class = CardModel
    
    def create_card(
        self,
        template_id: str,
        card_payload,
        tier: Optional[str] = None,
        options = None,
        template_overrides = None
    ) -> SignUpResponse:
        """
        Create a new card.
        
        Args:
            template_id: ID of the template to use
            card_payload: Card data (email, phone, custom fields, etc.)
            options: Optional card creation options (e.g., {"emailInvitationEnabled": True})
            tier: Optional tier for multi-tiered templates
            template_overrides: Optional template overrides for custom locations, images, etc.
            
        Returns:
            Card creation response with card details
        """
        if not hasattr(self._client, '_make_request_sync'):
            raise TypeError("This method requires a synchronous client")
        
        if not isinstance(card_payload, BaseCardPayload):
            card_payload = BaseCardPayload(**card_payload)
            
        request_data = {
            "templateId": template_id,
            "cardPayload": card_payload.model_dump(exclude_none=True)
        }
        
        if options:
            if not isinstance(options, SignUpOptions):
                options = SignUpOptions(**options)
            request_data["options"] = options.model_dump(exclude_none=True)
        
        if tier:
            request_data["tier"] = tier
            
        if template_overrides:
            if not isinstance(template_overrides, TemplateOverridesV1):
                template_overrides = TemplateOverridesV1(**template_overrides)
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
        card_payload = None,
        sync_static_fields: Optional[bool] = None,
        tier: Optional[str] = None,
        template_overrides = None
    ) -> Dict[str, Any]:
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
        """
        if not hasattr(self._client, '_make_request_sync'):
            raise TypeError("This method requires a synchronous client")
        
        request_data = {
            "cardId": card_id
        }
        
        if card_payload:
            if not isinstance(card_payload, BaseCardPayload):
                card_payload = BaseCardPayload(**card_payload)
            request_data["cardPayload"] = card_payload.model_dump(exclude_none=True)
        
        if sync_static_fields is not None:
            request_data["syncStaticFields"] = sync_static_fields
        
        if tier:
            request_data["tier"] = tier
            
        if template_overrides:
            if not isinstance(template_overrides, TemplateOverridesV1):
                template_overrides = TemplateOverridesV1(**template_overrides)
            request_data["templateOverrides"] = template_overrides.model_dump(exclude_none=True)
        
        response = self._client._make_request_sync(
            "PATCH",
            self._build_url(),
            json_data=request_data
        )
        
        return response
    
    def set_card_status(self, card_id: str, status: CardStatus) -> Dict[str, Any]:
        """
        Set card status (ACTIVE, INACTIVE, DELETED).
        
        Args:
            card_id: Card ID
            status: New status
            
        Returns:
            Success response
        """
        if not hasattr(self._client, '_make_request_sync'):
            raise TypeError("This method requires a synchronous client")
        
        url = self._build_url(suffix="status")
        response = self._client._make_request_sync(
            "POST",
            url,
            json_data={"cardId": card_id, "status": status.value}
        )
        
        return response
    
    def get_card(self, card_id: str) -> 'Card':
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
    ) -> Union[List['Card'], PaginatedResponse['Card']]:
        """
        Get cards by template ID.
        
        Args:
            template_id: Template ID
            limit: Maximum number of cards to return
            next_token: Token for pagination
            paginated: Return PaginatedResponse instead of list
            
        Returns:
            List of cards or paginated response
        """
        if not hasattr(self._client, '_make_request_sync'):
            raise TypeError("This method requires a synchronous client")
        
        params = {}
        if limit is not None:
            params["limit"] = limit
        if next_token:
            params["next"] = next_token
        
        url = f"/api/v1/card/template/{template_id}"
        return self.list(url=url, paginated=paginated, **params)
    
    def create_card_and_template(
        self,
        template_payload: Dict[str, Any],
        card_payload: Dict[str, Any],
        options: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Create both card and template in one request.
        
        Args:
            template_payload: Template configuration
            card_payload: Card data
            options: Optional card creation options
            
        Returns:
            Response with both template and card details
        """
        if not hasattr(self._client, '_make_request_sync'):
            raise TypeError("This method requires a synchronous client")
        
        request_data = {
            "templatePayload": template_payload,
            "cardPayload": card_payload
        }
        
        if options:
            request_data["options"] = options
        
        url = self._build_url(suffix="template")
        response = self._client._make_request_sync(
            "POST",
            url,
            json_data=request_data
        )
        
        return response
    
    def generate_business_card(
        self,
        template_id: str,
        card_payload: Dict[str, Any],
        business_card: Dict[str, Any],
        options: Optional[Dict[str, Any]] = None
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
        """
        if not hasattr(self._client, '_make_request_sync'):
            raise TypeError("This method requires a synchronous client")
        
        request_data = {
            "templateId": template_id,
            "cardPayload": card_payload,
            "businessCard": business_card
        }
        
        if options:
            request_data["options"] = options
        
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
        card_payload,
        tier: Optional[str] = None,
        options = None,
        template_overrides = None
    ) -> SignUpResponse:
        """
        Create a new card asynchronously.
        
        Args:
            template_id: ID of the template to use
            card_payload: Card data (email, phone, custom fields, etc.)
            options: Optional card creation options (e.g., {"emailInvitationEnabled": True})
            tier: Optional tier for multi-tiered templates
            template_overrides: Optional template overrides for custom locations, images, etc.
            
        Returns:
            Card creation response with card details
        """
        if not hasattr(self._client, '_make_request_async'):
            raise TypeError("This method requires an asynchronous client")
        
        if not isinstance(card_payload, BaseCardPayload):
            card_payload = BaseCardPayload(**card_payload)
            
        request_data = {
            "templateId": template_id,
            "cardPayload": card_payload.model_dump(exclude_none=True)
        }
        
        if options:
            if not isinstance(options, SignUpOptions):
                options = SignUpOptions(**options)
            request_data["options"] = options.model_dump(exclude_none=True)
        
        if tier:
            request_data["tier"] = tier
            
        if template_overrides:
            if not isinstance(template_overrides, TemplateOverridesV1):
                template_overrides = TemplateOverridesV1(**template_overrides)
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
        card_payload = None,
        sync_static_fields: Optional[bool] = None,
        tier: Optional[str] = None,
        template_overrides = None
    ) -> Dict[str, Any]:
        """
        Update an existing card asynchronously.
        
        Args:
            card_id: Card ID to update
            card_payload: Updated card data (optional)
            sync_static_fields: Flag to sync static fields
            tier: Optional tier for multi-tiered templates
            template_overrides: Optional template overrides for custom locations, images, etc.
            
        Returns:
            Update response
        """
        if not hasattr(self._client, '_make_request_async'):
            raise TypeError("This method requires an asynchronous client")
        
        request_data = {
            "cardId": card_id
        }
        
        if card_payload:
            if not isinstance(card_payload, BaseCardPayload):
                card_payload = BaseCardPayload(**card_payload)
            request_data["cardPayload"] = card_payload.model_dump(exclude_none=True)
        
        if sync_static_fields is not None:
            request_data["syncStaticFields"] = sync_static_fields
        
        if tier:
            request_data["tier"] = tier
            
        if template_overrides:
            if not isinstance(template_overrides, TemplateOverridesV1):
                template_overrides = TemplateOverridesV1(**template_overrides)
            request_data["templateOverrides"] = template_overrides.model_dump(exclude_none=True)
        
        response = await self._client._make_request_async(
            "PATCH",
            self._build_url(),
            json_data=request_data
        )
        
        return response
    
    async def set_card_status_async(self, card_id: str, status: CardStatus) -> Dict[str, Any]:
        """
        Set card status asynchronously (ACTIVE, INACTIVE, DELETED).
        
        Args:
            card_id: Card ID
            status: New status
            
        Returns:
            Success response
        """
        if not hasattr(self._client, '_make_request_async'):
            raise TypeError("This method requires an asynchronous client")
        
        url = self._build_url(suffix="status")
        response = await self._client._make_request_async(
            "POST",
            url,
            json_data={"cardId": card_id, "status": status.value}
        )
        
        return response
    
    async def get_card_async(self, card_id: str) -> 'Card':
        """
        Get a card by ID asynchronously.
        
        Args:
            card_id: Card ID
            
        Returns:
            Card instance
        """
        return await self.get_async(card_id)
    
    async def list_cards_by_template_async(
        self,
        template_id: str,
        limit: int = 10,
        next_token: Optional[str] = None,
        paginated: bool = False
    ) -> Union[List['Card'], PaginatedResponse['Card']]:
        """
        Get cards by template ID asynchronously.
        
        Args:
            template_id: Template ID
            limit: Maximum number of cards to return
            next_token: Token for pagination
            paginated: Return PaginatedResponse instead of list
            
        Returns:
            List of cards or paginated response
        """
        if not hasattr(self._client, '_make_request_async'):
            raise TypeError("This method requires an asynchronous client")
        
        params = {}
        if limit is not None:
            params["limit"] = limit
        if next_token:
            params["next"] = next_token
        
        url = f"/api/v1/card/template/{template_id}"
        return await self.list_async(url=url, paginated=paginated, **params)
    
    async def create_card_and_template_async(
        self,
        template_payload: Dict[str, Any],
        card_payload: Dict[str, Any],
        options: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Create both card and template in one request asynchronously.
        
        Args:
            template_payload: Template configuration
            card_payload: Card data
            options: Optional card creation options
            
        Returns:
            Response with both template and card details
        """
        if not hasattr(self._client, '_make_request_async'):
            raise TypeError("This method requires an asynchronous client")
        
        request_data = {
            "templatePayload": template_payload,
            "cardPayload": card_payload
        }
        
        if options:
            request_data["options"] = options
        
        url = self._build_url(suffix="template")
        response = await self._client._make_request_async(
            "POST",
            url,
            json_data=request_data
        )
        
        return response
    
    async def generate_business_card_async(
        self,
        template_id: str,
        card_payload: Dict[str, Any],
        business_card: Dict[str, Any],
        options: Optional[Dict[str, Any]] = None
    ) -> SignUpResponse:
        """
        Generate a business card asynchronously.
        
        Args:
            template_id: Template ID
            card_payload: Card data
            business_card: Business card specific data
            options: Optional card creation options
            
        Returns:
            Card creation response
        """
        if not hasattr(self._client, '_make_request_async'):
            raise TypeError("This method requires an asynchronous client")
        
        request_data = {
            "templateId": template_id,
            "cardPayload": card_payload,
            "businessCard": business_card
        }
        
        if options:
            request_data["options"] = options
        
        url = "/api/v1/card/business"
        response = await self._client._make_request_async(
            "POST",
            url,
            json_data=request_data
        )
        
        return SignUpResponse(**response)
