from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.apple_app_linking_settings import AppleAppLinkingSettings
    from ..models.google_app_linking_settings import GoogleAppLinkingSettings


T = TypeVar("T", bound="TemplateAppLinking")


@_attrs_define
class TemplateAppLinking:
    """Template Settings to Allow AppLinking on the pass.

    Attributes:
        google_settings (Union[Unset, GoogleAppLinkingSettings]): Google settings for AppLinking
        apple_settings (Union[Unset, AppleAppLinkingSettings]): Apple Settings for AppLinking
    """

    google_settings: Union[Unset, "GoogleAppLinkingSettings"] = UNSET
    apple_settings: Union[Unset, "AppleAppLinkingSettings"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        google_settings: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.google_settings, Unset):
            google_settings = self.google_settings.to_dict()

        apple_settings: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.apple_settings, Unset):
            apple_settings = self.apple_settings.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if google_settings is not UNSET:
            field_dict["googleSettings"] = google_settings
        if apple_settings is not UNSET:
            field_dict["appleSettings"] = apple_settings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.apple_app_linking_settings import AppleAppLinkingSettings
        from ..models.google_app_linking_settings import GoogleAppLinkingSettings

        d = dict(src_dict)
        _google_settings = d.pop("googleSettings", UNSET)
        google_settings: Union[Unset, GoogleAppLinkingSettings]
        if isinstance(_google_settings, Unset):
            google_settings = UNSET
        else:
            google_settings = GoogleAppLinkingSettings.from_dict(_google_settings)

        _apple_settings = d.pop("appleSettings", UNSET)
        apple_settings: Union[Unset, AppleAppLinkingSettings]
        if isinstance(_apple_settings, Unset):
            apple_settings = UNSET
        else:
            apple_settings = AppleAppLinkingSettings.from_dict(_apple_settings)

        template_app_linking = cls(
            google_settings=google_settings,
            apple_settings=apple_settings,
        )

        template_app_linking.additional_properties = d
        return template_app_linking

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
