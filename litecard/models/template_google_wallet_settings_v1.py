from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.template_google_wallet_settings_v1_multiple_devices_and_users_status import (
    TemplateGoogleWalletSettingsV1MultipleDevicesAndUsersStatus,
)
from ..models.template_google_wallet_settings_v1_pass_type import TemplateGoogleWalletSettingsV1PassType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.template_google_wallet_settings_v1_event_ticket import TemplateGoogleWalletSettingsV1EventTicket
    from ..models.template_google_wallet_settings_v1_offer import TemplateGoogleWalletSettingsV1Offer


T = TypeVar("T", bound="TemplateGoogleWalletSettingsV1")


@_attrs_define
class TemplateGoogleWalletSettingsV1:
    """Settings specific to google wallet

    Attributes:
        pass_type (TemplateGoogleWalletSettingsV1PassType): Google wallet card type Example: LOYALTY.
        offer (Union[Unset, TemplateGoogleWalletSettingsV1Offer]): Google offer settings
        event_ticket (Union[Unset, TemplateGoogleWalletSettingsV1EventTicket]): Event Ticket settings for google. Ref:
            https://developers.google.com/wallet/tickets/events/resources/template
        security_shimmer (Union[Unset, bool]): Enable Google Barcode Shimmer for in-person screenshot protection
            Example: True.
        multiple_devices_and_users_status (Union[Unset, TemplateGoogleWalletSettingsV1MultipleDevicesAndUsersStatus]):
            Identifies whether multiple users and devices can save the same pass
        title (Union[Unset, str]): Text that appears beside your logo on the pass Example: Litecard.
        header (Union[Unset, str]): Text that appears within your pass before expanding Example: Your membership Pass.
        sub_header (Union[Unset, str]): The Label for the header section Example: Welcome!.
    """

    pass_type: TemplateGoogleWalletSettingsV1PassType
    offer: Union[Unset, "TemplateGoogleWalletSettingsV1Offer"] = UNSET
    event_ticket: Union[Unset, "TemplateGoogleWalletSettingsV1EventTicket"] = UNSET
    security_shimmer: Union[Unset, bool] = UNSET
    multiple_devices_and_users_status: Union[Unset, TemplateGoogleWalletSettingsV1MultipleDevicesAndUsersStatus] = UNSET
    title: Union[Unset, str] = UNSET
    header: Union[Unset, str] = UNSET
    sub_header: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pass_type = self.pass_type.value

        offer: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.offer, Unset):
            offer = self.offer.to_dict()

        event_ticket: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.event_ticket, Unset):
            event_ticket = self.event_ticket.to_dict()

        security_shimmer = self.security_shimmer

        multiple_devices_and_users_status: Union[Unset, str] = UNSET
        if not isinstance(self.multiple_devices_and_users_status, Unset):
            multiple_devices_and_users_status = self.multiple_devices_and_users_status.value

        title = self.title

        header = self.header

        sub_header = self.sub_header

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "passType": pass_type,
            }
        )
        if offer is not UNSET:
            field_dict["offer"] = offer
        if event_ticket is not UNSET:
            field_dict["eventTicket"] = event_ticket
        if security_shimmer is not UNSET:
            field_dict["securityShimmer"] = security_shimmer
        if multiple_devices_and_users_status is not UNSET:
            field_dict["multipleDevicesAndUsersStatus"] = multiple_devices_and_users_status
        if title is not UNSET:
            field_dict["title"] = title
        if header is not UNSET:
            field_dict["header"] = header
        if sub_header is not UNSET:
            field_dict["subHeader"] = sub_header

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.template_google_wallet_settings_v1_event_ticket import TemplateGoogleWalletSettingsV1EventTicket
        from ..models.template_google_wallet_settings_v1_offer import TemplateGoogleWalletSettingsV1Offer

        d = dict(src_dict)
        pass_type = TemplateGoogleWalletSettingsV1PassType(d.pop("passType"))

        _offer = d.pop("offer", UNSET)
        offer: Union[Unset, TemplateGoogleWalletSettingsV1Offer]
        if isinstance(_offer, Unset):
            offer = UNSET
        else:
            offer = TemplateGoogleWalletSettingsV1Offer.from_dict(_offer)

        _event_ticket = d.pop("eventTicket", UNSET)
        event_ticket: Union[Unset, TemplateGoogleWalletSettingsV1EventTicket]
        if isinstance(_event_ticket, Unset):
            event_ticket = UNSET
        else:
            event_ticket = TemplateGoogleWalletSettingsV1EventTicket.from_dict(_event_ticket)

        security_shimmer = d.pop("securityShimmer", UNSET)

        _multiple_devices_and_users_status = d.pop("multipleDevicesAndUsersStatus", UNSET)
        multiple_devices_and_users_status: Union[Unset, TemplateGoogleWalletSettingsV1MultipleDevicesAndUsersStatus]
        if isinstance(_multiple_devices_and_users_status, Unset):
            multiple_devices_and_users_status = UNSET
        else:
            multiple_devices_and_users_status = TemplateGoogleWalletSettingsV1MultipleDevicesAndUsersStatus(
                _multiple_devices_and_users_status
            )

        title = d.pop("title", UNSET)

        header = d.pop("header", UNSET)

        sub_header = d.pop("subHeader", UNSET)

        template_google_wallet_settings_v1 = cls(
            pass_type=pass_type,
            offer=offer,
            event_ticket=event_ticket,
            security_shimmer=security_shimmer,
            multiple_devices_and_users_status=multiple_devices_and_users_status,
            title=title,
            header=header,
            sub_header=sub_header,
        )

        template_google_wallet_settings_v1.additional_properties = d
        return template_google_wallet_settings_v1

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
