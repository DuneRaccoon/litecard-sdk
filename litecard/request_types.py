"""
Request payload types for the Litecard API.

This module contains TypedDict classes that define the structure of request payloads
for various API endpoints. These provide better IDE support and type checking
for developers using the SDK.
"""

from typing import Any, Dict, List, Optional, Union
from typing_extensions import TypedDict, NotRequired
from datetime import datetime

# Card-related request types

class CreateCardRequest(TypedDict):
    """Request payload for creating a card."""
    templateId: str
    cardPayload: Dict[str, Any]  # Will use BaseCardPayload model
    options: NotRequired[Dict[str, Any]]  # Will use SignUpOptions model
    tier: NotRequired[str]
    templateOverrides: NotRequired[Dict[str, Any]]  # Will use TemplateOverridesV1 model


class UpdateCardRequest(TypedDict):
    """Request payload for updating a card."""
    cardId: str
    cardPayload: NotRequired[Dict[str, Any]]
    syncStaticFields: NotRequired[bool]
    tier: NotRequired[str]
    templateOverrides: NotRequired[Dict[str, Any]]


class SetCardStatusRequest(TypedDict):
    """Request payload for setting card status."""
    cardId: str
    status: str  # Will use CardStatus enum


class CreateCardAndTemplateRequest(TypedDict):
    """Request payload for creating both card and template."""
    templatePayload: Dict[str, Any]
    cardPayload: Dict[str, Any]
    options: NotRequired[Dict[str, Any]]


class GenerateBusinessCardRequest(TypedDict):
    """Request payload for generating a business card."""
    templateId: str
    cardPayload: Dict[str, Any]
    businessCard: Dict[str, Any]
    options: NotRequired[Dict[str, Any]]


# Template-related request types

class CreateTemplateRequest(TypedDict):
    """Request payload for creating a template."""
    name: str
    description: str
    businessName: str
    type: NotRequired[str]  # PassType enum
    appleWalletSettings: Dict[str, Any]
    googleWalletSettings: Dict[str, Any]
    colours: Dict[str, Any]
    images: Dict[str, Any]
    barcode: Dict[str, Any]
    cardExpiry: NotRequired[Dict[str, Any]]
    formId: NotRequired[str]


class UpdateTemplateRequest(TypedDict):
    """Request payload for updating a template."""
    id: str
    name: NotRequired[str]
    description: NotRequired[str]
    businessName: NotRequired[str]
    type: NotRequired[str]
    appleWalletSettings: NotRequired[Dict[str, Any]]
    googleWalletSettings: NotRequired[Dict[str, Any]]
    colours: NotRequired[Dict[str, Any]]
    images: NotRequired[Dict[str, Any]]
    barcode: NotRequired[Dict[str, Any]]
    cardExpiry: NotRequired[Dict[str, Any]]


class SetTemplateStatusRequest(TypedDict):
    """Request payload for setting template status."""
    status: str  # TemplateStatus enum


# Notification-related request types

class NotificationPayload(TypedDict):
    """Notification content payload."""
    title: str
    message: str
    url: NotRequired[str]
    imageUrl: NotRequired[str]
    deepLinkUrl: NotRequired[str]


class NotificationSegments(TypedDict):
    """Notification segmentation options."""
    includeApple: NotRequired[bool]
    includeGoogle: NotRequired[bool]
    includeSamsung: NotRequired[bool]
    includeEmail: NotRequired[bool]
    includeSms: NotRequired[bool]


class NotificationOptions(TypedDict):
    """Notification sending options."""
    scheduleTime: NotRequired[datetime]
    priority: NotRequired[str]  # HIGH, NORMAL, LOW
    soundEnabled: NotRequired[bool]
    vibrationEnabled: NotRequired[bool]


class SendNotificationRequest(TypedDict):
    """Request payload for sending notifications."""
    cardIds: NotRequired[List[str]]
    notification: NotificationPayload
    segments: NotRequired[NotificationSegments]
    templateIds: NotRequired[List[str]]
    options: NotRequired[NotificationOptions]


class SendReminderRequest(TypedDict):
    """Request payload for sending email reminders."""
    emailTemplate: str
    templateId: NotRequired[str]


# Scan-related request types

class ScanCardRequest(TypedDict):
    """Request payload for scanning a card."""
    barcodeValue: str
    businessId: NotRequired[str]


class ScanAction(TypedDict):
    """Action to apply during scanning."""
    actionType: str  # e.g., "POINTS_ADD", "VISIT_INCREMENT", etc.
    value: NotRequired[Union[int, float, str]]
    fieldName: NotRequired[str]
    parameters: NotRequired[Dict[str, Any]]


class ApplyTemplateActionsRequest(TypedDict):
    """Request payload for applying template actions."""
    cardId: str
    actions: List[ScanAction]


