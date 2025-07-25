from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CardOwnerRequestBody")


@_attrs_define
class CardOwnerRequestBody:
    """
    Attributes:
        first_name (Union[Unset, str]): First name of the user Example: John.
        last_name (Union[Unset, str]): Last name of the user Example: Doe.
        email (Union[Unset, str]): Email address of the user Example: john@litecard.com.au.
        phone (Union[Unset, str]): Phone number of the user Example: 1234567890.
        state (Union[Unset, str]): State of Residence Example: VIC.
        form_id (Union[Unset, str]): Id to define the schema for field inputs used to create/update the card.. Example:
            kSwoChd.
        business_id (Union[Unset, str]): Business Id of the sign up form Example: sample_dev_company.
    """

    first_name: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    phone: Union[Unset, str] = UNSET
    state: Union[Unset, str] = UNSET
    form_id: Union[Unset, str] = UNSET
    business_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        first_name = self.first_name

        last_name = self.last_name

        email = self.email

        phone = self.phone

        state = self.state

        form_id = self.form_id

        business_id = self.business_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if email is not UNSET:
            field_dict["email"] = email
        if phone is not UNSET:
            field_dict["phone"] = phone
        if state is not UNSET:
            field_dict["state"] = state
        if form_id is not UNSET:
            field_dict["formId"] = form_id
        if business_id is not UNSET:
            field_dict["businessId"] = business_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        first_name = d.pop("firstName", UNSET)

        last_name = d.pop("lastName", UNSET)

        email = d.pop("email", UNSET)

        phone = d.pop("phone", UNSET)

        state = d.pop("state", UNSET)

        form_id = d.pop("formId", UNSET)

        business_id = d.pop("businessId", UNSET)

        card_owner_request_body = cls(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            state=state,
            form_id=form_id,
            business_id=business_id,
        )

        card_owner_request_body.additional_properties = d
        return card_owner_request_body

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
