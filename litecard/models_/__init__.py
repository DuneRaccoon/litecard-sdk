"""
Pydantic models for Litecard API responses and requests.

This module contains all the data models used by the Litecard API SDK.
They are based on the OpenAPI specification.
"""

from datetime import datetime
from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field


# Base models
class DatabaseMetaData(BaseModel):
    """Database metadata for resources."""
    created_at: Optional[datetime] = Field(None, description="Record creation date")
    updated_at: Optional[datetime] = Field(None, description="Record update date") 
    created_by: Optional[str] = Field(None, description="User ID of the creator")


# Authentication models
class AuthenticationRequest(BaseModel):
    """Authentication request payload."""
    username: str = Field(description="Credential: username")
    password: str = Field(description="Credential: password")


class AuthenticationResponse(BaseModel):
    """Authentication response payload."""
    access_token: str = Field(description="JWT Token used for API authentication")
    type: str = Field(description="Type of Token", default="Bearer")
    expires_in: int = Field(description="Time in seconds before token expires", default=3600)


# Error models
class ErrorResponse(BaseModel):
    """Standard error response."""
    error_code: str = Field(alias="errorCode")
    message: Optional[str] = None


# Enums
class CardStatus(str, Enum):
    """Card status enumeration."""
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    DELETED = "DELETED"
    RESERVED = "RESERVED"
    ERROR = "ERROR"


class TemplateStatus(str, Enum):
    """Template status enumeration."""
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    DELETED = "DELETED"


class PassType(str, Enum):
    """Pass type enumeration."""
    BUSINESS_CARD = "BUSINESS_CARD"
    GENERIC = "GENERIC"
    COUPON = "COUPON"
    EVENT_TICKET = "EVENT_TICKET"


class ApplePassType(str, Enum):
    """Apple pass type enumeration."""
    STORE_CARD = "STORE_CARD"
    BOARDING_PASS = "BOARDING_PASS"
    COUPON = "COUPON"
    EVENT_TICKET = "EVENT_TICKET"
    GENERIC = "GENERIC"


class GooglePassType(str, Enum):
    """Google pass type enumeration."""
    EVENT_TICKET = "EVENT_TICKET"
    FLIGHT = "FLIGHT"
    GIFT_CARD = "GIFT_CARD"
    LOYALTY = "LOYALTY"
    OFFER = "OFFER"
    TRANSIT = "TRANSIT"
    GENERIC = "GENERIC"


class BarcodeType(str, Enum):
    """Barcode type enumeration."""
    NOT_USED = "NOT_USED"
    QR_CODE = "QR_CODE"
    CODE_128 = "CODE_128"
    PDF_417 = "PDF_417"
    AZTEC = "AZTEC"


class ExpiryType(str, Enum):
    """Card expiry type enumeration."""
    NEVER = "NEVER"
    FIXED_DATE = "FIXED_DATE"
    FROM_ACTIVATION = "FROM_ACTIVATION"
    FIXED_SCANS = "FIXED_SCANS"


class DateTimeMeasurement(str, Enum):
    """Date time measurement enumeration."""
    DAYS = "DAYS"
    MONTHS = "MONTHS"
    YEARS = "YEARS"


class EmailType(str, Enum):
    """Email type enumeration."""
    STANDARD = "STANDARD"
    MARKETING = "MARKETING"


# Template models
class TemplateColours(BaseModel):
    """Template color configuration."""
    background: str = Field(description="Background colour of the pass")
    label: str = Field(description="Label colour of the apple pass")
    foreground: str = Field(description="Text colour of the apple pass")
    strip: Optional[str] = Field(None, description="Text colour on top of strip image")
    samsung_blink: Optional[str] = Field(None, alias="samsungBlink", description="Samsung blink color")
    samsung_font: Optional[str] = Field(None, alias="samsungFont", description="Samsung font color")


class TemplateImages(BaseModel):
    """Template image configuration."""
    logo: str = Field(description="URL of uploaded logo image")
    logo_dark_mode: Optional[str] = Field(None, alias="logoDarkMode", description="Dark mode logo")
    logo_light_mode: Optional[str] = Field(None, alias="logoLightMode", description="Light mode logo")
    hero: Optional[str] = Field(None, description="URL of uploaded hero image")
    strip: Optional[str] = Field(None, description="URL of uploaded strip image")
    apple_logo_override: Optional[str] = Field(None, alias="appleLogoOverride", description="Apple logo override")
    icon: str = Field(description="URL of uploaded icon image")
    thumbnail: Optional[str] = Field(None, description="URL of uploaded thumbnail image")
    background: Optional[str] = Field(None, description="URL of uploaded background image")


