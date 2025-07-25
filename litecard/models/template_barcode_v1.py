from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.template_barcode_v1_type import TemplateBarcodeV1Type
from ..types import UNSET, Unset

T = TypeVar("T", bound="TemplateBarcodeV1")


@_attrs_define
class TemplateBarcodeV1:
    """Barcode Fields of the template

    Attributes:
        barcode_value (Union[Unset, str]): Value of the Barcode Example: 4805723345.
        message_encoding (Union[None, Unset, str]): Message Encoding of the Barcode Example: iso-8859-1.
        type_ (Union[Unset, TemplateBarcodeV1Type]): Type of the Barcode Example: CODE_128.
        alt_text (Union[None, Unset, str]): Displayed alternative value at the bottom of the barcode Example: 1231244.
        field_map (Union[None, Unset, str]): If barcodeValue is set to ${CUSTOM}. fieldMap must be present to identify
            which field the barcodeValue should be set from. Example: memberId.
    """

    barcode_value: Union[Unset, str] = UNSET
    message_encoding: Union[None, Unset, str] = UNSET
    type_: Union[Unset, TemplateBarcodeV1Type] = UNSET
    alt_text: Union[None, Unset, str] = UNSET
    field_map: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        barcode_value = self.barcode_value

        message_encoding: Union[None, Unset, str]
        if isinstance(self.message_encoding, Unset):
            message_encoding = UNSET
        else:
            message_encoding = self.message_encoding

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        alt_text: Union[None, Unset, str]
        if isinstance(self.alt_text, Unset):
            alt_text = UNSET
        else:
            alt_text = self.alt_text

        field_map: Union[None, Unset, str]
        if isinstance(self.field_map, Unset):
            field_map = UNSET
        else:
            field_map = self.field_map

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if barcode_value is not UNSET:
            field_dict["barcodeValue"] = barcode_value
        if message_encoding is not UNSET:
            field_dict["messageEncoding"] = message_encoding
        if type_ is not UNSET:
            field_dict["type"] = type_
        if alt_text is not UNSET:
            field_dict["altText"] = alt_text
        if field_map is not UNSET:
            field_dict["fieldMap"] = field_map

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        barcode_value = d.pop("barcodeValue", UNSET)

        def _parse_message_encoding(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        message_encoding = _parse_message_encoding(d.pop("messageEncoding", UNSET))

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, TemplateBarcodeV1Type]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = TemplateBarcodeV1Type(_type_)

        def _parse_alt_text(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        alt_text = _parse_alt_text(d.pop("altText", UNSET))

        def _parse_field_map(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        field_map = _parse_field_map(d.pop("fieldMap", UNSET))

        template_barcode_v1 = cls(
            barcode_value=barcode_value,
            message_encoding=message_encoding,
            type_=type_,
            alt_text=alt_text,
            field_map=field_map,
        )

        template_barcode_v1.additional_properties = d
        return template_barcode_v1

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
