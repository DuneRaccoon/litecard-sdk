from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.table_config_cards_table import TableConfigCardsTable


T = TypeVar("T", bound="TableConfig")


@_attrs_define
class TableConfig:
    """
    Attributes:
        cards_table (Union[Unset, TableConfigCardsTable]):
    """

    cards_table: Union[Unset, "TableConfigCardsTable"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cards_table: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.cards_table, Unset):
            cards_table = self.cards_table.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cards_table is not UNSET:
            field_dict["cardsTable"] = cards_table

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.table_config_cards_table import TableConfigCardsTable

        d = dict(src_dict)
        _cards_table = d.pop("cardsTable", UNSET)
        cards_table: Union[Unset, TableConfigCardsTable]
        if isinstance(_cards_table, Unset):
            cards_table = UNSET
        else:
            cards_table = TableConfigCardsTable.from_dict(_cards_table)

        table_config = cls(
            cards_table=cards_table,
        )

        table_config.additional_properties = d
        return table_config

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
