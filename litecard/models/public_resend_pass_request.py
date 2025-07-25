from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PublicResendPassRequest")


@_attrs_define
class PublicResendPassRequest:
    """
    Attributes:
        form_id (str): Id for field input form Example: 00000001.
        email (Union[Unset, str]): Email Example: johndoe@example.com.
        phone (Union[Unset, str]): Email Example: johndoe@example.com.
    """

    form_id: str
    email: Union[Unset, str] = UNSET
    phone: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        form_id = self.form_id

        email = self.email

        phone = self.phone

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "formId": form_id,
            }
        )
        if email is not UNSET:
            field_dict["email"] = email
        if phone is not UNSET:
            field_dict["phone"] = phone

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        form_id = d.pop("formId")

        email = d.pop("email", UNSET)

        phone = d.pop("phone", UNSET)

        public_resend_pass_request = cls(
            form_id=form_id,
            email=email,
            phone=phone,
        )

        public_resend_pass_request.additional_properties = d
        return public_resend_pass_request

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
