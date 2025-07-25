from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rate_limit_v1_type_1_rule_date_limit_measurement import RateLimitV1Type1RuleDateLimitMeasurement
from ..types import UNSET, Unset

T = TypeVar("T", bound="RateLimitV1Type1RuleDateLimit")


@_attrs_define
class RateLimitV1Type1RuleDateLimit:
    """
    Attributes:
        amount (Union[Unset, str]): The amount of time between scan periods. Example: 10.
        measurement (Union[Unset, RateLimitV1Type1RuleDateLimitMeasurement]): The unit of measurement to calculate
            between scan periods. Example: YEARS.
    """

    amount: Union[Unset, str] = UNSET
    measurement: Union[Unset, RateLimitV1Type1RuleDateLimitMeasurement] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        amount = self.amount

        measurement: Union[Unset, str] = UNSET
        if not isinstance(self.measurement, Unset):
            measurement = self.measurement.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if amount is not UNSET:
            field_dict["amount"] = amount
        if measurement is not UNSET:
            field_dict["measurement"] = measurement

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        amount = d.pop("amount", UNSET)

        _measurement = d.pop("measurement", UNSET)
        measurement: Union[Unset, RateLimitV1Type1RuleDateLimitMeasurement]
        if isinstance(_measurement, Unset):
            measurement = UNSET
        else:
            measurement = RateLimitV1Type1RuleDateLimitMeasurement(_measurement)

        rate_limit_v1_type_1_rule_date_limit = cls(
            amount=amount,
            measurement=measurement,
        )

        rate_limit_v1_type_1_rule_date_limit.additional_properties = d
        return rate_limit_v1_type_1_rule_date_limit

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
