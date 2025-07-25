from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CustomFormDesignBackgroundStyles")


@_attrs_define
class CustomFormDesignBackgroundStyles:
    """Background styling options

    Attributes:
        colour (Union[Unset, str]): Background color Default: '#FFFFFF'. Example: lightgrey.
        text_colour (Union[Unset, str]): Text color Default: '#000000'. Example: #000000.
    """

    colour: Union[Unset, str] = "#FFFFFF"
    text_colour: Union[Unset, str] = "#000000"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        colour = self.colour

        text_colour = self.text_colour

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if colour is not UNSET:
            field_dict["colour"] = colour
        if text_colour is not UNSET:
            field_dict["textColour"] = text_colour

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        colour = d.pop("colour", UNSET)

        text_colour = d.pop("textColour", UNSET)

        custom_form_design_background_styles = cls(
            colour=colour,
            text_colour=text_colour,
        )

        custom_form_design_background_styles.additional_properties = d
        return custom_form_design_background_styles

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
