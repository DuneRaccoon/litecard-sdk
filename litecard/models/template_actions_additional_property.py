from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.template_action_condition import TemplateActionCondition
    from ..models.template_action_params import TemplateActionParams


T = TypeVar("T", bound="TemplateActionsAdditionalProperty")


@_attrs_define
class TemplateActionsAdditionalProperty:
    """
    Attributes:
        condition (TemplateActionCondition):
        action (TemplateActionParams):
        label (Union[Unset, str]): Name of the Action Example: Redeem Burger.
    """

    condition: "TemplateActionCondition"
    action: "TemplateActionParams"
    label: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        condition = self.condition.to_dict()

        action = self.action.to_dict()

        label = self.label

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "condition": condition,
                "action": action,
            }
        )
        if label is not UNSET:
            field_dict["label"] = label

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.template_action_condition import TemplateActionCondition
        from ..models.template_action_params import TemplateActionParams

        d = dict(src_dict)
        condition = TemplateActionCondition.from_dict(d.pop("condition"))

        action = TemplateActionParams.from_dict(d.pop("action"))

        label = d.pop("label", UNSET)

        template_actions_additional_property = cls(
            condition=condition,
            action=action,
            label=label,
        )

        template_actions_additional_property.additional_properties = d
        return template_actions_additional_property

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
