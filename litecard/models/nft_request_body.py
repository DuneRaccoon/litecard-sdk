from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nft_request_body_metadata import NFTRequestBodyMetadata
    from ..models.nft_request_body_nft_page import NFTRequestBodyNftPage


T = TypeVar("T", bound="NFTRequestBody")


@_attrs_define
class NFTRequestBody:
    """
    Attributes:
        metadata (NFTRequestBodyMetadata):
        signature (str): Hash of the metadata
        nft_page (Union[Unset, NFTRequestBodyNftPage]):
        qr_code_url (Union[None, Unset, str]): Url that is displayed on the card
    """

    metadata: "NFTRequestBodyMetadata"
    signature: str
    nft_page: Union[Unset, "NFTRequestBodyNftPage"] = UNSET
    qr_code_url: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        metadata = self.metadata.to_dict()

        signature = self.signature

        nft_page: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.nft_page, Unset):
            nft_page = self.nft_page.to_dict()

        qr_code_url: Union[None, Unset, str]
        if isinstance(self.qr_code_url, Unset):
            qr_code_url = UNSET
        else:
            qr_code_url = self.qr_code_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "metadata": metadata,
                "signature": signature,
            }
        )
        if nft_page is not UNSET:
            field_dict["nftPage"] = nft_page
        if qr_code_url is not UNSET:
            field_dict["qrCodeUrl"] = qr_code_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.nft_request_body_metadata import NFTRequestBodyMetadata
        from ..models.nft_request_body_nft_page import NFTRequestBodyNftPage

        d = dict(src_dict)
        metadata = NFTRequestBodyMetadata.from_dict(d.pop("metadata"))

        signature = d.pop("signature")

        _nft_page = d.pop("nftPage", UNSET)
        nft_page: Union[Unset, NFTRequestBodyNftPage]
        if isinstance(_nft_page, Unset):
            nft_page = UNSET
        else:
            nft_page = NFTRequestBodyNftPage.from_dict(_nft_page)

        def _parse_qr_code_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        qr_code_url = _parse_qr_code_url(d.pop("qrCodeUrl", UNSET))

        nft_request_body = cls(
            metadata=metadata,
            signature=signature,
            nft_page=nft_page,
            qr_code_url=qr_code_url,
        )

        nft_request_body.additional_properties = d
        return nft_request_body

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
