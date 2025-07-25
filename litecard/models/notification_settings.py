from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.notification_settings_trigger import NotificationSettingsTrigger
from ..models.notification_settings_type import NotificationSettingsType
from ..types import UNSET, Unset

T = TypeVar("T", bound="NotificationSettings")


@_attrs_define
class NotificationSettings:
    """Settings for setting up automated notifications

    Attributes:
        trigger (NotificationSettingsTrigger): Notification trigger type
        type_ (NotificationSettingsType): What rule the coupon should be using
        title (str): Title of the push notification
        message (str): Message contents of the push notifications
        valid_start_date (Union[Unset, str]): Start date where this notification is valid
        valid_end_date (Union[Unset, str]): End date where this notification is valid
        delay (Union[Unset, float]): User key to be used to retrieve client credentials and verify owner
        data_field_key (Union[Unset, str]): Key of the push notification field. Default: notificationKey
    """

    trigger: NotificationSettingsTrigger
    type_: NotificationSettingsType
    title: str
    message: str
    valid_start_date: Union[Unset, str] = UNSET
    valid_end_date: Union[Unset, str] = UNSET
    delay: Union[Unset, float] = UNSET
    data_field_key: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        trigger = self.trigger.value

        type_ = self.type_.value

        title = self.title

        message = self.message

        valid_start_date = self.valid_start_date

        valid_end_date = self.valid_end_date

        delay = self.delay

        data_field_key = self.data_field_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "trigger": trigger,
                "type": type_,
                "title": title,
                "message": message,
            }
        )
        if valid_start_date is not UNSET:
            field_dict["validStartDate"] = valid_start_date
        if valid_end_date is not UNSET:
            field_dict["validEndDate"] = valid_end_date
        if delay is not UNSET:
            field_dict["delay"] = delay
        if data_field_key is not UNSET:
            field_dict["dataFieldKey"] = data_field_key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        trigger = NotificationSettingsTrigger(d.pop("trigger"))

        type_ = NotificationSettingsType(d.pop("type"))

        title = d.pop("title")

        message = d.pop("message")

        valid_start_date = d.pop("validStartDate", UNSET)

        valid_end_date = d.pop("validEndDate", UNSET)

        delay = d.pop("delay", UNSET)

        data_field_key = d.pop("dataFieldKey", UNSET)

        notification_settings = cls(
            trigger=trigger,
            type_=type_,
            title=title,
            message=message,
            valid_start_date=valid_start_date,
            valid_end_date=valid_end_date,
            delay=delay,
            data_field_key=data_field_key,
        )

        notification_settings.additional_properties = d
        return notification_settings

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
