from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.pass_counts_history_duration import PassCountsHistoryDuration
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pass_count_details import PassCountDetails


T = TypeVar("T", bound="PassCountsHistory")


@_attrs_define
class PassCountsHistory:
    """Schema for the history of pass counts including the duration and associated businesses.

    Attributes:
        duration (Union[Unset, PassCountsHistoryDuration]): Duration
        businesses (Union[Unset, list['PassCountDetails']]): List of businesses related to the pass counts.
    """

    duration: Union[Unset, PassCountsHistoryDuration] = UNSET
    businesses: Union[Unset, list["PassCountDetails"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        duration: Union[Unset, str] = UNSET
        if not isinstance(self.duration, Unset):
            duration = self.duration.value

        businesses: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.businesses, Unset):
            businesses = []
            for businesses_item_data in self.businesses:
                businesses_item = businesses_item_data.to_dict()
                businesses.append(businesses_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if duration is not UNSET:
            field_dict["duration"] = duration
        if businesses is not UNSET:
            field_dict["businesses"] = businesses

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pass_count_details import PassCountDetails

        d = dict(src_dict)
        _duration = d.pop("duration", UNSET)
        duration: Union[Unset, PassCountsHistoryDuration]
        if isinstance(_duration, Unset):
            duration = UNSET
        else:
            duration = PassCountsHistoryDuration(_duration)

        businesses = []
        _businesses = d.pop("businesses", UNSET)
        for businesses_item_data in _businesses or []:
            businesses_item = PassCountDetails.from_dict(businesses_item_data)

            businesses.append(businesses_item)

        pass_counts_history = cls(
            duration=duration,
            businesses=businesses,
        )

        pass_counts_history.additional_properties = d
        return pass_counts_history

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
