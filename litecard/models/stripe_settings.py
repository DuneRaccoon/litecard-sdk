from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.stripe_settings_type import StripeSettingsType
from ..types import UNSET, Unset

T = TypeVar("T", bound="StripeSettings")


@_attrs_define
class StripeSettings:
    """
    Attributes:
        type_ (Union[Unset, StripeSettingsType]): The Type of Stripe Flow
        price_id (Union[Unset, str]): Stripe ID of the product the price is associated with, setting this value will
            require stripe checkout on card creation Example: price_1MfJi0CHalkCPRwLFiBsMDXW.
        account_id (Union[Unset, str]): If user has a stripe connect account. Provide account Id here.
        payment_fee (Union[Unset, str]): Fee Litecard will take off from the transaction. Example: 123.
        payment_perecent (Union[Unset, str]): Fee Litecard for subscription transactions Example: 123.
    """

    type_: Union[Unset, StripeSettingsType] = UNSET
    price_id: Union[Unset, str] = UNSET
    account_id: Union[Unset, str] = UNSET
    payment_fee: Union[Unset, str] = UNSET
    payment_perecent: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        price_id = self.price_id

        account_id = self.account_id

        payment_fee = self.payment_fee

        payment_perecent = self.payment_perecent

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if price_id is not UNSET:
            field_dict["priceId"] = price_id
        if account_id is not UNSET:
            field_dict["accountId"] = account_id
        if payment_fee is not UNSET:
            field_dict["paymentFee"] = payment_fee
        if payment_perecent is not UNSET:
            field_dict["paymentPerecent"] = payment_perecent

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, StripeSettingsType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = StripeSettingsType(_type_)

        price_id = d.pop("priceId", UNSET)

        account_id = d.pop("accountId", UNSET)

        payment_fee = d.pop("paymentFee", UNSET)

        payment_perecent = d.pop("paymentPerecent", UNSET)

        stripe_settings = cls(
            type_=type_,
            price_id=price_id,
            account_id=account_id,
            payment_fee=payment_fee,
            payment_perecent=payment_perecent,
        )

        stripe_settings.additional_properties = d
        return stripe_settings

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
