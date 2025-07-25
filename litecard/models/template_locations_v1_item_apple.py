from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TemplateLocationsV1ItemApple")


@_attrs_define
class TemplateLocationsV1ItemApple:
    """Apple specific location fields

    Attributes:
        lock_screen_message (Union[Unset, str]): Lock screen message displayed when a pass within proximity of the
            location Example: Buy 1 get 1 free today only.
    """

    lock_screen_message: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        lock_screen_message = self.lock_screen_message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if lock_screen_message is not UNSET:
            field_dict["lockScreenMessage"] = lock_screen_message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        lock_screen_message = d.pop("lockScreenMessage", UNSET)

        template_locations_v1_item_apple = cls(
            lock_screen_message=lock_screen_message,
        )

        template_locations_v1_item_apple.additional_properties = d
        return template_locations_v1_item_apple

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
