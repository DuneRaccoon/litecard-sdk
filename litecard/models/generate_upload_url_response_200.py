from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GenerateUploadURLResponse200")


@_attrs_define
class GenerateUploadURLResponse200:
    """
    Attributes:
        url (Union[Unset, str]):
        csv_id (Union[Unset, str]):
    """

    url: Union[Unset, str] = UNSET
    csv_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        csv_id = self.csv_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if url is not UNSET:
            field_dict["url"] = url
        if csv_id is not UNSET:
            field_dict["csvId"] = csv_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        url = d.pop("url", UNSET)

        csv_id = d.pop("csvId", UNSET)

        generate_upload_url_response_200 = cls(
            url=url,
            csv_id=csv_id,
        )

        generate_upload_url_response_200.additional_properties = d
        return generate_upload_url_response_200

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
