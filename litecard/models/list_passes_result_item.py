from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.list_passes_result_item_id import ListPassesResultItemId


T = TypeVar("T", bound="ListPassesResultItem")


@_attrs_define
class ListPassesResultItem:
    """Fields that are returned for each passId

    Attributes:
        id (Union[Unset, ListPassesResultItemId]): passId Example: 00000001.
    """

    id: Union[Unset, "ListPassesResultItemId"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.id, Unset):
            id = self.id.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_passes_result_item_id import ListPassesResultItemId

        d = dict(src_dict)
        _id = d.pop("id", UNSET)
        id: Union[Unset, ListPassesResultItemId]
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = ListPassesResultItemId.from_dict(_id)

        list_passes_result_item = cls(
            id=id,
        )

        list_passes_result_item.additional_properties = d
        return list_passes_result_item

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
