from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ScanCheckInRequestBody")


@_attrs_define
class ScanCheckInRequestBody:
    """
    Attributes:
        card_id (str): Scanned Card Id Example: 123456789.
        device_id (Union[Unset, str]): Device ID of the barcode scanner Example: DFAS87GgjHJG.
        device_name (Union[Unset, str]): Scanner Name Example: CryoGym Frontdoor Scanner.
        location (Union[Unset, str]): Location Name Example: CryoGym.
    """

    card_id: str
    device_id: Union[Unset, str] = UNSET
    device_name: Union[Unset, str] = UNSET
    location: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        card_id = self.card_id

        device_id = self.device_id

        device_name = self.device_name

        location = self.location

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cardId": card_id,
            }
        )
        if device_id is not UNSET:
            field_dict["deviceId"] = device_id
        if device_name is not UNSET:
            field_dict["deviceName"] = device_name
        if location is not UNSET:
            field_dict["location"] = location

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        card_id = d.pop("cardId")

        device_id = d.pop("deviceId", UNSET)

        device_name = d.pop("deviceName", UNSET)

        location = d.pop("location", UNSET)

        scan_check_in_request_body = cls(
            card_id=card_id,
            device_id=device_id,
            device_name=device_name,
            location=location,
        )

        scan_check_in_request_body.additional_properties = d
        return scan_check_in_request_body

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
