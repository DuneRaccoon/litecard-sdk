from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateTemplateV1Images")


@_attrs_define
class CreateTemplateV1Images:
    """Images of the template

    Attributes:
        logo (str): URL of uploaded a logo image (square), used by Apple, Google & Samsung, 300px by 300px. Example:
            https://s3bucketlocation/business-name/logo.png.
        icon (str): URL of uploaded icon image, used by Apple Example: https://s3bucketlocation/business-name/icon.png.
        logo_dark_mode (Union[Unset, str]): URL of uploaded a logo image (square), used by Samsung, 300px by 300px. Used
            specifically for dark mode. Example: https://s3bucketlocation/business-name/logo.png.
        logo_light_mode (Union[Unset, str]): URL of uploaded a logo image (square), used by Samsung, 300px by 300px.
            Used specifically for light mode. Example: https://s3bucketlocation/business-name/logo.png.
        hero (Union[Unset, str]): URL of uploaded hero image, used by Google. 1032px x 336px Example:
            https://s3bucketlocation/business-name/hero.png.
        strip (Union[Unset, str]): URL of uploaded strip image, used by Apple. 1125px by 432px. Will overwrite Apple's
            thumbnail image. Example: https://s3bucketlocation/business-name/hero.png.
        apple_logo_override (Union[Unset, str]): URL of uploaded logo image used by Apple. This will replace the shared
            logo image. 150px height with max width of 480px Example: https://s3bucketlocation/business-name/hero.png.
        thumbnail (Union[Unset, str]): URL of uploaded thumbnail image. 270px by 270px. Only available on Apple Event
            Ticket and Generic card types and certain Samsung Card Types. Example: https://s3bucketlocation/business-
            name/thumbnail.png.
        background (Union[Unset, str]): URL of uploaded background image. 270px by 270px. Only available on Apple Event
            Ticket card types Example: https://s3bucketlocation/business-name/background.png.
    """

    logo: str
    icon: str
    logo_dark_mode: Union[Unset, str] = UNSET
    logo_light_mode: Union[Unset, str] = UNSET
    hero: Union[Unset, str] = UNSET
    strip: Union[Unset, str] = UNSET
    apple_logo_override: Union[Unset, str] = UNSET
    thumbnail: Union[Unset, str] = UNSET
    background: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        logo = self.logo

        icon = self.icon

        logo_dark_mode = self.logo_dark_mode

        logo_light_mode = self.logo_light_mode

        hero = self.hero

        strip = self.strip

        apple_logo_override = self.apple_logo_override

        thumbnail = self.thumbnail

        background = self.background

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "logo": logo,
                "icon": icon,
            }
        )
        if logo_dark_mode is not UNSET:
            field_dict["logoDarkMode"] = logo_dark_mode
        if logo_light_mode is not UNSET:
            field_dict["logoLightMode"] = logo_light_mode
        if hero is not UNSET:
            field_dict["hero"] = hero
        if strip is not UNSET:
            field_dict["strip"] = strip
        if apple_logo_override is not UNSET:
            field_dict["appleLogoOverride"] = apple_logo_override
        if thumbnail is not UNSET:
            field_dict["thumbnail"] = thumbnail
        if background is not UNSET:
            field_dict["background"] = background

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        logo = d.pop("logo")

        icon = d.pop("icon")

        logo_dark_mode = d.pop("logoDarkMode", UNSET)

        logo_light_mode = d.pop("logoLightMode", UNSET)

        hero = d.pop("hero", UNSET)

        strip = d.pop("strip", UNSET)

        apple_logo_override = d.pop("appleLogoOverride", UNSET)

        thumbnail = d.pop("thumbnail", UNSET)

        background = d.pop("background", UNSET)

        create_template_v1_images = cls(
            logo=logo,
            icon=icon,
            logo_dark_mode=logo_dark_mode,
            logo_light_mode=logo_light_mode,
            hero=hero,
            strip=strip,
            apple_logo_override=apple_logo_override,
            thumbnail=thumbnail,
            background=background,
        )

        create_template_v1_images.additional_properties = d
        return create_template_v1_images

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
