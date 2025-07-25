from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NotificationV1Notification")


@_attrs_define
class NotificationV1Notification:
    """
    Attributes:
        title (str): Title of push notification Example: Litecard - Notification.
        message (str): Body message of push notification Example: Welcome to Litecard.
        data_field_key (str): Key of data field used to store push notification in digital wallet card Example:
            notificationKey.
        send_time (Union[Unset, str]): Time to send the notification. Uses UTC time. Example: 2022-11-07T04:31:15.246Z.
    """

    title: str
    message: str
    data_field_key: str
    send_time: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        message = self.message

        data_field_key = self.data_field_key

        send_time = self.send_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "message": message,
                "dataFieldKey": data_field_key,
            }
        )
        if send_time is not UNSET:
            field_dict["sendTime"] = send_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        title = d.pop("title")

        message = d.pop("message")

        data_field_key = d.pop("dataFieldKey")

        send_time = d.pop("sendTime", UNSET)

        notification_v1_notification = cls(
            title=title,
            message=message,
            data_field_key=data_field_key,
            send_time=send_time,
        )

        notification_v1_notification.additional_properties = d
        return notification_v1_notification

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
