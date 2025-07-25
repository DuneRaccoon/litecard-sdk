from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.notification_v1_options_email_type import NotificationV1OptionsEmailType
from ..types import UNSET, Unset

T = TypeVar("T", bound="NotificationV1Options")


@_attrs_define
class NotificationV1Options:
    """
    Attributes:
        push_notification (bool): Send push notification Default: True.
        email (Union[Unset, bool]): Send email notification Default: False.
        email_type (Union[Unset, NotificationV1OptionsEmailType]): Optional. Senders email address, standard is used for
            most cases unless a marketing email address has been set up Default: NotificationV1OptionsEmailType.STANDARD.
        send_all (Union[Unset, bool]): Send to all active users within business Default: False.
    """

    push_notification: bool = True
    email: Union[Unset, bool] = False
    email_type: Union[Unset, NotificationV1OptionsEmailType] = NotificationV1OptionsEmailType.STANDARD
    send_all: Union[Unset, bool] = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        push_notification = self.push_notification

        email = self.email

        email_type: Union[Unset, str] = UNSET
        if not isinstance(self.email_type, Unset):
            email_type = self.email_type.value

        send_all = self.send_all

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "pushNotification": push_notification,
            }
        )
        if email is not UNSET:
            field_dict["email"] = email
        if email_type is not UNSET:
            field_dict["emailType"] = email_type
        if send_all is not UNSET:
            field_dict["sendAll"] = send_all

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        push_notification = d.pop("pushNotification")

        email = d.pop("email", UNSET)

        _email_type = d.pop("emailType", UNSET)
        email_type: Union[Unset, NotificationV1OptionsEmailType]
        if isinstance(_email_type, Unset):
            email_type = UNSET
        else:
            email_type = NotificationV1OptionsEmailType(_email_type)

        send_all = d.pop("sendAll", UNSET)

        notification_v1_options = cls(
            push_notification=push_notification,
            email=email,
            email_type=email_type,
            send_all=send_all,
        )

        notification_v1_options.additional_properties = d
        return notification_v1_options

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
