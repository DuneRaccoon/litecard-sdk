from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Certificate")


@_attrs_define
class Certificate:
    """
    Attributes:
        apple (Union[Unset, str]): Apple Certificate Id Example: st3dfdAsaaf.
        google (Union[Unset, str]): Google Certificate Id Example: z2pkdjkASg3.
    """

    apple: Union[Unset, str] = UNSET
    google: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        apple = self.apple

        google = self.google

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if apple is not UNSET:
            field_dict["apple"] = apple
        if google is not UNSET:
            field_dict["google"] = google

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        apple = d.pop("apple", UNSET)

        google = d.pop("google", UNSET)

        certificate = cls(
            apple=apple,
            google=google,
        )

        certificate.additional_properties = d
        return certificate

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
