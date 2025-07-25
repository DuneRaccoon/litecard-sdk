from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_card_response_card_data_field_update import UpdateCardResponseCardDataFieldUpdate
    from ..models.update_card_response_card_owner_update import UpdateCardResponseCardOwnerUpdate


T = TypeVar("T", bound="UpdateCardResponse")


@_attrs_define
class UpdateCardResponse:
    """
    Attributes:
        card_owner_update (Union[Unset, UpdateCardResponseCardOwnerUpdate]): Updated fields on the card owner
        card_data_field_update (Union[Unset, UpdateCardResponseCardDataFieldUpdate]): Updated fields on the card
        success (Union[Unset, bool]): Returns whether the request was successful Example: True.
    """

    card_owner_update: Union[Unset, "UpdateCardResponseCardOwnerUpdate"] = UNSET
    card_data_field_update: Union[Unset, "UpdateCardResponseCardDataFieldUpdate"] = UNSET
    success: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        card_owner_update: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.card_owner_update, Unset):
            card_owner_update = self.card_owner_update.to_dict()

        card_data_field_update: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.card_data_field_update, Unset):
            card_data_field_update = self.card_data_field_update.to_dict()

        success = self.success

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if card_owner_update is not UNSET:
            field_dict["cardOwnerUpdate"] = card_owner_update
        if card_data_field_update is not UNSET:
            field_dict["cardDataFieldUpdate"] = card_data_field_update
        if success is not UNSET:
            field_dict["success"] = success

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_card_response_card_data_field_update import UpdateCardResponseCardDataFieldUpdate
        from ..models.update_card_response_card_owner_update import UpdateCardResponseCardOwnerUpdate

        d = dict(src_dict)
        _card_owner_update = d.pop("cardOwnerUpdate", UNSET)
        card_owner_update: Union[Unset, UpdateCardResponseCardOwnerUpdate]
        if isinstance(_card_owner_update, Unset):
            card_owner_update = UNSET
        else:
            card_owner_update = UpdateCardResponseCardOwnerUpdate.from_dict(_card_owner_update)

        _card_data_field_update = d.pop("cardDataFieldUpdate", UNSET)
        card_data_field_update: Union[Unset, UpdateCardResponseCardDataFieldUpdate]
        if isinstance(_card_data_field_update, Unset):
            card_data_field_update = UNSET
        else:
            card_data_field_update = UpdateCardResponseCardDataFieldUpdate.from_dict(_card_data_field_update)

        success = d.pop("success", UNSET)

        update_card_response = cls(
            card_owner_update=card_owner_update,
            card_data_field_update=card_data_field_update,
            success=success,
        )

        update_card_response.additional_properties = d
        return update_card_response

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
