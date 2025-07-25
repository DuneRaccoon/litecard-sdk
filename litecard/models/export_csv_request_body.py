from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.export_csv_request_body_table_name import ExportCsvRequestBodyTableName
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.export_csv_request_body_dynamic_columns_item import ExportCsvRequestBodyDynamicColumnsItem


T = TypeVar("T", bound="ExportCsvRequestBody")


@_attrs_define
class ExportCsvRequestBody:
    """
    Attributes:
        dynamic_columns (Union[Unset, list['ExportCsvRequestBodyDynamicColumnsItem']]):
        table_name (Union[Unset, ExportCsvRequestBodyTableName]): The name of the table Example: SCAN_TABLE.
        start_date_time (Union[Unset, str]): StartDateTime of the exporting data Example: 2022-02-04T06:22:37.773Z.
        end_date_time (Union[Unset, str]): EndDateTime of the exporting data Example: 2022-02-04T06:22:37.773Z.
    """

    dynamic_columns: Union[Unset, list["ExportCsvRequestBodyDynamicColumnsItem"]] = UNSET
    table_name: Union[Unset, ExportCsvRequestBodyTableName] = UNSET
    start_date_time: Union[Unset, str] = UNSET
    end_date_time: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dynamic_columns: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.dynamic_columns, Unset):
            dynamic_columns = []
            for dynamic_columns_item_data in self.dynamic_columns:
                dynamic_columns_item = dynamic_columns_item_data.to_dict()
                dynamic_columns.append(dynamic_columns_item)

        table_name: Union[Unset, str] = UNSET
        if not isinstance(self.table_name, Unset):
            table_name = self.table_name.value

        start_date_time = self.start_date_time

        end_date_time = self.end_date_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dynamic_columns is not UNSET:
            field_dict["dynamicColumns"] = dynamic_columns
        if table_name is not UNSET:
            field_dict["tableName"] = table_name
        if start_date_time is not UNSET:
            field_dict["startDateTime"] = start_date_time
        if end_date_time is not UNSET:
            field_dict["endDateTime"] = end_date_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.export_csv_request_body_dynamic_columns_item import ExportCsvRequestBodyDynamicColumnsItem

        d = dict(src_dict)
        dynamic_columns = []
        _dynamic_columns = d.pop("dynamicColumns", UNSET)
        for dynamic_columns_item_data in _dynamic_columns or []:
            dynamic_columns_item = ExportCsvRequestBodyDynamicColumnsItem.from_dict(dynamic_columns_item_data)

            dynamic_columns.append(dynamic_columns_item)

        _table_name = d.pop("tableName", UNSET)
        table_name: Union[Unset, ExportCsvRequestBodyTableName]
        if isinstance(_table_name, Unset):
            table_name = UNSET
        else:
            table_name = ExportCsvRequestBodyTableName(_table_name)

        start_date_time = d.pop("startDateTime", UNSET)

        end_date_time = d.pop("endDateTime", UNSET)

        export_csv_request_body = cls(
            dynamic_columns=dynamic_columns,
            table_name=table_name,
            start_date_time=start_date_time,
            end_date_time=end_date_time,
        )

        export_csv_request_body.additional_properties = d
        return export_csv_request_body

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
