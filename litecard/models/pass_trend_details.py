from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PassTrendDetails")


@_attrs_define
class PassTrendDetails:
    """Statistics for a single business related to pass counts.

    Attributes:
        date (str): The date for the pass trend.(YYYY-MM-DD)
        downloaded_apple_pass_count (int): The count of Apple passes downloaded for this business.
        downloaded_google_pass_count (int): The count of Google passes downloaded for this business.
        deleted_apple_pass_count (Union[Unset, int]): The count of Apple passes downloaded for this business.
        deleted_google_pass_count (Union[Unset, int]): The count of Google passes downloaded for this business.
        cards_count (Union[Unset, int]): The count of cards created during this duration.
        downloads_count (Union[Unset, int]): The count of card downloads for this duration.
        active_cards_count (Union[Unset, int]): The count of active cards created during this duration.
        deleted_cards_count (Union[Unset, int]): The count of deleted cards created during this duration.
        inactive_cards_count (Union[Unset, int]): The count of inactive cards created during this duration.
        inactive_apple_pass_count (Union[Unset, int]): The count of inactive Apple passes for this business.
        inactive_google_pass_count (Union[Unset, int]): The count of inactive Google passes for this business.
        payments_required_count (Union[Unset, int]): The count of passes payments is not yet completed for this
            business.
    """

    date: str
    downloaded_apple_pass_count: int
    downloaded_google_pass_count: int
    deleted_apple_pass_count: Union[Unset, int] = UNSET
    deleted_google_pass_count: Union[Unset, int] = UNSET
    cards_count: Union[Unset, int] = UNSET
    downloads_count: Union[Unset, int] = UNSET
    active_cards_count: Union[Unset, int] = UNSET
    deleted_cards_count: Union[Unset, int] = UNSET
    inactive_cards_count: Union[Unset, int] = UNSET
    inactive_apple_pass_count: Union[Unset, int] = UNSET
    inactive_google_pass_count: Union[Unset, int] = UNSET
    payments_required_count: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date = self.date

        downloaded_apple_pass_count = self.downloaded_apple_pass_count

        downloaded_google_pass_count = self.downloaded_google_pass_count

        deleted_apple_pass_count = self.deleted_apple_pass_count

        deleted_google_pass_count = self.deleted_google_pass_count

        cards_count = self.cards_count

        downloads_count = self.downloads_count

        active_cards_count = self.active_cards_count

        deleted_cards_count = self.deleted_cards_count

        inactive_cards_count = self.inactive_cards_count

        inactive_apple_pass_count = self.inactive_apple_pass_count

        inactive_google_pass_count = self.inactive_google_pass_count

        payments_required_count = self.payments_required_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "date": date,
                "downloadedApplePassCount": downloaded_apple_pass_count,
                "downloadedGooglePassCount": downloaded_google_pass_count,
            }
        )
        if deleted_apple_pass_count is not UNSET:
            field_dict["deletedApplePassCount"] = deleted_apple_pass_count
        if deleted_google_pass_count is not UNSET:
            field_dict["deletedGooglePassCount"] = deleted_google_pass_count
        if cards_count is not UNSET:
            field_dict["cardsCount"] = cards_count
        if downloads_count is not UNSET:
            field_dict["downloadsCount"] = downloads_count
        if active_cards_count is not UNSET:
            field_dict["activeCardsCount"] = active_cards_count
        if deleted_cards_count is not UNSET:
            field_dict["deletedCardsCount"] = deleted_cards_count
        if inactive_cards_count is not UNSET:
            field_dict["inactiveCardsCount"] = inactive_cards_count
        if inactive_apple_pass_count is not UNSET:
            field_dict["inactiveApplePassCount"] = inactive_apple_pass_count
        if inactive_google_pass_count is not UNSET:
            field_dict["inactiveGooglePassCount"] = inactive_google_pass_count
        if payments_required_count is not UNSET:
            field_dict["paymentsRequiredCount"] = payments_required_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        date = d.pop("date")

        downloaded_apple_pass_count = d.pop("downloadedApplePassCount")

        downloaded_google_pass_count = d.pop("downloadedGooglePassCount")

        deleted_apple_pass_count = d.pop("deletedApplePassCount", UNSET)

        deleted_google_pass_count = d.pop("deletedGooglePassCount", UNSET)

        cards_count = d.pop("cardsCount", UNSET)

        downloads_count = d.pop("downloadsCount", UNSET)

        active_cards_count = d.pop("activeCardsCount", UNSET)

        deleted_cards_count = d.pop("deletedCardsCount", UNSET)

        inactive_cards_count = d.pop("inactiveCardsCount", UNSET)

        inactive_apple_pass_count = d.pop("inactiveApplePassCount", UNSET)

        inactive_google_pass_count = d.pop("inactiveGooglePassCount", UNSET)

        payments_required_count = d.pop("paymentsRequiredCount", UNSET)

        pass_trend_details = cls(
            date=date,
            downloaded_apple_pass_count=downloaded_apple_pass_count,
            downloaded_google_pass_count=downloaded_google_pass_count,
            deleted_apple_pass_count=deleted_apple_pass_count,
            deleted_google_pass_count=deleted_google_pass_count,
            cards_count=cards_count,
            downloads_count=downloads_count,
            active_cards_count=active_cards_count,
            deleted_cards_count=deleted_cards_count,
            inactive_cards_count=inactive_cards_count,
            inactive_apple_pass_count=inactive_apple_pass_count,
            inactive_google_pass_count=inactive_google_pass_count,
            payments_required_count=payments_required_count,
        )

        pass_trend_details.additional_properties = d
        return pass_trend_details

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
