from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WebhookRegistrationRequestBodyAuthConfig")


@_attrs_define
class WebhookRegistrationRequestBodyAuthConfig:
    """The properties we need to use for Authentication

    Attributes:
        security_header (Union[Unset, str]): The header to use in the request when entering the key Example: X-API-KEY.
        api_key (Union[Unset, str]): API Key to use to authenticate with the webhook Example: abc123.
    """

    security_header: Union[Unset, str] = UNSET
    api_key: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        security_header = self.security_header

        api_key = self.api_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if security_header is not UNSET:
            field_dict["securityHeader"] = security_header
        if api_key is not UNSET:
            field_dict["apiKey"] = api_key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        security_header = d.pop("securityHeader", UNSET)

        api_key = d.pop("apiKey", UNSET)

        webhook_registration_request_body_auth_config = cls(
            security_header=security_header,
            api_key=api_key,
        )

        webhook_registration_request_body_auth_config.additional_properties = d
        return webhook_registration_request_body_auth_config

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
