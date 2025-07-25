from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.card_upload_group_v1 import CardUploadGroupV1


T = TypeVar("T", bound="ListCardsUploadGroupsV1Response200")


@_attrs_define
class ListCardsUploadGroupsV1Response200:
    """
    Attributes:
        groups (Union[Unset, list['CardUploadGroupV1']]):
        next_ (Union[Unset, str]): Key used to next set of results
    """

    groups: Union[Unset, list["CardUploadGroupV1"]] = UNSET
    next_: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        groups: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.groups, Unset):
            groups = []
            for groups_item_data in self.groups:
                groups_item = groups_item_data.to_dict()
                groups.append(groups_item)

        next_ = self.next_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if groups is not UNSET:
            field_dict["groups"] = groups
        if next_ is not UNSET:
            field_dict["next"] = next_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.card_upload_group_v1 import CardUploadGroupV1

        d = dict(src_dict)
        groups = []
        _groups = d.pop("groups", UNSET)
        for groups_item_data in _groups or []:
            groups_item = CardUploadGroupV1.from_dict(groups_item_data)

            groups.append(groups_item)

        next_ = d.pop("next", UNSET)

        list_cards_upload_groups_v1_response_200 = cls(
            groups=groups,
            next_=next_,
        )

        list_cards_upload_groups_v1_response_200.additional_properties = d
        return list_cards_upload_groups_v1_response_200

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
