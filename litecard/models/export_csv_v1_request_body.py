from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.export_csv_v1_request_body_table_name import ExportCsvV1RequestBodyTableName
from ..types import UNSET, Unset

T = TypeVar("T", bound="ExportCsvV1RequestBody")


@_attrs_define
class ExportCsvV1RequestBody:
    """
    Attributes:
        table_name (Union[Unset, ExportCsvV1RequestBodyTableName]): The name of the front end table that is to be
            exported Example: SCAN_TABLE.
        start_date_time (Union[Unset, str]): StartDateTime of the exporting data Example: 2022-02-04T06:22:37.773Z.
        end_date_time (Union[Unset, str]): EndDateTime of the exporting data Example: 2022-02-04T06:22:37.773Z.
        template_id (Union[Unset, str]): Id of the template to be exported Example: template-123.
    """

    table_name: Union[Unset, ExportCsvV1RequestBodyTableName] = UNSET
    start_date_time: Union[Unset, str] = UNSET
    end_date_time: Union[Unset, str] = UNSET
    template_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        table_name: Union[Unset, str] = UNSET
        if not isinstance(self.table_name, Unset):
            table_name = self.table_name.value

        start_date_time = self.start_date_time

        end_date_time = self.end_date_time

        template_id = self.template_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if table_name is not UNSET:
            field_dict["tableName"] = table_name
        if start_date_time is not UNSET:
            field_dict["startDateTime"] = start_date_time
        if end_date_time is not UNSET:
            field_dict["endDateTime"] = end_date_time
        if template_id is not UNSET:
            field_dict["templateId"] = template_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _table_name = d.pop("tableName", UNSET)
        table_name: Union[Unset, ExportCsvV1RequestBodyTableName]
        if isinstance(_table_name, Unset):
            table_name = UNSET
        else:
            table_name = ExportCsvV1RequestBodyTableName(_table_name)

        start_date_time = d.pop("startDateTime", UNSET)

        end_date_time = d.pop("endDateTime", UNSET)

        template_id = d.pop("templateId", UNSET)

        export_csv_v1_request_body = cls(
            table_name=table_name,
            start_date_time=start_date_time,
            end_date_time=end_date_time,
            template_id=template_id,
        )

        export_csv_v1_request_body.additional_properties = d
        return export_csv_v1_request_body

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
