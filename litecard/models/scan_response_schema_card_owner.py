from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ScanResponseSchemaCardOwner")


@_attrs_define
class ScanResponseSchemaCardOwner:
    """Fields that are returned for each card owner

    Attributes:
        id (str): Id of the card Example: -jJWhjZ1a.
        first_name (Union[Unset, str]): First name of card owner Example: Ankus Fang.
        last_name (Union[Unset, str]): Last name of card owner Example: AHVW1qv4I_Teqdu4VjwMA.
        phone (Union[Unset, str]): phoneNumber of the card owner Example: 0409381912.
        email (Union[Unset, str]): Email of the card owner Example: test@litecard.io.
        user_type (Union[Unset, str]): User Type Example: basic.
        state (Union[Unset, str]): State the user is from  Example: VIC.
    """

    id: str
    first_name: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    phone: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    user_type: Union[Unset, str] = UNSET
    state: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        first_name = self.first_name

        last_name = self.last_name

        phone = self.phone

        email = self.email

        user_type = self.user_type

        state = self.state

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if phone is not UNSET:
            field_dict["phone"] = phone
        if email is not UNSET:
            field_dict["email"] = email
        if user_type is not UNSET:
            field_dict["userType"] = user_type
        if state is not UNSET:
            field_dict["state"] = state

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        first_name = d.pop("firstName", UNSET)

        last_name = d.pop("lastName", UNSET)

        phone = d.pop("phone", UNSET)

        email = d.pop("email", UNSET)

        user_type = d.pop("userType", UNSET)

        state = d.pop("state", UNSET)

        scan_response_schema_card_owner = cls(
            id=id,
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            email=email,
            user_type=user_type,
            state=state,
        )

        scan_response_schema_card_owner.additional_properties = d
        return scan_response_schema_card_owner

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
