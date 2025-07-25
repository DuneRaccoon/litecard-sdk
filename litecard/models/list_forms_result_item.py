from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.list_forms_result_item_id import ListFormsResultItemId


T = TypeVar("T", bound="ListFormsResultItem")


@_attrs_define
class ListFormsResultItem:
    """Fields that are returned for each formId

    Attributes:
        id (Union[Unset, ListFormsResultItemId]): formId Example: -jJWhjZ1a.
    """

    id: Union[Unset, "ListFormsResultItemId"] = UNSET
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
        from ..models.list_forms_result_item_id import ListFormsResultItemId

        d = dict(src_dict)
        _id = d.pop("id", UNSET)
        id: Union[Unset, ListFormsResultItemId]
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = ListFormsResultItemId.from_dict(_id)

        list_forms_result_item = cls(
            id=id,
        )

        list_forms_result_item.additional_properties = d
        return list_forms_result_item

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
