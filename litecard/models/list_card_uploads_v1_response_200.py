from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.card_upload_group_v1 import CardUploadGroupV1
    from ..models.card_upload_v1 import CardUploadV1


T = TypeVar("T", bound="ListCardUploadsV1Response200")


@_attrs_define
class ListCardUploadsV1Response200:
    """
    Attributes:
        uploads (Union[Unset, list['CardUploadV1']]):
        group (Union[Unset, CardUploadGroupV1]): Schema for Card Upload Group
        next_ (Union[Unset, str]): Key used to next set of results
    """

    uploads: Union[Unset, list["CardUploadV1"]] = UNSET
    group: Union[Unset, "CardUploadGroupV1"] = UNSET
    next_: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uploads: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.uploads, Unset):
            uploads = []
            for uploads_item_data in self.uploads:
                uploads_item = uploads_item_data.to_dict()
                uploads.append(uploads_item)

        group: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.group, Unset):
            group = self.group.to_dict()

        next_ = self.next_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if uploads is not UNSET:
            field_dict["uploads"] = uploads
        if group is not UNSET:
            field_dict["group"] = group
        if next_ is not UNSET:
            field_dict["next"] = next_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.card_upload_group_v1 import CardUploadGroupV1
        from ..models.card_upload_v1 import CardUploadV1

        d = dict(src_dict)
        uploads = []
        _uploads = d.pop("uploads", UNSET)
        for uploads_item_data in _uploads or []:
            uploads_item = CardUploadV1.from_dict(uploads_item_data)

            uploads.append(uploads_item)

        _group = d.pop("group", UNSET)
        group: Union[Unset, CardUploadGroupV1]
        if isinstance(_group, Unset):
            group = UNSET
        else:
            group = CardUploadGroupV1.from_dict(_group)

        next_ = d.pop("next", UNSET)

        list_card_uploads_v1_response_200 = cls(
            uploads=uploads,
            group=group,
            next_=next_,
        )

        list_card_uploads_v1_response_200.additional_properties = d
        return list_card_uploads_v1_response_200

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
