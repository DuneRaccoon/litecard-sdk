from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.template_data_field_v1_google_field_settings_field_type import (
    TemplateDataFieldV1GoogleFieldSettingsFieldType,
)
from ..models.template_data_field_v1_google_field_settings_google_field_type import (
    TemplateDataFieldV1GoogleFieldSettingsGoogleFieldType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="TemplateDataFieldV1GoogleFieldSettings")


@_attrs_define
class TemplateDataFieldV1GoogleFieldSettings:
    """Google wallet settings

    Attributes:
        location (TemplateDataFieldV1GoogleFieldSettingsGoogleFieldType): The type of google field Example:
            TEXT_MODULE_DATA.
        position (Union[Unset, int]): The position in the text modules data array. e.g. A position of 0 means it is
            first in order to be rendered in that section. Positions start from 0. Example: 1.
        card_row (Union[Unset, bool]): If this field should be displayed on the front of the pass
        field_type (Union[Unset, TemplateDataFieldV1GoogleFieldSettingsFieldType]): If using MESSAGES location, what
            type of MESSAGE field it is
    """

    location: TemplateDataFieldV1GoogleFieldSettingsGoogleFieldType
    position: Union[Unset, int] = UNSET
    card_row: Union[Unset, bool] = UNSET
    field_type: Union[Unset, TemplateDataFieldV1GoogleFieldSettingsFieldType] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        location = self.location.value

        position = self.position

        card_row = self.card_row

        field_type: Union[Unset, str] = UNSET
        if not isinstance(self.field_type, Unset):
            field_type = self.field_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "location": location,
            }
        )
        if position is not UNSET:
            field_dict["position"] = position
        if card_row is not UNSET:
            field_dict["cardRow"] = card_row
        if field_type is not UNSET:
            field_dict["fieldType"] = field_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        location = TemplateDataFieldV1GoogleFieldSettingsGoogleFieldType(d.pop("location"))

        position = d.pop("position", UNSET)

        card_row = d.pop("cardRow", UNSET)

        _field_type = d.pop("fieldType", UNSET)
        field_type: Union[Unset, TemplateDataFieldV1GoogleFieldSettingsFieldType]
        if isinstance(_field_type, Unset):
            field_type = UNSET
        else:
            field_type = TemplateDataFieldV1GoogleFieldSettingsFieldType(_field_type)

        template_data_field_v1_google_field_settings = cls(
            location=location,
            position=position,
            card_row=card_row,
            field_type=field_type,
        )

        template_data_field_v1_google_field_settings.additional_properties = d
        return template_data_field_v1_google_field_settings

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