class TemplateBarcode(BaseModel):
    """Template barcode configuration."""
    barcode_value: str = Field(alias="barcodeValue", description="Value of the barcode")
    message_encoding: Optional[str] = Field(None, alias="messageEncoding", description="Message encoding")
    type: BarcodeType = Field(description="Type of the barcode")
    alt_text: Optional[str] = Field(None, alias="altText", description="Alternative text")
    field_map: Optional[str] = Field(None, alias="fieldMap", description="Field mapping")


class TemplateCardExpiry(BaseModel):
    """Template card expiry configuration."""
    expiry_type: ExpiryType = Field(alias="expiryType", description="Type of expiry")
    start_date: Optional[datetime] = Field(None, alias="startDate", description="Start date")
    end_date: Optional[datetime] = Field(None, alias="endDate", description="End date")
    from_activation: Optional[Dict[str, Any]] = Field(None, alias="fromActivation", description="From activation config")
    scans: Optional[int] = Field(None, description="Number of scans before expiry")


class AppleWalletSettings(BaseModel):
    """Apple wallet settings."""
    pass_type: ApplePassType = Field(alias="passType", description="Apple wallet card type")
    hide_logo: Optional[bool] = Field(False, alias="hideLogo", description="Hide logo")
    hide_logo_text: Optional[bool] = Field(False, alias="hideLogoText", description="Hide logo text")
    disable_sharing: Optional[bool] = Field(False, alias="disableSharing", description="Disable sharing")


class GoogleWalletSettings(BaseModel):
    """Google wallet settings."""
    pass_type: GooglePassType = Field(alias="passType", description="Google wallet card type")
    security_shimmer: Optional[bool] = Field(False, alias="securityShimmer", description="Security shimmer")
    title: Optional[str] = Field(None, description="Title on the pass")
    header: Optional[str] = Field(None, description="Header text")
    sub_header: Optional[str] = Field(None, alias="subHeader", description="Sub header text")


class Template(BaseModel):
    """Template model."""
    id: Optional[str] = Field(None, description="Template ID")
    name: str = Field(description="Human readable name of the template")
    description: str = Field(description="Template description")
    business_name: str = Field(alias="businessName", description="Name of the business")
    business_id: Optional[str] = Field(None, alias="businessId", description="Business ID")
    is_internal: Optional[bool] = Field(False, alias="isInternal", description="Public visibility")
    type: Optional[PassType] = Field(None, description="The type of pass")
    external_id: Optional[str] = Field(None, alias="externalId", description="External ID mapping")
    status: Optional[TemplateStatus] = Field(None, description="Template status")
    apple_wallet_settings: AppleWalletSettings = Field(alias="appleWalletSettings")
    google_wallet_settings: GoogleWalletSettings = Field(alias="googleWalletSettings")
    colours: TemplateColours = Field(description="Color configuration")
    images: TemplateImages = Field(description="Image configuration")
    barcode: TemplateBarcode = Field(description="Barcode configuration")
    card_expiry: Optional[TemplateCardExpiry] = Field(None, alias="cardExpiry", description="Card expiry config")
    form_id: Optional[str] = Field(None, alias="formId", description="Associated form ID")
    version: Optional[int] = Field(None, description="Template version")
    card_count: Optional[int] = Field(None, alias="cardCount", description="Number of active cards")
    downloads_count: Optional[int] = Field(None, alias="downloadsCount", description="Number of downloads")
    downloaded_apple_pass_count: Optional[int] = Field(None, alias="downloadedApplePassCount")
    downloaded_google_pass_count: Optional[int] = Field(None, alias="downloadedGooglePassCount")


# Card models  
class BaseCardPayload(BaseModel):
    """Base card payload with common fields."""
    email: Optional[str] = Field(None, description="Email address")
    phone: Optional[str] = Field(None, description="Mobile number")
    
    class Config:
        extra = "allow"  # Allow additional fields


class CardOwner(BaseModel):
    """Copy of card owner information."""
    id: str = Field(alias="id", description="ID of the card owner")
    first_name: Optional[str] = Field(None, alias="firstName", description="First name of the card owner")
    last_name: Optional[str] = Field(None, alias="lastName", description="Last name of the card owner")
    email: Optional[str] = Field(None, description="Email address of the card owner")
    phone: Optional[str] = Field(None, description="Phone number of the card owner")
    form_id: Optional[str] = Field(None, alias="formId", description="Form ID for card owner data")
    business_id: Optional[str] = Field(None, alias="businessId", description="Business ID")
    account_name: Optional[str] = Field(None, alias="accountName", description="Account name")
    user_type: Optional[str] = Field(None, alias="userType", description="User type")
    created_at: datetime = Field(alias="createdAt", description="Creation date")
    updated_at: Optional[datetime] = Field(None, alias="updatedAt", description="Update date")
    state: Optional[str] = Field(None, description="State of the card owner", examples=["VIC", "NSW", "QLD"])
    version: Optional[int] = Field(None, description="Version of the card owner data")
    
