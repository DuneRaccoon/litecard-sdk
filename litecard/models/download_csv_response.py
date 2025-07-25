from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DownloadCsvResponse")


@_attrs_define
class DownloadCsvResponse:
    """
    Attributes:
        signed_url (Union[Unset, str]): url for downloading the csv Example: https://lc-business.
        expiry_time (Union[Unset, str]): Expiry time for the url Example: 2022-02-04T06:22:37.773Z.
        start_date_time (Union[Unset, str]): Start date time of the exporting data Example: 2022-02-04T06:22:37.773Z.
        end_date_time (Union[Unset, str]): End date time of the exporting data Example: 2022-02-04T06:22:37.773Z.
    """

    signed_url: Union[Unset, str] = UNSET
    expiry_time: Union[Unset, str] = UNSET
    start_date_time: Union[Unset, str] = UNSET
    end_date_time: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        signed_url = self.signed_url

        expiry_time = self.expiry_time

        start_date_time = self.start_date_time

        end_date_time = self.end_date_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if signed_url is not UNSET:
            field_dict["signedUrl"] = signed_url
        if expiry_time is not UNSET:
            field_dict["expiryTime"] = expiry_time
        if start_date_time is not UNSET:
            field_dict["startDateTime"] = start_date_time
        if end_date_time is not UNSET:
            field_dict["endDateTime"] = end_date_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        signed_url = d.pop("signedUrl", UNSET)

        expiry_time = d.pop("expiryTime", UNSET)

        start_date_time = d.pop("startDateTime", UNSET)

        end_date_time = d.pop("endDateTime", UNSET)

        download_csv_response = cls(
            signed_url=signed_url,
            expiry_time=expiry_time,
            start_date_time=start_date_time,
            end_date_time=end_date_time,
        )

        download_csv_response.additional_properties = d
        return download_csv_response

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
