from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="StripeCheckoutBody")


@_attrs_define
class StripeCheckoutBody:
    """
    Attributes:
        price_id (Union[Unset, str]): priceId for stripe Example: price_abc123....
        origin (Union[Unset, str]): Page for stripe to redirect to on success or cancel Example: http://localhost:5000.
        quantity (Union[Unset, float]): Set to '1' for one subscription and set to 'undefined' for metered subscription
            Example: 1.
    """

    price_id: Union[Unset, str] = UNSET
    origin: Union[Unset, str] = UNSET
    quantity: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        price_id = self.price_id

        origin = self.origin

        quantity = self.quantity

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if price_id is not UNSET:
            field_dict["priceId"] = price_id
        if origin is not UNSET:
            field_dict["origin"] = origin
        if quantity is not UNSET:
            field_dict["quantity"] = quantity

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        price_id = d.pop("priceId", UNSET)

        origin = d.pop("origin", UNSET)

        quantity = d.pop("quantity", UNSET)

        stripe_checkout_body = cls(
            price_id=price_id,
            origin=origin,
            quantity=quantity,
        )

        stripe_checkout_body.additional_properties = d
        return stripe_checkout_body

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
