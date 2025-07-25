from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.private_resend_pass_request_email_type import PrivateResendPassRequestEmailType
from ..types import UNSET, Unset

T = TypeVar("T", bound="PrivateResendPassRequest")


@_attrs_define
class PrivateResendPassRequest:
    """
    Attributes:
        card_id (Union[Unset, str]): Card Id Example: 00000001.
        form_id (Union[Unset, str]): Id for field input form Example: 00000001.
        card_owner_id (Union[Unset, str]): Card Owner Id Example: 00000001.
        email_template_type (Union[Unset, str]): Email Template Type Example: litecardpass.
        email_type (Union[Unset, PrivateResendPassRequestEmailType]): Type of Email Example: STANDARD.
        subject (Union[Unset, str]): Subject of Email Example: LiteCard Invitation.
        send_all_not_downloaded (Union[Unset, bool]): Send to all users who have not downloaded the pass Example: True.
    """

    card_id: Union[Unset, str] = UNSET
    form_id: Union[Unset, str] = UNSET
    card_owner_id: Union[Unset, str] = UNSET
    email_template_type: Union[Unset, str] = UNSET
    email_type: Union[Unset, PrivateResendPassRequestEmailType] = UNSET
    subject: Union[Unset, str] = UNSET
    send_all_not_downloaded: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        card_id = self.card_id

        form_id = self.form_id

        card_owner_id = self.card_owner_id

        email_template_type = self.email_template_type

        email_type: Union[Unset, str] = UNSET
        if not isinstance(self.email_type, Unset):
            email_type = self.email_type.value

        subject = self.subject

        send_all_not_downloaded = self.send_all_not_downloaded

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if card_id is not UNSET:
            field_dict["cardId"] = card_id
        if form_id is not UNSET:
            field_dict["formId"] = form_id
        if card_owner_id is not UNSET:
            field_dict["cardOwnerId"] = card_owner_id
        if email_template_type is not UNSET:
            field_dict["emailTemplateType"] = email_template_type
        if email_type is not UNSET:
            field_dict["emailType"] = email_type
        if subject is not UNSET:
            field_dict["subject"] = subject
        if send_all_not_downloaded is not UNSET:
            field_dict["sendAllNotDownloaded"] = send_all_not_downloaded

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        card_id = d.pop("cardId", UNSET)

        form_id = d.pop("formId", UNSET)

        card_owner_id = d.pop("cardOwnerId", UNSET)

        email_template_type = d.pop("emailTemplateType", UNSET)

        _email_type = d.pop("emailType", UNSET)
        email_type: Union[Unset, PrivateResendPassRequestEmailType]
        if isinstance(_email_type, Unset):
            email_type = UNSET
        else:
            email_type = PrivateResendPassRequestEmailType(_email_type)

        subject = d.pop("subject", UNSET)

        send_all_not_downloaded = d.pop("sendAllNotDownloaded", UNSET)

        private_resend_pass_request = cls(
            card_id=card_id,
            form_id=form_id,
            card_owner_id=card_owner_id,
            email_template_type=email_template_type,
            email_type=email_type,
            subject=subject,
            send_all_not_downloaded=send_all_not_downloaded,
        )

        private_resend_pass_request.additional_properties = d
        return private_resend_pass_request

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
