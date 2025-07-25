from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.public_redeem_request_body_update_payload import PublicRedeemRequestBodyUpdatePayload


T = TypeVar("T", bound="PublicRedeemRequestBody")


@_attrs_define
class PublicRedeemRequestBody:
    """
    Attributes:
        barcode_value (str): barcode value from pass Example: 1234567890.
        business_id (str): ID of the business that owns the pass Example: R9xh12dga8i.
        update_payload (PublicRedeemRequestBodyUpdatePayload): Update payload
    """

    barcode_value: str
    business_id: str
    update_payload: "PublicRedeemRequestBodyUpdatePayload"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        barcode_value = self.barcode_value

        business_id = self.business_id

        update_payload = self.update_payload.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "barcodeValue": barcode_value,
                "businessId": business_id,
                "updatePayload": update_payload,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.public_redeem_request_body_update_payload import PublicRedeemRequestBodyUpdatePayload

        d = dict(src_dict)
        barcode_value = d.pop("barcodeValue")

        business_id = d.pop("businessId")

        update_payload = PublicRedeemRequestBodyUpdatePayload.from_dict(d.pop("updatePayload"))

        public_redeem_request_body = cls(
            barcode_value=barcode_value,
            business_id=business_id,
            update_payload=update_payload,
        )

        public_redeem_request_body.additional_properties = d
        return public_redeem_request_body

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
