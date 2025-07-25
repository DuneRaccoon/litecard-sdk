from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateScanBody")


@_attrs_define
class CreateScanBody:
    """
    Attributes:
        id (str): Id of the scan Example: 2fhajJWhjZ1a.
        created_by (str): Auth0 ID of Creator Example: Ankus Fang.
        business_id (str): Business Name Example: CryoGym.
        device_id (Union[Unset, str]): Id of the USB Scanner used Example: CryoGym.
        device_name (Union[Unset, str]): Name of the USB Scanner Example: AHVW1qv4I_Teqdu4VjwMA.
        location (Union[Unset, str]): Location of the USB Scanner Example: eqdu4VjAHVW1qv4I_TwMA.
        created_at (Union[Unset, str]): Date when pass was first created, in ISO-8601 format Example:
            2021-08-11T03:15:56.860Z.
        updated_at (Union[Unset, str]): Date when pass was last updated, in ISO-8601 format Example:
            2021-08-1T03:15:56.860Z.
    """

    id: str
    created_by: str
    business_id: str
    device_id: Union[Unset, str] = UNSET
    device_name: Union[Unset, str] = UNSET
    location: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        created_by = self.created_by

        business_id = self.business_id

        device_id = self.device_id

        device_name = self.device_name

        location = self.location

        created_at = self.created_at

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "createdBy": created_by,
                "businessId": business_id,
            }
        )
        if device_id is not UNSET:
            field_dict["deviceId"] = device_id
        if device_name is not UNSET:
            field_dict["deviceName"] = device_name
        if location is not UNSET:
            field_dict["location"] = location
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        created_by = d.pop("createdBy")

        business_id = d.pop("businessId")

        device_id = d.pop("deviceId", UNSET)

        device_name = d.pop("deviceName", UNSET)

        location = d.pop("location", UNSET)

        created_at = d.pop("createdAt", UNSET)

        updated_at = d.pop("updatedAt", UNSET)

        create_scan_body = cls(
            id=id,
            created_by=created_by,
            business_id=business_id,
            device_id=device_id,
            device_name=device_name,
            location=location,
            created_at=created_at,
            updated_at=updated_at,
        )

        create_scan_body.additional_properties = d
        return create_scan_body

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
