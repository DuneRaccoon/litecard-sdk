from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.template_action_params_v1_post_calc import TemplateActionParamsV1PostCalc


T = TypeVar("T", bound="TemplateActionParamsV1")


@_attrs_define
class TemplateActionParamsV1:
    """
    Attributes:
        type_ (str): Type of action to be executed Example: INCREMENT.
        amount (Union[Unset, int]): Value used in conjunction with the action Example: 10.
        field (Union[Unset, str]): Field name to perform action on Example: points.
        increment_amount (Union[Unset, int]): Used with the INCREMENT_DECREMENT action, amount to be incremented by
            Example: 1.
        increment_field (Union[Unset, str]): Used with the INCREMENT_DECREMENT action, field to be incremented Example:
            points.
        decrement_amount (Union[Unset, int]): Used with the INCREMENT_DECREMENT action, amount to be decremented by
            Example: 10.
        decrement_field (Union[Unset, str]): Used with the INCREMENT_DECREMENT action, field to be decremented Example:
            points.
        post_calc (Union[Unset, TemplateActionParamsV1PostCalc]): Settings to be applied to the amount for post
            calculation
    """

    type_: str
    amount: Union[Unset, int] = UNSET
    field: Union[Unset, str] = UNSET
    increment_amount: Union[Unset, int] = UNSET
    increment_field: Union[Unset, str] = UNSET
    decrement_amount: Union[Unset, int] = UNSET
    decrement_field: Union[Unset, str] = UNSET
    post_calc: Union[Unset, "TemplateActionParamsV1PostCalc"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        amount = self.amount

        field = self.field

        increment_amount = self.increment_amount

        increment_field = self.increment_field

        decrement_amount = self.decrement_amount

        decrement_field = self.decrement_field

        post_calc: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.post_calc, Unset):
            post_calc = self.post_calc.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if amount is not UNSET:
            field_dict["amount"] = amount
        if field is not UNSET:
            field_dict["field"] = field
        if increment_amount is not UNSET:
            field_dict["incrementAmount"] = increment_amount
        if increment_field is not UNSET:
            field_dict["incrementField"] = increment_field
        if decrement_amount is not UNSET:
            field_dict["decrementAmount"] = decrement_amount
        if decrement_field is not UNSET:
            field_dict["decrementField"] = decrement_field
        if post_calc is not UNSET:
            field_dict["postCalc"] = post_calc

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.template_action_params_v1_post_calc import TemplateActionParamsV1PostCalc

        d = dict(src_dict)
        type_ = d.pop("type")

        amount = d.pop("amount", UNSET)

        field = d.pop("field", UNSET)

        increment_amount = d.pop("incrementAmount", UNSET)

        increment_field = d.pop("incrementField", UNSET)

        decrement_amount = d.pop("decrementAmount", UNSET)

        decrement_field = d.pop("decrementField", UNSET)

        _post_calc = d.pop("postCalc", UNSET)
        post_calc: Union[Unset, TemplateActionParamsV1PostCalc]
        if isinstance(_post_calc, Unset):
            post_calc = UNSET
        else:
            post_calc = TemplateActionParamsV1PostCalc.from_dict(_post_calc)

        template_action_params_v1 = cls(
            type_=type_,
            amount=amount,
            field=field,
            increment_amount=increment_amount,
            increment_field=increment_field,
            decrement_amount=decrement_amount,
            decrement_field=decrement_field,
            post_calc=post_calc,
        )

        template_action_params_v1.additional_properties = d
        return template_action_params_v1

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
