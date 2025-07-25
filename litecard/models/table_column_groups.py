from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.table_column_groups_additional_property import TableColumnGroupsAdditionalProperty


T = TypeVar("T", bound="TableColumnGroups")


@_attrs_define
class TableColumnGroups:
    """Group specific properties, each key represents a unique group name"""

    additional_properties: dict[str, "TableColumnGroupsAdditionalProperty"] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.table_column_groups_additional_property import TableColumnGroupsAdditionalProperty

        d = dict(src_dict)
        table_column_groups = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = TableColumnGroupsAdditionalProperty.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        table_column_groups.additional_properties = additional_properties
        return table_column_groups

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> "TableColumnGroupsAdditionalProperty":
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: "TableColumnGroupsAdditionalProperty") -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
