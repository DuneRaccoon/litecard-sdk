from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FormV1Style")


@_attrs_define
class FormV1Style:
    """
    Attributes:
        bg_primary (Union[Unset, str]): Primary colour for the form background Example: #1890ff.
        bg_secondary (Union[Unset, str]): Secondary colour for the form background Example: #1890ff.
        btn_primary (Union[Unset, str]): Secondary colour for the button Example: #1890ff.
        btn_secondary (Union[Unset, str]): Secondary colour for the button Example: #1890ff.
        label (Union[Unset, str]): Label colour for Apple Passes Example: #f1f0f2.
        custom_css_links (Union[Unset, list[str]]): List of custom css links
    """

    bg_primary: Union[Unset, str] = UNSET
    bg_secondary: Union[Unset, str] = UNSET
    btn_primary: Union[Unset, str] = UNSET
    btn_secondary: Union[Unset, str] = UNSET
    label: Union[Unset, str] = UNSET
    custom_css_links: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bg_primary = self.bg_primary

        bg_secondary = self.bg_secondary

        btn_primary = self.btn_primary

        btn_secondary = self.btn_secondary

        label = self.label

        custom_css_links: Union[Unset, list[str]] = UNSET
        if not isinstance(self.custom_css_links, Unset):
            custom_css_links = self.custom_css_links

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bg_primary is not UNSET:
            field_dict["bgPrimary"] = bg_primary
        if bg_secondary is not UNSET:
            field_dict["bgSecondary"] = bg_secondary
        if btn_primary is not UNSET:
            field_dict["btnPrimary"] = btn_primary
        if btn_secondary is not UNSET:
            field_dict["btnSecondary"] = btn_secondary
        if label is not UNSET:
            field_dict["label"] = label
        if custom_css_links is not UNSET:
            field_dict["customCssLinks"] = custom_css_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bg_primary = d.pop("bgPrimary", UNSET)

        bg_secondary = d.pop("bgSecondary", UNSET)

        btn_primary = d.pop("btnPrimary", UNSET)

        btn_secondary = d.pop("btnSecondary", UNSET)

        label = d.pop("label", UNSET)

        custom_css_links = cast(list[str], d.pop("customCssLinks", UNSET))

        form_v1_style = cls(
            bg_primary=bg_primary,
            bg_secondary=bg_secondary,
            btn_primary=btn_primary,
            btn_secondary=btn_secondary,
            label=label,
            custom_css_links=custom_css_links,
        )

        form_v1_style.additional_properties = d
        return form_v1_style

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
