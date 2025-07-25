from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AnalyticsNotificationsResultsSchemaResultsQueryParameters")


@_attrs_define
class AnalyticsNotificationsResultsSchemaResultsQueryParameters:
    """
    Attributes:
        start_date_time (Union[Unset, str]):  Example: 2020-12-01.
        end_date_time (Union[Unset, str]):  Example: 2020-12-01.
    """

    start_date_time: Union[Unset, str] = UNSET
    end_date_time: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        start_date_time = self.start_date_time

        end_date_time = self.end_date_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if start_date_time is not UNSET:
            field_dict["startDateTime"] = start_date_time
        if end_date_time is not UNSET:
            field_dict["endDateTime"] = end_date_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        start_date_time = d.pop("startDateTime", UNSET)

        end_date_time = d.pop("endDateTime", UNSET)

        analytics_notifications_results_schema_results_query_parameters = cls(
            start_date_time=start_date_time,
            end_date_time=end_date_time,
        )

        analytics_notifications_results_schema_results_query_parameters.additional_properties = d
        return analytics_notifications_results_schema_results_query_parameters

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
