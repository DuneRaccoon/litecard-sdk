from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TemplateColours")


@_attrs_define
class TemplateColours:
    """Colours of the template

    Attributes:
        background (Union[Unset, str]): Background colour of the template Example: #ffffff.
        label (Union[Unset, str]): Label colour of the template Example: #ffffff.
        foreground (Union[Unset, str]): Foreground colour of the template Example: #ffffff.
    """

    background: Union[Unset, str] = UNSET
    label: Union[Unset, str] = UNSET
    foreground: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        background = self.background

        label = self.label

        foreground = self.foreground

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if background is not UNSET:
            field_dict["background"] = background
        if label is not UNSET:
            field_dict["label"] = label
        if foreground is not UNSET:
            field_dict["foreground"] = foreground

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        background = d.pop("background", UNSET)

        label = d.pop("label", UNSET)

        foreground = d.pop("foreground", UNSET)

        template_colours = cls(
            background=background,
            label=label,
            foreground=foreground,
        )

        template_colours.additional_properties = d
        return template_colours

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
