"""
Litecard Python SDK

A Python SDK for interacting with the Litecard API.
"""

__version__ = "0.1.0"

from .client import LitecardClient, LitecardAsyncClient
from .exceptions import (
    LitecardAPIError,
    AuthenticationError,
    RateLimitError,
    ValidationError,
    NotFoundError,
    ServerError
)

# Import utility functions for easy access
from .utils import (
    create_card_payload,
    create_location_override,
    create_template_overrides_with_locations,
    create_notification_payload,
    build_welcome_url,
    validate_email,
    format_phone_international
)

# Import request types for easy access
from .request_types import (
    # Card request types
    CreateCardRequest,
    UpdateCardRequest,
    SetCardStatusRequest,
    CreateCardAndTemplateRequest,
    GenerateBusinessCardRequest,
    
    # Template request types
    CreateTemplateRequest,
    UpdateTemplateRequest,
    SetTemplateStatusRequest,
    
    # Notification request types
    NotificationPayload,
    NotificationSegments,
    NotificationOptions,
    SendNotificationRequest,
    SendReminderRequest,
    
    # Scan request types
    ScanCardRequest,
    ScanAction,
    ApplyTemplateActionsRequest,
    
    # Common types
    SuccessResponse,
    ErrorResponse as ErrorResponseType,
    PaginatedListResponse,
    DownloadCountResponse,
    DownloadTrendResponse,
    
    # Query parameter types
    PaginationParams,
    TemplateQueryParams,
    CardQueryParams,
    ScanQueryParams,
)

# Import models for easy access
from .models_ import (
    # Authentication models
    AuthenticationRequest,
    AuthenticationResponse,
    
    # Error models
    ErrorResponse,
    
    # Enums
    CardStatus,
    TemplateStatus,
    PassType,
    ApplePassType,
    GooglePassType,
    BarcodeType,
    ExpiryType,
    DateTimeMeasurement,
    EmailType,
    
    # Template models
    TemplateColours,
    TemplateImages,
    TemplateBarcode,
    TemplateCardExpiry,
    AppleWalletSettings,
    GoogleWalletSettings,
    Template,
    
    # Card models
    BaseCardPayload,
    CardOwner,
    Card,
    
    # Sign up models
    SignUpOptions,
    PrivateSignUpRequest,
    SignUpResponse,
    
    # Notification models
    NotificationRequest,
    NotificationGroup,
    
    # Scan models
    ScanRequest,
    Scan,
    ScanResponse,
    
    # Certificate models
    CertificateUpload,
    Certificate,
    
    # Download models
    WelcomeDetails,
    
    # Form models
    FormField,
    Form,
    
    # Business models
    Business,
    
    # User models
    User,
    
    # Webhook models
    WebhookRegistrationRequest,
    
    # Export models
    ExportRequest,
    ExportResponse,
)

__all__ = [
    # Client classes
    "LitecardClient",
    "LitecardAsyncClient",
    
    # Exception classes
    "LitecardAPIError",
    "AuthenticationError", 
    "RateLimitError",
    "ValidationError",
    "NotFoundError",
    "ServerError",
    
    # Utility functions
    "create_card_payload",
    "create_location_override",
    "create_template_overrides_with_locations",
    "create_notification_payload",
    "build_welcome_url",
    "validate_email",
    "format_phone_international",
    
    # Request type classes
    "CreateCardRequest",
    "UpdateCardRequest",
    "SetCardStatusRequest",
    "CreateCardAndTemplateRequest",
    "GenerateBusinessCardRequest",
    "CreateTemplateRequest",
    "UpdateTemplateRequest",
    "SetTemplateStatusRequest",
    "NotificationPayload",
    "NotificationSegments",
    "NotificationOptions",
    "SendNotificationRequest",
    "SendReminderRequest",
    "ScanCardRequest",
    "ScanAction",
    "ApplyTemplateActionsRequest",
    "SuccessResponse",
    "ErrorResponseType",
    "PaginatedListResponse",
    "DownloadCountResponse",
    "DownloadTrendResponse",
    "PaginationParams",
    "TemplateQueryParams",
    "CardQueryParams",
    "ScanQueryParams",
    
    # Model classes
    "AuthenticationRequest",
    "AuthenticationResponse",
    "ErrorResponse",
    "CardStatus",
    "TemplateStatus",
    "PassType",
    "ApplePassType",
    "GooglePassType",
    "BarcodeType",
    "ExpiryType",
    "DateTimeMeasurement",
    "EmailType",
    "TemplateColours",
    "TemplateImages",
    "TemplateBarcode",
    "TemplateCardExpiry",
    "AppleWalletSettings",
    "GoogleWalletSettings",
    "Template",
    "BaseCardPayload",
    "CardOwner",
    "Card",
    "SignUpOptions",
    "PrivateSignUpRequest",
    "SignUpResponse",
    "NotificationRequest",
    "NotificationGroup",
    "ScanRequest",
    "Scan",
    "ScanResponse",
    "CertificateUpload",
    "Certificate",
    "WelcomeDetails",
    "FormField",
    "Form",
    "Business",
    "User",
    "WebhookRegistrationRequest",
    "ExportRequest",
    "ExportResponse",
]
