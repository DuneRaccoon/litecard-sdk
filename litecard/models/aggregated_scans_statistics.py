from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.aggregated_scans_statistics_templates_item import AggregatedScansStatisticsTemplatesItem


T = TypeVar("T", bound="AggregatedScansStatistics")


@_attrs_define
class AggregatedScansStatistics:
    """Aggregated Scans Statistics

    Attributes:
        date (Union[Unset, str]):  Example: 2021-11-09T00:00:00.000Z.
        templates (Union[Unset, list['AggregatedScansStatisticsTemplatesItem']]):
        total (Union[Unset, float]): Total number of scans on a given timestamp
    """

    date: Union[Unset, str] = UNSET
    templates: Union[Unset, list["AggregatedScansStatisticsTemplatesItem"]] = UNSET
    total: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date = self.date

        templates: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.templates, Unset):
            templates = []
            for templates_item_data in self.templates:
                templates_item = templates_item_data.to_dict()
                templates.append(templates_item)

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if date is not UNSET:
            field_dict["date"] = date
        if templates is not UNSET:
            field_dict["templates"] = templates
        if total is not UNSET:
            field_dict["total"] = total

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.aggregated_scans_statistics_templates_item import AggregatedScansStatisticsTemplatesItem

        d = dict(src_dict)
        date = d.pop("date", UNSET)

        templates = []
        _templates = d.pop("templates", UNSET)
        for templates_item_data in _templates or []:
            templates_item = AggregatedScansStatisticsTemplatesItem.from_dict(templates_item_data)

            templates.append(templates_item)

        total = d.pop("total", UNSET)

        aggregated_scans_statistics = cls(
            date=date,
            templates=templates,
            total=total,
        )

        aggregated_scans_statistics.additional_properties = d
        return aggregated_scans_statistics

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
