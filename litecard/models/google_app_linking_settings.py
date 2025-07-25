from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GoogleAppLinkingSettings")


@_attrs_define
class GoogleAppLinkingSettings:
    """Google settings for AppLinking

    Attributes:
        title (Union[Unset, str]): Title for the App
        app_logo (Union[Unset, str]): URL to the logo of the app
        app_uri (Union[Unset, str]): URL to the app. Recommended to use a dynamic Link
        description (Union[Unset, str]): Description of the app
    """

    title: Union[Unset, str] = UNSET
    app_logo: Union[Unset, str] = UNSET
    app_uri: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        app_logo = self.app_logo

        app_uri = self.app_uri

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if app_logo is not UNSET:
            field_dict["appLogo"] = app_logo
        if app_uri is not UNSET:
            field_dict["appUri"] = app_uri
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        title = d.pop("title", UNSET)

        app_logo = d.pop("appLogo", UNSET)

        app_uri = d.pop("appUri", UNSET)

        description = d.pop("description", UNSET)

        google_app_linking_settings = cls(
            title=title,
            app_logo=app_logo,
            app_uri=app_uri,
            description=description,
        )

        google_app_linking_settings.additional_properties = d
        return google_app_linking_settings

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
