from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BaseCardPayload")


@_attrs_define
class BaseCardPayload:
    """Datafields used by the card

    Attributes:
        email (Union[Unset, str]): Example field for email address Example: john@litecard.com.au.
        phone (Union[Unset, str]): Users mobile number for text notifications Example: +61401234567.
        example_property (Union[Unset, str]): Example card property, properties are predefined in the card template
    """

    email: Union[Unset, str] = UNSET
    phone: Union[Unset, str] = UNSET
    example_property: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        phone = self.phone

        example_property = self.example_property

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if email is not UNSET:
            field_dict["email"] = email
        if phone is not UNSET:
            field_dict["phone"] = phone
        if example_property is not UNSET:
            field_dict["exampleProperty"] = example_property

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        email = d.pop("email", UNSET)

        phone = d.pop("phone", UNSET)

        example_property = d.pop("exampleProperty", UNSET)

        base_card_payload = cls(
            email=email,
            phone=phone,
            example_property=example_property,
        )

        base_card_payload.additional_properties = d
        return base_card_payload

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
