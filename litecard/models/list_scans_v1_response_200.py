from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.scan import Scan


T = TypeVar("T", bound="ListScansV1Response200")


@_attrs_define
class ListScansV1Response200:
    """
    Attributes:
        scans (Union[Unset, list['Scan']]):
        next_ (Union[Unset, str]): Key used to next set of results
    """

    scans: Union[Unset, list["Scan"]] = UNSET
    next_: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        scans: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.scans, Unset):
            scans = []
            for scans_item_data in self.scans:
                scans_item = scans_item_data.to_dict()
                scans.append(scans_item)

        next_ = self.next_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if scans is not UNSET:
            field_dict["scans"] = scans
        if next_ is not UNSET:
            field_dict["next"] = next_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.scan import Scan

        d = dict(src_dict)
        scans = []
        _scans = d.pop("scans", UNSET)
        for scans_item_data in _scans or []:
            scans_item = Scan.from_dict(scans_item_data)

            scans.append(scans_item)

        next_ = d.pop("next", UNSET)

        list_scans_v1_response_200 = cls(
            scans=scans,
            next_=next_,
        )

        list_scans_v1_response_200.additional_properties = d
        return list_scans_v1_response_200

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
