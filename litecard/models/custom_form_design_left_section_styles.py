from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CustomFormDesignLeftSectionStyles")


@_attrs_define
class CustomFormDesignLeftSectionStyles:
    """Styling options for the left section

    Attributes:
        logo_full_with (Union[Unset, bool]): Flag to indicate if the logo should use full width Default: True.
    """

    logo_full_with: Union[Unset, bool] = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        logo_full_with = self.logo_full_with

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if logo_full_with is not UNSET:
            field_dict["logoFullWith"] = logo_full_with

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        logo_full_with = d.pop("logoFullWith", UNSET)

        custom_form_design_left_section_styles = cls(
            logo_full_with=logo_full_with,
        )

        custom_form_design_left_section_styles.additional_properties = d
        return custom_form_design_left_section_styles

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
