from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.base_card_payload import BaseCardPayload
    from ..models.business_card_options import BusinessCardOptions
    from ..models.sign_up_options import SignUpOptions


T = TypeVar("T", bound="BusinessCardRequestBody")


@_attrs_define
class BusinessCardRequestBody:
    """
    Attributes:
        business_id (Union[Unset, str]): Id for the Business that this entity belongs to Example: LiteCard.
        template_id (Union[Unset, str]): Id for the apple/google pass template used to create the card. Example:
            test_business.
        card_payload (Union[Unset, BaseCardPayload]): Datafields used by the card
        options (Union[Unset, SignUpOptions]):
        business_card (Union[Unset, BusinessCardOptions]):
    """

    business_id: Union[Unset, str] = UNSET
    template_id: Union[Unset, str] = UNSET
    card_payload: Union[Unset, "BaseCardPayload"] = UNSET
    options: Union[Unset, "SignUpOptions"] = UNSET
    business_card: Union[Unset, "BusinessCardOptions"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        business_id = self.business_id

        template_id = self.template_id

        card_payload: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.card_payload, Unset):
            card_payload = self.card_payload.to_dict()

        options: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.options, Unset):
            options = self.options.to_dict()

        business_card: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.business_card, Unset):
            business_card = self.business_card.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if business_id is not UNSET:
            field_dict["businessId"] = business_id
        if template_id is not UNSET:
            field_dict["templateId"] = template_id
        if card_payload is not UNSET:
            field_dict["cardPayload"] = card_payload
        if options is not UNSET:
            field_dict["options"] = options
        if business_card is not UNSET:
            field_dict["businessCard"] = business_card

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.base_card_payload import BaseCardPayload
        from ..models.business_card_options import BusinessCardOptions
        from ..models.sign_up_options import SignUpOptions

        d = dict(src_dict)
        business_id = d.pop("businessId", UNSET)

        template_id = d.pop("templateId", UNSET)

        _card_payload = d.pop("cardPayload", UNSET)
        card_payload: Union[Unset, BaseCardPayload]
        if isinstance(_card_payload, Unset):
            card_payload = UNSET
        else:
            card_payload = BaseCardPayload.from_dict(_card_payload)

        _options = d.pop("options", UNSET)
        options: Union[Unset, SignUpOptions]
        if isinstance(_options, Unset):
            options = UNSET
        else:
            options = SignUpOptions.from_dict(_options)

        _business_card = d.pop("businessCard", UNSET)
        business_card: Union[Unset, BusinessCardOptions]
        if isinstance(_business_card, Unset):
            business_card = UNSET
        else:
            business_card = BusinessCardOptions.from_dict(_business_card)

        business_card_request_body = cls(
            business_id=business_id,
            template_id=template_id,
            card_payload=card_payload,
            options=options,
            business_card=business_card,
        )

        business_card_request_body.additional_properties = d
        return business_card_request_body

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
