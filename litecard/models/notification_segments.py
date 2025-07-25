from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NotificationSegments")


@_attrs_define
class NotificationSegments:
    """
    Attributes:
        segment1 (Union[Unset, list[str]]): List of segment values
        segment2 (Union[Unset, list[str]]): List of segment values
        segment3 (Union[Unset, list[str]]): List of segment values
        segment4 (Union[Unset, list[str]]): List of segment values
        segment5 (Union[Unset, list[str]]): List of segment values
    """

    segment1: Union[Unset, list[str]] = UNSET
    segment2: Union[Unset, list[str]] = UNSET
    segment3: Union[Unset, list[str]] = UNSET
    segment4: Union[Unset, list[str]] = UNSET
    segment5: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        segment1: Union[Unset, list[str]] = UNSET
        if not isinstance(self.segment1, Unset):
            segment1 = self.segment1

        segment2: Union[Unset, list[str]] = UNSET
        if not isinstance(self.segment2, Unset):
            segment2 = self.segment2

        segment3: Union[Unset, list[str]] = UNSET
        if not isinstance(self.segment3, Unset):
            segment3 = self.segment3

        segment4: Union[Unset, list[str]] = UNSET
        if not isinstance(self.segment4, Unset):
            segment4 = self.segment4

        segment5: Union[Unset, list[str]] = UNSET
        if not isinstance(self.segment5, Unset):
            segment5 = self.segment5

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if segment1 is not UNSET:
            field_dict["segment1"] = segment1
        if segment2 is not UNSET:
            field_dict["segment2"] = segment2
        if segment3 is not UNSET:
            field_dict["segment3"] = segment3
        if segment4 is not UNSET:
            field_dict["segment4"] = segment4
        if segment5 is not UNSET:
            field_dict["segment5"] = segment5

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        segment1 = cast(list[str], d.pop("segment1", UNSET))

        segment2 = cast(list[str], d.pop("segment2", UNSET))

        segment3 = cast(list[str], d.pop("segment3", UNSET))

        segment4 = cast(list[str], d.pop("segment4", UNSET))

        segment5 = cast(list[str], d.pop("segment5", UNSET))

        notification_segments = cls(
            segment1=segment1,
            segment2=segment2,
            segment3=segment3,
            segment4=segment4,
            segment5=segment5,
        )

        notification_segments.additional_properties = d
        return notification_segments

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
