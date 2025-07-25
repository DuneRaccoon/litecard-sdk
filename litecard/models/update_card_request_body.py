from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.template_overrides_v1 import TemplateOverridesV1
    from ..models.update_card_request_body_card_payload import UpdateCardRequestBodyCardPayload


T = TypeVar("T", bound="UpdateCardRequestBody")


@_attrs_define
class UpdateCardRequestBody:
    """
    Attributes:
        card_id (str): Unique Card Id Example: -jJWhjZ1a.
        sync_static_fields (Union[Unset, bool]): Flag to sync static fields Example: True.
        tier (Union[Unset, str]): For multi tiered templates. This is to select which tier to build Example: GOLD.
        card_payload (Union[Unset, UpdateCardRequestBodyCardPayload]):
        template_overrides (Union[Unset, TemplateOverridesV1]): Template Overrides
    """

    card_id: str
    sync_static_fields: Union[Unset, bool] = UNSET
    tier: Union[Unset, str] = UNSET
    card_payload: Union[Unset, "UpdateCardRequestBodyCardPayload"] = UNSET
    template_overrides: Union[Unset, "TemplateOverridesV1"] = UNSET

    def to_dict(self) -> dict[str, Any]:
        card_id = self.card_id

        sync_static_fields = self.sync_static_fields

        tier = self.tier

        card_payload: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.card_payload, Unset):
            card_payload = self.card_payload.to_dict()

        template_overrides: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.template_overrides, Unset):
            template_overrides = self.template_overrides.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "cardId": card_id,
            }
        )
        if sync_static_fields is not UNSET:
            field_dict["syncStaticFields"] = sync_static_fields
        if tier is not UNSET:
            field_dict["tier"] = tier
        if card_payload is not UNSET:
            field_dict["cardPayload"] = card_payload
        if template_overrides is not UNSET:
            field_dict["templateOverrides"] = template_overrides

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.template_overrides_v1 import TemplateOverridesV1
        from ..models.update_card_request_body_card_payload import UpdateCardRequestBodyCardPayload

        d = dict(src_dict)
        card_id = d.pop("cardId")

        sync_static_fields = d.pop("syncStaticFields", UNSET)

        tier = d.pop("tier", UNSET)

        _card_payload = d.pop("cardPayload", UNSET)
        card_payload: Union[Unset, UpdateCardRequestBodyCardPayload]
        if isinstance(_card_payload, Unset):
            card_payload = UNSET
        else:
            card_payload = UpdateCardRequestBodyCardPayload.from_dict(_card_payload)

        _template_overrides = d.pop("templateOverrides", UNSET)
        template_overrides: Union[Unset, TemplateOverridesV1]
        if isinstance(_template_overrides, Unset):
            template_overrides = UNSET
        else:
            template_overrides = TemplateOverridesV1.from_dict(_template_overrides)

        update_card_request_body = cls(
            card_id=card_id,
            sync_static_fields=sync_static_fields,
            tier=tier,
            card_payload=card_payload,
            template_overrides=template_overrides,
        )

        return update_card_request_body
