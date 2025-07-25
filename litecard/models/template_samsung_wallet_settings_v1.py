from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.template_samsung_wallet_settings_v1_pass_type import TemplateSamsungWalletSettingsV1PassType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.template_samsung_wallet_settings_v1_customer_service_info import (
        TemplateSamsungWalletSettingsV1CustomerServiceInfo,
    )


T = TypeVar("T", bound="TemplateSamsungWalletSettingsV1")


@_attrs_define
class TemplateSamsungWalletSettingsV1:
    """Settings specific to samsung wallet

    Attributes:
        pass_type (TemplateSamsungWalletSettingsV1PassType): Samsung wallet card type Example: EVENT_TICKET.
        wallet_card_id (str): Unique wallet card Id that is generated when you create the wallet template on the samsung
            portal Example: 3ftjqoit67i00.
        partner_id (str): Samsung Partner ID Example: 4847413840325458240.
        app_link_logo (Union[Unset, str]): Logo of the relevant app Example: https://image.
        app_link_name (Union[Unset, str]): Name of the relevant app Example: Joe's Pizza.
        app_link_data (Union[Unset, str]): Link to the application or website Example: https://joespizza.com.
        customer_service_info (Union[Unset, TemplateSamsungWalletSettingsV1CustomerServiceInfo]): Customer service
            contact details. Known as 'csInfo' on samsung fields
    """

    pass_type: TemplateSamsungWalletSettingsV1PassType
    wallet_card_id: str
    partner_id: str
    app_link_logo: Union[Unset, str] = UNSET
    app_link_name: Union[Unset, str] = UNSET
    app_link_data: Union[Unset, str] = UNSET
    customer_service_info: Union[Unset, "TemplateSamsungWalletSettingsV1CustomerServiceInfo"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pass_type = self.pass_type.value

        wallet_card_id = self.wallet_card_id

        partner_id = self.partner_id

        app_link_logo = self.app_link_logo

        app_link_name = self.app_link_name

        app_link_data = self.app_link_data

        customer_service_info: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.customer_service_info, Unset):
            customer_service_info = self.customer_service_info.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "passType": pass_type,
                "walletCardId": wallet_card_id,
                "partnerId": partner_id,
            }
        )
        if app_link_logo is not UNSET:
            field_dict["appLinkLogo"] = app_link_logo
        if app_link_name is not UNSET:
            field_dict["appLinkName"] = app_link_name
        if app_link_data is not UNSET:
            field_dict["appLinkData"] = app_link_data
        if customer_service_info is not UNSET:
            field_dict["customerServiceInfo"] = customer_service_info

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.template_samsung_wallet_settings_v1_customer_service_info import (
            TemplateSamsungWalletSettingsV1CustomerServiceInfo,
        )

        d = dict(src_dict)
        pass_type = TemplateSamsungWalletSettingsV1PassType(d.pop("passType"))

        wallet_card_id = d.pop("walletCardId")

        partner_id = d.pop("partnerId")

        app_link_logo = d.pop("appLinkLogo", UNSET)

        app_link_name = d.pop("appLinkName", UNSET)

        app_link_data = d.pop("appLinkData", UNSET)

        _customer_service_info = d.pop("customerServiceInfo", UNSET)
        customer_service_info: Union[Unset, TemplateSamsungWalletSettingsV1CustomerServiceInfo]
        if isinstance(_customer_service_info, Unset):
            customer_service_info = UNSET
        else:
            customer_service_info = TemplateSamsungWalletSettingsV1CustomerServiceInfo.from_dict(_customer_service_info)

        template_samsung_wallet_settings_v1 = cls(
            pass_type=pass_type,
            wallet_card_id=wallet_card_id,
            partner_id=partner_id,
            app_link_logo=app_link_logo,
            app_link_name=app_link_name,
            app_link_data=app_link_data,
            customer_service_info=customer_service_info,
        )

        template_samsung_wallet_settings_v1.additional_properties = d
        return template_samsung_wallet_settings_v1

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
