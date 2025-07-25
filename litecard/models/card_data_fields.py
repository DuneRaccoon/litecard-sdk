from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CardDataFields")


@_attrs_define
class CardDataFields:
    """
    Attributes:
        example_data_field (Union[Unset, str]): Example Value Example: example value.
        full_name (Union[Unset, str]): Full name of owner of card Example: John Doe.
    """

    example_data_field: Union[Unset, str] = UNSET
    full_name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        example_data_field = self.example_data_field

        full_name = self.full_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if example_data_field is not UNSET:
            field_dict["exampleDataField"] = example_data_field
        if full_name is not UNSET:
            field_dict["fullName"] = full_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        example_data_field = d.pop("exampleDataField", UNSET)

        full_name = d.pop("fullName", UNSET)

        card_data_fields = cls(
            example_data_field=example_data_field,
            full_name=full_name,
        )

        card_data_fields.additional_properties = d
        return card_data_fields

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
