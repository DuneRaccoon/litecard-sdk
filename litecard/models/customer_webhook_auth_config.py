from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CustomerWebhookAuthConfig")


@_attrs_define
class CustomerWebhookAuthConfig:
    """The properties we need to use for Authentication

    Attributes:
        security_header (Union[Unset, str]): The header to use in the request when entering the key Example: X-API-KEY.
    """

    security_header: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        security_header = self.security_header

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if security_header is not UNSET:
            field_dict["securityHeader"] = security_header

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        security_header = d.pop("securityHeader", UNSET)

        customer_webhook_auth_config = cls(
            security_header=security_header,
        )

        customer_webhook_auth_config.additional_properties = d
        return customer_webhook_auth_config

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
