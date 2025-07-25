"""Contains all the data models used in inputs/outputs"""

from .aggregated_billing_statistics import AggregatedBillingStatistics
from .aggregated_notifications_statistics import AggregatedNotificationsStatistics
from .aggregated_scans_statistics import AggregatedScansStatistics
from .aggregated_scans_statistics_templates_item import AggregatedScansStatisticsTemplatesItem
from .aggregated_scans_statistics_templates_item_additional_property import (
    AggregatedScansStatisticsTemplatesItemAdditionalProperty,
)
from .analytics_billing_results_schema import AnalyticsBillingResultsSchema
from .analytics_billing_results_schema_results import AnalyticsBillingResultsSchemaResults
from .analytics_billing_results_schema_results_query_parameters import (
    AnalyticsBillingResultsSchemaResultsQueryParameters,
)
from .analytics_notifications_results_schema import AnalyticsNotificationsResultsSchema
from .analytics_notifications_results_schema_results import AnalyticsNotificationsResultsSchemaResults
from .analytics_notifications_results_schema_results_query_parameters import (
    AnalyticsNotificationsResultsSchemaResultsQueryParameters,
)
from .analytics_scans_results_schema import AnalyticsScansResultsSchema
from .analytics_scans_results_schema_results import AnalyticsScansResultsSchemaResults
from .analytics_scans_results_schema_results_query_parameters import AnalyticsScansResultsSchemaResultsQueryParameters
from .apple_app_linking_settings import AppleAppLinkingSettings
from .apple_date_time_style_v1 import AppleDateTimeStyleV1
from .apple_number_style_v1 import AppleNumberStyleV1
from .authenticate_x_user_tenant import AuthenticateXUserTenant
from .authentication_request_body import AuthenticationRequestBody
from .authentication_response import AuthenticationResponse
from .base_card_payload import BaseCardPayload
from .base_template_v1 import BaseTemplateV1
from .base_template_v1_tiers import BaseTemplateV1Tiers
from .base_template_v1_type import BaseTemplateV1Type
from .business import Business
from .business_card_options import BusinessCardOptions
from .business_card_request_body import BusinessCardRequestBody
from .business_card_response_200 import BusinessCardResponse200
from .business_mailchimp import BusinessMailchimp
from .cancel_notifications_by_group_id_v1_response_200 import CancelNotificationsByGroupIdV1Response200
from .card import Card
from .card_card_owner_copy import CardCardOwnerCopy
from .card_data_fields import CardDataFields
from .card_mapping_payload import CardMappingPayload
from .card_owner import CardOwner
from .card_owner_request_body import CardOwnerRequestBody
from .card_owners_scan_request_body import CardOwnersScanRequestBody
from .card_status import CardStatus
from .card_upload_group_v1 import CardUploadGroupV1
from .card_upload_group_v1_count import CardUploadGroupV1Count
from .card_upload_group_v1_status import CardUploadGroupV1Status
from .card_upload_v1 import CardUploadV1
from .card_upload_v1_card_payload import CardUploadV1CardPayload
from .card_upload_v1_status import CardUploadV1Status
from .cards_upload_csvv1_body import CardsUploadCSVV1Body
from .cards_upload_csvv1_body_header_mappings import CardsUploadCSVV1BodyHeaderMappings
from .cards_upload_csvv1_response_200 import CardsUploadCSVV1Response200
from .certificate import Certificate
from .certificate_upload_v1 import CertificateUploadV1
from .certificate_upload_v1_response_200 import CertificateUploadV1Response200
from .column_values import ColumnValues
from .coupon import Coupon
from .coupon_redemption import CouponRedemption
from .create_coupon_response_schema import CreateCouponResponseSchema
from .create_pass_template_request_body import CreatePassTemplateRequestBody
from .create_pass_template_response_body import CreatePassTemplateResponseBody
from .create_pass_template_response_body_card_details import CreatePassTemplateResponseBodyCardDetails
from .create_profile_body import CreateProfileBody
from .create_scan_body import CreateScanBody
from .create_sub_business_request_body import CreateSubBusinessRequestBody
from .create_template_v1 import CreateTemplateV1
from .create_template_v1_barcode import CreateTemplateV1Barcode
from .create_template_v1_barcode_type import CreateTemplateV1BarcodeType
from .create_template_v1_colours import CreateTemplateV1Colours
from .create_template_v1_colours_samsung_font import CreateTemplateV1ColoursSamsungFont
from .create_template_v1_images import CreateTemplateV1Images
from .create_template_v1_response_201 import CreateTemplateV1Response201
from .create_template_v1_tiers import CreateTemplateV1Tiers
from .create_template_v1_type import CreateTemplateV1Type
from .custom_form_design_background_styles import CustomFormDesignBackgroundStyles
from .custom_form_design_common_styles import CustomFormDesignCommonStyles
from .custom_form_design_footer_section import CustomFormDesignFooterSection
from .custom_form_design_left_section import CustomFormDesignLeftSection
from .custom_form_design_left_section_styles import CustomFormDesignLeftSectionStyles
from .custom_form_design_right_section import CustomFormDesignRightSection
from .custom_form_design_right_section_form_styles import CustomFormDesignRightSectionFormStyles
from .custom_form_design_schema import CustomFormDesignSchema
from .customer_webhook import CustomerWebhook
from .customer_webhook_auth_config import CustomerWebhookAuthConfig
from .customer_webhook_auth_type import CustomerWebhookAuthType
from .customer_webhook_events_item import CustomerWebhookEventsItem
from .customer_webhook_method import CustomerWebhookMethod
from .database_meta_data import DatabaseMetaData
from .date_time_style import DateTimeStyle
from .delete_card_owner_response_schema import DeleteCardOwnerResponseSchema
from .delete_coupon_response_schema import DeleteCouponResponseSchema
from .delete_scan_v1_response_200 import DeleteScanV1Response200
from .delete_scan_v1_response_schema import DeleteScanV1ResponseSchema
from .delete_webhook_response_200 import DeleteWebhookResponse200
from .download_csv_response import DownloadCsvResponse
from .email_reminders_request_body import EmailRemindersRequestBody
from .email_reminders_request_body_email_template import EmailRemindersRequestBodyEmailTemplate
from .error_response import ErrorResponse
from .export_csv_request_body import ExportCsvRequestBody
from .export_csv_request_body_dynamic_columns_item import ExportCsvRequestBodyDynamicColumnsItem
from .export_csv_request_body_table_name import ExportCsvRequestBodyTableName
from .export_csv_v1_request_body import ExportCsvV1RequestBody
from .export_csv_v1_request_body_table_name import ExportCsvV1RequestBodyTableName
from .external_call_back_v1_response_200 import ExternalCallBackV1Response200
from .external_callback_v1 import ExternalCallbackV1
from .form import Form
from .form_field_usage_item import FormFieldUsageItem
from .form_fields import FormFields
from .form_fields_options_item import FormFieldsOptionsItem
from .form_fields_type import FormFieldsType
from .form_fields_v1 import FormFieldsV1
from .form_fields_v1_mapping_type import FormFieldsV1MappingType
from .form_fields_v1_options_item import FormFieldsV1OptionsItem
from .form_fields_v1_rules_item import FormFieldsV1RulesItem
from .form_fields_v1_type import FormFieldsV1Type
from .form_mailchimp_settings import FormMailchimpSettings
from .form_mailchimp_settings_merge_field_mapping import FormMailchimpSettingsMergeFieldMapping
from .form_request import FormRequest
from .form_request_status import FormRequestStatus
from .form_request_style import FormRequestStyle
from .form_style import FormStyle
from .form_v1 import FormV1
from .form_v1_mailchimp_settings import FormV1MailchimpSettings
from .form_v1_mailchimp_settings_merge_field_format import FormV1MailchimpSettingsMergeFieldFormat
from .form_v1_mailchimp_settings_merge_field_mapping import FormV1MailchimpSettingsMergeFieldMapping
from .form_v1_status import FormV1Status
from .form_v1_style import FormV1Style
from .generate_upload_url_response_200 import GenerateUploadURLResponse200
from .get_backlink_v1_response_200 import GetBacklinkV1Response200
from .get_backlinks_response import GetBacklinksResponse
from .get_card_response_200 import GetCardResponse200
from .get_cards_of_card_owner_response_200 import GetCardsOfCardOwnerResponse200
from .get_certificates_v1_response_200 import GetCertificatesV1Response200
from .get_csrv1_response_200 import GetCSRV1Response200
from .get_template_v1_response_200 import GetTemplateV1Response200
from .get_welcome_v1_response_200 import GetWelcomeV1Response200
from .google_app_linking_settings import GoogleAppLinkingSettings
from .health_check_response_200 import HealthCheckResponse200
from .image_content import ImageContent
from .image_content_image_type import ImageContentImageType
from .image_upload_response import ImageUploadResponse
from .list_card_owners_response import ListCardOwnersResponse
from .list_card_uploads_v1_response_200 import ListCardUploadsV1Response200
from .list_cards_by_template_id_response_200 import ListCardsByTemplateIdResponse200
from .list_cards_detail import ListCardsDetail
from .list_cards_detail_data_fields import ListCardsDetailDataFields
from .list_cards_upload_groups_v1_response_200 import ListCardsUploadGroupsV1Response200
from .list_certificates_response_v1 import ListCertificatesResponseV1
from .list_forms_result_item import ListFormsResultItem
from .list_forms_result_item_id import ListFormsResultItemId
from .list_forms_result_item_id_style import ListFormsResultItemIdStyle
from .list_notification_groups_response import ListNotificationGroupsResponse
from .list_pass_of_card_owner_request_v1 import ListPassOfCardOwnerRequestV1
from .list_pass_request_v1 import ListPassRequestV1
from .list_passes_result_item import ListPassesResultItem
from .list_passes_result_item_id import ListPassesResultItemId
from .list_passes_result_item_id_data_fields import ListPassesResultItemIdDataFields
from .list_passes_v1_response_200 import ListPassesV1Response200
from .list_scans_v1_response_200 import ListScansV1Response200
from .list_templates_v1_response_200 import ListTemplatesV1Response200
from .list_users_response_200 import ListUsersResponse200
from .mailchimp_tag_settings import MailchimpTagSettings
from .nft_request_body import NFTRequestBody
from .nft_request_body_metadata import NFTRequestBodyMetadata
from .nft_request_body_metadata_urls_item import NFTRequestBodyMetadataUrlsItem
from .nft_request_body_nft_page import NFTRequestBodyNftPage
from .nft_request_body_nft_page_urls_item import NFTRequestBodyNftPageUrlsItem
from .notification_group import NotificationGroup
from .notification_group_sent_via_item import NotificationGroupSentViaItem
from .notification_group_sent_via_item_platform import NotificationGroupSentViaItemPlatform
from .notification_group_sent_via_item_type import NotificationGroupSentViaItemType
from .notification_group_status import NotificationGroupStatus
from .notification_segments import NotificationSegments
from .notification_settings import NotificationSettings
from .notification_settings_trigger import NotificationSettingsTrigger
from .notification_settings_type import NotificationSettingsType
from .notification_v1 import NotificationV1
from .notification_v1_notification import NotificationV1Notification
from .notification_v1_options import NotificationV1Options
from .notification_v1_options_email_type import NotificationV1OptionsEmailType
from .onboard_mailchimp_body import OnboardMailchimpBody
from .onboard_mailchimp_body_additional_merge_fields_item import OnboardMailchimpBodyAdditionalMergeFieldsItem
from .pass_count_details import PassCountDetails
from .pass_count_details_for_template import PassCountDetailsForTemplate
from .pass_counts_for_template import PassCountsForTemplate
from .pass_counts_for_template_duration import PassCountsForTemplateDuration
from .pass_counts_history import PassCountsHistory
from .pass_counts_history_duration import PassCountsHistoryDuration
from .pass_download_trend_v1_response_200 import PassDownloadTrendV1Response200
from .pass_downloads_count_v1_duration import PassDownloadsCountV1Duration
from .pass_trend_details import PassTrendDetails
from .payment_and_sign_up_response_schema import PaymentAndSignUpResponseSchema
from .private_resend_pass_request import PrivateResendPassRequest
from .private_resend_pass_request_email_type import PrivateResendPassRequestEmailType
from .private_sign_up_request_body import PrivateSignUpRequestBody
from .profile import Profile
from .public_redeem_request_body import PublicRedeemRequestBody
from .public_redeem_request_body_update_payload import PublicRedeemRequestBodyUpdatePayload
from .public_resend_pass_request import PublicResendPassRequest
from .public_scan_barcode_v1_request_body import PublicScanBarcodeV1RequestBody
from .public_scan_v1_response_200 import PublicScanV1Response200
from .public_sign_up_request_body import PublicSignUpRequestBody
from .rate_limit import RateLimit
from .rate_limit_rule import RateLimitRule
from .rate_limit_v1_type_0_limit_type import RateLimitV1Type0LimitType
from .rate_limit_v1_type_0_rule import RateLimitV1Type0Rule
from .rate_limit_v1_type_1_limit_type import RateLimitV1Type1LimitType
from .rate_limit_v1_type_1_rule_date_limit import RateLimitV1Type1RuleDateLimit
from .rate_limit_v1_type_1_rule_date_limit_measurement import RateLimitV1Type1RuleDateLimitMeasurement
from .register_business_request_body import RegisterBusinessRequestBody
from .register_business_response import RegisterBusinessResponse
from .register_webhook_response_201 import RegisterWebhookResponse201
from .response_body import ResponseBody
from .scan import Scan
from .scan_barcode_v1_request_body import ScanBarcodeV1RequestBody
from .scan_check_in_request_body import ScanCheckInRequestBody
from .scan_data_fields import ScanDataFields
from .scan_redemption_request_body import ScanRedemptionRequestBody
from .scan_request_body import ScanRequestBody
from .scan_response_schema import ScanResponseSchema
from .scan_response_schema_actions import ScanResponseSchemaActions
from .scan_response_schema_actions_additional_property import ScanResponseSchemaActionsAdditionalProperty
from .scan_response_schema_card import ScanResponseSchemaCard
from .scan_response_schema_card_data_fields import ScanResponseSchemaCardDataFields
from .scan_response_schema_card_owner import ScanResponseSchemaCardOwner
from .scan_response_schema_card_status import ScanResponseSchemaCardStatus
from .scan_scan_type import ScanScanType
from .scan_status import ScanStatus
from .scan_v1_response_200 import ScanV1Response200
from .scan_v1_response_schema import ScanV1ResponseSchema
from .scan_v1_response_schema_card import ScanV1ResponseSchemaCard
from .scan_v1_response_schema_card_card_owner_copy import ScanV1ResponseSchemaCardCardOwnerCopy
from .scan_v1_response_schema_card_data_fields import ScanV1ResponseSchemaCardDataFields
from .scan_v1_response_schema_card_owner import ScanV1ResponseSchemaCardOwner
from .scan_v1_response_schema_card_status import ScanV1ResponseSchemaCardStatus
from .schedule_task_v1 import ScheduleTaskV1
from .schedule_task_v1_response_200 import ScheduleTaskV1Response200
from .send_notification_queue_v1_response_200 import SendNotificationQueueV1Response200
from .send_notification_request_body import SendNotificationRequestBody
from .send_notification_request_body_email_type import SendNotificationRequestBodyEmailType
from .send_notification_v1_response_200 import SendNotificationV1Response200
from .send_reminders_response_200 import SendRemindersResponse200
from .set_card_status_body import SetCardStatusBody
from .set_card_status_body_status import SetCardStatusBodyStatus
from .set_card_status_response_200 import SetCardStatusResponse200
from .set_template_status_body import SetTemplateStatusBody
from .set_template_status_body_status import SetTemplateStatusBodyStatus
from .set_template_status_response_200 import SetTemplateStatusResponse200
from .settings_v1 import SettingsV1
from .settings_v1_external_provider import SettingsV1ExternalProvider
from .settings_v1_external_system_config import SettingsV1ExternalSystemConfig
from .settings_v1_primary_contact import SettingsV1PrimaryContact
from .settings_v1_source_email import SettingsV1SourceEmail
from .shopfify_settings import ShopfifySettings
from .sign_up_options import SignUpOptions
from .sign_up_options_email_type import SignUpOptionsEmailType
from .sign_up_options_source_email import SignUpOptionsSourceEmail
from .sign_up_response_schema import SignUpResponseSchema
from .social_media import SocialMedia
from .spin_to_win_response import SpinToWinResponse
from .spin_to_win_response_prize import SpinToWinResponsePrize
from .stripe_checkout_body import StripeCheckoutBody
from .stripe_customer_portal_body import StripeCustomerPortalBody
from .stripe_settings import StripeSettings
from .stripe_settings_type import StripeSettingsType
from .sub_business_roles import SubBusinessRoles
from .sub_business_summary import SubBusinessSummary
from .table_column import TableColumn
from .table_column_format import TableColumnFormat
from .table_column_groups import TableColumnGroups
from .table_column_groups_additional_property import TableColumnGroupsAdditionalProperty
from .table_column_groups_additional_property_mappings import TableColumnGroupsAdditionalPropertyMappings
from .table_column_usage_item import TableColumnUsageItem
from .table_config import TableConfig
from .table_config_cards_table import TableConfigCardsTable
from .template_action_condition import TemplateActionCondition
from .template_action_condition_v1 import TemplateActionConditionV1
from .template_action_params import TemplateActionParams
from .template_action_params_v1 import TemplateActionParamsV1
from .template_action_params_v1_post_calc import TemplateActionParamsV1PostCalc
from .template_action_params_v1_post_calc_modifier import TemplateActionParamsV1PostCalcModifier
from .template_actions import TemplateActions
from .template_actions_additional_property import TemplateActionsAdditionalProperty
from .template_actions_request_body import TemplateActionsRequestBody
from .template_actions_request_body_actions_item import TemplateActionsRequestBodyActionsItem
from .template_actions_response_200 import TemplateActionsResponse200
from .template_actions_response_schema import TemplateActionsResponseSchema
from .template_actions_v1 import TemplateActionsV1
from .template_actions_v1_additional_property import TemplateActionsV1AdditionalProperty
from .template_app_linking import TemplateAppLinking
from .template_apple_wallet_settings_v1 import TemplateAppleWalletSettingsV1
from .template_apple_wallet_settings_v1_pass_type import TemplateAppleWalletSettingsV1PassType
from .template_barcode import TemplateBarcode
from .template_barcode_v1 import TemplateBarcodeV1
from .template_barcode_v1_type import TemplateBarcodeV1Type
from .template_card_expiry_type_0 import TemplateCardExpiryType0
from .template_card_expiry_type_0_expiry_type import TemplateCardExpiryType0ExpiryType
from .template_card_expiry_type_1 import TemplateCardExpiryType1
from .template_card_expiry_type_1_expiry_type import TemplateCardExpiryType1ExpiryType
from .template_card_expiry_type_2_expiry_type import TemplateCardExpiryType2ExpiryType
from .template_card_expiry_type_2_from_activation import TemplateCardExpiryType2FromActivation
from .template_card_expiry_type_2_from_activation_measurement import TemplateCardExpiryType2FromActivationMeasurement
from .template_card_expiry_type_3 import TemplateCardExpiryType3
from .template_card_expiry_type_3_expiry_type import TemplateCardExpiryType3ExpiryType
from .template_card_expiry_v1_type_0 import TemplateCardExpiryV1Type0
from .template_card_expiry_v1_type_0_expiry_type import TemplateCardExpiryV1Type0ExpiryType
from .template_card_expiry_v1_type_1 import TemplateCardExpiryV1Type1
from .template_card_expiry_v1_type_1_expiry_type import TemplateCardExpiryV1Type1ExpiryType
from .template_card_expiry_v1_type_2_expiry_type import TemplateCardExpiryV1Type2ExpiryType
from .template_card_expiry_v1_type_2_from_activation import TemplateCardExpiryV1Type2FromActivation
from .template_card_expiry_v1_type_2_from_activation_measurement import (
    TemplateCardExpiryV1Type2FromActivationMeasurement,
)
from .template_card_expiry_v1_type_2_from_activation_timezone import TemplateCardExpiryV1Type2FromActivationTimezone
from .template_card_expiry_v1_type_3 import TemplateCardExpiryV1Type3
from .template_card_expiry_v1_type_3_expiry_type import TemplateCardExpiryV1Type3ExpiryType
from .template_certificates_v1 import TemplateCertificatesV1
from .template_certificates_v1_apple_settings import TemplateCertificatesV1AppleSettings
from .template_certificates_v1_google_settings import TemplateCertificatesV1GoogleSettings
from .template_certificates_v1_nfc import TemplateCertificatesV1Nfc
from .template_certificates_v1_nfc_payload_type import TemplateCertificatesV1NfcPayloadType
from .template_colours import TemplateColours
from .template_colours_v1 import TemplateColoursV1
from .template_colours_v1_samsung_font import TemplateColoursV1SamsungFont
from .template_data_field_v1 import TemplateDataFieldV1
from .template_data_field_v1_apple_field_settings import TemplateDataFieldV1AppleFieldSettings
from .template_data_field_v1_apple_field_settings_apple_field_type import (
    TemplateDataFieldV1AppleFieldSettingsAppleFieldType,
)
from .template_data_field_v1_apple_field_settings_text_alignment import (
    TemplateDataFieldV1AppleFieldSettingsTextAlignment,
)
from .template_data_field_v1_form_field_settings import TemplateDataFieldV1FormFieldSettings
from .template_data_field_v1_form_field_settings_data_type import TemplateDataFieldV1FormFieldSettingsDataType
from .template_data_field_v1_form_field_settings_external_provider_mapping import (
    TemplateDataFieldV1FormFieldSettingsExternalProviderMapping,
)
from .template_data_field_v1_form_field_settings_options_item import TemplateDataFieldV1FormFieldSettingsOptionsItem
from .template_data_field_v1_form_field_settings_rules_item import TemplateDataFieldV1FormFieldSettingsRulesItem
from .template_data_field_v1_formatter import TemplateDataFieldV1Formatter
from .template_data_field_v1_front_end_mapping_item import TemplateDataFieldV1FrontEndMappingItem
from .template_data_field_v1_google_field_settings import TemplateDataFieldV1GoogleFieldSettings
from .template_data_field_v1_google_field_settings_field_type import TemplateDataFieldV1GoogleFieldSettingsFieldType
from .template_data_field_v1_google_field_settings_google_field_type import (
    TemplateDataFieldV1GoogleFieldSettingsGoogleFieldType,
)
from .template_data_field_v1_samsung_field_settings import TemplateDataFieldV1SamsungFieldSettings
from .template_data_field_v1_samsung_field_settings_samsung_field_type import (
    TemplateDataFieldV1SamsungFieldSettingsSamsungFieldType,
)
from .template_google_wallet_settings_v1 import TemplateGoogleWalletSettingsV1
from .template_google_wallet_settings_v1_event_ticket import TemplateGoogleWalletSettingsV1EventTicket
from .template_google_wallet_settings_v1_event_ticket_confirmation_code_label import (
    TemplateGoogleWalletSettingsV1EventTicketConfirmationCodeLabel,
)
from .template_google_wallet_settings_v1_event_ticket_gate_label import (
    TemplateGoogleWalletSettingsV1EventTicketGateLabel,
)
from .template_google_wallet_settings_v1_event_ticket_row_label import TemplateGoogleWalletSettingsV1EventTicketRowLabel
from .template_google_wallet_settings_v1_event_ticket_seat_label import (
    TemplateGoogleWalletSettingsV1EventTicketSeatLabel,
)
from .template_google_wallet_settings_v1_event_ticket_section_label import (
    TemplateGoogleWalletSettingsV1EventTicketSectionLabel,
)
from .template_google_wallet_settings_v1_multiple_devices_and_users_status import (
    TemplateGoogleWalletSettingsV1MultipleDevicesAndUsersStatus,
)
from .template_google_wallet_settings_v1_offer import TemplateGoogleWalletSettingsV1Offer
from .template_google_wallet_settings_v1_offer_redemption_channel import (
    TemplateGoogleWalletSettingsV1OfferRedemptionChannel,
)
from .template_google_wallet_settings_v1_pass_type import TemplateGoogleWalletSettingsV1PassType
from .template_images import TemplateImages
from .template_images_v1 import TemplateImagesV1
from .template_link_v1 import TemplateLinkV1
from .template_link_v1_type import TemplateLinkV1Type
from .template_locations_v1_item import TemplateLocationsV1Item
from .template_locations_v1_item_apple import TemplateLocationsV1ItemApple
from .template_locations_v1_item_samsung import TemplateLocationsV1ItemSamsung
from .template_notification_fields import TemplateNotificationFields
from .template_notification_fields_apple_text_alignment import TemplateNotificationFieldsAppleTextAlignment
from .template_overrides_v1 import TemplateOverridesV1
from .template_pass_download_trend_v1_response_200 import TemplatePassDownloadTrendV1Response200
from .template_pass_downloads_count_v1_duration import TemplatePassDownloadsCountV1Duration
from .template_request_status import TemplateRequestStatus
from .template_response import TemplateResponse
from .template_samsung_wallet_settings_v1 import TemplateSamsungWalletSettingsV1
from .template_samsung_wallet_settings_v1_customer_service_info import (
    TemplateSamsungWalletSettingsV1CustomerServiceInfo,
)
from .template_samsung_wallet_settings_v1_pass_type import TemplateSamsungWalletSettingsV1PassType
from .template_usage_v1_item import TemplateUsageV1Item
from .template_v1 import TemplateV1
from .template_v1_status import TemplateV1Status
from .template_wallet_settings import TemplateWalletSettings
from .tier_template_settings import TierTemplateSettings
from .tier_template_settings_google_wallet_settings import TierTemplateSettingsGoogleWalletSettings
from .ui_config import UIConfig
from .ui_page_schema import UIPageSchema
from .update_card_request_body import UpdateCardRequestBody
from .update_card_request_body_card_payload import UpdateCardRequestBodyCardPayload
from .update_card_response import UpdateCardResponse
from .update_card_response_card_data_field_update import UpdateCardResponseCardDataFieldUpdate
from .update_card_response_card_owner_update import UpdateCardResponseCardOwnerUpdate
from .update_profile_body import UpdateProfileBody
from .update_template_v1 import UpdateTemplateV1
from .update_template_v1_response_201 import UpdateTemplateV1Response201
from .update_template_v1_status import UpdateTemplateV1Status
from .user import User
from .validate_password_body import ValidatePasswordBody
from .voucher_codes_csv_upload_v1_body import VoucherCodesCSVUploadV1Body
from .voucher_codes_csv_upload_v1_body_type import VoucherCodesCSVUploadV1BodyType
from .voucher_codes_csv_upload_v1_response_200 import VoucherCodesCSVUploadV1Response200
from .webhook_registration_request_body import WebhookRegistrationRequestBody
from .webhook_registration_request_body_auth_config import WebhookRegistrationRequestBodyAuthConfig
from .webhook_registration_request_body_auth_type import WebhookRegistrationRequestBodyAuthType
from .webhook_registration_request_body_events_item import WebhookRegistrationRequestBodyEventsItem
from .webhook_registration_request_body_method import WebhookRegistrationRequestBodyMethod
from .welcome_details_response import WelcomeDetailsResponse