class Card(BaseModel):
    """Card model."""
    id: str = Field(description="ID of the pass")
    download_id: Optional[str] = Field(None, alias="downloadId", description="Download ID for landing page")
    apple_link: Optional[str] = Field(None, alias="appleLink", description="URL for the apple pass")
    google_link: Optional[str] = Field(None, alias="googleLink", description="URL for the google pass")
    samsung_link: Optional[str] = Field(None, alias="samsungLink", description="URL for the samsung pass")
    business_id: str = Field(alias="businessId", description="ID of the business")
    user_type: Optional[str] = Field(None, alias="userType", description="Type of user")
    created_at: datetime = Field(alias="createdAt", description="Date time card was created")
    updated_at: Optional[datetime] = Field(None, alias="updatedAt", description="Date time card was updated")
    google_pass_id: Optional[str] = Field(None, alias="googlePassId", description="ID of google pass")
    auth_token: Optional[str] = Field(None, alias="authToken", description="Apple device auth token")
    pass_type: Optional[str] = Field(None, alias="passType", description="Mobile wallet pass type")
    template_id: str = Field(alias="templateId", description="ID for the template used to create the card")
    data_fields: Optional[Dict[str, Any]] = Field(None, alias="dataFields", description="Data fields")
    form_id: str = Field(alias="formId", description="ID for field input form")
    pk_pass_id: Optional[str] = Field(None, alias="pkPassId", description="ID of Apple pass")
    barcode_value: Optional[str] = Field(None, alias="barcodeValue", description="Barcode value")
    apple_status: Optional[str] = Field(None, alias="appleStatus", description="Status in Apple Wallet")
    google_status: Optional[str] = Field(None, alias="googleStatus", description="Status in Google Wallet")
    card_owner_id: Optional[str] = Field(None, alias="cardOwnerId", description="ID of the card owner")
    status: CardStatus = Field(description="Activation status of the card")
    expiry: Optional[datetime] = Field(None, description="Expiry of card")
    barcode_link: Optional[str] = Field(None, alias="barcodeLink", description="Link to the barcode image")
    card_owner_copy: Optional[CardOwner] = Field(None, alias="cardOwnerCopy", description="Card owner copy")
    disable_qr: Optional[bool] = Field(None, alias="disableQR", description="Disable QR code")
    stripe_customer_id: Optional[str] = Field(None, alias="stripeCustomerId", description="Stripe customer ID")
    disable_download: Optional[bool] = Field(None, alias="disableDownload", description="Disable download")


# Sign up options and requests
class SignUpOptions(BaseModel):
    """Sign up options."""
    download_id: Optional[str] = Field(None, alias="downloadId", description="Specify download ID")
    password: Optional[str] = Field(None, description="Password for protected sign ups")
    email_type: Optional[EmailType] = Field(EmailType.STANDARD, alias="emailType", description="Email type")
    email_invitation_enabled: Optional[bool] = Field(False, alias="emailInvitationEnabled", description="Send email invitation")
    email_template: Optional[str] = Field(None, alias="emailTemplate", description="Email template to use")
    sms_invitation_enabled: Optional[bool] = Field(False, alias="smsInvitationEnabled", description="Send SMS invitation")
    sms_template: Optional[str] = Field(None, alias="smsTemplate", description="SMS template to use")
    source_email: Optional[str] = Field(None, alias="sourceEmail", description="From email address")
    no_pi: Optional[bool] = Field(False, alias="noPI", description="Disable PI requirement")


class PrivateSignUpRequest(BaseModel):
    """Private sign up request."""
    template_id: str = Field(alias="templateId", description="Template ID")
    tier: Optional[str] = Field(None, description="Tier selection for multi-tiered templates")
    card_payload: BaseCardPayload = Field(alias="cardPayload", description="Card data")
    options: Optional[SignUpOptions] = Field(None, description="Sign up options")


class SignUpResponse(BaseModel):
    """Sign up response."""
    card_id: str = Field(alias="cardId", description="ID of created card")
    success: bool = Field(description="Whether the request was successful")
    download_id: str = Field(alias="downloadId", description="ID for hosted landing page")


