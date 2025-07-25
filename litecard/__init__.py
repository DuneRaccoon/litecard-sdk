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

# Import models for easy access
from .models import (
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
    CardOwnerCopy,
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
    "CardOwnerCopy",
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
