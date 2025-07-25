from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.table_column_format import TableColumnFormat
from ..models.table_column_usage_item import TableColumnUsageItem
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.column_values import ColumnValues
    from ..models.table_column_groups import TableColumnGroups


T = TypeVar("T", bound="TableColumn")


@_attrs_define
class TableColumn:
    """
    Attributes:
        key (Union[Unset, str]): DynamoDB path to get data
        label (Union[Unset, str]): Column Header
        mapping (Union[Unset, str]): Map special values to the segments
        format_ (Union[Unset, TableColumnFormat]): Format the display
        values (Union[Unset, list['ColumnValues']]): Values for the segment
        usage (Union[Unset, list[TableColumnUsageItem]]): Visibility of the column in csv export and api response
        groups (Union[Unset, TableColumnGroups]): Group specific properties, each key represents a unique group name
    """

    key: Union[Unset, str] = UNSET
    label: Union[Unset, str] = UNSET
    mapping: Union[Unset, str] = UNSET
    format_: Union[Unset, TableColumnFormat] = UNSET
    values: Union[Unset, list["ColumnValues"]] = UNSET
    usage: Union[Unset, list[TableColumnUsageItem]] = UNSET
    groups: Union[Unset, "TableColumnGroups"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        label = self.label

        mapping = self.mapping

        format_: Union[Unset, str] = UNSET
        if not isinstance(self.format_, Unset):
            format_ = self.format_.value

        values: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.values, Unset):
            values = []
            for values_item_data in self.values:
                values_item = values_item_data.to_dict()
                values.append(values_item)

        usage: Union[Unset, list[str]] = UNSET
        if not isinstance(self.usage, Unset):
            usage = []
            for usage_item_data in self.usage:
                usage_item = usage_item_data.value
                usage.append(usage_item)

        groups: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.groups, Unset):
            groups = self.groups.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if key is not UNSET:
            field_dict["key"] = key
        if label is not UNSET:
            field_dict["label"] = label
        if mapping is not UNSET:
            field_dict["mapping"] = mapping
        if format_ is not UNSET:
            field_dict["format"] = format_
        if values is not UNSET:
            field_dict["values"] = values
        if usage is not UNSET:
            field_dict["usage"] = usage
        if groups is not UNSET:
            field_dict["groups"] = groups

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.column_values import ColumnValues
        from ..models.table_column_groups import TableColumnGroups

        d = dict(src_dict)
        key = d.pop("key", UNSET)

        label = d.pop("label", UNSET)

        mapping = d.pop("mapping", UNSET)

        _format_ = d.pop("format", UNSET)
        format_: Union[Unset, TableColumnFormat]
        if isinstance(_format_, Unset):
            format_ = UNSET
        else:
            format_ = TableColumnFormat(_format_)

        values = []
        _values = d.pop("values", UNSET)
        for values_item_data in _values or []:
            values_item = ColumnValues.from_dict(values_item_data)

            values.append(values_item)

        usage = []
        _usage = d.pop("usage", UNSET)
        for usage_item_data in _usage or []:
            usage_item = TableColumnUsageItem(usage_item_data)

            usage.append(usage_item)

        _groups = d.pop("groups", UNSET)
        groups: Union[Unset, TableColumnGroups]
        if isinstance(_groups, Unset):
            groups = UNSET
        else:
            groups = TableColumnGroups.from_dict(_groups)

        table_column = cls(
            key=key,
            label=label,
            mapping=mapping,
            format_=format_,
            values=values,
            usage=usage,
            groups=groups,
        )

        table_column.additional_properties = d
        return table_column

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
