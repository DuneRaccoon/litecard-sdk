import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="CardOwner")


@_attrs_define
class CardOwner:
    """Information about the card owner

    Attributes:
        id (Union[Unset, str]): Unique identifier for the card owner Example: JUJCSVGnLihP6xcTRElpJ.
        business_id (Union[Unset, str]): Identifier for the business associated with the card owner Example:
            L3ZrB748fLxlFD8ZjFVgX.
        phone (Union[Unset, str]): Phone number of the card owner Example: +61402221795.
        email (Union[Unset, str]): Email address of the card owner Example: dzuy.pham+test@corplite.com.
        account_name (Union[Unset, str]): Owner of the card Example: Ankus Fang.
        user_type (Union[Unset, str]): User Type Example: basic.
        created_at (Union[Unset, datetime.datetime]): Timestamp of when the card owner record was created Example:
            2023-10-19T09:05:52.771Z.
        first_name (Union[Unset, str]): First name of the card owner Example: Dzuy.
        form_id (Union[Unset, str]): Identifier for the form associated with the card owner Example:
            TmtB-B7gadaNbH8aF7Pan.
        last_name (Union[Unset, str]): Last name of the card owner Example: Pham.
        state (Union[Unset, str]): State of residence of the card owner Example: VIC.
        updated_at (Union[Unset, datetime.datetime]): Timestamp of the last update to the card owner's record Example:
            2023-10-19T09:05:52.771Z.
        version (Union[Unset, int]): Version number of the card owner's record Example: 1.
    """

    id: Union[Unset, str] = UNSET
    business_id: Union[Unset, str] = UNSET
    phone: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    account_name: Union[Unset, str] = UNSET
    user_type: Union[Unset, str] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    first_name: Union[Unset, str] = UNSET
    form_id: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    state: Union[Unset, str] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    version: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        business_id = self.business_id

        phone = self.phone

        email = self.email

        account_name = self.account_name

        user_type = self.user_type

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        first_name = self.first_name

        form_id = self.form_id

        last_name = self.last_name

        state = self.state

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if business_id is not UNSET:
            field_dict["businessId"] = business_id
        if phone is not UNSET:
            field_dict["phone"] = phone
        if email is not UNSET:
            field_dict["email"] = email
        if account_name is not UNSET:
            field_dict["accountName"] = account_name
        if user_type is not UNSET:
            field_dict["userType"] = user_type
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if form_id is not UNSET:
            field_dict["formId"] = form_id
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if state is not UNSET:
            field_dict["state"] = state
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        business_id = d.pop("businessId", UNSET)

        phone = d.pop("phone", UNSET)

        email = d.pop("email", UNSET)

        account_name = d.pop("accountName", UNSET)

        user_type = d.pop("userType", UNSET)

        _created_at = d.pop("createdAt", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        first_name = d.pop("firstName", UNSET)

        form_id = d.pop("formId", UNSET)

        last_name = d.pop("lastName", UNSET)

        state = d.pop("state", UNSET)

        _updated_at = d.pop("updatedAt", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        version = d.pop("version", UNSET)

        card_owner = cls(
            id=id,
            business_id=business_id,
            phone=phone,
            email=email,
            account_name=account_name,
            user_type=user_type,
            created_at=created_at,
            first_name=first_name,
            form_id=form_id,
            last_name=last_name,
            state=state,
            updated_at=updated_at,
            version=version,
        )

        card_owner.additional_properties = d
        return card_owner

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
