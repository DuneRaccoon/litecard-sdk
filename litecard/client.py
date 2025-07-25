import httpx
import asyncio
import time
import logging
from typing import Optional, Any, Dict, Union
from datetime import datetime, timedelta

from .exceptions import (
    LitecardAPIError, 
    AuthenticationError, 
    create_exception_from_response
)
from . import utils
from .resources import (
    Authentication,
    Template,
    Card,
    Notification,
    Scan,
    Certificate,
    Download,
    Backlink,
    Form,
    CardOwner,
    Pass,
    NotificationGroup,
    SubBusiness,
    Business,
    User,
    Schedule,
    Export,
    Webhook,
    CardUpload,
    VoucherCode
)
from .throttler import throttler, async_throttler

logger = logging.getLogger(__name__)

DEFAULT_BASE_URL = "https://bff-api.demo.litecard.io"
DEFAULT_TIMEOUT = 60.0


class BaseLitecardClient:
    def __init__(
        self,
        *,
        username: Optional[str] = None,
        password: Optional[str] = None,
        api_token: Optional[str] = None,
        base_url: str = DEFAULT_BASE_URL,
        timeout: float = DEFAULT_TIMEOUT,
        max_retries: int = 5,
        tenant: Optional[str] = None,
        active_business_id: Optional[str] = None,
    ):
        if not api_token and not (username and password):
            raise ValueError("Either api_token or both username and password are required.")

        self.username = username
        self.password = password
        self._api_token = api_token
        self._token_expires_at: Optional[datetime] = None
        self.base_url = base_url.rstrip('/')
        self.timeout = timeout
        self.max_retries = max_retries
        self.tenant = tenant
        self.active_business_id = active_business_id
        self.utils = utils  # Make utils accessible

        self._client: Optional[Union[httpx.Client, httpx.AsyncClient]] = None

        # Initialize resource classes
        self._initialize_resources()

    def _initialize_resources(self):
        """Initialize resource classes."""
        self.auth = Authentication(client=self)
        self.templates = Template(client=self)
        self.cards = Card(client=self)
        self.notifications = Notification(client=self)
        self.scans = Scan(client=self)
        self.certificates = Certificate(client=self)
        self.downloads = Download(client=self)
        self.backlinks = Backlink(client=self)
        self.forms = Form(client=self)
        self.card_owners = CardOwner(client=self)
        self.passes = Pass(client=self)
        self.notification_groups = NotificationGroup(client=self)
        self.sub_businesses = SubBusiness(client=self)
        self.business = Business(client=self)
        self.users = User(client=self)
        self.schedules = Schedule(client=self)
        self.exports = Export(client=self)
        self.webhooks = Webhook(client=self)
        self.card_uploads = CardUpload(client=self)
        self.voucher_codes = VoucherCode(client=self)

    def _is_token_valid(self) -> bool:
        """Check if current token is valid and not expired."""
        if not self._api_token:
            return False
        if not self._token_expires_at:
            return True  # If no expiry set, assume valid
        return datetime.now() < self._token_expires_at

    def _get_api_token(self) -> str:
        """Get a valid API token, refreshing if necessary."""
        if self._is_token_valid():
            return self._api_token
        
        if not (self.username and self.password):
            raise AuthenticationError("Token expired and no credentials available for refresh")
        
        # Token needs refresh - this will be implemented in sync/async specific methods
        raise NotImplementedError("Token refresh must be implemented in subclasses")

    def _get_auth_headers(self) -> Dict[str, str]:
        """Generate authorization headers for Litecard API."""
        token = self._get_api_token()
        headers = {
            "Authorization": f"Bearer {token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        
        if self.tenant:
            headers["x-user-tenant"] = self.tenant
        
        if self.active_business_id:
            headers["x-active-business-id"] = self.active_business_id
            
        return headers

    def _handle_error_response(self, response: httpx.Response, method: str, url: str, **kwargs):
        """Centralized error handling."""
        logger.error(
            f"Litecard API Error: {response.status_code} on {method} {url}. "
            f"Response: {response.content[:500] if response.content else 'No content'}"
        )
        
        # Use our generic exception creation helper
        raise create_exception_from_response(response, method, url, **kwargs)


class LitecardClient(BaseLitecardClient):
    """Synchronous Litecard API client."""
    
    def __init__(self, *args, **kwargs):
        self._client = None
        super().__init__(*args, **kwargs)
        self._client = httpx.Client(base_url=self.base_url, timeout=self.timeout)

    def _get_api_token(self) -> str:
        """Get a valid API token, refreshing if necessary (sync version)."""
        if self._is_token_valid():
            return self._api_token
        
        if not (self.username and self.password):
            raise AuthenticationError("Token expired and no credentials available for refresh")
        
        # Refresh token
        self._refresh_token_sync()
        return self._api_token

    def _refresh_token_sync(self) -> None:
        """Refresh the API token synchronously."""
        if not isinstance(self._client, httpx.Client):
            raise TypeError("HTTP client must be an instance of httpx.Client")
        
        auth_data = {
            "username": self.username,
            "password": self.password
        }
        
        headers = {"Accept": "application/json", "Content-Type": "application/json"}
        if self.tenant:
            headers["x-user-tenant"] = self.tenant
        
        try:
            response = self._client.request(
                "POST",
                "/api/v1/token",
                json=auth_data,
                headers=headers,
            )
            
            if 200 <= response.status_code < 300:
                data = response.json()
                self._api_token = data["access_token"]
                expires_in = data.get("expires_in", 86400)  # Default 24 hours
                self._token_expires_at = datetime.now() + timedelta(seconds=expires_in - 300)  # 5 min buffer
            else:
                self._handle_error_response(response, "POST", "/api/v1/token")
                
        except httpx.RequestError as e:
            raise LitecardAPIError(f"Failed to authenticate: {str(e)}")

    @throttler.throttle()
    def _make_request_sync(
        self,
        method: str,
        path: str,
        params: Optional[Dict[str, Any]] = None,
        json_data: Optional[Dict[str, Any]] = None,
        form_data: Optional[Dict[str, Any]] = None,
        files: Optional[Dict[str, Any]] = None,
    ) -> Any:
        """Make a synchronous HTTP request to the Litecard API."""
        
        if not isinstance(self._client, httpx.Client):
            raise TypeError("HTTP client must be an instance of httpx.Client")
        
        headers = self._get_auth_headers()
        
        params = utils.clean_params(params) if params else {}
        
        # Ensure path starts with /
        if not path.startswith('/'):
            path = '/' + path
        
        retries = self.max_retries
        while True:
            try:
                response = self._client.request(
                    method,
                    path,
                    params=params,
                    json=json_data,
                    data=form_data,
                    files=files,
                    headers=headers,
                )
            
                if 200 <= response.status_code < 300:
                    if response.content:
                        try:
                            return response.json()
                        except ValueError:
                            # Response is not JSON, return text
                            return response.text
                    return {}  # For 204 No Content
                
                # Handle 401 errors by refreshing token
                if response.status_code == 401 and retries > 0:
                    logger.warning("Received 401, refreshing token and retrying")
                    self._refresh_token_sync()
                    headers = self._get_auth_headers()
                    retries -= 1
                    continue
                
                retry_after_header = response.headers.get("Retry-After")
                should_retry_rate_limit = response.status_code == 429 and retry_after_header and retry_after_header.isdigit()
                should_retry_maintenance = response.status_code == 503 and retry_after_header and retry_after_header.isdigit()
                
                if (should_retry_rate_limit or should_retry_maintenance) and retries > 0:
                    wait_time = int(retry_after_header)
                    logger.warning(f"Status {response.status_code}, retrying after {wait_time}s. Retries left: {retries-1}")
                    time.sleep(wait_time)
                    retries -= 1
                    continue

                self._handle_error_response(response, method, path, params=params, json=json_data, data=form_data)
                return {}

            except LitecardAPIError as e:
                if hasattr(e, 'retry_after') and getattr(e, 'retry_after') and isinstance(e.retry_after, (int, float)) and retries > 0:
                    logger.warning(f"Caught {type(e).__name__}, retrying after {e.retry_after}s. Retries left: {retries-1}")
                    time.sleep(e.retry_after)
                    retries -= 1
                    continue
                raise
            except httpx.RequestError as e:
                if retries > 0:
                    logger.warning(f"Network error: {e}. Retrying in 3s. Retries left: {retries-1}")
                    time.sleep(3)
                    retries -= 1
                    continue
                # Create a dummy response for network errors
                dummy_response = httpx.Response(500, request=httpx.Request(method, self.base_url + path))
                raise LitecardAPIError(
                    message=f"Network request failed: {str(e)}",
                    response=dummy_response
                )

    def close(self):
        """Close the HTTP client."""
        if self._client and isinstance(self._client, httpx.Client):
            self._client.close()


class LitecardAsyncClient(BaseLitecardClient):
    """Asynchronous Litecard API client."""
    
    def __init__(self, *args, **kwargs):
        self._client = None
        super().__init__(*args, **kwargs)
        self._client = httpx.AsyncClient(base_url=self.base_url, timeout=self.timeout)

    def _get_api_token(self) -> str:
        """Get a valid API token, refreshing if necessary (async version)."""
        if self._is_token_valid():
            return self._api_token
        
        raise AuthenticationError("Token expired - use await refresh_token_async() first")

    async def _refresh_token_async(self) -> None:
        """Refresh the API token asynchronously."""
        if not isinstance(self._client, httpx.AsyncClient):
            raise TypeError("HTTP client must be an instance of httpx.AsyncClient")
        
        if not (self.username and self.password):
            raise AuthenticationError("Username and password required for token refresh")
        
        auth_data = {
            "username": self.username,
            "password": self.password
        }
        
        headers = {"Accept": "application/json", "Content-Type": "application/json"}
        if self.tenant:
            headers["x-user-tenant"] = self.tenant
        
        try:
            response = await self._client.request(
                "POST",
                "/api/v1/token",
                json=auth_data,
                headers=headers,
            )
            
            if 200 <= response.status_code < 300:
                data = response.json()
                self._api_token = data["access_token"]
                expires_in = data.get("expires_in", 86400)  # Default 24 hours
                self._token_expires_at = datetime.now() + timedelta(seconds=expires_in - 300)  # 5 min buffer
            else:
                self._handle_error_response(response, "POST", "/api/v1/token")
                
        except httpx.RequestError as e:
            raise LitecardAPIError(f"Failed to authenticate: {str(e)}")

    @async_throttler.throttle()
    async def _make_request_async(
        self,
        method: str,
        path: str,
        params: Optional[Dict[str, Any]] = None,
        json_data: Optional[Dict[str, Any]] = None,
        form_data: Optional[Dict[str, Any]] = None,
        files: Optional[Dict[str, Any]] = None,
    ) -> Any:
        """Make an asynchronous HTTP request to the Litecard API."""
        
        if not isinstance(self._client, httpx.AsyncClient):
            raise TypeError("HTTP client must be an instance of httpx.AsyncClient")
        
        params = utils.clean_params(params) if params else {}
        
        headers = self._get_auth_headers()
        
        # Ensure path starts with /
        if not path.startswith('/'):
            path = '/' + path

        retries = self.max_retries
        while True:
            try:
                response = await self._client.request(
                    method,
                    path,
                    params=params,
                    json=json_data,
                    data=form_data,
                    files=files,
                    headers=headers,
                )
                
                if 200 <= response.status_code < 300:
                    if response.content:
                        try:
                            return response.json()
                        except ValueError:
                            # Response is not JSON, return text
                            return response.text
                    return {}

                # Handle 401 errors by refreshing token
                if response.status_code == 401 and retries > 0:
                    logger.warning("Received 401, refreshing token and retrying")
                    await self._refresh_token_async()
                    headers = self._get_auth_headers()
                    retries -= 1
                    continue

                retry_after_header = response.headers.get("Retry-After")
                should_retry_rate_limit = response.status_code == 429 and retry_after_header and retry_after_header.isdigit()
                should_retry_maintenance = response.status_code == 503 and retry_after_header and retry_after_header.isdigit()

                if (should_retry_rate_limit or should_retry_maintenance) and retries > 0:
                    wait_time = int(retry_after_header)
                    logger.warning(f"Status {response.status_code}, retrying after {wait_time}s. Retries left: {retries-1}")
                    await asyncio.sleep(wait_time)
                    retries -= 1
                    continue
                
                self._handle_error_response(response, method, path, params=params, json=json_data, data=form_data)
                return {}

            except LitecardAPIError as e:
                if hasattr(e, 'retry_after') and getattr(e, 'retry_after') and isinstance(e.retry_after, (int, float)) and retries > 0:
                    logger.warning(f"Caught {type(e).__name__}, retrying after {e.retry_after}s. Retries left: {retries-1}")
                    await asyncio.sleep(e.retry_after)
                    retries -= 1
                    continue
                raise
            except httpx.RequestError as e:
                if retries > 0:
                    logger.warning(f"Network error: {e}. Retrying in 3s. Retries left: {retries-1}")
                    await asyncio.sleep(3)
                    retries -= 1
                    continue
                # Create a dummy response for network errors
                dummy_response = httpx.Response(500, request=httpx.Request(method, self.base_url + path))
                raise LitecardAPIError(
                    message=f"Network request failed: {str(e)}",
                    response=dummy_response
                )
                
    async def close(self):
        """Close the HTTP client asynchronously."""
        if self._client and isinstance(self._client, httpx.AsyncClient):
            await self._client.aclose()
