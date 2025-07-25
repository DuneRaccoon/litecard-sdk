from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.template_colours_v1_samsung_font import TemplateColoursV1SamsungFont
from ..types import UNSET, Unset

T = TypeVar("T", bound="TemplateColoursV1")


@_attrs_define
class TemplateColoursV1:
    """Colours of the template

    Attributes:
        background (Union[Unset, str]): Background colour of the pass Example: #ffffff.
        label (Union[Unset, str]): Label colour of the apple pass Example: #ffffff.
        foreground (Union[Unset, str]): Text colour of the apple pass Example: #ffffff.
        strip (Union[Unset, str]): Text colour on top of strip image of the apple pass Example: #ffffff.
        samsung_blink (Union[Unset, str]): Colour of the blinking indicating area in samsung wallet Example: #00ffaa.
        samsung_font (Union[Unset, TemplateColoursV1SamsungFont]): Colour of the font on the Samsung card
    """

    background: Union[Unset, str] = UNSET
    label: Union[Unset, str] = UNSET
    foreground: Union[Unset, str] = UNSET
    strip: Union[Unset, str] = UNSET
    samsung_blink: Union[Unset, str] = UNSET
    samsung_font: Union[Unset, TemplateColoursV1SamsungFont] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        background = self.background

        label = self.label

        foreground = self.foreground

        strip = self.strip

        samsung_blink = self.samsung_blink

        samsung_font: Union[Unset, str] = UNSET
        if not isinstance(self.samsung_font, Unset):
            samsung_font = self.samsung_font.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if background is not UNSET:
            field_dict["background"] = background
        if label is not UNSET:
            field_dict["label"] = label
        if foreground is not UNSET:
            field_dict["foreground"] = foreground
        if strip is not UNSET:
            field_dict["strip"] = strip
        if samsung_blink is not UNSET:
            field_dict["samsungBlink"] = samsung_blink
        if samsung_font is not UNSET:
            field_dict["samsungFont"] = samsung_font

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        background = d.pop("background", UNSET)

        label = d.pop("label", UNSET)

        foreground = d.pop("foreground", UNSET)

        strip = d.pop("strip", UNSET)

        samsung_blink = d.pop("samsungBlink", UNSET)

        _samsung_font = d.pop("samsungFont", UNSET)
        samsung_font: Union[Unset, TemplateColoursV1SamsungFont]
        if isinstance(_samsung_font, Unset):
            samsung_font = UNSET
        else:
            samsung_font = TemplateColoursV1SamsungFont(_samsung_font)

        template_colours_v1 = cls(
            background=background,
            label=label,
            foreground=foreground,
            strip=strip,
            samsung_blink=samsung_blink,
            samsung_font=samsung_font,
        )

        template_colours_v1.additional_properties = d
        return template_colours_v1

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
