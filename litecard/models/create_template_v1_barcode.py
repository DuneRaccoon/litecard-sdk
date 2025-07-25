from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_template_v1_barcode_type import CreateTemplateV1BarcodeType
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateTemplateV1Barcode")


@_attrs_define
class CreateTemplateV1Barcode:
    """Barcode Fields of the template

    Attributes:
        barcode_value (str): Value of the Barcode Example: 4805723345.
        type_ (CreateTemplateV1BarcodeType): Type of the Barcode Example: CODE_128.
        alt_text (Union[None, str]): Displayed alternative value at the bottom of the barcode Example: 1231244.
        message_encoding (Union[None, Unset, str]): Message Encoding of the Barcode Example: iso-8859-1.
        field_map (Union[None, Unset, str]): If barcodeValue is set to ${CUSTOM}. fieldMap must be present to identify
            which field the barcodeValue should be set from. Example: memberId.
    """

    barcode_value: str
    type_: CreateTemplateV1BarcodeType
    alt_text: Union[None, str]
    message_encoding: Union[None, Unset, str] = UNSET
    field_map: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        barcode_value = self.barcode_value

        type_ = self.type_.value

        alt_text: Union[None, str]
        alt_text = self.alt_text

        message_encoding: Union[None, Unset, str]
        if isinstance(self.message_encoding, Unset):
            message_encoding = UNSET
        else:
            message_encoding = self.message_encoding

        field_map: Union[None, Unset, str]
        if isinstance(self.field_map, Unset):
            field_map = UNSET
        else:
            field_map = self.field_map

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "barcodeValue": barcode_value,
                "type": type_,
                "altText": alt_text,
            }
        )
        if message_encoding is not UNSET:
            field_dict["messageEncoding"] = message_encoding
        if field_map is not UNSET:
            field_dict["fieldMap"] = field_map

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        barcode_value = d.pop("barcodeValue")

        type_ = CreateTemplateV1BarcodeType(d.pop("type"))

        def _parse_alt_text(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        alt_text = _parse_alt_text(d.pop("altText"))

        def _parse_message_encoding(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        message_encoding = _parse_message_encoding(d.pop("messageEncoding", UNSET))

        def _parse_field_map(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        field_map = _parse_field_map(d.pop("fieldMap", UNSET))

        create_template_v1_barcode = cls(
            barcode_value=barcode_value,
            type_=type_,
            alt_text=alt_text,
            message_encoding=message_encoding,
            field_map=field_map,
        )

        create_template_v1_barcode.additional_properties = d
        return create_template_v1_barcode

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
