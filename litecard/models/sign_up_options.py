from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.sign_up_options_email_type import SignUpOptionsEmailType
from ..models.sign_up_options_source_email import SignUpOptionsSourceEmail
from ..types import UNSET, Unset

T = TypeVar("T", bound="SignUpOptions")


@_attrs_define
class SignUpOptions:
    """
    Attributes:
        download_id (Union[None, Unset, str]): Optional. Specify the downloadId that should be used. This Id can be used
            to get the download urls for the created card
        password (Union[Unset, str]): Optional. For password protected public sign ups Example: password123.
        email_type (Union[Unset, SignUpOptionsEmailType]): Optional. Senders email address, standard is used for most
            cases unless a marketing email address has been set up Default: SignUpOptionsEmailType.STANDARD. Example:
            STANDARD.
        email_invitation_enabled (Union[Unset, bool]): Flag to send an email invitation with Apple/Google wallet cards
            to the user
        email_template (Union[Unset, str]): Select which email template option to use. Example: litecardpass.
        sms_invitation_enabled (Union[Unset, bool]): Flag to send an sms invitation with Apple/Google wallet cards to
            the user
        sms_template (Union[Unset, str]): Select which email template option to use. Example: litecardpass.
        source_email (Union[Unset, SignUpOptionsSourceEmail]): IF not using default from domain, specify what from
            address to use Example: tarfish@litecard.io.
        no_pi (Union[Unset, bool]): Flag to disable requirement for Email or Phone in card payload. Default: false
            Example: True.
    """

    download_id: Union[None, Unset, str] = UNSET
    password: Union[Unset, str] = UNSET
    email_type: Union[Unset, SignUpOptionsEmailType] = SignUpOptionsEmailType.STANDARD
    email_invitation_enabled: Union[Unset, bool] = UNSET
    email_template: Union[Unset, str] = UNSET
    sms_invitation_enabled: Union[Unset, bool] = UNSET
    sms_template: Union[Unset, str] = UNSET
    source_email: Union[Unset, SignUpOptionsSourceEmail] = UNSET
    no_pi: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        download_id: Union[None, Unset, str]
        if isinstance(self.download_id, Unset):
            download_id = UNSET
        else:
            download_id = self.download_id

        password = self.password

        email_type: Union[Unset, str] = UNSET
        if not isinstance(self.email_type, Unset):
            email_type = self.email_type.value

        email_invitation_enabled = self.email_invitation_enabled

        email_template = self.email_template

        sms_invitation_enabled = self.sms_invitation_enabled

        sms_template = self.sms_template

        source_email: Union[Unset, str] = UNSET
        if not isinstance(self.source_email, Unset):
            source_email = self.source_email.value

        no_pi = self.no_pi

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if download_id is not UNSET:
            field_dict["downloadId"] = download_id
        if password is not UNSET:
            field_dict["password"] = password
        if email_type is not UNSET:
            field_dict["emailType"] = email_type
        if email_invitation_enabled is not UNSET:
            field_dict["emailInvitationEnabled"] = email_invitation_enabled
        if email_template is not UNSET:
            field_dict["emailTemplate"] = email_template
        if sms_invitation_enabled is not UNSET:
            field_dict["smsInvitationEnabled"] = sms_invitation_enabled
        if sms_template is not UNSET:
            field_dict["smsTemplate"] = sms_template
        if source_email is not UNSET:
            field_dict["sourceEmail"] = source_email
        if no_pi is not UNSET:
            field_dict["noPI"] = no_pi

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_download_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        download_id = _parse_download_id(d.pop("downloadId", UNSET))

        password = d.pop("password", UNSET)

        _email_type = d.pop("emailType", UNSET)
        email_type: Union[Unset, SignUpOptionsEmailType]
        if isinstance(_email_type, Unset):
            email_type = UNSET
        else:
            email_type = SignUpOptionsEmailType(_email_type)

        email_invitation_enabled = d.pop("emailInvitationEnabled", UNSET)

        email_template = d.pop("emailTemplate", UNSET)

        sms_invitation_enabled = d.pop("smsInvitationEnabled", UNSET)

        sms_template = d.pop("smsTemplate", UNSET)

        _source_email = d.pop("sourceEmail", UNSET)
        source_email: Union[Unset, SignUpOptionsSourceEmail]
        if isinstance(_source_email, Unset):
            source_email = UNSET
        else:
            source_email = SignUpOptionsSourceEmail(_source_email)

        no_pi = d.pop("noPI", UNSET)

        sign_up_options = cls(
            download_id=download_id,
            password=password,
            email_type=email_type,
            email_invitation_enabled=email_invitation_enabled,
            email_template=email_template,
            sms_invitation_enabled=sms_invitation_enabled,
            sms_template=sms_template,
            source_email=source_email,
            no_pi=no_pi,
        )

        sign_up_options.additional_properties = d
        return sign_up_options

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
