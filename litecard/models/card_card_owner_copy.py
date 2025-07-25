from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CardCardOwnerCopy")


@_attrs_define
class CardCardOwnerCopy:
    """A copy of the card owner's information

    Attributes:
        id (Union[Unset, str]): Unique identifier for the card owner Example: JUJCSVGnLihP6xcTRElpJ.
        business_id (Union[Unset, str]): Identifier for the business associated with the card owner Example:
            LgAcJKiMP5qJf8mKv9a9S.
        name (Union[Unset, str]): Full name of the card owner Example: John Doe.
        membership_number (Union[Unset, str]): Membership number associated with the card Example: M123456789.
    """

    id: Union[Unset, str] = UNSET
    business_id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    membership_number: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        business_id = self.business_id

        name = self.name

        membership_number = self.membership_number

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if business_id is not UNSET:
            field_dict["businessId"] = business_id
        if name is not UNSET:
            field_dict["name"] = name
        if membership_number is not UNSET:
            field_dict["membershipNumber"] = membership_number

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        business_id = d.pop("businessId", UNSET)

        name = d.pop("name", UNSET)

        membership_number = d.pop("membershipNumber", UNSET)

        card_card_owner_copy = cls(
            id=id,
            business_id=business_id,
            name=name,
            membership_number=membership_number,
        )

        card_card_owner_copy.additional_properties = d
        return card_card_owner_copy

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
