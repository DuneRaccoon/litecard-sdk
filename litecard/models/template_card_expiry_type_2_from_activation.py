from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.template_card_expiry_type_2_from_activation_measurement import (
    TemplateCardExpiryType2FromActivationMeasurement,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="TemplateCardExpiryType2FromActivation")


@_attrs_define
class TemplateCardExpiryType2FromActivation:
    """
    Attributes:
        amount (Union[Unset, str]): The amount of time (based on the cardExpiry.fromActivation.measurement field)
            between the activation of the card produced by this template, and the expiry date Example: 10.
        measurement (Union[Unset, TemplateCardExpiryType2FromActivationMeasurement]): The unit of measurement to
            calculate the amount of time between the activation of the card produced by this template, and the expiry date
            Example: YEARS.
    """

    amount: Union[Unset, str] = UNSET
    measurement: Union[Unset, TemplateCardExpiryType2FromActivationMeasurement] = UNSET
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
        measurement: Union[Unset, TemplateCardExpiryType2FromActivationMeasurement]
        if isinstance(_measurement, Unset):
            measurement = UNSET
        else:
            measurement = TemplateCardExpiryType2FromActivationMeasurement(_measurement)

        template_card_expiry_type_2_from_activation = cls(
            amount=amount,
            measurement=measurement,
        )

        template_card_expiry_type_2_from_activation.additional_properties = d
        return template_card_expiry_type_2_from_activation

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
