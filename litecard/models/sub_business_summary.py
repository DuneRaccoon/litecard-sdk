from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SubBusinessSummary")


@_attrs_define
class SubBusinessSummary:
    """
    Attributes:
        id (Union[Unset, str]): Business Id Example: CryoGym.
        business_name (Union[Unset, str]): Business name Example: Cryo gym.
        sub_business_name (Union[Unset, str]): Name to show on sub business selection Example: Cryo gym - Sub 1.
        logo_url (Union[Unset, str]): Business logo image file Example: https://assets.dev.litecard.io/Logo-Badge_3.png.
    """

    id: Union[Unset, str] = UNSET
    business_name: Union[Unset, str] = UNSET
    sub_business_name: Union[Unset, str] = UNSET
    logo_url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        business_name = self.business_name

        sub_business_name = self.sub_business_name

        logo_url = self.logo_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if business_name is not UNSET:
            field_dict["businessName"] = business_name
        if sub_business_name is not UNSET:
            field_dict["subBusinessName"] = sub_business_name
        if logo_url is not UNSET:
            field_dict["logoUrl"] = logo_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        business_name = d.pop("businessName", UNSET)

        sub_business_name = d.pop("subBusinessName", UNSET)

        logo_url = d.pop("logoUrl", UNSET)

        sub_business_summary = cls(
            id=id,
            business_name=business_name,
            sub_business_name=sub_business_name,
            logo_url=logo_url,
        )

        sub_business_summary.additional_properties = d
        return sub_business_summary

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
