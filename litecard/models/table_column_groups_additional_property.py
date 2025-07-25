from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.table_column_groups_additional_property_mappings import TableColumnGroupsAdditionalPropertyMappings


T = TypeVar("T", bound="TableColumnGroupsAdditionalProperty")


@_attrs_define
class TableColumnGroupsAdditionalProperty:
    """
    Attributes:
        default_value (Union[Unset, str]): The default value for the group
        label (Union[Unset, str]): The label for the group
        mappings (Union[Unset, TableColumnGroupsAdditionalPropertyMappings]): Key-value pairs mapping strings to strings
    """

    default_value: Union[Unset, str] = UNSET
    label: Union[Unset, str] = UNSET
    mappings: Union[Unset, "TableColumnGroupsAdditionalPropertyMappings"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        default_value = self.default_value

        label = self.label

        mappings: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.mappings, Unset):
            mappings = self.mappings.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if default_value is not UNSET:
            field_dict["defaultValue"] = default_value
        if label is not UNSET:
            field_dict["label"] = label
        if mappings is not UNSET:
            field_dict["mappings"] = mappings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.table_column_groups_additional_property_mappings import (
            TableColumnGroupsAdditionalPropertyMappings,
        )

        d = dict(src_dict)
        default_value = d.pop("defaultValue", UNSET)

        label = d.pop("label", UNSET)

        _mappings = d.pop("mappings", UNSET)
        mappings: Union[Unset, TableColumnGroupsAdditionalPropertyMappings]
        if isinstance(_mappings, Unset):
            mappings = UNSET
        else:
            mappings = TableColumnGroupsAdditionalPropertyMappings.from_dict(_mappings)

        table_column_groups_additional_property = cls(
            default_value=default_value,
            label=label,
            mappings=mappings,
        )

        table_column_groups_additional_property.additional_properties = d
        return table_column_groups_additional_property

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
