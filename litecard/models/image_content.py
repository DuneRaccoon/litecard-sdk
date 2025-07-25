from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.image_content_image_type import ImageContentImageType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ImageContent")


@_attrs_define
class ImageContent:
    """
    Attributes:
        image_id (Union[Unset, str]): Image Id Example: bDy_EeG2Ivd7vVrX45jx.
        image_type (Union[Unset, ImageContentImageType]): Image Type
        content (Union[Unset, str]): base64 encoded string Example: data:image/png;base64, iVBORw0KGgoAAAANSUhEUgAAAAUAA
            AAFCAYAAACNbyblAAAAHElEQVQI12P4//8/w38GIAXDIBKE0DHxgljNBAAO9TXL0Y4OHwAAAABJRU5ErkJggg==.
    """

    image_id: Union[Unset, str] = UNSET
    image_type: Union[Unset, ImageContentImageType] = UNSET
    content: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        image_id = self.image_id

        image_type: Union[Unset, str] = UNSET
        if not isinstance(self.image_type, Unset):
            image_type = self.image_type.value

        content = self.content

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if image_id is not UNSET:
            field_dict["imageId"] = image_id
        if image_type is not UNSET:
            field_dict["imageType"] = image_type
        if content is not UNSET:
            field_dict["content"] = content

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        image_id = d.pop("imageId", UNSET)

        _image_type = d.pop("imageType", UNSET)
        image_type: Union[Unset, ImageContentImageType]
        if isinstance(_image_type, Unset):
            image_type = UNSET
        else:
            image_type = ImageContentImageType(_image_type)

        content = d.pop("content", UNSET)

        image_content = cls(
            image_id=image_id,
            image_type=image_type,
            content=content,
        )

        image_content.additional_properties = d
        return image_content

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
