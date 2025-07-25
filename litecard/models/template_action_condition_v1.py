from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TemplateActionConditionV1")


@_attrs_define
class TemplateActionConditionV1:
    """
    Attributes:
        type_ (str): Type of condition to be run Example: CHECK_IN.
        optional (bool): Condition to run action on every invocation to the endpoint Example: True.
        order (Union[Unset, int]): Order of actions to be run on each invocation Example: 1.
        field (Union[Unset, str]): Field name used for conditional checking Example: points.
        value (Union[Unset, int]): Value to be compared against during the conditional check Example: 10.
    """

    type_: str
    optional: bool
    order: Union[Unset, int] = UNSET
    field: Union[Unset, str] = UNSET
    value: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        optional = self.optional

        order = self.order

        field = self.field

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "optional": optional,
            }
        )
        if order is not UNSET:
            field_dict["order"] = order
        if field is not UNSET:
            field_dict["field"] = field
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type")

        optional = d.pop("optional")

        order = d.pop("order", UNSET)

        field = d.pop("field", UNSET)

        value = d.pop("value", UNSET)

        template_action_condition_v1 = cls(
            type_=type_,
            optional=optional,
            order=order,
            field=field,
            value=value,
        )

        template_action_condition_v1.additional_properties = d
        return template_action_condition_v1

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
