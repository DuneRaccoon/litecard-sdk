from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.template_action_params_v1_post_calc_modifier import TemplateActionParamsV1PostCalcModifier

T = TypeVar("T", bound="TemplateActionParamsV1PostCalc")


@_attrs_define
class TemplateActionParamsV1PostCalc:
    """Settings to be applied to the amount for post calculation

    Attributes:
        modifier (TemplateActionParamsV1PostCalcModifier): Type of calculation to be applied to the amount Example:
            PERCENTAGE.
        amount (float): Amount to be applied. Should be the whole number (e.g. 10 for 10 percent) Example: 10.
    """

    modifier: TemplateActionParamsV1PostCalcModifier
    amount: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        modifier = self.modifier.value

        amount = self.amount

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "modifier": modifier,
                "amount": amount,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        modifier = TemplateActionParamsV1PostCalcModifier(d.pop("modifier"))

        amount = d.pop("amount")

        template_action_params_v1_post_calc = cls(
            modifier=modifier,
            amount=amount,
        )

        template_action_params_v1_post_calc.additional_properties = d
        return template_action_params_v1_post_calc

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
