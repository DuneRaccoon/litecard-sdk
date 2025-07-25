from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CustomFormDesignFooterSection")


@_attrs_define
class CustomFormDesignFooterSection:
    """Configuration for the footer section of the form

    Attributes:
        content1 (Union[Unset, str]): Footer header text Example: Footer Header.
        content2 (Union[Unset, str]): Content for the footer Example: This is the footer content..
        image (Union[Unset, str]): URL of the footer image Example: /path/to/footer-image.png.
        text_colour (Union[Unset, str]): Colour of the text Example: #000000.
    """

    content1: Union[Unset, str] = UNSET
    content2: Union[Unset, str] = UNSET
    image: Union[Unset, str] = UNSET
    text_colour: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        content1 = self.content1

        content2 = self.content2

        image = self.image

        text_colour = self.text_colour

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if content1 is not UNSET:
            field_dict["content1"] = content1
        if content2 is not UNSET:
            field_dict["content2"] = content2
        if image is not UNSET:
            field_dict["image"] = image
        if text_colour is not UNSET:
            field_dict["textColour"] = text_colour

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        content1 = d.pop("content1", UNSET)

        content2 = d.pop("content2", UNSET)

        image = d.pop("image", UNSET)

        text_colour = d.pop("textColour", UNSET)

        custom_form_design_footer_section = cls(
            content1=content1,
            content2=content2,
            image=image,
            text_colour=text_colour,
        )

        custom_form_design_footer_section.additional_properties = d
        return custom_form_design_footer_section

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
