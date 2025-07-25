from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TemplateImages")


@_attrs_define
class TemplateImages:
    """Images of the template

    Attributes:
        logo (Union[Unset, str]): URL of uploaded logo image Example: https://s3bucketlocation/business-name/logo.png.
        hero (Union[Unset, str]): URL of uploaded hero image Example: https://s3bucketlocation/business-name/hero.png.
        full_hero (Union[Unset, str]): URL of uploaded hero image Example: https://s3bucketlocation/business-
            name/hero.png.
        icon (Union[Unset, str]): URL of uploaded icon image Example: https://s3bucketlocation/business-name/icon.png.
        thumbnail (Union[Unset, str]): URL of uploaded thumbnail image Example: https://s3bucketlocation/business-
            name/thumbnail.png.
    """

    logo: Union[Unset, str] = UNSET
    hero: Union[Unset, str] = UNSET
    full_hero: Union[Unset, str] = UNSET
    icon: Union[Unset, str] = UNSET
    thumbnail: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        logo = self.logo

        hero = self.hero

        full_hero = self.full_hero

        icon = self.icon

        thumbnail = self.thumbnail

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if logo is not UNSET:
            field_dict["logo"] = logo
        if hero is not UNSET:
            field_dict["hero"] = hero
        if full_hero is not UNSET:
            field_dict["fullHero"] = full_hero
        if icon is not UNSET:
            field_dict["icon"] = icon
        if thumbnail is not UNSET:
            field_dict["thumbnail"] = thumbnail

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        logo = d.pop("logo", UNSET)

        hero = d.pop("hero", UNSET)

        full_hero = d.pop("fullHero", UNSET)

        icon = d.pop("icon", UNSET)

        thumbnail = d.pop("thumbnail", UNSET)

        template_images = cls(
            logo=logo,
            hero=hero,
            full_hero=full_hero,
            icon=icon,
            thumbnail=thumbnail,
        )

        template_images.additional_properties = d
        return template_images

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
