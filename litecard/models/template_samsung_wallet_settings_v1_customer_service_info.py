from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TemplateSamsungWalletSettingsV1CustomerServiceInfo")


@_attrs_define
class TemplateSamsungWalletSettingsV1CustomerServiceInfo:
    """Customer service contact details. Known as 'csInfo' on samsung fields

    Attributes:
        call (Union[Unset, str]): Phone number Example: +61 (03) 9999 9000.
        email (Union[Unset, str]): Email address Example: restaurant-name@gmail.com.
        website (Union[Unset, str]): Website url Example: https://www.restaurant-name.com/.
    """

    call: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    website: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        call = self.call

        email = self.email

        website = self.website

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if call is not UNSET:
            field_dict["call"] = call
        if email is not UNSET:
            field_dict["email"] = email
        if website is not UNSET:
            field_dict["website"] = website

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        call = d.pop("call", UNSET)

        email = d.pop("email", UNSET)

        website = d.pop("website", UNSET)

        template_samsung_wallet_settings_v1_customer_service_info = cls(
            call=call,
            email=email,
            website=website,
        )

        template_samsung_wallet_settings_v1_customer_service_info.additional_properties = d
        return template_samsung_wallet_settings_v1_customer_service_info

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
