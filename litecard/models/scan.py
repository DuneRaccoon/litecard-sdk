import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.scan_scan_type import ScanScanType
from ..models.scan_status import ScanStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.scan_data_fields import ScanDataFields


T = TypeVar("T", bound="Scan")


@_attrs_define
class Scan:
    """
    Attributes:
        id (Union[Unset, str]): The unique identifier for the scan event. Example: yiur9CQTcrLKmELe4_enI.
        account_name (Union[Unset, str]): The name of the account associated with the scan. Example: Danny Bui.
        business_id (Union[Unset, str]): The unique identifier for the business associated with the scan. Example:
            eFGbNdZEQHJX8RdnLMtP_.
        card_id (Union[Unset, str]): The unique identifier for the card that was scanned. Example: 4048866019.
        card_owner_id (Union[Unset, str]): The unique identifier for the owner of the card. Example:
            -3xlaPTtLTGnmbKoaiyKH.
        created_at (Union[Unset, datetime.datetime]): The date and time when the scan event was created. Example:
            2023-07-19T04:36:06.937Z.
        created_by (Union[Unset, str]): The identifier of the user or system that created the scan event. Example:
            auth0|64928a1d73375442becf490d.
        device_id (Union[Unset, str]): The identifier for the device used to perform the scan, if known. Example:
            12345-device-id.
        device_name (Union[Unset, str]): The name of the device used to perform the scan, if known. Example: Front
            Counter POS #1.
        location (Union[Unset, str]): The physical location where the scan took place, if known. Example: Main Store -
            POS #1.
        template_id (Union[Unset, str]): The unique identifier for the template associated with the scan event. Example:
            HtXloDbbAz7Q-IgT7WpLn.
        updated_at (Union[Unset, datetime.datetime]): The date and time when the scan event was last updated. Example:
            2023-07-19T04:36:06.937Z.
        user_type (Union[Unset, str]): User Type Example: patron.
        data_fields (Union[Unset, ScanDataFields]): Structured data associated with the scan.
        form_id (Union[Unset, str]): The unique identifier for the form used to capture the scan data. Example:
            xGScW8kBMGFJfxIoGHg7C.
        scan_type (Union[Unset, ScanScanType]): The type of scan event, which can be either a 'SCAN' or a 'REDEEM'.
            Example: SCAN.
        status (Union[Unset, ScanStatus]): The current status of the scan. Example: ACTIVE.
    """

    id: Union[Unset, str] = UNSET
    account_name: Union[Unset, str] = UNSET
    business_id: Union[Unset, str] = UNSET
    card_id: Union[Unset, str] = UNSET
    card_owner_id: Union[Unset, str] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    created_by: Union[Unset, str] = UNSET
    device_id: Union[Unset, str] = UNSET
    device_name: Union[Unset, str] = UNSET
    location: Union[Unset, str] = UNSET
    template_id: Union[Unset, str] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    user_type: Union[Unset, str] = UNSET
    data_fields: Union[Unset, "ScanDataFields"] = UNSET
    form_id: Union[Unset, str] = UNSET
    scan_type: Union[Unset, ScanScanType] = UNSET
    status: Union[Unset, ScanStatus] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        account_name = self.account_name

        business_id = self.business_id

        card_id = self.card_id

        card_owner_id = self.card_owner_id

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        created_by = self.created_by

        device_id = self.device_id

        device_name = self.device_name

        location = self.location

        template_id = self.template_id

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        user_type = self.user_type

        data_fields: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.data_fields, Unset):
            data_fields = self.data_fields.to_dict()

        form_id = self.form_id

        scan_type: Union[Unset, str] = UNSET
        if not isinstance(self.scan_type, Unset):
            scan_type = self.scan_type.value

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if account_name is not UNSET:
            field_dict["accountName"] = account_name
        if business_id is not UNSET:
            field_dict["businessId"] = business_id
        if card_id is not UNSET:
            field_dict["cardId"] = card_id
        if card_owner_id is not UNSET:
            field_dict["cardOwnerId"] = card_owner_id
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if device_id is not UNSET:
            field_dict["deviceId"] = device_id
        if device_name is not UNSET:
            field_dict["deviceName"] = device_name
        if location is not UNSET:
            field_dict["location"] = location
        if template_id is not UNSET:
            field_dict["templateId"] = template_id
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if user_type is not UNSET:
            field_dict["userType"] = user_type
        if data_fields is not UNSET:
            field_dict["dataFields"] = data_fields
        if form_id is not UNSET:
            field_dict["formId"] = form_id
        if scan_type is not UNSET:
            field_dict["scanType"] = scan_type
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.scan_data_fields import ScanDataFields

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        account_name = d.pop("accountName", UNSET)

        business_id = d.pop("businessId", UNSET)

        card_id = d.pop("cardId", UNSET)

        card_owner_id = d.pop("cardOwnerId", UNSET)

        _created_at = d.pop("createdAt", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        created_by = d.pop("createdBy", UNSET)

        device_id = d.pop("deviceId", UNSET)

        device_name = d.pop("deviceName", UNSET)

        location = d.pop("location", UNSET)

        template_id = d.pop("templateId", UNSET)

        _updated_at = d.pop("updatedAt", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        user_type = d.pop("userType", UNSET)

        _data_fields = d.pop("dataFields", UNSET)
        data_fields: Union[Unset, ScanDataFields]
        if isinstance(_data_fields, Unset):
            data_fields = UNSET
        else:
            data_fields = ScanDataFields.from_dict(_data_fields)

        form_id = d.pop("formId", UNSET)

        _scan_type = d.pop("scanType", UNSET)
        scan_type: Union[Unset, ScanScanType]
        if isinstance(_scan_type, Unset):
            scan_type = UNSET
        else:
            scan_type = ScanScanType(_scan_type)

        _status = d.pop("status", UNSET)
        status: Union[Unset, ScanStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ScanStatus(_status)

        scan = cls(
            id=id,
            account_name=account_name,
            business_id=business_id,
            card_id=card_id,
            card_owner_id=card_owner_id,
            created_at=created_at,
            created_by=created_by,
            device_id=device_id,
            device_name=device_name,
            location=location,
            template_id=template_id,
            updated_at=updated_at,
            user_type=user_type,
            data_fields=data_fields,
            form_id=form_id,
            scan_type=scan_type,
            status=status,
        )

        scan.additional_properties = d
        return scan

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
