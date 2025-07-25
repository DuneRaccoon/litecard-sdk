from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.template_actions_request_body_actions_item import TemplateActionsRequestBodyActionsItem


T = TypeVar("T", bound="TemplateActionsRequestBody")


@_attrs_define
class TemplateActionsRequestBody:
    """
    Attributes:
        card_id (Union[Unset, str]): Id for the Business that this entity belongs to Example: LiteCard.
        actions (Union[Unset, list['TemplateActionsRequestBodyActionsItem']]):
    """

    card_id: Union[Unset, str] = UNSET
    actions: Union[Unset, list["TemplateActionsRequestBodyActionsItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        card_id = self.card_id

        actions: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.actions, Unset):
            actions = []
            for actions_item_data in self.actions:
                actions_item = actions_item_data.to_dict()
                actions.append(actions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if card_id is not UNSET:
            field_dict["cardId"] = card_id
        if actions is not UNSET:
            field_dict["actions"] = actions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.template_actions_request_body_actions_item import TemplateActionsRequestBodyActionsItem

        d = dict(src_dict)
        card_id = d.pop("cardId", UNSET)

        actions = []
        _actions = d.pop("actions", UNSET)
        for actions_item_data in _actions or []:
            actions_item = TemplateActionsRequestBodyActionsItem.from_dict(actions_item_data)

            actions.append(actions_item)

        template_actions_request_body = cls(
            card_id=card_id,
            actions=actions,
        )

        template_actions_request_body.additional_properties = d
        return template_actions_request_body

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
