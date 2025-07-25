from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nft_request_body_nft_page_urls_item import NFTRequestBodyNftPageUrlsItem


T = TypeVar("T", bound="NFTRequestBodyNftPage")


@_attrs_define
class NFTRequestBodyNftPage:
    """
    Attributes:
        title (str): Title of the NFT Page
        urls (list['NFTRequestBodyNftPageUrlsItem']):
        description (Union[Unset, str]): Short description of NFT Page
    """

    title: str
    urls: list["NFTRequestBodyNftPageUrlsItem"]
    description: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        urls = []
        for urls_item_data in self.urls:
            urls_item = urls_item_data.to_dict()
            urls.append(urls_item)

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "urls": urls,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.nft_request_body_nft_page_urls_item import NFTRequestBodyNftPageUrlsItem

        d = dict(src_dict)
        title = d.pop("title")

        urls = []
        _urls = d.pop("urls")
        for urls_item_data in _urls:
            urls_item = NFTRequestBodyNftPageUrlsItem.from_dict(urls_item_data)

            urls.append(urls_item)

        description = d.pop("description", UNSET)

        nft_request_body_nft_page = cls(
            title=title,
            urls=urls,
            description=description,
        )

        nft_request_body_nft_page.additional_properties = d
        return nft_request_body_nft_page

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
