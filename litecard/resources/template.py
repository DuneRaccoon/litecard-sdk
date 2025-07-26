"""
Template resource for the Litecard API.
"""

from typing import Dict, Any, List, Union, Optional
from .base import LitecardResource, PaginatedResponse
from ..models_ import (
    Template as TemplateModel,
    TemplateStatus,
    TemplateColours,
    TemplateImages,
    TemplateBarcode,
    AppleWalletSettings,
    GoogleWalletSettings,
    TemplateCardExpiry,
    PassType,
)
from ..request_types import (
    CreateTemplateRequest,
    UpdateTemplateRequest,
    SetTemplateStatusRequest,
    TemplateQueryParams,
    SuccessResponse,
    DownloadCountResponse,
    DownloadTrendResponse,
)


class Template(LitecardResource):
    """
    Template resource for managing card templates.
    """
    
    endpoint = "template"
    model_class = TemplateModel
    
    def create_template(
        self,
        name: str,
        description: str,
        business_name: str,
        apple_wallet_settings: AppleWalletSettings,
        google_wallet_settings: GoogleWalletSettings,
        colours: TemplateColours,
        images: TemplateImages,
        barcode: TemplateBarcode,
        template_type: Optional[PassType] = None,
        card_expiry: Optional[TemplateCardExpiry] = None,
        form_id: Optional[str] = None
    ) -> TemplateModel:
        """
        Create a new template.
        
        Args:
            name: Human readable name of the template
            description: Template description
            business_name: Name of the business
            apple_wallet_settings: Apple wallet configuration
            google_wallet_settings: Google wallet configuration
            colours: Color configuration
            images: Image configuration
            barcode: Barcode configuration
            template_type: The type of pass (optional)
            card_expiry: Card expiry configuration (optional)
            form_id: Associated form ID (optional)
            
        Returns:
            Created template instance
            
        Example:
            ```python
            from litecard.models_ import (
                AppleWalletSettings, GoogleWalletSettings,
                TemplateColours, TemplateImages, TemplateBarcode,
                ApplePassType, GooglePassType, BarcodeType, PassType
            )
            
            # Configure wallet settings
            apple_settings = AppleWalletSettings(
                passType=ApplePassType.STORE_CARD,
                hideLogo=False
            )
            
            google_settings = GoogleWalletSettings(
                passType=GooglePassType.LOYALTY,
                title="My Loyalty Card"
            )
            
            # Configure colors and images
            colours = TemplateColours(
                background="#FF0000",
                label="#FFFFFF",
                foreground="#000000"
            )
            
            images = TemplateImages(
                logo="https://example.com/logo.png",
                icon="https://example.com/icon.png"
            )
            
            barcode = TemplateBarcode(
                barcodeValue="123456789",
                type=BarcodeType.QR_CODE
            )
            
            template = template_resource.create_template(
                name="My Template",
                description="A sample template",
                business_name="My Business",
                apple_wallet_settings=apple_settings,
                google_wallet_settings=google_settings,
                colours=colours,
                images=images,
                barcode=barcode,
                template_type=PassType.BUSINESS_CARD
            )
            ```
        """
        if not hasattr(self._client, '_make_request_sync'):
            raise TypeError("This method requires a synchronous client")
        
        request_data: CreateTemplateRequest = {
            "name": name,
            "description": description,
            "businessName": business_name,
            "appleWalletSettings": apple_wallet_settings.model_dump(exclude_none=True),
            "googleWalletSettings": google_wallet_settings.model_dump(exclude_none=True),
            "colours": colours.model_dump(exclude_none=True),
            "images": images.model_dump(exclude_none=True),
            "barcode": barcode.model_dump(exclude_none=True)
        }
        
        if template_type:
            request_data["type"] = template_type.value
        
        if card_expiry:
            request_data["cardExpiry"] = card_expiry.model_dump(exclude_none=True)
        
        if form_id:
            request_data["formId"] = form_id
        
        response = self._client._make_request_sync(
            "POST",
            self._build_url(),
            json_data=request_data
        )
        
        return self._create_instance(response)
    
    def update_template(
        self, 
        template_id: str,
        name: Optional[str] = None,
        description: Optional[str] = None,
        business_name: Optional[str] = None,
        apple_wallet_settings: Optional[AppleWalletSettings] = None,
        google_wallet_settings: Optional[GoogleWalletSettings] = None,
        colours: Optional[TemplateColours] = None,
        images: Optional[TemplateImages] = None,
        barcode: Optional[TemplateBarcode] = None,
        template_type: Optional[PassType] = None,
        card_expiry: Optional[TemplateCardExpiry] = None
    ) -> TemplateModel:
        """
        Update an existing template.
        
        Args:
            template_id: ID of the template to update
            name: Human readable name of the template (optional)
            description: Template description (optional)
            business_name: Name of the business (optional)
            apple_wallet_settings: Apple wallet configuration (optional)
            google_wallet_settings: Google wallet configuration (optional)
            colours: Color configuration (optional)
            images: Image configuration (optional)
            barcode: Barcode configuration (optional)
            template_type: The type of pass (optional)
            card_expiry: Card expiry configuration (optional)
            
        Returns:
            Updated template instance
            
        Example:
            ```python
            from litecard.models_ import TemplateColours
            
            # Update only colors
            new_colours = TemplateColours(
                background="#00FF00",
                label="#FFFFFF",
                foreground="#000000"
            )
            
            updated_template = template_resource.update_template(
                template_id="template_123",
                name="Updated Template Name",
                colours=new_colours
            )
            ```
        """
        if not hasattr(self._client, '_make_request_sync'):
            raise TypeError("This method requires a synchronous client")
        
        request_data: UpdateTemplateRequest = {
            "id": template_id
        }
        
        if name is not None:
            request_data["name"] = name
        
        if description is not None:
            request_data["description"] = description
        
        if business_name is not None:
            request_data["businessName"] = business_name
        
        if apple_wallet_settings is not None:
            request_data["appleWalletSettings"] = apple_wallet_settings.model_dump(exclude_none=True)
        
        if google_wallet_settings is not None:
            request_data["googleWalletSettings"] = google_wallet_settings.model_dump(exclude_none=True)
        
        if colours is not None:
            request_data["colours"] = colours.model_dump(exclude_none=True)
        
        if images is not None:
            request_data["images"] = images.model_dump(exclude_none=True)
        
        if barcode is not None:
            request_data["barcode"] = barcode.model_dump(exclude_none=True)
        
        if template_type is not None:
            request_data["type"] = template_type.value
        
        if card_expiry is not None:
            request_data["cardExpiry"] = card_expiry.model_dump(exclude_none=True)
        
        response = self._client._make_request_sync(
            "PUT",
            self._build_url(),
            json_data=request_data
        )
        
        return self._create_instance(response)
    
    def set_status(
        self, 
        template_id: str, 
        status: TemplateStatus
    ) -> SuccessResponse:
        """
        Set template status (ACTIVE, INACTIVE, DELETED).
        
        Args:
            template_id: Template ID
            status: New status from TemplateStatus enum
            
        Returns:
            Success response
            
        Example:
            ```python
            from litecard.models_ import TemplateStatus
            
            response = template_resource.set_status(
                template_id="template_123",
                status=TemplateStatus.INACTIVE
            )
            ```
        """
        if not hasattr(self._client, '_make_request_sync'):
            raise TypeError("This method requires a synchronous client")
        
        request_data: SetTemplateStatusRequest = {
            "status": status.value
        }
        
        url = self._build_url(suffix=f"status/{template_id}")
        response = self._client._make_request_sync(
            "POST",
            url,
            json_data=request_data
        )
        
        return response
    
    def list_templates(
        self, 
        limit: Optional[int] = None,
        next_token: Optional[str] = None,
        status: Optional[TemplateStatus] = None,
        business_id: Optional[str] = None,
        paginated: bool = False
    ) -> Union[List[TemplateModel], PaginatedResponse[TemplateModel]]:
        """
        List templates.
        
        Args:
            limit: Maximum number of templates to return
            next_token: Token for pagination
            status: Filter by template status (optional)
            business_id: Filter by business ID (optional)
            paginated: Return PaginatedResponse instead of list
            
        Returns:
            List of templates or paginated response
            
        Example:
            ```python
            from litecard.models_ import TemplateStatus
            
            # Get active templates only
            active_templates = template_resource.list_templates(
                status=TemplateStatus.ACTIVE,
                limit=20
            )
            
            # Get paginated response
            paginated_templates = template_resource.list_templates(
                limit=10,
                paginated=True
            )
            ```
        """
        if not hasattr(self._client, '_make_request_sync'):
            raise TypeError("This method requires a synchronous client")
        
        params: TemplateQueryParams = {}
        if limit is not None:
            params["limit"] = limit
        if next_token:
            params["next"] = next_token
        if status is not None:
            params["status"] = status.value
        if business_id is not None:
            params["businessId"] = business_id
            
        url = "/api/v1/templates"  # Use the correct endpoint for listing
        return self.list(url=url, paginated=paginated, **params)
    
    def get_pass_downloads_count(
        self, 
        template_id: str, 
        duration: str = "PAST_7_DAYS"
    ) -> DownloadCountResponse:
        """
        Get pass downloads count for a template.
        
        Args:
            template_id: Template ID
            duration: Duration (PAST_7_DAYS, PAST_30_DAYS, ALL)
            
        Returns:
            Pass counts data with typed response
            
        Example:
            ```python
            # Get download counts for the past 7 days
            counts = template_resource.get_pass_downloads_count(
                template_id="template_123",
                duration="PAST_7_DAYS"
            )
            
            print(f"Apple downloads: {counts['appleCount']}")
            print(f"Google downloads: {counts['googleCount']}")
            print(f"Total downloads: {counts['totalCount']}")
            ```
        """
        if not hasattr(self._client, '_make_request_sync'):
            raise TypeError("This method requires a synchronous client")
        
        url = f"/api/v1/template/{template_id}/downloads/count"
        params = {"duration": duration}
        
        response = self._client._make_request_sync("GET", url, params=params)
        return response
    
    def get_pass_download_trend(
        self, 
        template_id: str, 
        days: int = 7
    ) -> DownloadTrendResponse:
        """
        Get pass download trend for a template.
        
        Args:
            template_id: Template ID
            days: Number of days (7 or 30)
            
        Returns:
            Trend data with typed response
            
        Example:
            ```python
            # Get download trend for the past 30 days
            trend = template_resource.get_pass_download_trend(
                template_id="template_123",
                days=30
            )
            
            for data_point in trend['trend']:
                print(f"Date: {data_point['date']}, Downloads: {data_point['value']}")
            ```
        """
        if not hasattr(self._client, '_make_request_sync'):
            raise TypeError("This method requires a synchronous client")
        
        url = f"/api/v1/template/{template_id}/downloads/trend"
        params = {"days": days}
        
        response = self._client._make_request_sync("GET", url, params=params)
        return response
    
    # Async methods
    
    async def create_template_async(
        self,
        name: str,
        description: str,
        business_name: str,
        apple_wallet_settings: AppleWalletSettings,
        google_wallet_settings: GoogleWalletSettings,
        colours: TemplateColours,
        images: TemplateImages,
        barcode: TemplateBarcode,
        template_type: Optional[PassType] = None,
        card_expiry: Optional[TemplateCardExpiry] = None,
        form_id: Optional[str] = None
    ) -> TemplateModel:
        """Create a new template asynchronously."""
        if not hasattr(self._client, '_make_request_async'):
            raise TypeError("This method requires an asynchronous client")
        
        request_data: CreateTemplateRequest = {
            "name": name,
            "description": description,
            "businessName": business_name,
            "appleWalletSettings": apple_wallet_settings.model_dump(exclude_none=True),
            "googleWalletSettings": google_wallet_settings.model_dump(exclude_none=True),
            "colours": colours.model_dump(exclude_none=True),
            "images": images.model_dump(exclude_none=True),
            "barcode": barcode.model_dump(exclude_none=True)
        }
        
        if template_type:
            request_data["type"] = template_type.value
        
        if card_expiry:
            request_data["cardExpiry"] = card_expiry.model_dump(exclude_none=True)
        
        if form_id:
            request_data["formId"] = form_id
        
        response = await self._client._make_request_async(
            "POST",
            self._build_url(),
            json_data=request_data
        )
        
        return self._create_instance(response)
    
    async def update_template_async(
        self, 
        template_id: str,
        name: Optional[str] = None,
        description: Optional[str] = None,
        business_name: Optional[str] = None,
        apple_wallet_settings: Optional[AppleWalletSettings] = None,
        google_wallet_settings: Optional[GoogleWalletSettings] = None,
        colours: Optional[TemplateColours] = None,
        images: Optional[TemplateImages] = None,
        barcode: Optional[TemplateBarcode] = None,
        template_type: Optional[PassType] = None,
        card_expiry: Optional[TemplateCardExpiry] = None
    ) -> TemplateModel:
        """Update an existing template asynchronously."""
        if not hasattr(self._client, '_make_request_async'):
            raise TypeError("This method requires an asynchronous client")
        
        request_data: UpdateTemplateRequest = {
            "id": template_id
        }
        
        if name is not None:
            request_data["name"] = name
        
        if description is not None:
            request_data["description"] = description
        
        if business_name is not None:
            request_data["businessName"] = business_name
        
        if apple_wallet_settings is not None:
            request_data["appleWalletSettings"] = apple_wallet_settings.model_dump(exclude_none=True)
        
        if google_wallet_settings is not None:
            request_data["googleWalletSettings"] = google_wallet_settings.model_dump(exclude_none=True)
        
        if colours is not None:
            request_data["colours"] = colours.model_dump(exclude_none=True)
        
        if images is not None:
            request_data["images"] = images.model_dump(exclude_none=True)
        
        if barcode is not None:
            request_data["barcode"] = barcode.model_dump(exclude_none=True)
        
        if template_type is not None:
            request_data["type"] = template_type.value
        
        if card_expiry is not None:
            request_data["cardExpiry"] = card_expiry.model_dump(exclude_none=True)
        
        response = await self._client._make_request_async(
            "PUT",
            self._build_url(),
            json_data=request_data
        )
        
        return self._create_instance(response)
    
    async def set_status_async(
        self, 
        template_id: str, 
        status: TemplateStatus
    ) -> SuccessResponse:
        """Set template status asynchronously."""
        if not hasattr(self._client, '_make_request_async'):
            raise TypeError("This method requires an asynchronous client")
        
        request_data: SetTemplateStatusRequest = {
            "status": status.value
        }
        
        url = self._build_url(suffix=f"status/{template_id}")
        response = await self._client._make_request_async(
            "POST",
            url,
            json_data=request_data
        )
        
        return response
    
    async def list_templates_async(
        self,
        limit: Optional[int] = None,
        next_token: Optional[str] = None,
        status: Optional[TemplateStatus] = None,
        business_id: Optional[str] = None,
        paginated: bool = False
    ) -> Union[List[TemplateModel], PaginatedResponse[TemplateModel]]:
        """List templates asynchronously."""
        if not hasattr(self._client, '_make_request_async'):
            raise TypeError("This method requires an asynchronous client")
        
        params: TemplateQueryParams = {}
        if limit is not None:
            params["limit"] = limit
        if next_token:
            params["next"] = next_token
        if status is not None:
            params["status"] = status.value
        if business_id is not None:
            params["businessId"] = business_id
            
        url = "/api/v1/templates"
        return await self.list_async(url=url, paginated=paginated, **params)
    
    async def get_pass_downloads_count_async(
        self,
        template_id: str,
        duration: str = "PAST_7_DAYS"
    ) -> DownloadCountResponse:
        """Get pass downloads count asynchronously."""
        if not hasattr(self._client, '_make_request_async'):
            raise TypeError("This method requires an asynchronous client")
        
        url = f"/api/v1/template/{template_id}/downloads/count"
        params = {"duration": duration}
        
        response = await self._client._make_request_async("GET", url, params=params)
        return response
    
    async def get_pass_download_trend_async(
        self,
        template_id: str,
        days: int = 7
    ) -> DownloadTrendResponse:
        """Get pass download trend asynchronously."""
        if not hasattr(self._client, '_make_request_async'):
            raise TypeError("This method requires an asynchronous client")
        
        url = f"/api/v1/template/{template_id}/downloads/trend"
        params = {"days": days}
        
        response = await self._client._make_request_async("GET", url, params=params)
        return response
