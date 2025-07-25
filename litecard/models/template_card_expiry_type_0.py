from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.template_card_expiry_type_0_expiry_type import TemplateCardExpiryType0ExpiryType
from ..types import UNSET, Unset

T = TypeVar("T", bound="TemplateCardExpiryType0")


@_attrs_define
class TemplateCardExpiryType0:
    """
    Attributes:
        expiry_type (Union[Unset, TemplateCardExpiryType0ExpiryType]): Type of expiry, either NEVER, FIXED_DATE,
            FROM_ACTIVATION  Example: NEVER.
    """

    expiry_type: Union[Unset, TemplateCardExpiryType0ExpiryType] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        expiry_type: Union[Unset, str] = UNSET
        if not isinstance(self.expiry_type, Unset):
            expiry_type = self.expiry_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if expiry_type is not UNSET:
            field_dict["expiryType"] = expiry_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _expiry_type = d.pop("expiryType", UNSET)
        expiry_type: Union[Unset, TemplateCardExpiryType0ExpiryType]
        if isinstance(_expiry_type, Unset):
            expiry_type = UNSET
        else:
            expiry_type = TemplateCardExpiryType0ExpiryType(_expiry_type)

        template_card_expiry_type_0 = cls(
            expiry_type=expiry_type,
        )

        template_card_expiry_type_0.additional_properties = d
        return template_card_expiry_type_0

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
