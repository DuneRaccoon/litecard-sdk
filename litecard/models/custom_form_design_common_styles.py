from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CustomFormDesignCommonStyles")


@_attrs_define
class CustomFormDesignCommonStyles:
    """Common styles applied throughout the form

    Attributes:
        input_bg_colour (Union[Unset, str]): Background color for input fields Default: '#FFFFFF'. Example: #FFFFFF.
        input_text_colour (Union[Unset, str]): Text color for input fields Default: '#000000'. Example: #000000.
        input_border_colour (Union[Unset, str]): Border color for input fields Default: '#000000'. Example: #000000.
        icon_bg_colour (Union[Unset, str]): Background color for icons Default: '#000000'. Example: #000000.
        icon_colour (Union[Unset, str]): Color for icons Default: '#FFFFFF'. Example: #FFFFFF.
        link_colour (Union[Unset, str]): Colour of the links Default: '#1677ff'. Example: #1677ff.
        active_input_bg_colour (Union[Unset, str]): Background color for active input fields Example: #F0F0F0.
        active_input_text_colour (Union[Unset, str]): Text color for active input fields Example: #333333.
        active_link_colour (Union[Unset, str]): Colour of active links Example: #0056b3.
        disabled_input_bg_colour (Union[Unset, str]): Background color for disabled input fields Example: #E0E0E0.
        disabled_input_text_colour (Union[Unset, str]): Text color for disabled input fields Example: #999999.
        error_text_colour (Union[Unset, str]): Colour of error text Default: 'red'. Example: red.
        left_section_font_family (Union[Unset, str]): Font family for the left section Example: Arial.
        header_font_family (Union[Unset, str]): Font family for the header Example: Arial.
    """

    input_bg_colour: Union[Unset, str] = "#FFFFFF"
    input_text_colour: Union[Unset, str] = "#000000"
    input_border_colour: Union[Unset, str] = "#000000"
    icon_bg_colour: Union[Unset, str] = "#000000"
    icon_colour: Union[Unset, str] = "#FFFFFF"
    link_colour: Union[Unset, str] = "#1677ff"
    active_input_bg_colour: Union[Unset, str] = UNSET
    active_input_text_colour: Union[Unset, str] = UNSET
    active_link_colour: Union[Unset, str] = UNSET
    disabled_input_bg_colour: Union[Unset, str] = UNSET
    disabled_input_text_colour: Union[Unset, str] = UNSET
    error_text_colour: Union[Unset, str] = "red"
    left_section_font_family: Union[Unset, str] = UNSET
    header_font_family: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        input_bg_colour = self.input_bg_colour

        input_text_colour = self.input_text_colour

        input_border_colour = self.input_border_colour

        icon_bg_colour = self.icon_bg_colour

        icon_colour = self.icon_colour

        link_colour = self.link_colour

        active_input_bg_colour = self.active_input_bg_colour

        active_input_text_colour = self.active_input_text_colour

        active_link_colour = self.active_link_colour

        disabled_input_bg_colour = self.disabled_input_bg_colour

        disabled_input_text_colour = self.disabled_input_text_colour

        error_text_colour = self.error_text_colour

        left_section_font_family = self.left_section_font_family

        header_font_family = self.header_font_family

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if input_bg_colour is not UNSET:
            field_dict["inputBgColour"] = input_bg_colour
        if input_text_colour is not UNSET:
            field_dict["inputTextColour"] = input_text_colour
        if input_border_colour is not UNSET:
            field_dict["inputBorderColour"] = input_border_colour
        if icon_bg_colour is not UNSET:
            field_dict["iconBgColour"] = icon_bg_colour
        if icon_colour is not UNSET:
            field_dict["iconColour"] = icon_colour
        if link_colour is not UNSET:
            field_dict["linkColour"] = link_colour
        if active_input_bg_colour is not UNSET:
            field_dict["activeInputBgColour"] = active_input_bg_colour
        if active_input_text_colour is not UNSET:
            field_dict["activeInputTextColour"] = active_input_text_colour
        if active_link_colour is not UNSET:
            field_dict["activeLinkColour"] = active_link_colour
        if disabled_input_bg_colour is not UNSET:
            field_dict["disabledInputBgColour"] = disabled_input_bg_colour
        if disabled_input_text_colour is not UNSET:
            field_dict["disabledInputTextColour"] = disabled_input_text_colour
        if error_text_colour is not UNSET:
            field_dict["errorTextColour"] = error_text_colour
        if left_section_font_family is not UNSET:
            field_dict["leftSectionFontFamily"] = left_section_font_family
        if header_font_family is not UNSET:
            field_dict["headerFontFamily"] = header_font_family

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        input_bg_colour = d.pop("inputBgColour", UNSET)

        input_text_colour = d.pop("inputTextColour", UNSET)

        input_border_colour = d.pop("inputBorderColour", UNSET)

        icon_bg_colour = d.pop("iconBgColour", UNSET)

        icon_colour = d.pop("iconColour", UNSET)

        link_colour = d.pop("linkColour", UNSET)

        active_input_bg_colour = d.pop("activeInputBgColour", UNSET)

        active_input_text_colour = d.pop("activeInputTextColour", UNSET)

        active_link_colour = d.pop("activeLinkColour", UNSET)

        disabled_input_bg_colour = d.pop("disabledInputBgColour", UNSET)

        disabled_input_text_colour = d.pop("disabledInputTextColour", UNSET)

        error_text_colour = d.pop("errorTextColour", UNSET)

        left_section_font_family = d.pop("leftSectionFontFamily", UNSET)

        header_font_family = d.pop("headerFontFamily", UNSET)

        custom_form_design_common_styles = cls(
            input_bg_colour=input_bg_colour,
            input_text_colour=input_text_colour,
            input_border_colour=input_border_colour,
            icon_bg_colour=icon_bg_colour,
            icon_colour=icon_colour,
            link_colour=link_colour,
            active_input_bg_colour=active_input_bg_colour,
            active_input_text_colour=active_input_text_colour,
            active_link_colour=active_link_colour,
            disabled_input_bg_colour=disabled_input_bg_colour,
            disabled_input_text_colour=disabled_input_text_colour,
            error_text_colour=error_text_colour,
            left_section_font_family=left_section_font_family,
            header_font_family=header_font_family,
        )

        custom_form_design_common_styles.additional_properties = d
        return custom_form_design_common_styles

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
