from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.settings_v1_external_provider import SettingsV1ExternalProvider
from ..models.settings_v1_primary_contact import SettingsV1PrimaryContact
from ..models.settings_v1_source_email import SettingsV1SourceEmail
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.settings_v1_external_system_config import SettingsV1ExternalSystemConfig


T = TypeVar("T", bound="SettingsV1")


@_attrs_define
class SettingsV1:
    """
    Attributes:
        payment_required (Union[Unset, bool]): If card creation requires payment
        enforce_unique_email (Union[Unset, bool]): Only allow one email address per template
        enforce_unique_phone (Union[Unset, bool]): Only allow one phone number per template
        resend_for_unique_email (Union[Unset, bool]): Resend card if email is unique
        resend_for_unique_phone (Union[Unset, bool]): Resend card if phone is unique
        timezone (Union[Unset, str]): Timezone used for displaying dates and times on the pass. Default is UTC Example:
            Australia/Melbourne.
        source_email (Union[Unset, SettingsV1SourceEmail]): IF not using default from domain, specify what from address
            to use Example: tarfish@litecard.io.
        email_template (Union[Unset, str]): Email template used when creating a new card Example: litecardpass.
        email_subject (Union[Unset, str]): The subject of the Invitation email sent when a pass is generated Example:
            Welcome to Litecard.
        form_password (Union[Unset, str]): Form Password Example: Litecard2023.
        sms_template (Union[Unset, str]): SMS template used when creating a new card Example: litecardpass.
        disable_backlink (Union[Unset, bool]): Disable backlink trackining. Default is enabled Example: True.
        barcode_image (Union[Unset, bool]): Provides an image alternative of the barcode Example: True.
        tac_url (Union[Unset, str]): Use this if client requires an alternative terms and conditions link Example:
            https://example.com.
        hide_form (Union[Unset, bool]): Hide this Form from the private create card page Example: True.
        disable_qr (Union[Unset, bool]): Disable QR code on Download page Example: True.
        primary_contact (Union[Unset, SettingsV1PrimaryContact]): Preferred medium to use when sending invitation emails
            Example: SMS.
        external_provider (Union[Unset, SettingsV1ExternalProvider]): External Provider Example: SQUARE.
        disable_download (Union[Unset, bool]): Option to disable download page if pass is active. Default: false
            Example: True.
        quick_sign_up (Union[Unset, bool]): Option to enable quick sign up for card creation Example: True.
        is_deduplicate_device_and_ip (Union[Unset, bool]): Option to remove creating duplicate passes for quick signup
            forms. (Applicable only quickSignUp is true) Example: True.
        external_system_config (Union[Unset, SettingsV1ExternalSystemConfig]): External System Configuration Example:
            {'configKey1': 'configValue1', 'configKey2': 'configValue2'}.
        disable_invitation_email (Union[Unset, bool]): Option to disable Invitation Email being sent. This will override
            the option inside options payload Example: True.
        disable_invitation_sms (Union[Unset, bool]): Option to disable Invitation Phone being sent. This will override
            the option inside options payload. Example: True.
        multi_tier (Union[Unset, bool]): Flag to notify whether this template has multiple tier options Example: True.
    """

    payment_required: Union[Unset, bool] = UNSET
    enforce_unique_email: Union[Unset, bool] = UNSET
    enforce_unique_phone: Union[Unset, bool] = UNSET
    resend_for_unique_email: Union[Unset, bool] = UNSET
    resend_for_unique_phone: Union[Unset, bool] = UNSET
    timezone: Union[Unset, str] = UNSET
    source_email: Union[Unset, SettingsV1SourceEmail] = UNSET
    email_template: Union[Unset, str] = UNSET
    email_subject: Union[Unset, str] = UNSET
    form_password: Union[Unset, str] = UNSET
    sms_template: Union[Unset, str] = UNSET
    disable_backlink: Union[Unset, bool] = UNSET
    barcode_image: Union[Unset, bool] = UNSET
    tac_url: Union[Unset, str] = UNSET
    hide_form: Union[Unset, bool] = UNSET
    disable_qr: Union[Unset, bool] = UNSET
    primary_contact: Union[Unset, SettingsV1PrimaryContact] = UNSET
    external_provider: Union[Unset, SettingsV1ExternalProvider] = UNSET
    disable_download: Union[Unset, bool] = UNSET
    quick_sign_up: Union[Unset, bool] = UNSET
    is_deduplicate_device_and_ip: Union[Unset, bool] = UNSET
    external_system_config: Union[Unset, "SettingsV1ExternalSystemConfig"] = UNSET
    disable_invitation_email: Union[Unset, bool] = UNSET
    disable_invitation_sms: Union[Unset, bool] = UNSET
    multi_tier: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        payment_required = self.payment_required

        enforce_unique_email = self.enforce_unique_email

        enforce_unique_phone = self.enforce_unique_phone

        resend_for_unique_email = self.resend_for_unique_email

        resend_for_unique_phone = self.resend_for_unique_phone

        timezone = self.timezone

        source_email: Union[Unset, str] = UNSET
        if not isinstance(self.source_email, Unset):
            source_email = self.source_email.value

        email_template = self.email_template

        email_subject = self.email_subject

        form_password = self.form_password

        sms_template = self.sms_template

        disable_backlink = self.disable_backlink

        barcode_image = self.barcode_image

        tac_url = self.tac_url

        hide_form = self.hide_form

        disable_qr = self.disable_qr

        primary_contact: Union[Unset, str] = UNSET
        if not isinstance(self.primary_contact, Unset):
            primary_contact = self.primary_contact.value

        external_provider: Union[Unset, str] = UNSET
        if not isinstance(self.external_provider, Unset):
            external_provider = self.external_provider.value

        disable_download = self.disable_download

        quick_sign_up = self.quick_sign_up

        is_deduplicate_device_and_ip = self.is_deduplicate_device_and_ip

        external_system_config: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.external_system_config, Unset):
            external_system_config = self.external_system_config.to_dict()

        disable_invitation_email = self.disable_invitation_email

        disable_invitation_sms = self.disable_invitation_sms

        multi_tier = self.multi_tier

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if payment_required is not UNSET:
            field_dict["paymentRequired"] = payment_required
        if enforce_unique_email is not UNSET:
            field_dict["enforceUniqueEmail"] = enforce_unique_email
        if enforce_unique_phone is not UNSET:
            field_dict["enforceUniquePhone"] = enforce_unique_phone
        if resend_for_unique_email is not UNSET:
            field_dict["resendForUniqueEmail"] = resend_for_unique_email
        if resend_for_unique_phone is not UNSET:
            field_dict["resendForUniquePhone"] = resend_for_unique_phone
        if timezone is not UNSET:
            field_dict["timezone"] = timezone
        if source_email is not UNSET:
            field_dict["sourceEmail"] = source_email
        if email_template is not UNSET:
            field_dict["emailTemplate"] = email_template
        if email_subject is not UNSET:
            field_dict["emailSubject"] = email_subject
        if form_password is not UNSET:
            field_dict["formPassword"] = form_password
        if sms_template is not UNSET:
            field_dict["smsTemplate"] = sms_template
        if disable_backlink is not UNSET:
            field_dict["disableBacklink"] = disable_backlink
        if barcode_image is not UNSET:
            field_dict["barcodeImage"] = barcode_image
        if tac_url is not UNSET:
            field_dict["tacURL"] = tac_url
        if hide_form is not UNSET:
            field_dict["hideForm"] = hide_form
        if disable_qr is not UNSET:
            field_dict["disableQR"] = disable_qr
        if primary_contact is not UNSET:
            field_dict["primaryContact"] = primary_contact
        if external_provider is not UNSET:
            field_dict["externalProvider"] = external_provider
        if disable_download is not UNSET:
            field_dict["disableDownload"] = disable_download
        if quick_sign_up is not UNSET:
            field_dict["quickSignUp"] = quick_sign_up
        if is_deduplicate_device_and_ip is not UNSET:
            field_dict["isDeduplicateDeviceAndIp"] = is_deduplicate_device_and_ip
        if external_system_config is not UNSET:
            field_dict["externalSystemConfig"] = external_system_config
        if disable_invitation_email is not UNSET:
            field_dict["disableInvitationEmail"] = disable_invitation_email
        if disable_invitation_sms is not UNSET:
            field_dict["disableInvitationSMS"] = disable_invitation_sms
        if multi_tier is not UNSET:
            field_dict["multiTier"] = multi_tier

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.settings_v1_external_system_config import SettingsV1ExternalSystemConfig

        d = dict(src_dict)
        payment_required = d.pop("paymentRequired", UNSET)

        enforce_unique_email = d.pop("enforceUniqueEmail", UNSET)

        enforce_unique_phone = d.pop("enforceUniquePhone", UNSET)

        resend_for_unique_email = d.pop("resendForUniqueEmail", UNSET)

        resend_for_unique_phone = d.pop("resendForUniquePhone", UNSET)

        timezone = d.pop("timezone", UNSET)

        _source_email = d.pop("sourceEmail", UNSET)
        source_email: Union[Unset, SettingsV1SourceEmail]
        if isinstance(_source_email, Unset):
            source_email = UNSET
        else:
            source_email = SettingsV1SourceEmail(_source_email)

        email_template = d.pop("emailTemplate", UNSET)

        email_subject = d.pop("emailSubject", UNSET)

        form_password = d.pop("formPassword", UNSET)

        sms_template = d.pop("smsTemplate", UNSET)

        disable_backlink = d.pop("disableBacklink", UNSET)

        barcode_image = d.pop("barcodeImage", UNSET)

        tac_url = d.pop("tacURL", UNSET)

        hide_form = d.pop("hideForm", UNSET)

        disable_qr = d.pop("disableQR", UNSET)

        _primary_contact = d.pop("primaryContact", UNSET)
        primary_contact: Union[Unset, SettingsV1PrimaryContact]
        if isinstance(_primary_contact, Unset):
            primary_contact = UNSET
        else:
            primary_contact = SettingsV1PrimaryContact(_primary_contact)

        _external_provider = d.pop("externalProvider", UNSET)
        external_provider: Union[Unset, SettingsV1ExternalProvider]
        if isinstance(_external_provider, Unset):
            external_provider = UNSET
        else:
            external_provider = SettingsV1ExternalProvider(_external_provider)

        disable_download = d.pop("disableDownload", UNSET)

        quick_sign_up = d.pop("quickSignUp", UNSET)

        is_deduplicate_device_and_ip = d.pop("isDeduplicateDeviceAndIp", UNSET)

        _external_system_config = d.pop("externalSystemConfig", UNSET)
        external_system_config: Union[Unset, SettingsV1ExternalSystemConfig]
        if isinstance(_external_system_config, Unset):
            external_system_config = UNSET
        else:
            external_system_config = SettingsV1ExternalSystemConfig.from_dict(_external_system_config)

        disable_invitation_email = d.pop("disableInvitationEmail", UNSET)

        disable_invitation_sms = d.pop("disableInvitationSMS", UNSET)

        multi_tier = d.pop("multiTier", UNSET)

        settings_v1 = cls(
            payment_required=payment_required,
            enforce_unique_email=enforce_unique_email,
            enforce_unique_phone=enforce_unique_phone,
            resend_for_unique_email=resend_for_unique_email,
            resend_for_unique_phone=resend_for_unique_phone,
            timezone=timezone,
            source_email=source_email,
            email_template=email_template,
            email_subject=email_subject,
            form_password=form_password,
            sms_template=sms_template,
            disable_backlink=disable_backlink,
            barcode_image=barcode_image,
            tac_url=tac_url,
            hide_form=hide_form,
            disable_qr=disable_qr,
            primary_contact=primary_contact,
            external_provider=external_provider,
            disable_download=disable_download,
            quick_sign_up=quick_sign_up,
            is_deduplicate_device_and_ip=is_deduplicate_device_and_ip,
            external_system_config=external_system_config,
            disable_invitation_email=disable_invitation_email,
            disable_invitation_sms=disable_invitation_sms,
            multi_tier=multi_tier,
        )

        settings_v1.additional_properties = d
        return settings_v1

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
