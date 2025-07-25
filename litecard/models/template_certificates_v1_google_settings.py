from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TemplateCertificatesV1GoogleSettings")


@_attrs_define
class TemplateCertificatesV1GoogleSettings:
    """Google specific settings

    Attributes:
        cert_id (Union[Unset, str]): Google Certificate Litecard Id Example: s2pkdjkASg3.
        google_issuer_id (Union[Unset, str]): Google Issuer Id Example: 123524234.
        redemption_issuers (Union[Unset, list[str]]): List of Redemption Issuers Example: ['33315096237343'].
    """

    cert_id: Union[Unset, str] = UNSET
    google_issuer_id: Union[Unset, str] = UNSET
    redemption_issuers: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cert_id = self.cert_id

        google_issuer_id = self.google_issuer_id

        redemption_issuers: Union[Unset, list[str]] = UNSET
        if not isinstance(self.redemption_issuers, Unset):
            redemption_issuers = self.redemption_issuers

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cert_id is not UNSET:
            field_dict["certId"] = cert_id
        if google_issuer_id is not UNSET:
            field_dict["googleIssuerId"] = google_issuer_id
        if redemption_issuers is not UNSET:
            field_dict["redemptionIssuers"] = redemption_issuers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cert_id = d.pop("certId", UNSET)

        google_issuer_id = d.pop("googleIssuerId", UNSET)

        redemption_issuers = cast(list[str], d.pop("redemptionIssuers", UNSET))

        template_certificates_v1_google_settings = cls(
            cert_id=cert_id,
            google_issuer_id=google_issuer_id,
            redemption_issuers=redemption_issuers,
        )

        template_certificates_v1_google_settings.additional_properties = d
        return template_certificates_v1_google_settings

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
