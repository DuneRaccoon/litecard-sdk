from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.scan_v1_response_schema_card import ScanV1ResponseSchemaCard
    from ..models.scan_v1_response_schema_card_owner import ScanV1ResponseSchemaCardOwner


T = TypeVar("T", bound="ScanV1ResponseSchema")


@_attrs_define
class ScanV1ResponseSchema:
    """
    Attributes:
        card (ScanV1ResponseSchemaCard):
        card_owner (ScanV1ResponseSchemaCardOwner): Fields that are returned for each card owner
    """

    card: "ScanV1ResponseSchemaCard"
    card_owner: "ScanV1ResponseSchemaCardOwner"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        card = self.card.to_dict()

        card_owner = self.card_owner.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "card": card,
                "cardOwner": card_owner,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.scan_v1_response_schema_card import ScanV1ResponseSchemaCard
        from ..models.scan_v1_response_schema_card_owner import ScanV1ResponseSchemaCardOwner

        d = dict(src_dict)
        card = ScanV1ResponseSchemaCard.from_dict(d.pop("card"))

        card_owner = ScanV1ResponseSchemaCardOwner.from_dict(d.pop("cardOwner"))

        scan_v1_response_schema = cls(
            card=card,
            card_owner=card_owner,
        )

        scan_v1_response_schema.additional_properties = d
        return scan_v1_response_schema

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
