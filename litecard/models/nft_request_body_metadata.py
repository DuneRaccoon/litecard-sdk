from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nft_request_body_metadata_urls_item import NFTRequestBodyMetadataUrlsItem


T = TypeVar("T", bound="NFTRequestBodyMetadata")


@_attrs_define
class NFTRequestBodyMetadata:
    """
    Attributes:
        contract_address (str): Contract Address for the NFT Collection
        token_id (str): Token Id of the NFT
        collection_name (str): Name of the NFT Collection
        image (str): Image URI
        owner_of (str): Wallet address of the owner
        urls (Union[Unset, list['NFTRequestBodyMetadataUrlsItem']]): List of relevant URLs about the NFT
    """

    contract_address: str
    token_id: str
    collection_name: str
    image: str
    owner_of: str
    urls: Union[Unset, list["NFTRequestBodyMetadataUrlsItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        contract_address = self.contract_address

        token_id = self.token_id

        collection_name = self.collection_name

        image = self.image

        owner_of = self.owner_of

        urls: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.urls, Unset):
            urls = []
            for urls_item_data in self.urls:
                urls_item = urls_item_data.to_dict()
                urls.append(urls_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "contractAddress": contract_address,
                "tokenId": token_id,
                "collectionName": collection_name,
                "image": image,
                "ownerOf": owner_of,
            }
        )
        if urls is not UNSET:
            field_dict["urls"] = urls

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.nft_request_body_metadata_urls_item import NFTRequestBodyMetadataUrlsItem

        d = dict(src_dict)
        contract_address = d.pop("contractAddress")

        token_id = d.pop("tokenId")

        collection_name = d.pop("collectionName")

        image = d.pop("image")

        owner_of = d.pop("ownerOf")

        urls = []
        _urls = d.pop("urls", UNSET)
        for urls_item_data in _urls or []:
            urls_item = NFTRequestBodyMetadataUrlsItem.from_dict(urls_item_data)

            urls.append(urls_item)

        nft_request_body_metadata = cls(
            contract_address=contract_address,
            token_id=token_id,
            collection_name=collection_name,
            image=image,
            owner_of=owner_of,
            urls=urls,
        )

        nft_request_body_metadata.additional_properties = d
        return nft_request_body_metadata

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
