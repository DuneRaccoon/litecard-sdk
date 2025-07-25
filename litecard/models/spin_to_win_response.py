from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.spin_to_win_response_prize import SpinToWinResponsePrize


T = TypeVar("T", bound="SpinToWinResponse")


@_attrs_define
class SpinToWinResponse:
    """
    Attributes:
        prize (Union[Unset, SpinToWinResponsePrize]): Prize for the spin to win result Example: FREE_BURGER.
        prize_options (Union[Unset, list[str]]):
        download_id (Union[Unset, str]): DownloadId used for reward page Example: V1StGXR8_Z5jdHi6B-myT.
    """

    prize: Union[Unset, "SpinToWinResponsePrize"] = UNSET
    prize_options: Union[Unset, list[str]] = UNSET
    download_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        prize: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.prize, Unset):
            prize = self.prize.to_dict()

        prize_options: Union[Unset, list[str]] = UNSET
        if not isinstance(self.prize_options, Unset):
            prize_options = self.prize_options

        download_id = self.download_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if prize is not UNSET:
            field_dict["prize"] = prize
        if prize_options is not UNSET:
            field_dict["prizeOptions"] = prize_options
        if download_id is not UNSET:
            field_dict["downloadId"] = download_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.spin_to_win_response_prize import SpinToWinResponsePrize

        d = dict(src_dict)
        _prize = d.pop("prize", UNSET)
        prize: Union[Unset, SpinToWinResponsePrize]
        if isinstance(_prize, Unset):
            prize = UNSET
        else:
            prize = SpinToWinResponsePrize.from_dict(_prize)

        prize_options = cast(list[str], d.pop("prizeOptions", UNSET))

        download_id = d.pop("downloadId", UNSET)

        spin_to_win_response = cls(
            prize=prize,
            prize_options=prize_options,
            download_id=download_id,
        )

        spin_to_win_response.additional_properties = d
        return spin_to_win_response

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
