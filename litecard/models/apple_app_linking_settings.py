from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AppleAppLinkingSettings")


@_attrs_define
class AppleAppLinkingSettings:
    """Apple Settings for AppLinking

    Attributes:
        store_identifier (Union[Unset, float]): App Store Identifier
    """

    store_identifier: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        store_identifier = self.store_identifier

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if store_identifier is not UNSET:
            field_dict["storeIdentifier"] = store_identifier

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        store_identifier = d.pop("storeIdentifier", UNSET)

        apple_app_linking_settings = cls(
            store_identifier=store_identifier,
        )

        apple_app_linking_settings.additional_properties = d
        return apple_app_linking_settings

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
