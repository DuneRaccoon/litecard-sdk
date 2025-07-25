from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ScanDataFields")


@_attrs_define
class ScanDataFields:
    """Structured data associated with the scan.

    Attributes:
        full_name (Union[Unset, str]): The full name as it appears on the card. Example: Danny Bui.
        intro (Union[Unset, str]): An introductory message or description related to the scan. Example: Scan or show
            your digital pass at checkout to earn points, discounts, exclusive deals and access to promotions..
        notification_key (Union[Unset, str]): A key for managing notifications post-scan. Example: No new notifications.
        points (Union[Unset, int]): The number of points associated with this scan. Example: 6.
        store (Union[Unset, str]): The store or location name where the scan took place. Example: CHAI CHEE.
        updates (Union[Unset, str]): Information on updates or alerts to be sent to the card owner. Example: You will
            receive periodic alerts and notifications through this digital membership or via email..
    """

    full_name: Union[Unset, str] = UNSET
    intro: Union[Unset, str] = UNSET
    notification_key: Union[Unset, str] = UNSET
    points: Union[Unset, int] = UNSET
    store: Union[Unset, str] = UNSET
    updates: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        full_name = self.full_name

        intro = self.intro

        notification_key = self.notification_key

        points = self.points

        store = self.store

        updates = self.updates

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if full_name is not UNSET:
            field_dict["fullName"] = full_name
        if intro is not UNSET:
            field_dict["intro"] = intro
        if notification_key is not UNSET:
            field_dict["notificationKey"] = notification_key
        if points is not UNSET:
            field_dict["points"] = points
        if store is not UNSET:
            field_dict["store"] = store
        if updates is not UNSET:
            field_dict["updates"] = updates

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        full_name = d.pop("fullName", UNSET)

        intro = d.pop("intro", UNSET)

        notification_key = d.pop("notificationKey", UNSET)

        points = d.pop("points", UNSET)

        store = d.pop("store", UNSET)

        updates = d.pop("updates", UNSET)

        scan_data_fields = cls(
            full_name=full_name,
            intro=intro,
            notification_key=notification_key,
            points=points,
            store=store,
            updates=updates,
        )

        scan_data_fields.additional_properties = d
        return scan_data_fields

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
