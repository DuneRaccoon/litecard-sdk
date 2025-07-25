from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ListPassRequestV1")


@_attrs_define
class ListPassRequestV1:
    """
    Attributes:
        next_ (Union[Unset, str]): Next key for dynamoDB query
        projection_expression (Union[Unset, str]): What keys to get inside card table
    """

    next_: Union[Unset, str] = UNSET
    projection_expression: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        next_ = self.next_

        projection_expression = self.projection_expression

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if next_ is not UNSET:
            field_dict["next"] = next_
        if projection_expression is not UNSET:
            field_dict["projectionExpression"] = projection_expression

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        next_ = d.pop("next", UNSET)

        projection_expression = d.pop("projectionExpression", UNSET)

        list_pass_request_v1 = cls(
            next_=next_,
            projection_expression=projection_expression,
        )

        list_pass_request_v1.additional_properties = d
        return list_pass_request_v1

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