# User and Business request types

class CreateBusinessRequest(TypedDict):
    """Request payload for creating a business."""
    businessName: str
    email: str
    logoUrl: NotRequired[str]
    tier: NotRequired[str]


class UpdateBusinessRequest(TypedDict):
    """Request payload for updating a business."""
    businessName: NotRequired[str]
    email: NotRequired[str]
    logoUrl: NotRequired[str]


# Webhook-related request types

class WebhookAuthConfig(TypedDict):
    """Webhook authentication configuration."""
    apiKey: NotRequired[str]
    bearerToken: NotRequired[str]
    basicAuth: NotRequired[Dict[str, str]]  # {"username": "...", "password": "..."}
    customHeaders: NotRequired[Dict[str, str]]


class RegisterWebhookRequest(TypedDict):
    """Request payload for registering a webhook."""
    webhookUrl: str
    method: NotRequired[str]  # Default: "POST"
    authType: str  # "API_KEY", "BEARER_TOKEN", "BASIC_AUTH", "NONE"
    authConfig: WebhookAuthConfig
    events: List[str]  # Available events: "CARD_CREATED", "CARD_SCANNED", "CARD_DOWNLOADED", etc.
    provider: NotRequired[str]  # Optional provider schema


class DeleteWebhookRequest(TypedDict):
    """Request payload for deleting a webhook."""
    webhookId: str


# Export-related request types

class ExportCSVRequest(TypedDict):
    """Request payload for exporting CSV data."""
    tableName: str
    startDateTime: NotRequired[datetime]
    endDateTime: NotRequired[datetime]
    templateId: NotRequired[str]


# Form-related request types

class CreateFormRequest(TypedDict):
    """Request payload for creating a form."""
    fields: List[Dict[str, Any]]
    formName: str
    businessId: str
    passwordEnabled: NotRequired[bool]
    logo: NotRequired[str]
    title: NotRequired[str]
    description: NotRequired[str]
    style: NotRequired[Dict[str, Any]]
    connectIDEnabled: NotRequired[bool]
    isInternal: NotRequired[bool]
    templateId: NotRequired[str]


class UpdateFormRequest(TypedDict):
    """Request payload for updating a form."""
    id: str
    fields: NotRequired[List[Dict[str, Any]]]
    formName: NotRequired[str]
    passwordEnabled: NotRequired[bool]
    logo: NotRequired[str]
    title: NotRequired[str]
    description: NotRequired[str]
    style: NotRequired[Dict[str, Any]]
    connectIDEnabled: NotRequired[bool]
    isInternal: NotRequired[bool]


# Certificate-related request types

class UploadCertificateRequest(TypedDict):
    """Request payload for uploading a certificate."""
    certificate: str  # Base64 encoded
    description: NotRequired[str]


# Pass-related request types

class CreatePassRequest(TypedDict):
    """Request payload for creating a pass."""
    templateId: str
    cardId: str
    customFields: NotRequired[Dict[str, Any]]


# Generic pagination parameters

class PaginationParams(TypedDict):
    """Common pagination parameters."""
    limit: NotRequired[int]
    next: NotRequired[str]


# Common query parameters

class TemplateQueryParams(PaginationParams):
    """Query parameters for template endpoints."""
    status: NotRequired[str]
    businessId: NotRequired[str]


class CardQueryParams(PaginationParams):
    """Query parameters for card endpoints."""
    templateId: NotRequired[str]
    status: NotRequired[str]
    cardOwnerId: NotRequired[str]


class ScanQueryParams(PaginationParams):
    """Query parameters for scan endpoints."""
    templateId: NotRequired[str]
    cardId: NotRequired[str]
    startDate: NotRequired[datetime]
    endDate: NotRequired[datetime]


# Response types (for method return type annotations)

class SuccessResponse(TypedDict):
    """Generic success response."""
    success: bool
    message: NotRequired[str]


class ErrorResponse(TypedDict):
    """Generic error response."""
    errorCode: str
    message: NotRequired[str]


class PaginatedListResponse(TypedDict):
    """Paginated list response structure."""
    items: List[Dict[str, Any]]
    nextToken: NotRequired[str]
    hasMore: NotRequired[bool]
    total: NotRequired[int]


# Statistics and analytics response types

class DownloadCountResponse(TypedDict):
    """Response for download count statistics."""
    appleCount: int
    googleCount: int
    samsungCount: NotRequired[int]
    totalCount: int


class TrendDataPoint(TypedDict):
    """Single data point in trend data."""
    date: str
    value: int


class DownloadTrendResponse(TypedDict):
    """Response for download trend data."""
    trend: List[TrendDataPoint]
    summary: Dict[str, Any]
