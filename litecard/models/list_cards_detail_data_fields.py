from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ListCardsDetailDataFields")


@_attrs_define
class ListCardsDetailDataFields:
    """Data Fields of the pass

    Attributes:
        member_since (Union[Unset, str]): Date time when becoming a member Example: 2021-10-11T07:00:15.075Z.
        full_name (Union[Unset, str]): Full name of the pass Example: Test name.
        num_entries_remaining (Union[Unset, float]): Numbers of entries remaining Example: 10.
        user_type (Union[Unset, str]): User type Example: Patron.
        position (Union[Unset, str]): Position for the user Example: Staff.
    """

    member_since: Union[Unset, str] = UNSET
    full_name: Union[Unset, str] = UNSET
    num_entries_remaining: Union[Unset, float] = UNSET
    user_type: Union[Unset, str] = UNSET
    position: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        member_since = self.member_since

        full_name = self.full_name

        num_entries_remaining = self.num_entries_remaining

        user_type = self.user_type

        position = self.position

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if member_since is not UNSET:
            field_dict["memberSince"] = member_since
        if full_name is not UNSET:
            field_dict["fullName"] = full_name
        if num_entries_remaining is not UNSET:
            field_dict["numEntriesRemaining"] = num_entries_remaining
        if user_type is not UNSET:
            field_dict["userType"] = user_type
        if position is not UNSET:
            field_dict["position"] = position

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        member_since = d.pop("memberSince", UNSET)

        full_name = d.pop("fullName", UNSET)

        num_entries_remaining = d.pop("numEntriesRemaining", UNSET)

        user_type = d.pop("userType", UNSET)

        position = d.pop("position", UNSET)

        list_cards_detail_data_fields = cls(
            member_since=member_since,
            full_name=full_name,
            num_entries_remaining=num_entries_remaining,
            user_type=user_type,
            position=position,
        )

        list_cards_detail_data_fields.additional_properties = d
        return list_cards_detail_data_fields

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
