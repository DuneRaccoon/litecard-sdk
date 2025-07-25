from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.send_notification_request_body_email_type import SendNotificationRequestBodyEmailType
from ..types import UNSET, Unset

T = TypeVar("T", bound="SendNotificationRequestBody")


@_attrs_define
class SendNotificationRequestBody:
    """
    Attributes:
        title (Union[Unset, str]): Title of the Notification Example: Friday Sales.
        message (Union[Unset, str]): Message Body of the Notification Example: Buy 2 Get The 3rd 20% Off.
        is_push_notification (Union[Unset, bool]): Toggle for Sending Apple Push Notifications Example: True.
        email_type (Union[Unset, SendNotificationRequestBodyEmailType]): Type of Email Example: MARKETING.
    """

    title: Union[Unset, str] = UNSET
    message: Union[Unset, str] = UNSET
    is_push_notification: Union[Unset, bool] = UNSET
    email_type: Union[Unset, SendNotificationRequestBodyEmailType] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        message = self.message

        is_push_notification = self.is_push_notification

        email_type: Union[Unset, str] = UNSET
        if not isinstance(self.email_type, Unset):
            email_type = self.email_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if message is not UNSET:
            field_dict["message"] = message
        if is_push_notification is not UNSET:
            field_dict["isPushNotification"] = is_push_notification
        if email_type is not UNSET:
            field_dict["emailType"] = email_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        title = d.pop("title", UNSET)

        message = d.pop("message", UNSET)

        is_push_notification = d.pop("isPushNotification", UNSET)

        _email_type = d.pop("emailType", UNSET)
        email_type: Union[Unset, SendNotificationRequestBodyEmailType]
        if isinstance(_email_type, Unset):
            email_type = UNSET
        else:
            email_type = SendNotificationRequestBodyEmailType(_email_type)

        send_notification_request_body = cls(
            title=title,
            message=message,
            is_push_notification=is_push_notification,
            email_type=email_type,
        )

        send_notification_request_body.additional_properties = d
        return send_notification_request_body

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