__all__ = (
    "AggregatedBillingStatistics",
    "AggregatedNotificationsStatistics",
    "AggregatedScansStatistics",
    "AggregatedScansStatisticsTemplatesItem",
    "AggregatedScansStatisticsTemplatesItemAdditionalProperty",
    "AnalyticsBillingResultsSchema",
    "AnalyticsBillingResultsSchemaResults",
    "AnalyticsBillingResultsSchemaResultsQueryParameters",
    "AnalyticsNotificationsResultsSchema",
    "AnalyticsNotificationsResultsSchemaResults",
    "AnalyticsNotificationsResultsSchemaResultsQueryParameters",
    "AnalyticsScansResultsSchema",
    "AnalyticsScansResultsSchemaResults",
    "AnalyticsScansResultsSchemaResultsQueryParameters",
    "AppleAppLinkingSettings",
    "AppleDateTimeStyleV1",
    "AppleNumberStyleV1",
    "AuthenticateXUserTenant",
    "AuthenticationRequestBody",
    "AuthenticationResponse",
    "BaseCardPayload",
    "BaseTemplateV1",
    "BaseTemplateV1Tiers",
    "BaseTemplateV1Type",
    "Business",
    "BusinessCardOptions",
    "BusinessCardRequestBody",
    "BusinessCardResponse200",
    "BusinessMailchimp",
    "CancelNotificationsByGroupIdV1Response200",
    "Card",
    "CardCardOwnerCopy",
    "CardDataFields",
    "CardMappingPayload",
    "CardOwner",
    "CardOwnerRequestBody",
    "CardOwnersScanRequestBody",
    "CardStatus",
    "CardsUploadCSVV1Body",
    "CardsUploadCSVV1BodyHeaderMappings",
    "CardsUploadCSVV1Response200",
    "CardUploadGroupV1",
    "CardUploadGroupV1Count",
    "CardUploadGroupV1Status",
    "CardUploadV1",
    "CardUploadV1CardPayload",
    "CardUploadV1Status",
    "Certificate",
    "CertificateUploadV1",
    "CertificateUploadV1Response200",
    "ColumnValues",
    "Coupon",
    "CouponRedemption",
    "CreateCouponResponseSchema",
    "CreatePassTemplateRequestBody",
    "CreatePassTemplateResponseBody",
    "CreatePassTemplateResponseBodyCardDetails",
    "CreateProfileBody",
    "CreateScanBody",
    "CreateSubBusinessRequestBody",
    "CreateTemplateV1",
    "CreateTemplateV1Barcode",
    "CreateTemplateV1BarcodeType",
    "CreateTemplateV1Colours",
    "CreateTemplateV1ColoursSamsungFont",
    "CreateTemplateV1Images",
    "CreateTemplateV1Response201",
    "CreateTemplateV1Tiers",
    "CreateTemplateV1Type",
    "CustomerWebhook",
    "CustomerWebhookAuthConfig",
    "CustomerWebhookAuthType",
    "CustomerWebhookEventsItem",
    "CustomerWebhookMethod",
    "CustomFormDesignBackgroundStyles",
    "CustomFormDesignCommonStyles",
    "CustomFormDesignFooterSection",
    "CustomFormDesignLeftSection",
    "CustomFormDesignLeftSectionStyles",
    "CustomFormDesignRightSection",
    "CustomFormDesignRightSectionFormStyles",
    "CustomFormDesignSchema",
    "DatabaseMetaData",
    "DateTimeStyle",
    "DeleteCardOwnerResponseSchema",
    "DeleteCouponResponseSchema",
    "DeleteScanV1Response200",
    "DeleteScanV1ResponseSchema",
    "DeleteWebhookResponse200",
    "DownloadCsvResponse",
    "EmailRemindersRequestBody",
    "EmailRemindersRequestBodyEmailTemplate",
    "ErrorResponse",
    "ExportCsvRequestBody",
    "ExportCsvRequestBodyDynamicColumnsItem",
    "ExportCsvRequestBodyTableName",
    "ExportCsvV1RequestBody",
    "ExportCsvV1RequestBodyTableName",
    "ExternalCallbackV1",
    "ExternalCallBackV1Response200",
    "Form",
    "FormFields",
    "FormFieldsOptionsItem",
    "FormFieldsType",
    "FormFieldsV1",
    "FormFieldsV1MappingType",
    "FormFieldsV1OptionsItem",
    "FormFieldsV1RulesItem",
    "FormFieldsV1Type",
    "FormFieldUsageItem",
    "FormMailchimpSettings",
    "FormMailchimpSettingsMergeFieldMapping",
    "FormRequest",
    "FormRequestStatus",
    "FormRequestStyle",
    "FormStyle",
    "FormV1",
    "FormV1MailchimpSettings",
    "FormV1MailchimpSettingsMergeFieldFormat",
    "FormV1MailchimpSettingsMergeFieldMapping",
    "FormV1Status",
    "FormV1Style",
    "GenerateUploadURLResponse200",
    "GetBacklinksResponse",
    "GetBacklinkV1Response200",
    "GetCardResponse200",
    "GetCardsOfCardOwnerResponse200",
    "GetCertificatesV1Response200",
    "GetCSRV1Response200",
    "GetTemplateV1Response200",
    "GetWelcomeV1Response200",
    "GoogleAppLinkingSettings",
    "HealthCheckResponse200",
    "ImageContent",
    "ImageContentImageType",
    "ImageUploadResponse",
    "ListCardOwnersResponse",
    "ListCardsByTemplateIdResponse200",
    "ListCardsDetail",
    "ListCardsDetailDataFields",
    "ListCardsUploadGroupsV1Response200",
    "ListCardUploadsV1Response200",
    "ListCertificatesResponseV1",
    "ListFormsResultItem",
    "ListFormsResultItemId",
    "ListFormsResultItemIdStyle",
    "ListNotificationGroupsResponse",
    "ListPassesResultItem",
    "ListPassesResultItemId",
    "ListPassesResultItemIdDataFields",
    "ListPassesV1Response200",
    "ListPassOfCardOwnerRequestV1",
    "ListPassRequestV1",
    "ListScansV1Response200",
    "ListTemplatesV1Response200",
    "ListUsersResponse200",
    "MailchimpTagSettings",
    "NFTRequestBody",
    "NFTRequestBodyMetadata",
    "NFTRequestBodyMetadataUrlsItem",
    "NFTRequestBodyNftPage",
    "NFTRequestBodyNftPageUrlsItem",
    "NotificationGroup",
    "NotificationGroupSentViaItem",
    "NotificationGroupSentViaItemPlatform",
    "NotificationGroupSentViaItemType",
    "NotificationGroupStatus",
    "NotificationSegments",
    "NotificationSettings",
    "NotificationSettingsTrigger",
    "NotificationSettingsType",
    "NotificationV1",
    "NotificationV1Notification",
    "NotificationV1Options",
    "NotificationV1OptionsEmailType",
    "OnboardMailchimpBody",
    "OnboardMailchimpBodyAdditionalMergeFieldsItem",
    "PassCountDetails",
    "PassCountDetailsForTemplate",
    "PassCountsForTemplate",
    "PassCountsForTemplateDuration",
    "PassCountsHistory",
    "PassCountsHistoryDuration",
    "PassDownloadsCountV1Duration",
    "PassDownloadTrendV1Response200",
    "PassTrendDetails",
    "PaymentAndSignUpResponseSchema",
    "PrivateResendPassRequest",
    "PrivateResendPassRequestEmailType",
    "PrivateSignUpRequestBody",
    "Profile",
    "PublicRedeemRequestBody",
    "PublicRedeemRequestBodyUpdatePayload",
    "PublicResendPassRequest",
    "PublicScanBarcodeV1RequestBody",
    "PublicScanV1Response200",
    "PublicSignUpRequestBody",
    "RateLimit",
    "RateLimitRule",
    "RateLimitV1Type0LimitType",
    "RateLimitV1Type0Rule",
    "RateLimitV1Type1LimitType",
    "RateLimitV1Type1RuleDateLimit",
    "RateLimitV1Type1RuleDateLimitMeasurement",
    "RegisterBusinessRequestBody",
    "RegisterBusinessResponse",
    "RegisterWebhookResponse201",
    "ResponseBody",
    "Scan",
    "ScanBarcodeV1RequestBody",
    "ScanCheckInRequestBody",
    "ScanDataFields",
    "ScanRedemptionRequestBody",
    "ScanRequestBody",
    "ScanResponseSchema",
    "ScanResponseSchemaActions",
    "ScanResponseSchemaActionsAdditionalProperty",
    "ScanResponseSchemaCard",
    "ScanResponseSchemaCardDataFields",
    "ScanResponseSchemaCardOwner",
    "ScanResponseSchemaCardStatus",
    "ScanScanType",
    "ScanStatus",
    "ScanV1Response200",
    "ScanV1ResponseSchema",
    "ScanV1ResponseSchemaCard",
    "ScanV1ResponseSchemaCardCardOwnerCopy",
    "ScanV1ResponseSchemaCardDataFields",
    "ScanV1ResponseSchemaCardOwner",
    "ScanV1ResponseSchemaCardStatus",
    "ScheduleTaskV1",
    "ScheduleTaskV1Response200",
    "SendNotificationQueueV1Response200",
    "SendNotificationRequestBody",
    "SendNotificationRequestBodyEmailType",
    "SendNotificationV1Response200",
    "SendRemindersResponse200",
    "SetCardStatusBody",
    "SetCardStatusBodyStatus",
    "SetCardStatusResponse200",
    "SetTemplateStatusBody",
    "SetTemplateStatusBodyStatus",
    "SetTemplateStatusResponse200",
    "SettingsV1",
    "SettingsV1ExternalProvider",
    "SettingsV1ExternalSystemConfig",
    "SettingsV1PrimaryContact",
    "SettingsV1SourceEmail",
    "ShopfifySettings",
    "SignUpOptions",
    "SignUpOptionsEmailType",
    "SignUpOptionsSourceEmail",
    "SignUpResponseSchema",
    "SocialMedia",
    "SpinToWinResponse",
    "SpinToWinResponsePrize",
    "StripeCheckoutBody",
    "StripeCustomerPortalBody",
    "StripeSettings",
    "StripeSettingsType",
    "SubBusinessRoles",
    "SubBusinessSummary",
    "TableColumn",
    "TableColumnFormat",
    "TableColumnGroups",
    "TableColumnGroupsAdditionalProperty",
    "TableColumnGroupsAdditionalPropertyMappings",
    "TableColumnUsageItem",
    "TableConfig",
    "TableConfigCardsTable",
    "TemplateActionCondition",
    "TemplateActionConditionV1",
    "TemplateActionParams",
    "TemplateActionParamsV1",
    "TemplateActionParamsV1PostCalc",
    "TemplateActionParamsV1PostCalcModifier",
    "TemplateActions",
    "TemplateActionsAdditionalProperty",
    "TemplateActionsRequestBody",
    "TemplateActionsRequestBodyActionsItem",
    "TemplateActionsResponse200",
    "TemplateActionsResponseSchema",
    "TemplateActionsV1",
    "TemplateActionsV1AdditionalProperty",
    "TemplateAppleWalletSettingsV1",
    "TemplateAppleWalletSettingsV1PassType",
    "TemplateAppLinking",
    "TemplateBarcode",
    "TemplateBarcodeV1",
    "TemplateBarcodeV1Type",
    "TemplateCardExpiryType0",
    "TemplateCardExpiryType0ExpiryType",
    "TemplateCardExpiryType1",
    "TemplateCardExpiryType1ExpiryType",
    "TemplateCardExpiryType2ExpiryType",
    "TemplateCardExpiryType2FromActivation",
    "TemplateCardExpiryType2FromActivationMeasurement",
    "TemplateCardExpiryType3",
    "TemplateCardExpiryType3ExpiryType",
    "TemplateCardExpiryV1Type0",
    "TemplateCardExpiryV1Type0ExpiryType",
    "TemplateCardExpiryV1Type1",
    "TemplateCardExpiryV1Type1ExpiryType",
    "TemplateCardExpiryV1Type2ExpiryType",
    "TemplateCardExpiryV1Type2FromActivation",
    "TemplateCardExpiryV1Type2FromActivationMeasurement",
    "TemplateCardExpiryV1Type2FromActivationTimezone",
    "TemplateCardExpiryV1Type3",
    "TemplateCardExpiryV1Type3ExpiryType",
    "TemplateCertificatesV1",
    "TemplateCertificatesV1AppleSettings",
    "TemplateCertificatesV1GoogleSettings",
    "TemplateCertificatesV1Nfc",
    "TemplateCertificatesV1NfcPayloadType",
    "TemplateColours",
    "TemplateColoursV1",
    "TemplateColoursV1SamsungFont",
    "TemplateDataFieldV1",
    "TemplateDataFieldV1AppleFieldSettings",
    "TemplateDataFieldV1AppleFieldSettingsAppleFieldType",
    "TemplateDataFieldV1AppleFieldSettingsTextAlignment",
    "TemplateDataFieldV1Formatter",
    "TemplateDataFieldV1FormFieldSettings",
    "TemplateDataFieldV1FormFieldSettingsDataType",
    "TemplateDataFieldV1FormFieldSettingsExternalProviderMapping",
    "TemplateDataFieldV1FormFieldSettingsOptionsItem",
    "TemplateDataFieldV1FormFieldSettingsRulesItem",
    "TemplateDataFieldV1FrontEndMappingItem",
    "TemplateDataFieldV1GoogleFieldSettings",
    "TemplateDataFieldV1GoogleFieldSettingsFieldType",
    "TemplateDataFieldV1GoogleFieldSettingsGoogleFieldType",
    "TemplateDataFieldV1SamsungFieldSettings",
    "TemplateDataFieldV1SamsungFieldSettingsSamsungFieldType",
    "TemplateGoogleWalletSettingsV1",
    "TemplateGoogleWalletSettingsV1EventTicket",
    "TemplateGoogleWalletSettingsV1EventTicketConfirmationCodeLabel",
    "TemplateGoogleWalletSettingsV1EventTicketGateLabel",
    "TemplateGoogleWalletSettingsV1EventTicketRowLabel",
    "TemplateGoogleWalletSettingsV1EventTicketSeatLabel",
    "TemplateGoogleWalletSettingsV1EventTicketSectionLabel",
    "TemplateGoogleWalletSettingsV1MultipleDevicesAndUsersStatus",
    "TemplateGoogleWalletSettingsV1Offer",
    "TemplateGoogleWalletSettingsV1OfferRedemptionChannel",
    "TemplateGoogleWalletSettingsV1PassType",
    "TemplateImages",
    "TemplateImagesV1",
    "TemplateLinkV1",
    "TemplateLinkV1Type",
    "TemplateLocationsV1Item",
    "TemplateLocationsV1ItemApple",
    "TemplateLocationsV1ItemSamsung",
    "TemplateNotificationFields",
    "TemplateNotificationFieldsAppleTextAlignment",
    "TemplateOverridesV1",
    "TemplatePassDownloadsCountV1Duration",
    "TemplatePassDownloadTrendV1Response200",
    "TemplateRequestStatus",
    "TemplateResponse",
    "TemplateSamsungWalletSettingsV1",
    "TemplateSamsungWalletSettingsV1CustomerServiceInfo",
    "TemplateSamsungWalletSettingsV1PassType",
    "TemplateUsageV1Item",
    "TemplateV1",
    "TemplateV1Status",
    "TemplateWalletSettings",
    "TierTemplateSettings",
    "TierTemplateSettingsGoogleWalletSettings",
    "UIConfig",
    "UIPageSchema",
    "UpdateCardRequestBody",
    "UpdateCardRequestBodyCardPayload",
    "UpdateCardResponse",
    "UpdateCardResponseCardDataFieldUpdate",
    "UpdateCardResponseCardOwnerUpdate",
    "UpdateProfileBody",
    "UpdateTemplateV1",
    "UpdateTemplateV1Response201",
    "UpdateTemplateV1Status",
    "User",
    "ValidatePasswordBody",
    "VoucherCodesCSVUploadV1Body",
    "VoucherCodesCSVUploadV1BodyType",
    "VoucherCodesCSVUploadV1Response200",
    "WebhookRegistrationRequestBody",
    "WebhookRegistrationRequestBodyAuthConfig",
    "WebhookRegistrationRequestBodyAuthType",
    "WebhookRegistrationRequestBodyEventsItem",
    "WebhookRegistrationRequestBodyMethod",
    "WelcomeDetailsResponse",
)
