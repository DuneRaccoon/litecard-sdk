from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.template_card_expiry_v1_type_3_expiry_type import TemplateCardExpiryV1Type3ExpiryType
from ..types import UNSET, Unset

T = TypeVar("T", bound="TemplateCardExpiryV1Type3")


@_attrs_define
class TemplateCardExpiryV1Type3:
    """
    Attributes:
        expiry_type (Union[Unset, TemplateCardExpiryV1Type3ExpiryType]): Type of expiry, either NEVER, FIXED_DATE,
            FROM_ACTIVATION or FIXED_SCANS Example: FIXED_SCANS.
        scans (Union[Unset, float]): Number of scans remaining before pass expires Example: 1.
    """

    expiry_type: Union[Unset, TemplateCardExpiryV1Type3ExpiryType] = UNSET
    scans: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        expiry_type: Union[Unset, str] = UNSET
        if not isinstance(self.expiry_type, Unset):
            expiry_type = self.expiry_type.value

        scans = self.scans

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if expiry_type is not UNSET:
            field_dict["expiryType"] = expiry_type
        if scans is not UNSET:
            field_dict["scans"] = scans

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _expiry_type = d.pop("expiryType", UNSET)
        expiry_type: Union[Unset, TemplateCardExpiryV1Type3ExpiryType]
        if isinstance(_expiry_type, Unset):
            expiry_type = UNSET
        else:
            expiry_type = TemplateCardExpiryV1Type3ExpiryType(_expiry_type)

        scans = d.pop("scans", UNSET)

        template_card_expiry_v1_type_3 = cls(
            expiry_type=expiry_type,
            scans=scans,
        )

        template_card_expiry_v1_type_3.additional_properties = d
        return template_card_expiry_v1_type_3

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
