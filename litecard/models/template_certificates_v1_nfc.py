from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.template_certificates_v1_nfc_payload_type import TemplateCertificatesV1NfcPayloadType
from ..types import UNSET, Unset

T = TypeVar("T", bound="TemplateCertificatesV1Nfc")


@_attrs_define
class TemplateCertificatesV1Nfc:
    """NFC settings

    Attributes:
        is_nfc_enabled (Union[Unset, bool]): Checks if NFC cert is provided for this template
        payload_type (Union[Unset, TemplateCertificatesV1NfcPayloadType]): Payload type sent over nfc e.g. `LITECARD_ID`
            means the nfc payload will be the same as the litecard card ID Example: BARCODE_VALUE.
    """

    is_nfc_enabled: Union[Unset, bool] = UNSET
    payload_type: Union[Unset, TemplateCertificatesV1NfcPayloadType] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_nfc_enabled = self.is_nfc_enabled

        payload_type: Union[Unset, str] = UNSET
        if not isinstance(self.payload_type, Unset):
            payload_type = self.payload_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_nfc_enabled is not UNSET:
            field_dict["isNFCEnabled"] = is_nfc_enabled
        if payload_type is not UNSET:
            field_dict["payloadType"] = payload_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_nfc_enabled = d.pop("isNFCEnabled", UNSET)

        _payload_type = d.pop("payloadType", UNSET)
        payload_type: Union[Unset, TemplateCertificatesV1NfcPayloadType]
        if isinstance(_payload_type, Unset):
            payload_type = UNSET
        else:
            payload_type = TemplateCertificatesV1NfcPayloadType(_payload_type)

        template_certificates_v1_nfc = cls(
            is_nfc_enabled=is_nfc_enabled,
            payload_type=payload_type,
        )

        template_certificates_v1_nfc.additional_properties = d
        return template_certificates_v1_nfc

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
