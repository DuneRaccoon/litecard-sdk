from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.coupon_redemption import CouponRedemption


T = TypeVar("T", bound="Coupon")


@_attrs_define
class Coupon:
    """
    Attributes:
        id (Union[Unset, str]): Id of the coupon Example: -jJWhjZ1a.
        name (Union[Unset, str]): Name of the coupon Example: Grab your first coupon here.
        description (Union[Unset, str]): description of the coupon Example: Promotions are only for the new registered
            card owners.
        discount_value (Union[Unset, float]): Coupon discount value Example: 100.
        expiry_date (Union[Unset, str]): Expire date of the coupon Example: 2021-08-15T03:15:56.860Z.
        redemption (Union[Unset, CouponRedemption]):
        created_at (Union[Unset, str]): Create date of the coupon Example: 2021-08-11T03:15:56.860Z.
        updated_at (Union[Unset, str]): Update date of the coupon Example: 2021-08-1T03:15:56.860Z.
        expiry_enabled (Union[Unset, bool]): Expire status of the coupon Example: true.
        created_by (Union[Unset, str]): Auth0 Id of the user who created this instance Example: V1StGXR8_Z5jdHi6B-myT.
        status (Union[Unset, str]): Redeem status of the coupon Example: ISSUED.
    """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    discount_value: Union[Unset, float] = UNSET
    expiry_date: Union[Unset, str] = UNSET
    redemption: Union[Unset, "CouponRedemption"] = UNSET
    created_at: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    expiry_enabled: Union[Unset, bool] = UNSET
    created_by: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        description = self.description

        discount_value = self.discount_value

        expiry_date = self.expiry_date

        redemption: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.redemption, Unset):
            redemption = self.redemption.to_dict()

        created_at = self.created_at

        updated_at = self.updated_at

        expiry_enabled = self.expiry_enabled

        created_by = self.created_by

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if discount_value is not UNSET:
            field_dict["discountValue"] = discount_value
        if expiry_date is not UNSET:
            field_dict["expiryDate"] = expiry_date
        if redemption is not UNSET:
            field_dict["redemption"] = redemption
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if expiry_enabled is not UNSET:
            field_dict["expiryEnabled"] = expiry_enabled
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.coupon_redemption import CouponRedemption

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        discount_value = d.pop("discountValue", UNSET)

        expiry_date = d.pop("expiryDate", UNSET)

        _redemption = d.pop("redemption", UNSET)
        redemption: Union[Unset, CouponRedemption]
        if isinstance(_redemption, Unset):
            redemption = UNSET
        else:
            redemption = CouponRedemption.from_dict(_redemption)

        created_at = d.pop("createdAt", UNSET)

        updated_at = d.pop("updatedAt", UNSET)

        expiry_enabled = d.pop("expiryEnabled", UNSET)

        created_by = d.pop("createdBy", UNSET)

        status = d.pop("status", UNSET)

        coupon = cls(
            id=id,
            name=name,
            description=description,
            discount_value=discount_value,
            expiry_date=expiry_date,
            redemption=redemption,
            created_at=created_at,
            updated_at=updated_at,
            expiry_enabled=expiry_enabled,
            created_by=created_by,
            status=status,
        )

        coupon.additional_properties = d
        return coupon

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
