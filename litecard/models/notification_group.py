import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.notification_group_status import NotificationGroupStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.notification_group_sent_via_item import NotificationGroupSentViaItem


T = TypeVar("T", bound="NotificationGroup")


@_attrs_define
class NotificationGroup:
    """
    Attributes:
        id (Union[Unset, str]): Unique identifier for the notification group
        title (Union[Unset, str]): Title of the notification group
        message (Union[Unset, str]): Message content of the notification group
        participants_count (Union[Unset, int]): Number of participants in the notification group
        sent_via (Union[Unset, list['NotificationGroupSentViaItem']]): Array of objects detailing the count of
            notifications sent via each method
        send_time (Union[Unset, datetime.datetime]): Creation date and time of the notification group
        created_at (Union[Unset, datetime.datetime]): Creation date and time of the notification group
        status (Union[Unset, NotificationGroupStatus]): Current status of the notification group
        business_id (Union[Unset, str]): ID of the business that owns the notification group
    """

    id: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    message: Union[Unset, str] = UNSET
    participants_count: Union[Unset, int] = UNSET
    sent_via: Union[Unset, list["NotificationGroupSentViaItem"]] = UNSET
    send_time: Union[Unset, datetime.datetime] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    status: Union[Unset, NotificationGroupStatus] = UNSET
    business_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        title = self.title

        message = self.message

        participants_count = self.participants_count

        sent_via: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.sent_via, Unset):
            sent_via = []
            for sent_via_item_data in self.sent_via:
                sent_via_item = sent_via_item_data.to_dict()
                sent_via.append(sent_via_item)

        send_time: Union[Unset, str] = UNSET
        if not isinstance(self.send_time, Unset):
            send_time = self.send_time.isoformat()

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        business_id = self.business_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if title is not UNSET:
            field_dict["title"] = title
        if message is not UNSET:
            field_dict["message"] = message
        if participants_count is not UNSET:
            field_dict["participantsCount"] = participants_count
        if sent_via is not UNSET:
            field_dict["sentVia"] = sent_via
        if send_time is not UNSET:
            field_dict["sendTime"] = send_time
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if status is not UNSET:
            field_dict["status"] = status
        if business_id is not UNSET:
            field_dict["businessId"] = business_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.notification_group_sent_via_item import NotificationGroupSentViaItem

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        title = d.pop("title", UNSET)

        message = d.pop("message", UNSET)

        participants_count = d.pop("participantsCount", UNSET)

        sent_via = []
        _sent_via = d.pop("sentVia", UNSET)
        for sent_via_item_data in _sent_via or []:
            sent_via_item = NotificationGroupSentViaItem.from_dict(sent_via_item_data)

            sent_via.append(sent_via_item)

        _send_time = d.pop("sendTime", UNSET)
        send_time: Union[Unset, datetime.datetime]
        if isinstance(_send_time, Unset):
            send_time = UNSET
        else:
            send_time = isoparse(_send_time)

        _created_at = d.pop("createdAt", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        _status = d.pop("status", UNSET)
        status: Union[Unset, NotificationGroupStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = NotificationGroupStatus(_status)

        business_id = d.pop("businessId", UNSET)

        notification_group = cls(
            id=id,
            title=title,
            message=message,
            participants_count=participants_count,
            sent_via=sent_via,
            send_time=send_time,
            created_at=created_at,
            status=status,
            business_id=business_id,
        )

        notification_group.additional_properties = d
        return notification_group

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
