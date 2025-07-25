from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ShopfifySettings")


@_attrs_define
class ShopfifySettings:
    """Shopify specific settings

    Attributes:
        generate_coupon (Union[Unset, bool]): Generate Coupon on Card Creation
        client (Union[Unset, str]): User key to be used to retrieve client credentials and verify owner
        rule_id (Union[Unset, float]): What rule the coupon should be using
    """

    generate_coupon: Union[Unset, bool] = UNSET
    client: Union[Unset, str] = UNSET
    rule_id: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        generate_coupon = self.generate_coupon

        client = self.client

        rule_id = self.rule_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if generate_coupon is not UNSET:
            field_dict["generateCoupon"] = generate_coupon
        if client is not UNSET:
            field_dict["client"] = client
        if rule_id is not UNSET:
            field_dict["ruleId"] = rule_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        generate_coupon = d.pop("generateCoupon", UNSET)

        client = d.pop("client", UNSET)

        rule_id = d.pop("ruleId", UNSET)

        shopfify_settings = cls(
            generate_coupon=generate_coupon,
            client=client,
            rule_id=rule_id,
        )

        shopfify_settings.additional_properties = d
        return shopfify_settings

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
