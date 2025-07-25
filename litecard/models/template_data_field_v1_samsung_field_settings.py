from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.template_data_field_v1_samsung_field_settings_samsung_field_type import (
    TemplateDataFieldV1SamsungFieldSettingsSamsungFieldType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="TemplateDataFieldV1SamsungFieldSettings")


@_attrs_define
class TemplateDataFieldV1SamsungFieldSettings:
    """Samsung field settings

    Attributes:
        location (TemplateDataFieldV1SamsungFieldSettingsSamsungFieldType): The type of samsung field Example:
            TEXT_MODULE_DATA.
        position (Union[Unset, int]): The position in the noticeDesc array. e.g. A position of 0 means it is first in
            order to be rendered in that section. Positions start from 0. Example: 1.
    """

    location: TemplateDataFieldV1SamsungFieldSettingsSamsungFieldType
    position: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        location = self.location.value

        position = self.position

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "location": location,
            }
        )
        if position is not UNSET:
            field_dict["position"] = position

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        location = TemplateDataFieldV1SamsungFieldSettingsSamsungFieldType(d.pop("location"))

        position = d.pop("position", UNSET)

        template_data_field_v1_samsung_field_settings = cls(
            location=location,
            position=position,
        )

        template_data_field_v1_samsung_field_settings.additional_properties = d
        return template_data_field_v1_samsung_field_settings

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
