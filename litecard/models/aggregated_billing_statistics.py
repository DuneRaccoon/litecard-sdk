from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AggregatedBillingStatistics")


@_attrs_define
class AggregatedBillingStatistics:
    """Aggregated Scans Statistics

    Attributes:
        date (str):  Example: 2021-11-09T00:00:00.000Z.
        members (float):  Example: 422.
        signups (float):  Example: 300.
        coupons (float):  Example: 56.
    """

    date: str
    members: float
    signups: float
    coupons: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date = self.date

        members = self.members

        signups = self.signups

        coupons = self.coupons

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "date": date,
                "members": members,
                "signups": signups,
                "coupons": coupons,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        date = d.pop("date")

        members = d.pop("members")

        signups = d.pop("signups")

        coupons = d.pop("coupons")

        aggregated_billing_statistics = cls(
            date=date,
            members=members,
            signups=signups,
            coupons=coupons,
        )

        aggregated_billing_statistics.additional_properties = d
        return aggregated_billing_statistics

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
