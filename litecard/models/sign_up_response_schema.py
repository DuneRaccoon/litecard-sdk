from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SignUpResponseSchema")


@_attrs_define
class SignUpResponseSchema:
    """
    Attributes:
        card_id (Union[Unset, str]): Id of created card Example: abc123.
        success (Union[Unset, bool]): Returns whether the request was successful Example: True.
        download_id (Union[Unset, str]): Id used for hosted litecard landing page e.g.
            https://app.dev.litecard.io/welcome/?id=5c_Wc9h-WCng0oxe8nHNn Example: 5c_Wc9h-WCng0oxe8nHNn.
    """

    card_id: Union[Unset, str] = UNSET
    success: Union[Unset, bool] = UNSET
    download_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        card_id = self.card_id

        success = self.success

        download_id = self.download_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if card_id is not UNSET:
            field_dict["cardId"] = card_id
        if success is not UNSET:
            field_dict["success"] = success
        if download_id is not UNSET:
            field_dict["downloadId"] = download_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        card_id = d.pop("cardId", UNSET)

        success = d.pop("success", UNSET)

        download_id = d.pop("downloadId", UNSET)

        sign_up_response_schema = cls(
            card_id=card_id,
            success=success,
            download_id=download_id,
        )

        sign_up_response_schema.additional_properties = d
        return sign_up_response_schema

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
