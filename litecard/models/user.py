from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="User")


@_attrs_define
class User:
    """User object with roles and access details

    Attributes:
        roles (list[str]):  Example: ['admin', 'editor'].
        api_access_allowed (bool):  Example: True.
        ui_dashboard_access (list[str]):  Example: ['overview', 'settings'].
        picture (str):  Example: https://example.com/avatar.jpg.
        username (str):  Example: john_doe.
        email (str):  Example: john@example.com.
        created_at (str):  Example: 2024-01-10T08:00:00.000Z.
        last_login_at (str):  Example: 2024-05-18T12:30:00.000Z.
    """

    roles: list[str]
    api_access_allowed: bool
    ui_dashboard_access: list[str]
    picture: str
    username: str
    email: str
    created_at: str
    last_login_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        roles = self.roles

        api_access_allowed = self.api_access_allowed

        ui_dashboard_access = self.ui_dashboard_access

        picture = self.picture

        username = self.username

        email = self.email

        created_at = self.created_at

        last_login_at = self.last_login_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "roles": roles,
                "apiAccessAllowed": api_access_allowed,
                "uiDashboardAccess": ui_dashboard_access,
                "picture": picture,
                "username": username,
                "email": email,
                "createdAt": created_at,
                "lastLoginAt": last_login_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        roles = cast(list[str], d.pop("roles"))

        api_access_allowed = d.pop("apiAccessAllowed")

        ui_dashboard_access = cast(list[str], d.pop("uiDashboardAccess"))

        picture = d.pop("picture")

        username = d.pop("username")

        email = d.pop("email")

        created_at = d.pop("createdAt")

        last_login_at = d.pop("lastLoginAt")

        user = cls(
            roles=roles,
            api_access_allowed=api_access_allowed,
            ui_dashboard_access=ui_dashboard_access,
            picture=picture,
            username=username,
            email=email,
            created_at=created_at,
            last_login_at=last_login_at,
        )

        user.additional_properties = d
        return user

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
