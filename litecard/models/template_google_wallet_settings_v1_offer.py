from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.template_google_wallet_settings_v1_offer_redemption_channel import (
    TemplateGoogleWalletSettingsV1OfferRedemptionChannel,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="TemplateGoogleWalletSettingsV1Offer")


@_attrs_define
class TemplateGoogleWalletSettingsV1Offer:
    """Google offer settings

    Attributes:
        redemption_channel (Union[Unset, TemplateGoogleWalletSettingsV1OfferRedemptionChannel]): The redemption channel
            application to the coupon (i.e. where the coupon can be redeemmed on)
    """

    redemption_channel: Union[Unset, TemplateGoogleWalletSettingsV1OfferRedemptionChannel] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        redemption_channel: Union[Unset, str] = UNSET
        if not isinstance(self.redemption_channel, Unset):
            redemption_channel = self.redemption_channel.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if redemption_channel is not UNSET:
            field_dict["redemptionChannel"] = redemption_channel

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _redemption_channel = d.pop("redemptionChannel", UNSET)
        redemption_channel: Union[Unset, TemplateGoogleWalletSettingsV1OfferRedemptionChannel]
        if isinstance(_redemption_channel, Unset):
            redemption_channel = UNSET
        else:
            redemption_channel = TemplateGoogleWalletSettingsV1OfferRedemptionChannel(_redemption_channel)

        template_google_wallet_settings_v1_offer = cls(
            redemption_channel=redemption_channel,
        )

        template_google_wallet_settings_v1_offer.additional_properties = d
        return template_google_wallet_settings_v1_offer

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
