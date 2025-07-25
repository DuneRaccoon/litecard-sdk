from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.scan_response_schema_actions import ScanResponseSchemaActions
    from ..models.scan_response_schema_card import ScanResponseSchemaCard
    from ..models.scan_response_schema_card_owner import ScanResponseSchemaCardOwner


T = TypeVar("T", bound="ScanResponseSchema")


@_attrs_define
class ScanResponseSchema:
    """
    Attributes:
        card (ScanResponseSchemaCard):
        card_owner (ScanResponseSchemaCardOwner): Fields that are returned for each card owner
        actions (Union[Unset, ScanResponseSchemaActions]):
    """

    card: "ScanResponseSchemaCard"
    card_owner: "ScanResponseSchemaCardOwner"
    actions: Union[Unset, "ScanResponseSchemaActions"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        card = self.card.to_dict()

        card_owner = self.card_owner.to_dict()

        actions: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.actions, Unset):
            actions = self.actions.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "card": card,
                "cardOwner": card_owner,
            }
        )
        if actions is not UNSET:
            field_dict["actions"] = actions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.scan_response_schema_actions import ScanResponseSchemaActions
        from ..models.scan_response_schema_card import ScanResponseSchemaCard
        from ..models.scan_response_schema_card_owner import ScanResponseSchemaCardOwner

        d = dict(src_dict)
        card = ScanResponseSchemaCard.from_dict(d.pop("card"))

        card_owner = ScanResponseSchemaCardOwner.from_dict(d.pop("cardOwner"))

        _actions = d.pop("actions", UNSET)
        actions: Union[Unset, ScanResponseSchemaActions]
        if isinstance(_actions, Unset):
            actions = UNSET
        else:
            actions = ScanResponseSchemaActions.from_dict(_actions)

        scan_response_schema = cls(
            card=card,
            card_owner=card_owner,
            actions=actions,
        )

        scan_response_schema.additional_properties = d
        return scan_response_schema

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
