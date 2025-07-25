from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SpinToWinResponsePrize")


@_attrs_define
class SpinToWinResponsePrize:
    """Prize for the spin to win result

    Example:
        FREE_BURGER

    Attributes:
        item (Union[Unset, str]): Prize for the spin to win result Example: FREE_BURGER.
        index (Union[Unset, float]): Index of the selected prize item Example: FREE_BURGER.
    """

    item: Union[Unset, str] = UNSET
    index: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        item = self.item

        index = self.index

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if item is not UNSET:
            field_dict["item"] = item
        if index is not UNSET:
            field_dict["index"] = index

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        item = d.pop("item", UNSET)

        index = d.pop("index", UNSET)

        spin_to_win_response_prize = cls(
            item=item,
            index=index,
        )

        spin_to_win_response_prize.additional_properties = d
        return spin_to_win_response_prize

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
