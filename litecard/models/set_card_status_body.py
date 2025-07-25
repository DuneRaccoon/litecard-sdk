from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.set_card_status_body_status import SetCardStatusBodyStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="SetCardStatusBody")


@_attrs_define
class SetCardStatusBody:
    """
    Attributes:
        status (SetCardStatusBodyStatus): Card status Example: ACTIVE.
        card_id (Union[Unset, str]): Unique identifier for the card Example: 7048582966.
    """

    status: SetCardStatusBodyStatus
    card_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        card_id = self.card_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
            }
        )
        if card_id is not UNSET:
            field_dict["cardId"] = card_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = SetCardStatusBodyStatus(d.pop("status"))

        card_id = d.pop("cardId", UNSET)

        set_card_status_body = cls(
            status=status,
            card_id=card_id,
        )

        set_card_status_body.additional_properties = d
        return set_card_status_body

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
