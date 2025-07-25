from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.custom_form_design_left_section_styles import CustomFormDesignLeftSectionStyles


T = TypeVar("T", bound="CustomFormDesignLeftSection")


@_attrs_define
class CustomFormDesignLeftSection:
    """Configuration for the left section of the form

    Attributes:
        header (Union[Unset, str]): Header text for the left section Example: Welcome to the form.
        header_text_colour (Union[Unset, str]): Colour of the header text Default: '#000000'. Example: #000000.
        header_logo (Union[Unset, str]): URL of the header logo image Example: /path/to/logo.png.
        background_image (Union[Unset, str]): URL of the background image Example: /path/to/logo.png.
        footer_header (Union[Unset, str]): Footer header text Example: Footer Header.
        footer_content (Union[Unset, str]): Content for the footer Example: This is the footer content..
        footer_image (Union[Unset, str]): URL of the footer image Example: /path/to/footer-image.png.
        footer_large_image (Union[Unset, str]): URL of the footer image Example: /path/to/footer-image.png.
        styles (Union[Unset, CustomFormDesignLeftSectionStyles]): Styling options for the left section
        header_class_name (Union[Unset, str]): Custom CSS class for the header Example: form-header.
    """

    header: Union[Unset, str] = UNSET
    header_text_colour: Union[Unset, str] = "#000000"
    header_logo: Union[Unset, str] = UNSET
    background_image: Union[Unset, str] = UNSET
    footer_header: Union[Unset, str] = UNSET
    footer_content: Union[Unset, str] = UNSET
    footer_image: Union[Unset, str] = UNSET
    footer_large_image: Union[Unset, str] = UNSET
    styles: Union[Unset, "CustomFormDesignLeftSectionStyles"] = UNSET
    header_class_name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        header = self.header

        header_text_colour = self.header_text_colour

        header_logo = self.header_logo

        background_image = self.background_image

        footer_header = self.footer_header

        footer_content = self.footer_content

        footer_image = self.footer_image

        footer_large_image = self.footer_large_image

        styles: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.styles, Unset):
            styles = self.styles.to_dict()

        header_class_name = self.header_class_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if header is not UNSET:
            field_dict["header"] = header
        if header_text_colour is not UNSET:
            field_dict["headerTextColour"] = header_text_colour
        if header_logo is not UNSET:
            field_dict["headerLogo"] = header_logo
        if background_image is not UNSET:
            field_dict["backgroundImage"] = background_image
        if footer_header is not UNSET:
            field_dict["footerHeader"] = footer_header
        if footer_content is not UNSET:
            field_dict["footerContent"] = footer_content
        if footer_image is not UNSET:
            field_dict["footerImage"] = footer_image
        if footer_large_image is not UNSET:
            field_dict["footerLargeImage"] = footer_large_image
        if styles is not UNSET:
            field_dict["styles"] = styles
        if header_class_name is not UNSET:
            field_dict["headerClassName"] = header_class_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.custom_form_design_left_section_styles import CustomFormDesignLeftSectionStyles

        d = dict(src_dict)
        header = d.pop("header", UNSET)

        header_text_colour = d.pop("headerTextColour", UNSET)

        header_logo = d.pop("headerLogo", UNSET)

        background_image = d.pop("backgroundImage", UNSET)

        footer_header = d.pop("footerHeader", UNSET)

        footer_content = d.pop("footerContent", UNSET)

        footer_image = d.pop("footerImage", UNSET)

        footer_large_image = d.pop("footerLargeImage", UNSET)

        _styles = d.pop("styles", UNSET)
        styles: Union[Unset, CustomFormDesignLeftSectionStyles]
        if isinstance(_styles, Unset):
            styles = UNSET
        else:
            styles = CustomFormDesignLeftSectionStyles.from_dict(_styles)

        header_class_name = d.pop("headerClassName", UNSET)

        custom_form_design_left_section = cls(
            header=header,
            header_text_colour=header_text_colour,
            header_logo=header_logo,
            background_image=background_image,
            footer_header=footer_header,
            footer_content=footer_content,
            footer_image=footer_image,
            footer_large_image=footer_large_image,
            styles=styles,
            header_class_name=header_class_name,
        )

        custom_form_design_left_section.additional_properties = d
        return custom_form_design_left_section

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
