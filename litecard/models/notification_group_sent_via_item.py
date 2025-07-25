from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.notification_group_sent_via_item_platform import NotificationGroupSentViaItemPlatform
from ..models.notification_group_sent_via_item_type import NotificationGroupSentViaItemType
from ..types import UNSET, Unset

T = TypeVar("T", bound="NotificationGroupSentViaItem")


@_attrs_define
class NotificationGroupSentViaItem:
    """
    Attributes:
        type_ (NotificationGroupSentViaItemType): The method used for sending the notification
        count (int): Number of notifications sent using the method
        platform (Union[Unset, NotificationGroupSentViaItemPlatform]): Platform used for sending the notification
        success_count (Union[Unset, int]): Number of successful notifications sent
        failed_count (Union[Unset, int]): Number of failed notifications
    """

    type_: NotificationGroupSentViaItemType
    count: int
    platform: Union[Unset, NotificationGroupSentViaItemPlatform] = UNSET
    success_count: Union[Unset, int] = UNSET
    failed_count: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        count = self.count

        platform: Union[Unset, str] = UNSET
        if not isinstance(self.platform, Unset):
            platform = self.platform.value

        success_count = self.success_count

        failed_count = self.failed_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "count": count,
            }
        )
        if platform is not UNSET:
            field_dict["platform"] = platform
        if success_count is not UNSET:
            field_dict["successCount"] = success_count
        if failed_count is not UNSET:
            field_dict["failedCount"] = failed_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = NotificationGroupSentViaItemType(d.pop("type"))

        count = d.pop("count")

        _platform = d.pop("platform", UNSET)
        platform: Union[Unset, NotificationGroupSentViaItemPlatform]
        if isinstance(_platform, Unset):
            platform = UNSET
        else:
            platform = NotificationGroupSentViaItemPlatform(_platform)

        success_count = d.pop("successCount", UNSET)

        failed_count = d.pop("failedCount", UNSET)

        notification_group_sent_via_item = cls(
            type_=type_,
            count=count,
            platform=platform,
            success_count=success_count,
            failed_count=failed_count,
        )

        notification_group_sent_via_item.additional_properties = d
        return notification_group_sent_via_item

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
