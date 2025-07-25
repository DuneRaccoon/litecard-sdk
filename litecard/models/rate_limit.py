from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rate_limit_rule import RateLimitRule


T = TypeVar("T", bound="RateLimit")


@_attrs_define
class RateLimit:
    """
    Attributes:
        enabled (Union[Unset, bool]): Enabled the rate limit Example: True.
        rule (Union[Unset, RateLimitRule]):
    """

    enabled: Union[Unset, bool] = UNSET
    rule: Union[Unset, "RateLimitRule"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        rule: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.rule, Unset):
            rule = self.rule.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if rule is not UNSET:
            field_dict["rule"] = rule

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rate_limit_rule import RateLimitRule

        d = dict(src_dict)
        enabled = d.pop("enabled", UNSET)

        _rule = d.pop("rule", UNSET)
        rule: Union[Unset, RateLimitRule]
        if isinstance(_rule, Unset):
            rule = UNSET
        else:
            rule = RateLimitRule.from_dict(_rule)

        rate_limit = cls(
            enabled=enabled,
            rule=rule,
        )

        rate_limit.additional_properties = d
        return rate_limit

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