# Notification models
class NotificationRequest(BaseModel):
    """Notification request."""
    card_ids: List[str] = Field(alias="cardIds", description="Array of card IDs")
    notification: Dict[str, Any] = Field(description="Notification details")
    segments: Optional[Dict[str, Any]] = Field(None, description="Notification segments")
    template_ids: Optional[List[str]] = Field(None, alias="templateIds", description="Template IDs")
    options: Optional[Dict[str, Any]] = Field(None, description="Notification options")


class NotificationGroup(BaseModel):
    """Notification group model."""
    id: str = Field(description="Unique identifier for the notification group")
    title: str = Field(description="Title of the notification group")
    message: str = Field(description="Message content")
    participants_count: int = Field(alias="participantsCount", description="Number of participants")
    sent_via: List[Dict[str, Any]] = Field(alias="sentVia", description="Notification sending methods")
    send_time: datetime = Field(alias="sendTime", description="Send time")
    created_at: datetime = Field(alias="createdAt", description="Creation time")
    status: str = Field(description="Status of the notification group")
    business_id: str = Field(alias="businessId", description="Business ID")


# Scan models
class ScanRequest(BaseModel):
    """Scan request."""
    barcode_value: str = Field(alias="barcodeValue", description="Scanned barcode")
    business_id: Optional[str] = Field(None, alias="businessId", description="Business ID")


class Scan(BaseModel):
    """Scan model."""
    id: str = Field(description="Unique identifier for the scan event")
    account_name: Optional[str] = Field(None, alias="accountName", description="Account name")
    business_id: str = Field(alias="businessId", description="Business ID")
    card_id: str = Field(alias="cardId", description="Card ID that was scanned")
    card_owner_id: str = Field(alias="cardOwnerId", description="Card owner ID")
    created_at: datetime = Field(alias="createdAt", description="Scan creation time")
    created_by: str = Field(alias="createdBy", description="Creator identifier")
    device_id: Optional[str] = Field(None, alias="deviceId", description="Device ID")
    device_name: Optional[str] = Field(None, alias="deviceName", description="Device name")
    location: Optional[str] = Field(None, description="Physical location")
    template_id: str = Field(alias="templateId", description="Template ID")
    updated_at: datetime = Field(alias="updatedAt", description="Last update time")
    user_type: Optional[str] = Field(None, alias="userType", description="User type")
    data_fields: Optional[Dict[str, Any]] = Field(None, alias="dataFields", description="Structured scan data")
    form_id: str = Field(alias="formId", description="Form ID")
    scan_type: Optional[str] = Field(None, alias="scanType", description="Type of scan")
    status: CardStatus = Field(description="Scan status")


class ScanResponse(BaseModel):
    """Scan response."""
    card: Card = Field(description="Card information")
    card_owner: Dict[str, Any] = Field(alias="cardOwner", description="Card owner information")
    actions: Optional[Dict[str, Any]] = Field(None, description="Available actions")


# Certificate models
class CertificateUpload(BaseModel):
    """Certificate upload request."""
    certificate: str = Field(description="Base64 encoded certificate")
    description: Optional[str] = Field(None, description="Certificate description")


class Certificate(BaseModel):
    """Certificate model."""
    name: str = Field(description="Name of the certificate")
    apple_pass_type_identifier: Optional[str] = Field(None, alias="applePassTypeIdentifier")
    apple_team_identifier: Optional[str] = Field(None, alias="appleTeamIdentifier")
    type: str = Field(description="Type of pass")
    expiry_date: datetime = Field(alias="expiryDate", description="Expiry timestamp")


# Download models
class WelcomeDetails(BaseModel):
    """Welcome page details."""
    download_id: str = Field(alias="downloadId", description="Download ID")
    apple_link: str = Field(alias="appleLink", description="Apple pass link")
    google_link: str = Field(alias="googleLink", description="Google pass link")
    barcode_link: Optional[str] = Field(None, alias="barcodeLink", description="Barcode image link")
    samsung_link: Optional[str] = Field(None, alias="samsungLink", description="Samsung pass link")
    ui_config: Optional[Dict[str, Any]] = Field(None, alias="uiConfig", description="UI configuration")
    disable_qr: Optional[bool] = Field(None, alias="disableQR", description="Disable QR code")


# Form models
class FormField(BaseModel):
    """Form field model."""
    type: str = Field(description="Field type")
    format: Optional[str] = Field(None, description="Field format")
    label: str = Field(description="Field label")
    help_text: Optional[str] = Field(None, alias="helpText", description="Help text")
    name: str = Field(description="Field name")
    rules: List[str] = Field(description="Validation rules")
    usage: Optional[List[str]] = Field(None, description="Field usage")
    value: Optional[Union[str, int]] = Field(None, description="Field value")
    placeholder: Optional[str] = Field(None, description="Placeholder text")
    default_country_code: Optional[str] = Field(None, alias="defaultCountryCode", description="Default country code")
    options: Optional[List[Dict[str, str]]] = Field(None, description="Field options")


