from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BusinessMailchimp")


@_attrs_define
class BusinessMailchimp:
    """Mailchimp configuration details for the business

    Attributes:
        access_token (Union[Unset, str]): Access token for Mailchimp API Example: __access_token__.
        from_email (Union[Unset, str]): Email address to send from using Mailchimp Example: news@corplite.com.
        server (Union[Unset, str]): Mailchimp server prefix Example: us14.
    """

    access_token: Union[Unset, str] = UNSET
    from_email: Union[Unset, str] = UNSET
    server: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        access_token = self.access_token

        from_email = self.from_email

        server = self.server

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if access_token is not UNSET:
            field_dict["accessToken"] = access_token
        if from_email is not UNSET:
            field_dict["fromEmail"] = from_email
        if server is not UNSET:
            field_dict["server"] = server

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        access_token = d.pop("accessToken", UNSET)

        from_email = d.pop("fromEmail", UNSET)

        server = d.pop("server", UNSET)

        business_mailchimp = cls(
            access_token=access_token,
            from_email=from_email,
            server=server,
        )

        business_mailchimp.additional_properties = d
        return business_mailchimp

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
