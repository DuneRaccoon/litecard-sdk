from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.template_card_expiry_v1_type_2_from_activation_measurement import (
    TemplateCardExpiryV1Type2FromActivationMeasurement,
)
from ..models.template_card_expiry_v1_type_2_from_activation_timezone import (
    TemplateCardExpiryV1Type2FromActivationTimezone,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="TemplateCardExpiryV1Type2FromActivation")


@_attrs_define
class TemplateCardExpiryV1Type2FromActivation:
    """
    Attributes:
        amount (Union[Unset, str]): The amount of time (based on the cardExpiry.fromActivation.measurement field)
            between the activation of the card produced by this template, and the expiry date Example: 10.
        measurement (Union[Unset, TemplateCardExpiryV1Type2FromActivationMeasurement]): The unit of measurement to
            calculate the amount of time between the activation of the card produced by this template, and the expiry date
            Example: YEARS.
        timezone (Union[Unset, TemplateCardExpiryV1Type2FromActivationTimezone]): By default expiry is set as UTC. This
            is to set it as a specific timezone Example: Australia/Melbourne.
    """

    amount: Union[Unset, str] = UNSET
    measurement: Union[Unset, TemplateCardExpiryV1Type2FromActivationMeasurement] = UNSET
    timezone: Union[Unset, TemplateCardExpiryV1Type2FromActivationTimezone] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        amount = self.amount

        measurement: Union[Unset, str] = UNSET
        if not isinstance(self.measurement, Unset):
            measurement = self.measurement.value

        timezone: Union[Unset, str] = UNSET
        if not isinstance(self.timezone, Unset):
            timezone = self.timezone.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if amount is not UNSET:
            field_dict["amount"] = amount
        if measurement is not UNSET:
            field_dict["measurement"] = measurement
        if timezone is not UNSET:
            field_dict["timezone"] = timezone

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        amount = d.pop("amount", UNSET)

        _measurement = d.pop("measurement", UNSET)
        measurement: Union[Unset, TemplateCardExpiryV1Type2FromActivationMeasurement]
        if isinstance(_measurement, Unset):
            measurement = UNSET
        else:
            measurement = TemplateCardExpiryV1Type2FromActivationMeasurement(_measurement)

        _timezone = d.pop("timezone", UNSET)
        timezone: Union[Unset, TemplateCardExpiryV1Type2FromActivationTimezone]
        if isinstance(_timezone, Unset):
            timezone = UNSET
        else:
            timezone = TemplateCardExpiryV1Type2FromActivationTimezone(_timezone)

        template_card_expiry_v1_type_2_from_activation = cls(
            amount=amount,
            measurement=measurement,
            timezone=timezone,
        )

        template_card_expiry_v1_type_2_from_activation.additional_properties = d
        return template_card_expiry_v1_type_2_from_activation

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