class Form(BaseModel):
    """Form model."""
    id: str = Field(description="Form ID")
    fields: List[FormField] = Field(description="Form fields")
    form_name: str = Field(alias="formName", description="Form name")
    business_id: str = Field(alias="businessId", description="Business ID")
    password_enabled: Optional[bool] = Field(False, alias="passwordEnabled", description="Password enabled")
    logo: Optional[str] = Field(None, description="Logo URL")
    title: Optional[str] = Field(None, description="Form title")
    description: Optional[str] = Field(None, description="Form description")
    style: Optional[Dict[str, Any]] = Field(None, description="Form style")
    connect_id_enabled: Optional[bool] = Field(False, alias="connectIDEnabled", description="ConnectID enabled")
    is_internal: Optional[bool] = Field(True, alias="isInternal", description="Internal visibility")
    template_id: Optional[str] = Field(None, alias="templateId", description="Template ID")
    status: TemplateStatus = Field(description="Form status")
    created_at: datetime = Field(alias="createdAt", description="Creation time")
    updated_at: datetime = Field(alias="updatedAt", description="Update time")
    created_by: str = Field(alias="createdBy", description="Creator ID")


# Business models
class Business(BaseModel):
    """Business model."""
    id: str = Field(description="Business ID")
    apple_team_identifier: Optional[str] = Field(None, alias="appleTeamIdentifier")
    business_name: str = Field(alias="businessName", description="Business name")
    card_count: Optional[int] = Field(None, alias="cardCount", description="Card count")
    card_limit: Optional[int] = Field(None, alias="cardLimit", description="Card limit")
    card_owner_count: Optional[int] = Field(None, alias="cardOwnerCount", description="Card owner count")
    cert_id: Optional[str] = Field(None, alias="certId", description="Certificate ID")
    created_at: datetime = Field(alias="createdAt", description="Creation time")
    email: str = Field(description="Business email")
    logo_url: Optional[str] = Field(None, alias="logoUrl", description="Logo URL")
    mailchimp: Optional[Dict[str, Any]] = Field(None, description="Mailchimp configuration")
    pass_type_identifier: Optional[str] = Field(None, alias="passTypeIdentifier")
    template_count: Optional[int] = Field(None, alias="templateCount", description="Template count")
    template_limit: Optional[int] = Field(None, alias="templateLimit", description="Template limit")
    tier: str = Field(description="Business tier")
    updated_at: datetime = Field(alias="updatedAt", description="Update time")


# User models
class User(BaseModel):
    """User model."""
    roles: List[str] = Field(description="User roles")
    api_access_allowed: bool = Field(alias="apiAccessAllowed", description="API access allowed")
    ui_dashboard_access: List[str] = Field(alias="uiDashboardAccess", description="UI dashboard access")
    picture: str = Field(description="Profile picture URL")
    username: str = Field(description="Username")
    email: str = Field(description="Email address")
    created_at: datetime = Field(alias="createdAt", description="Creation time")
    last_login_at: datetime = Field(alias="lastLoginAt", description="Last login time")


# Webhook models
class WebhookRegistrationRequest(BaseModel):
    """Webhook registration request."""
    webhook_url: str = Field(alias="webhookUrl", description="Webhook endpoint URL")
    method: str = Field(description="HTTP method", default="POST")
    auth_type: str = Field(alias="authType", description="Authentication type")
    auth_config: Dict[str, Any] = Field(alias="authConfig", description="Authentication configuration")
    events: List[str] = Field(description="Supported events")
    provider: Optional[str] = Field(None, description="Provider schema")


# Export models
class ExportRequest(BaseModel):
    """Export CSV request."""
    table_name: str = Field(alias="tableName", description="Table name to export")
    start_date_time: Optional[datetime] = Field(None, alias="startDateTime", description="Start date time")
    end_date_time: Optional[datetime] = Field(None, alias="endDateTime", description="End date time")
    template_id: Optional[str] = Field(None, alias="templateId", description="Template ID")


class ExportResponse(BaseModel):
    """Export CSV response."""
    signed_url: str = Field(alias="signedUrl", description="Download URL")
    expiry_time: datetime = Field(alias="expiryTime", description="URL expiry time")
    start_date_time: Optional[datetime] = Field(None, alias="startDateTime", description="Start date time")
    end_date_time: Optional[datetime] = Field(None, alias="endDateTime", description="End date time")
