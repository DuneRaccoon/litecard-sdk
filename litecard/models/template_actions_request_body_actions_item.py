from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TemplateActionsRequestBodyActionsItem")


@_attrs_define
class TemplateActionsRequestBodyActionsItem:
    """
    Attributes:
        name (Union[Unset, str]): Name of the template Action to be invoked Example: addLoyalty.
        amount (Union[Unset, float]): Optional. Value used in scanning logic
    """

    name: Union[Unset, str] = UNSET
    amount: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        amount = self.amount

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if amount is not UNSET:
            field_dict["amount"] = amount

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        amount = d.pop("amount", UNSET)

        template_actions_request_body_actions_item = cls(
            name=name,
            amount=amount,
        )

        template_actions_request_body_actions_item.additional_properties = d
        return template_actions_request_body_actions_item

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
