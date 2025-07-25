from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CouponRedemption")


@_attrs_define
class CouponRedemption:
    """
    Attributes:
        button_text (Union[Unset, str]): Button text of the coupon Example: Redeem Now (Bar Staff Only).
        instructions (Union[Unset, str]): Instructions of the coupon Example: Show this to the bar staff to redeem.
    """

    button_text: Union[Unset, str] = UNSET
    instructions: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        button_text = self.button_text

        instructions = self.instructions

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if button_text is not UNSET:
            field_dict["buttonText"] = button_text
        if instructions is not UNSET:
            field_dict["instructions"] = instructions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        button_text = d.pop("buttonText", UNSET)

        instructions = d.pop("instructions", UNSET)

        coupon_redemption = cls(
            button_text=button_text,
            instructions=instructions,
        )

        coupon_redemption.additional_properties = d
        return coupon_redemption

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
