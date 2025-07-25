from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.template_card_expiry_type_1_expiry_type import TemplateCardExpiryType1ExpiryType
from ..types import UNSET, Unset

T = TypeVar("T", bound="TemplateCardExpiryType1")


@_attrs_define
class TemplateCardExpiryType1:
    """
    Attributes:
        expiry_type (Union[Unset, TemplateCardExpiryType1ExpiryType]): Type of expiry, either NEVER, FIXED_DATE or
            FROM_ACTIVATION Example: FIXED_DATE.
        fixed_date (Union[Unset, str]): The fixed date the card produced by this template will expire Example:
            2022-01-10T07:00:15.075Z.
    """

    expiry_type: Union[Unset, TemplateCardExpiryType1ExpiryType] = UNSET
    fixed_date: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        expiry_type: Union[Unset, str] = UNSET
        if not isinstance(self.expiry_type, Unset):
            expiry_type = self.expiry_type.value

        fixed_date = self.fixed_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if expiry_type is not UNSET:
            field_dict["expiryType"] = expiry_type
        if fixed_date is not UNSET:
            field_dict["fixedDate"] = fixed_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _expiry_type = d.pop("expiryType", UNSET)
        expiry_type: Union[Unset, TemplateCardExpiryType1ExpiryType]
        if isinstance(_expiry_type, Unset):
            expiry_type = UNSET
        else:
            expiry_type = TemplateCardExpiryType1ExpiryType(_expiry_type)

        fixed_date = d.pop("fixedDate", UNSET)

        template_card_expiry_type_1 = cls(
            expiry_type=expiry_type,
            fixed_date=fixed_date,
        )

        template_card_expiry_type_1.additional_properties = d
        return template_card_expiry_type_1

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
