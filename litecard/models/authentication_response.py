from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AuthenticationResponse")


@_attrs_define
class AuthenticationResponse:
    """
    Attributes:
        access_token (Union[Unset, str]): JWT Token used for API authentication
        type_ (Union[Unset, str]): Type of Token Example: Bearer.
        expires_in (Union[Unset, float]): Time in seconds before token expires Example: 3600.
    """

    access_token: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    expires_in: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        access_token = self.access_token

        type_ = self.type_

        expires_in = self.expires_in

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if access_token is not UNSET:
            field_dict["access_token"] = access_token
        if type_ is not UNSET:
            field_dict["type"] = type_
        if expires_in is not UNSET:
            field_dict["expires_in"] = expires_in

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        access_token = d.pop("access_token", UNSET)

        type_ = d.pop("type", UNSET)

        expires_in = d.pop("expires_in", UNSET)

        authentication_response = cls(
            access_token=access_token,
            type_=type_,
            expires_in=expires_in,
        )

        authentication_response.additional_properties = d
        return authentication_response

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
