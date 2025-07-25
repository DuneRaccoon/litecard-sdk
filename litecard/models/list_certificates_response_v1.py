from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ListCertificatesResponseV1")


@_attrs_define
class ListCertificatesResponseV1:
    """
    Attributes:
        name (str): Name of the certificate
        type_ (str): Type of pass Example: APPLE.
        expiry_date (str): Timestamp of when pass will expire Example: 2023-01-01T00:00:00.000Z.
        apple_pass_type_identifier (Union[Unset, str]): Pass Type Identifier (APPLE only) Example:
            pass.com.example.test.
        apple_team_identifier (Union[Unset, str]): Team identifier (APPLE only) Example: ABCDE12345.
    """

    name: str
    type_: str
    expiry_date: str
    apple_pass_type_identifier: Union[Unset, str] = UNSET
    apple_team_identifier: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        type_ = self.type_

        expiry_date = self.expiry_date

        apple_pass_type_identifier = self.apple_pass_type_identifier

        apple_team_identifier = self.apple_team_identifier

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "type": type_,
                "expiryDate": expiry_date,
            }
        )
        if apple_pass_type_identifier is not UNSET:
            field_dict["applePassTypeIdentifier"] = apple_pass_type_identifier
        if apple_team_identifier is not UNSET:
            field_dict["appleTeamIdentifier"] = apple_team_identifier

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        type_ = d.pop("type")

        expiry_date = d.pop("expiryDate")

        apple_pass_type_identifier = d.pop("applePassTypeIdentifier", UNSET)

        apple_team_identifier = d.pop("appleTeamIdentifier", UNSET)

        list_certificates_response_v1 = cls(
            name=name,
            type_=type_,
            expiry_date=expiry_date,
            apple_pass_type_identifier=apple_pass_type_identifier,
            apple_team_identifier=apple_team_identifier,
        )

        list_certificates_response_v1.additional_properties = d
        return list_certificates_response_v1

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
