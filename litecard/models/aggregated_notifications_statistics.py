from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AggregatedNotificationsStatistics")


@_attrs_define
class AggregatedNotificationsStatistics:
    """Aggregated Notifications Statistics

    Attributes:
        date (Union[Unset, str]):  Example: 2021-11-09T00:00:00.000Z.
        error_apn (Union[Unset, float]):
        error_email (Union[Unset, float]):
        error_sms (Union[Unset, float]):
        queued_apn (Union[Unset, float]):
        queued_email (Union[Unset, float]):
        queued_sms (Union[Unset, float]):
        sent_apn (Union[Unset, float]):
        sent_email (Union[Unset, float]):
        sent_sms (Union[Unset, float]):
    """

    date: Union[Unset, str] = UNSET
    error_apn: Union[Unset, float] = UNSET
    error_email: Union[Unset, float] = UNSET
    error_sms: Union[Unset, float] = UNSET
    queued_apn: Union[Unset, float] = UNSET
    queued_email: Union[Unset, float] = UNSET
    queued_sms: Union[Unset, float] = UNSET
    sent_apn: Union[Unset, float] = UNSET
    sent_email: Union[Unset, float] = UNSET
    sent_sms: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date = self.date

        error_apn = self.error_apn

        error_email = self.error_email

        error_sms = self.error_sms

        queued_apn = self.queued_apn

        queued_email = self.queued_email

        queued_sms = self.queued_sms

        sent_apn = self.sent_apn

        sent_email = self.sent_email

        sent_sms = self.sent_sms

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if date is not UNSET:
            field_dict["date"] = date
        if error_apn is not UNSET:
            field_dict["errorAPN"] = error_apn
        if error_email is not UNSET:
            field_dict["errorEmail"] = error_email
        if error_sms is not UNSET:
            field_dict["errorSMS"] = error_sms
        if queued_apn is not UNSET:
            field_dict["queuedAPN"] = queued_apn
        if queued_email is not UNSET:
            field_dict["queuedEmail"] = queued_email
        if queued_sms is not UNSET:
            field_dict["queuedSMS"] = queued_sms
        if sent_apn is not UNSET:
            field_dict["sentAPN"] = sent_apn
        if sent_email is not UNSET:
            field_dict["sentEmail"] = sent_email
        if sent_sms is not UNSET:
            field_dict["sentSMS"] = sent_sms

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        date = d.pop("date", UNSET)

        error_apn = d.pop("errorAPN", UNSET)

        error_email = d.pop("errorEmail", UNSET)

        error_sms = d.pop("errorSMS", UNSET)

        queued_apn = d.pop("queuedAPN", UNSET)

        queued_email = d.pop("queuedEmail", UNSET)

        queued_sms = d.pop("queuedSMS", UNSET)

        sent_apn = d.pop("sentAPN", UNSET)

        sent_email = d.pop("sentEmail", UNSET)

        sent_sms = d.pop("sentSMS", UNSET)

        aggregated_notifications_statistics = cls(
            date=date,
            error_apn=error_apn,
            error_email=error_email,
            error_sms=error_sms,
            queued_apn=queued_apn,
            queued_email=queued_email,
            queued_sms=queued_sms,
            sent_apn=sent_apn,
            sent_email=sent_email,
            sent_sms=sent_sms,
        )

        aggregated_notifications_statistics.additional_properties = d
        return aggregated_notifications_statistics

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
