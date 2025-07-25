from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TemplateCertificatesV1AppleSettings")


@_attrs_define
class TemplateCertificatesV1AppleSettings:
    """Apple specific settings

    Attributes:
        cert_id (Union[Unset, str]): Apple Certificate Litecard Id Example: st3dfdAsaaf.
    """

    cert_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cert_id = self.cert_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cert_id is not UNSET:
            field_dict["certId"] = cert_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cert_id = d.pop("certId", UNSET)

        template_certificates_v1_apple_settings = cls(
            cert_id=cert_id,
        )

        template_certificates_v1_apple_settings.additional_properties = d
        return template_certificates_v1_apple_settings

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
