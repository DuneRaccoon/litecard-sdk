from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="NFTRequestBodyNftPageUrlsItem")


@_attrs_define
class NFTRequestBodyNftPageUrlsItem:
    """
    Attributes:
        title (str): Title of the Link
        link (str): URL link
        description (str): Description of the page link
    """

    title: str
    link: str
    description: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        link = self.link

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "link": link,
                "description": description,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        title = d.pop("title")

        link = d.pop("link")

        description = d.pop("description")

        nft_request_body_nft_page_urls_item = cls(
            title=title,
            link=link,
            description=description,
        )

        nft_request_body_nft_page_urls_item.additional_properties = d
        return nft_request_body_nft_page_urls_item

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
