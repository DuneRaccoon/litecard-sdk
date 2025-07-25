from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.voucher_codes_csv_upload_v1_body_type import VoucherCodesCSVUploadV1BodyType
from ..types import UNSET, Unset

T = TypeVar("T", bound="VoucherCodesCSVUploadV1Body")


@_attrs_define
class VoucherCodesCSVUploadV1Body:
    """
    Attributes:
        file (str):  Example: data:text/csv;base64,YXNkLHdlZHcsd2VkZQoxLDIsMwo=.
        template_id (str):  Example: template-1.
        type_ (Union[Unset, VoucherCodesCSVUploadV1BodyType]):  Example: VOUCHER.
    """

    file: str
    template_id: str
    type_: Union[Unset, VoucherCodesCSVUploadV1BodyType] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file = self.file

        template_id = self.template_id

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "file": file,
                "templateId": template_id,
            }
        )
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        file = d.pop("file")

        template_id = d.pop("templateId")

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, VoucherCodesCSVUploadV1BodyType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = VoucherCodesCSVUploadV1BodyType(_type_)

        voucher_codes_csv_upload_v1_body = cls(
            file=file,
            template_id=template_id,
            type_=type_,
        )

        voucher_codes_csv_upload_v1_body.additional_properties = d
        return voucher_codes_csv_upload_v1_body

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
