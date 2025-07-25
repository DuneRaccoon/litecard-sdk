from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.card_upload_v1_status import CardUploadV1Status
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.card_upload_v1_card_payload import CardUploadV1CardPayload


T = TypeVar("T", bound="CardUploadV1")


@_attrs_define
class CardUploadV1:
    """Schema for detailed card upload data

    Attributes:
        id (str):  Example: id.
        business_id (str):  Example: business-id.
        created_at (str):  Example: 2024-05-30T06:45:02.736Z.
        record_index (float):  Example: 2.
        status (CardUploadV1Status):  Example: VALIDATION_FAILED.
        template_id (str):  Example: template-id.
        card_id (Union[Unset, str]):  Example: card12345.
        card_payload (Union[Unset, CardUploadV1CardPayload]): Generic card payload with unspecified fields Example:
            {'email': '123214312', 'firstName': 'Nimesh', 'lastName': 'Jayamanne'}.
        errors (Union[Unset, list[str]]):
    """

    id: str
    business_id: str
    created_at: str
    record_index: float
    status: CardUploadV1Status
    template_id: str
    card_id: Union[Unset, str] = UNSET
    card_payload: Union[Unset, "CardUploadV1CardPayload"] = UNSET
    errors: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        business_id = self.business_id

        created_at = self.created_at

        record_index = self.record_index

        status = self.status.value

        template_id = self.template_id

        card_id = self.card_id

        card_payload: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.card_payload, Unset):
            card_payload = self.card_payload.to_dict()

        errors: Union[Unset, list[str]] = UNSET
        if not isinstance(self.errors, Unset):
            errors = self.errors

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "businessId": business_id,
                "createdAt": created_at,
                "recordIndex": record_index,
                "status": status,
                "templateId": template_id,
            }
        )
        if card_id is not UNSET:
            field_dict["cardId"] = card_id
        if card_payload is not UNSET:
            field_dict["cardPayload"] = card_payload
        if errors is not UNSET:
            field_dict["errors"] = errors

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.card_upload_v1_card_payload import CardUploadV1CardPayload

        d = dict(src_dict)
        id = d.pop("id")

        business_id = d.pop("businessId")

        created_at = d.pop("createdAt")

        record_index = d.pop("recordIndex")

        status = CardUploadV1Status(d.pop("status"))

        template_id = d.pop("templateId")

        card_id = d.pop("cardId", UNSET)

        _card_payload = d.pop("cardPayload", UNSET)
        card_payload: Union[Unset, CardUploadV1CardPayload]
        if isinstance(_card_payload, Unset):
            card_payload = UNSET
        else:
            card_payload = CardUploadV1CardPayload.from_dict(_card_payload)

        errors = cast(list[str], d.pop("errors", UNSET))

        card_upload_v1 = cls(
            id=id,
            business_id=business_id,
            created_at=created_at,
            record_index=record_index,
            status=status,
            template_id=template_id,
            card_id=card_id,
            card_payload=card_payload,
            errors=errors,
        )

        card_upload_v1.additional_properties = d
        return card_upload_v1

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
