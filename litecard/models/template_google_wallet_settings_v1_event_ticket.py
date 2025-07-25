from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.template_google_wallet_settings_v1_event_ticket_confirmation_code_label import (
    TemplateGoogleWalletSettingsV1EventTicketConfirmationCodeLabel,
)
from ..models.template_google_wallet_settings_v1_event_ticket_gate_label import (
    TemplateGoogleWalletSettingsV1EventTicketGateLabel,
)
from ..models.template_google_wallet_settings_v1_event_ticket_row_label import (
    TemplateGoogleWalletSettingsV1EventTicketRowLabel,
)
from ..models.template_google_wallet_settings_v1_event_ticket_seat_label import (
    TemplateGoogleWalletSettingsV1EventTicketSeatLabel,
)
from ..models.template_google_wallet_settings_v1_event_ticket_section_label import (
    TemplateGoogleWalletSettingsV1EventTicketSectionLabel,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="TemplateGoogleWalletSettingsV1EventTicket")


@_attrs_define
class TemplateGoogleWalletSettingsV1EventTicket:
    """Event Ticket settings for google. Ref: https://developers.google.com/wallet/tickets/events/resources/template

    Attributes:
        confirmation_code_label (Union[Unset, TemplateGoogleWalletSettingsV1EventTicketConfirmationCodeLabel]): The
            confirmation code of the event reservation. This may also take the form of an order number, confirmation number,
            reservation number, or other equivalent.
        gate_label (Union[Unset, TemplateGoogleWalletSettingsV1EventTicketGateLabel]): Gate Label, it could be gate,
            doors or entrace
        section_label (Union[Unset, TemplateGoogleWalletSettingsV1EventTicketSectionLabel]): Section label, it could be
            section or theater
        row_label (Union[Unset, TemplateGoogleWalletSettingsV1EventTicketRowLabel]): Row label, it could be row or
            unspecified
        seat_label (Union[Unset, TemplateGoogleWalletSettingsV1EventTicketSeatLabel]): Seat label, it could be seat or
            unspecified
    """

    confirmation_code_label: Union[Unset, TemplateGoogleWalletSettingsV1EventTicketConfirmationCodeLabel] = UNSET
    gate_label: Union[Unset, TemplateGoogleWalletSettingsV1EventTicketGateLabel] = UNSET
    section_label: Union[Unset, TemplateGoogleWalletSettingsV1EventTicketSectionLabel] = UNSET
    row_label: Union[Unset, TemplateGoogleWalletSettingsV1EventTicketRowLabel] = UNSET
    seat_label: Union[Unset, TemplateGoogleWalletSettingsV1EventTicketSeatLabel] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        confirmation_code_label: Union[Unset, str] = UNSET
        if not isinstance(self.confirmation_code_label, Unset):
            confirmation_code_label = self.confirmation_code_label.value

        gate_label: Union[Unset, str] = UNSET
        if not isinstance(self.gate_label, Unset):
            gate_label = self.gate_label.value

        section_label: Union[Unset, str] = UNSET
        if not isinstance(self.section_label, Unset):
            section_label = self.section_label.value

        row_label: Union[Unset, str] = UNSET
        if not isinstance(self.row_label, Unset):
            row_label = self.row_label.value

        seat_label: Union[Unset, str] = UNSET
        if not isinstance(self.seat_label, Unset):
            seat_label = self.seat_label.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if confirmation_code_label is not UNSET:
            field_dict["confirmationCodeLabel"] = confirmation_code_label
        if gate_label is not UNSET:
            field_dict["gateLabel"] = gate_label
        if section_label is not UNSET:
            field_dict["sectionLabel"] = section_label
        if row_label is not UNSET:
            field_dict["rowLabel"] = row_label
        if seat_label is not UNSET:
            field_dict["seatLabel"] = seat_label

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _confirmation_code_label = d.pop("confirmationCodeLabel", UNSET)
        confirmation_code_label: Union[Unset, TemplateGoogleWalletSettingsV1EventTicketConfirmationCodeLabel]
        if isinstance(_confirmation_code_label, Unset):
            confirmation_code_label = UNSET
        else:
            confirmation_code_label = TemplateGoogleWalletSettingsV1EventTicketConfirmationCodeLabel(
                _confirmation_code_label
            )

        _gate_label = d.pop("gateLabel", UNSET)
        gate_label: Union[Unset, TemplateGoogleWalletSettingsV1EventTicketGateLabel]
        if isinstance(_gate_label, Unset):
            gate_label = UNSET
        else:
            gate_label = TemplateGoogleWalletSettingsV1EventTicketGateLabel(_gate_label)

        _section_label = d.pop("sectionLabel", UNSET)
        section_label: Union[Unset, TemplateGoogleWalletSettingsV1EventTicketSectionLabel]
        if isinstance(_section_label, Unset):
            section_label = UNSET
        else:
            section_label = TemplateGoogleWalletSettingsV1EventTicketSectionLabel(_section_label)

        _row_label = d.pop("rowLabel", UNSET)
        row_label: Union[Unset, TemplateGoogleWalletSettingsV1EventTicketRowLabel]
        if isinstance(_row_label, Unset):
            row_label = UNSET
        else:
            row_label = TemplateGoogleWalletSettingsV1EventTicketRowLabel(_row_label)

        _seat_label = d.pop("seatLabel", UNSET)
        seat_label: Union[Unset, TemplateGoogleWalletSettingsV1EventTicketSeatLabel]
        if isinstance(_seat_label, Unset):
            seat_label = UNSET
        else:
            seat_label = TemplateGoogleWalletSettingsV1EventTicketSeatLabel(_seat_label)

        template_google_wallet_settings_v1_event_ticket = cls(
            confirmation_code_label=confirmation_code_label,
            gate_label=gate_label,
            section_label=section_label,
            row_label=row_label,
            seat_label=seat_label,
        )

        template_google_wallet_settings_v1_event_ticket.additional_properties = d
        return template_google_wallet_settings_v1_event_ticket

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
