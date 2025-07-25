from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MailchimpTagSettings")


@_attrs_define
class MailchimpTagSettings:
    """Mailchimp Tag Settings

    Attributes:
        value (Union[Unset, str]): Used if value is static. Value of the tag to be applied.
        field_map (Union[Unset, str]): If value is not static, map it to a specific form field
        static (Union[Unset, bool]): If the value is static across all passes or if it's dynamic based on pass
    """

    value: Union[Unset, str] = UNSET
    field_map: Union[Unset, str] = UNSET
    static: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        value = self.value

        field_map = self.field_map

        static = self.static

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if value is not UNSET:
            field_dict["value"] = value
        if field_map is not UNSET:
            field_dict["fieldMap"] = field_map
        if static is not UNSET:
            field_dict["static"] = static

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        value = d.pop("value", UNSET)

        field_map = d.pop("fieldMap", UNSET)

        static = d.pop("static", UNSET)

        mailchimp_tag_settings = cls(
            value=value,
            field_map=field_map,
            static=static,
        )

        mailchimp_tag_settings.additional_properties = d
        return mailchimp_tag_settings

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
