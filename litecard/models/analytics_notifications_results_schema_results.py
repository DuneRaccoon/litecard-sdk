from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.aggregated_notifications_statistics import AggregatedNotificationsStatistics
    from ..models.analytics_notifications_results_schema_results_query_parameters import (
        AnalyticsNotificationsResultsSchemaResultsQueryParameters,
    )


T = TypeVar("T", bound="AnalyticsNotificationsResultsSchemaResults")


@_attrs_define
class AnalyticsNotificationsResultsSchemaResults:
    """
    Attributes:
        business_id (Union[Unset, str]):  Example: litecard.
        query_parameters (Union[Unset, AnalyticsNotificationsResultsSchemaResultsQueryParameters]):
        num_results (Union[Unset, float]):  Example: 8.
        analytics (Union[Unset, list['AggregatedNotificationsStatistics']]):
    """

    business_id: Union[Unset, str] = UNSET
    query_parameters: Union[Unset, "AnalyticsNotificationsResultsSchemaResultsQueryParameters"] = UNSET
    num_results: Union[Unset, float] = UNSET
    analytics: Union[Unset, list["AggregatedNotificationsStatistics"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        business_id = self.business_id

        query_parameters: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.query_parameters, Unset):
            query_parameters = self.query_parameters.to_dict()

        num_results = self.num_results

        analytics: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.analytics, Unset):
            analytics = []
            for analytics_item_data in self.analytics:
                analytics_item = analytics_item_data.to_dict()
                analytics.append(analytics_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if business_id is not UNSET:
            field_dict["businessId"] = business_id
        if query_parameters is not UNSET:
            field_dict["queryParameters"] = query_parameters
        if num_results is not UNSET:
            field_dict["numResults"] = num_results
        if analytics is not UNSET:
            field_dict["analytics"] = analytics

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.aggregated_notifications_statistics import AggregatedNotificationsStatistics
        from ..models.analytics_notifications_results_schema_results_query_parameters import (
            AnalyticsNotificationsResultsSchemaResultsQueryParameters,
        )

        d = dict(src_dict)
        business_id = d.pop("businessId", UNSET)

        _query_parameters = d.pop("queryParameters", UNSET)
        query_parameters: Union[Unset, AnalyticsNotificationsResultsSchemaResultsQueryParameters]
        if isinstance(_query_parameters, Unset):
            query_parameters = UNSET
        else:
            query_parameters = AnalyticsNotificationsResultsSchemaResultsQueryParameters.from_dict(_query_parameters)

        num_results = d.pop("numResults", UNSET)

        analytics = []
        _analytics = d.pop("analytics", UNSET)
        for analytics_item_data in _analytics or []:
            analytics_item = AggregatedNotificationsStatistics.from_dict(analytics_item_data)

            analytics.append(analytics_item)

        analytics_notifications_results_schema_results = cls(
            business_id=business_id,
            query_parameters=query_parameters,
            num_results=num_results,
            analytics=analytics,
        )

        analytics_notifications_results_schema_results.additional_properties = d
        return analytics_notifications_results_schema_results

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
