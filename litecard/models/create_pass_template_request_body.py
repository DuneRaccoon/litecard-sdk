from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.base_card_payload import BaseCardPayload
    from ..models.create_template_v1 import CreateTemplateV1
    from ..models.sign_up_options import SignUpOptions


T = TypeVar("T", bound="CreatePassTemplateRequestBody")


@_attrs_define
class CreatePassTemplateRequestBody:
    """
    Attributes:
        template_payload (CreateTemplateV1): Template used to create apple/google wallet cards
        card_payload (BaseCardPayload): Datafields used by the card
        options (Union[Unset, SignUpOptions]):
    """

    template_payload: "CreateTemplateV1"
    card_payload: "BaseCardPayload"
    options: Union[Unset, "SignUpOptions"] = UNSET

    def to_dict(self) -> dict[str, Any]:
        template_payload = self.template_payload.to_dict()

        card_payload = self.card_payload.to_dict()

        options: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.options, Unset):
            options = self.options.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "templatePayload": template_payload,
                "cardPayload": card_payload,
            }
        )
        if options is not UNSET:
            field_dict["options"] = options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.base_card_payload import BaseCardPayload
        from ..models.create_template_v1 import CreateTemplateV1
        from ..models.sign_up_options import SignUpOptions

        d = dict(src_dict)
        template_payload = CreateTemplateV1.from_dict(d.pop("templatePayload"))

        card_payload = BaseCardPayload.from_dict(d.pop("cardPayload"))

        _options = d.pop("options", UNSET)
        options: Union[Unset, SignUpOptions]
        if isinstance(_options, Unset):
            options = UNSET
        else:
            options = SignUpOptions.from_dict(_options)

        create_pass_template_request_body = cls(
            template_payload=template_payload,
            card_payload=card_payload,
            options=options,
        )

        return create_pass_template_request_body
