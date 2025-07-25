from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.base_card_payload import BaseCardPayload
    from ..models.sign_up_options import SignUpOptions
    from ..models.template_overrides_v1 import TemplateOverridesV1


T = TypeVar("T", bound="PrivateSignUpRequestBody")


@_attrs_define
class PrivateSignUpRequestBody:
    """
    Attributes:
        template_id (str): Id for the apple/google pass template used to create the card. Example: test_business.
        card_payload (BaseCardPayload): Datafields used by the card
        tier (Union[Unset, str]): For multi tiered templates. This is to select which tier to build Example: GOLD.
        options (Union[Unset, SignUpOptions]):
        template_overrides (Union[Unset, TemplateOverridesV1]): Template Overrides
    """

    template_id: str
    card_payload: "BaseCardPayload"
    tier: Union[Unset, str] = UNSET
    options: Union[Unset, "SignUpOptions"] = UNSET
    template_overrides: Union[Unset, "TemplateOverridesV1"] = UNSET

    def to_dict(self) -> dict[str, Any]:
        template_id = self.template_id

        card_payload = self.card_payload.to_dict()

        tier = self.tier

        options: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.options, Unset):
            options = self.options.to_dict()

        template_overrides: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.template_overrides, Unset):
            template_overrides = self.template_overrides.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "templateId": template_id,
                "cardPayload": card_payload,
            }
        )
        if tier is not UNSET:
            field_dict["tier"] = tier
        if options is not UNSET:
            field_dict["options"] = options
        if template_overrides is not UNSET:
            field_dict["templateOverrides"] = template_overrides

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.base_card_payload import BaseCardPayload
        from ..models.sign_up_options import SignUpOptions
        from ..models.template_overrides_v1 import TemplateOverridesV1

        d = dict(src_dict)
        template_id = d.pop("templateId")

        card_payload = BaseCardPayload.from_dict(d.pop("cardPayload"))

        tier = d.pop("tier", UNSET)

        _options = d.pop("options", UNSET)
        options: Union[Unset, SignUpOptions]
        if isinstance(_options, Unset):
            options = UNSET
        else:
            options = SignUpOptions.from_dict(_options)

        _template_overrides = d.pop("templateOverrides", UNSET)
        template_overrides: Union[Unset, TemplateOverridesV1]
        if isinstance(_template_overrides, Unset):
            template_overrides = UNSET
        else:
            template_overrides = TemplateOverridesV1.from_dict(_template_overrides)

        private_sign_up_request_body = cls(
            template_id=template_id,
            card_payload=card_payload,
            tier=tier,
            options=options,
            template_overrides=template_overrides,
        )

        return private_sign_up_request_body
