from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pass_count_details_for_template import PassCountDetailsForTemplate
    from ..models.pass_trend_details import PassTrendDetails


T = TypeVar("T", bound="TemplatePassDownloadTrendV1Response200")


@_attrs_define
class TemplatePassDownloadTrendV1Response200:
    """Pass download trends for the template

    Attributes:
        trends (Union[Unset, list['PassTrendDetails']]):
        total_summary (Union[Unset, PassCountDetailsForTemplate]): Statistics for a business or template related to pass
            counts.
    """

    trends: Union[Unset, list["PassTrendDetails"]] = UNSET
    total_summary: Union[Unset, "PassCountDetailsForTemplate"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        trends: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.trends, Unset):
            trends = []
            for trends_item_data in self.trends:
                trends_item = trends_item_data.to_dict()
                trends.append(trends_item)

        total_summary: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.total_summary, Unset):
            total_summary = self.total_summary.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if trends is not UNSET:
            field_dict["trends"] = trends
        if total_summary is not UNSET:
            field_dict["totalSummary"] = total_summary

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pass_count_details_for_template import PassCountDetailsForTemplate
        from ..models.pass_trend_details import PassTrendDetails

        d = dict(src_dict)
        trends = []
        _trends = d.pop("trends", UNSET)
        for trends_item_data in _trends or []:
            trends_item = PassTrendDetails.from_dict(trends_item_data)

            trends.append(trends_item)

        _total_summary = d.pop("totalSummary", UNSET)
        total_summary: Union[Unset, PassCountDetailsForTemplate]
        if isinstance(_total_summary, Unset):
            total_summary = UNSET
        else:
            total_summary = PassCountDetailsForTemplate.from_dict(_total_summary)

        template_pass_download_trend_v1_response_200 = cls(
            trends=trends,
            total_summary=total_summary,
        )

        template_pass_download_trend_v1_response_200.additional_properties = d
        return template_pass_download_trend_v1_response_200

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
