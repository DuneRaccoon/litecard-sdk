from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.aggregated_billing_statistics import AggregatedBillingStatistics
    from ..models.analytics_billing_results_schema_results_query_parameters import (
        AnalyticsBillingResultsSchemaResultsQueryParameters,
    )


T = TypeVar("T", bound="AnalyticsBillingResultsSchemaResults")


@_attrs_define
class AnalyticsBillingResultsSchemaResults:
    """
    Attributes:
        business_id (str):  Example: litecard.
        query_parameters (AnalyticsBillingResultsSchemaResultsQueryParameters):
        num_results (float):  Example: 8.
        analytics (list['AggregatedBillingStatistics']):
    """

    business_id: str
    query_parameters: "AnalyticsBillingResultsSchemaResultsQueryParameters"
    num_results: float
    analytics: list["AggregatedBillingStatistics"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        business_id = self.business_id

        query_parameters = self.query_parameters.to_dict()

        num_results = self.num_results

        analytics = []
        for analytics_item_data in self.analytics:
            analytics_item = analytics_item_data.to_dict()
            analytics.append(analytics_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "businessId": business_id,
                "queryParameters": query_parameters,
                "numResults": num_results,
                "analytics": analytics,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.aggregated_billing_statistics import AggregatedBillingStatistics
        from ..models.analytics_billing_results_schema_results_query_parameters import (
            AnalyticsBillingResultsSchemaResultsQueryParameters,
        )

        d = dict(src_dict)
        business_id = d.pop("businessId")

        query_parameters = AnalyticsBillingResultsSchemaResultsQueryParameters.from_dict(d.pop("queryParameters"))

        num_results = d.pop("numResults")

        analytics = []
        _analytics = d.pop("analytics")
        for analytics_item_data in _analytics:
            analytics_item = AggregatedBillingStatistics.from_dict(analytics_item_data)

            analytics.append(analytics_item)

        analytics_billing_results_schema_results = cls(
            business_id=business_id,
            query_parameters=query_parameters,
            num_results=num_results,
            analytics=analytics,
        )

        analytics_billing_results_schema_results.additional_properties = d
        return analytics_billing_results_schema_results

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
