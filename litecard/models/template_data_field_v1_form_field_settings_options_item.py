from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TemplateDataFieldV1FormFieldSettingsOptionsItem")


@_attrs_define
class TemplateDataFieldV1FormFieldSettingsOptionsItem:
    """
    Attributes:
        value (Union[Unset, str]): Value of the selected option
        title (Union[Unset, str]): Label that front end displays
        order (Union[Unset, float]): Numbered by priority, the final order will be in ascending order Example: 1.
    """

    value: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    order: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        value = self.value

        title = self.title

        order = self.order

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if value is not UNSET:
            field_dict["value"] = value
        if title is not UNSET:
            field_dict["title"] = title
        if order is not UNSET:
            field_dict["order"] = order

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        value = d.pop("value", UNSET)

        title = d.pop("title", UNSET)

        order = d.pop("order", UNSET)

        template_data_field_v1_form_field_settings_options_item = cls(
            value=value,
            title=title,
            order=order,
        )

        template_data_field_v1_form_field_settings_options_item.additional_properties = d
        return template_data_field_v1_form_field_settings_options_item

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
