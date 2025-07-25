from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TemplateActionParams")


@_attrs_define
class TemplateActionParams:
    """
    Attributes:
        type_ (str): Type of action to be executed Example: INCREMENT.
        amount (Union[Unset, int]): Value used in conjuction with the action Example: 10.
        field (Union[Unset, str]): Field name to perform action on Example: points.
        increment_amount (Union[Unset, int]): Used with the INCREMENT_DECREMENT action, amount to be incremented by
            Example: 1.
        increment_field (Union[Unset, str]): Used with the INCREMENT_DECREMENT action, field to be incremented Example:
            freeBurgerCount.
        decrement_amount (Union[Unset, int]): Used with the INCREMENT_DECREMENT action, amount to be decremented by
            Example: 10.
        decrement_field (Union[Unset, str]): Used with the INCREMENT_DECREMENT action, field to be decremented Example:
            points.
    """

    type_: str
    amount: Union[Unset, int] = UNSET
    field: Union[Unset, str] = UNSET
    increment_amount: Union[Unset, int] = UNSET
    increment_field: Union[Unset, str] = UNSET
    decrement_amount: Union[Unset, int] = UNSET
    decrement_field: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        amount = self.amount

        field = self.field

        increment_amount = self.increment_amount

        increment_field = self.increment_field

        decrement_amount = self.decrement_amount

        decrement_field = self.decrement_field

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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type")

        amount = d.pop("amount", UNSET)

        field = d.pop("field", UNSET)

        increment_amount = d.pop("incrementAmount", UNSET)

        increment_field = d.pop("incrementField", UNSET)

        decrement_amount = d.pop("decrementAmount", UNSET)

        decrement_field = d.pop("decrementField", UNSET)

        template_action_params = cls(
            type_=type_,
            amount=amount,
            field=field,
            increment_amount=increment_amount,
            increment_field=increment_field,
            decrement_amount=decrement_amount,
            decrement_field=decrement_field,
        )

        template_action_params.additional_properties = d
        return template_action_params

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
