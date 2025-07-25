from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SocialMedia")


@_attrs_define
class SocialMedia:
    """
    Attributes:
        platform (Union[Unset, str]): Social Media Platform Example: Facebook.
        link (Union[Unset, str]): URL of social media profile Example: https://twitter.com/example.
        handle (Union[Unset, str]): Username of the social media platform Example: example1.
    """

    platform: Union[Unset, str] = UNSET
    link: Union[Unset, str] = UNSET
    handle: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        platform = self.platform

        link = self.link

        handle = self.handle

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if platform is not UNSET:
            field_dict["platform"] = platform
        if link is not UNSET:
            field_dict["link"] = link
        if handle is not UNSET:
            field_dict["handle"] = handle

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        platform = d.pop("platform", UNSET)

        link = d.pop("link", UNSET)

        handle = d.pop("handle", UNSET)

        social_media = cls(
            platform=platform,
            link=link,
            handle=handle,
        )

        social_media.additional_properties = d
        return social_media

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
