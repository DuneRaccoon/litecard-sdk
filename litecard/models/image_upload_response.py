from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ImageUploadResponse")


@_attrs_define
class ImageUploadResponse:
    """
    Attributes:
        success (Union[Unset, bool]):  Example: True.
        object_key (Union[Unset, str]): s3 object key Example: cryo/bDy_EeG2Ivd7vVrX45jx-logo@3x.png.
        image_url (Union[Unset, str]): s3 image url Example: https://lc-business-assets-dev.s3.ap-
            southeast-2.amazonaws.com/test-business/logo.png.
    """

    success: Union[Unset, bool] = UNSET
    object_key: Union[Unset, str] = UNSET
    image_url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        object_key = self.object_key

        image_url = self.image_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if success is not UNSET:
            field_dict["success"] = success
        if object_key is not UNSET:
            field_dict["objectKey"] = object_key
        if image_url is not UNSET:
            field_dict["imageUrl"] = image_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        success = d.pop("success", UNSET)

        object_key = d.pop("objectKey", UNSET)

        image_url = d.pop("imageUrl", UNSET)

        image_upload_response = cls(
            success=success,
            object_key=object_key,
            image_url=image_url,
        )

        image_upload_response.additional_properties = d
        return image_upload_response

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
