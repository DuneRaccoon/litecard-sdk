from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.list_passes_result_item import ListPassesResultItem


T = TypeVar("T", bound="ListCardsByTemplateIdResponse200")


@_attrs_define
class ListCardsByTemplateIdResponse200:
    """
    Attributes:
        passes (Union[Unset, list['ListPassesResultItem']]): List Passes Schema
        next_ (Union[Unset, str]): Key used to next set of results
    """

    passes: Union[Unset, list["ListPassesResultItem"]] = UNSET
    next_: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        passes: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.passes, Unset):
            passes = []
            for componentsschemas_list_passes_result_item_data in self.passes:
                componentsschemas_list_passes_result_item = componentsschemas_list_passes_result_item_data.to_dict()
                passes.append(componentsschemas_list_passes_result_item)

        next_ = self.next_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if passes is not UNSET:
            field_dict["passes"] = passes
        if next_ is not UNSET:
            field_dict["next"] = next_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_passes_result_item import ListPassesResultItem

        d = dict(src_dict)
        passes = []
        _passes = d.pop("passes", UNSET)
        for componentsschemas_list_passes_result_item_data in _passes or []:
            componentsschemas_list_passes_result_item = ListPassesResultItem.from_dict(
                componentsschemas_list_passes_result_item_data
            )

            passes.append(componentsschemas_list_passes_result_item)

        next_ = d.pop("next", UNSET)

        list_cards_by_template_id_response_200 = cls(
            passes=passes,
            next_=next_,
        )

        list_cards_by_template_id_response_200.additional_properties = d
        return list_cards_by_template_id_response_200

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
