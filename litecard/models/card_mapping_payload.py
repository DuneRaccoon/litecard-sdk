from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.base_card_payload import BaseCardPayload


T = TypeVar("T", bound="CardMappingPayload")


@_attrs_define
class CardMappingPayload:
    """
    Attributes:
        form_id (Union[Unset, str]): Id to define the schema for field inputs used to create/update the card. Example:
            kSwoChd.
        template_id (Union[Unset, str]): Id for the apple/google pass template used to create the card. Example:
            test_business.
        card_payload (Union[Unset, BaseCardPayload]): Datafields used by the card
    """

    form_id: Union[Unset, str] = UNSET
    template_id: Union[Unset, str] = UNSET
    card_payload: Union[Unset, "BaseCardPayload"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        form_id = self.form_id

        template_id = self.template_id

        card_payload: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.card_payload, Unset):
            card_payload = self.card_payload.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if form_id is not UNSET:
            field_dict["formId"] = form_id
        if template_id is not UNSET:
            field_dict["templateId"] = template_id
        if card_payload is not UNSET:
            field_dict["cardPayload"] = card_payload

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.base_card_payload import BaseCardPayload

        d = dict(src_dict)
        form_id = d.pop("formId", UNSET)

        template_id = d.pop("templateId", UNSET)

        _card_payload = d.pop("cardPayload", UNSET)
        card_payload: Union[Unset, BaseCardPayload]
        if isinstance(_card_payload, Unset):
            card_payload = UNSET
        else:
            card_payload = BaseCardPayload.from_dict(_card_payload)

        card_mapping_payload = cls(
            form_id=form_id,
            template_id=template_id,
            card_payload=card_payload,
        )

        card_mapping_payload.additional_properties = d
        return card_mapping_payload

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
