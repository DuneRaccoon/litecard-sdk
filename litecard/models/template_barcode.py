from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TemplateBarcode")


@_attrs_define
class TemplateBarcode:
    """Barcode Fields of the template

    Attributes:
        barcode_value (Union[None, Unset, str]): Value of the Barcode Example: 7048582966.
        message_encoding (Union[None, Unset, str]): Message Encoding of the Barcode Example: iso-8859-1.
        type_ (Union[None, Unset, str]): Type of the Barcode Example: CODE_128.
        alt_text (Union[Unset, bool]): Enable having the Pass ID displayed at the bottom of the barcode Default: True.
            Example: 1231244.
        enabled (Union[Unset, bool]): Whether the barcode is enabled Default: False. Example: True.
    """

    barcode_value: Union[None, Unset, str] = UNSET
    message_encoding: Union[None, Unset, str] = UNSET
    type_: Union[None, Unset, str] = UNSET
    alt_text: Union[Unset, bool] = True
    enabled: Union[Unset, bool] = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        barcode_value: Union[None, Unset, str]
        if isinstance(self.barcode_value, Unset):
            barcode_value = UNSET
        else:
            barcode_value = self.barcode_value

        message_encoding: Union[None, Unset, str]
        if isinstance(self.message_encoding, Unset):
            message_encoding = UNSET
        else:
            message_encoding = self.message_encoding

        type_: Union[None, Unset, str]
        if isinstance(self.type_, Unset):
            type_ = UNSET
        else:
            type_ = self.type_

        alt_text = self.alt_text

        enabled = self.enabled

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
        if enabled is not UNSET:
            field_dict["enabled"] = enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_barcode_value(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        barcode_value = _parse_barcode_value(d.pop("barcodeValue", UNSET))

        def _parse_message_encoding(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        message_encoding = _parse_message_encoding(d.pop("messageEncoding", UNSET))

        def _parse_type_(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        type_ = _parse_type_(d.pop("type", UNSET))

        alt_text = d.pop("altText", UNSET)

        enabled = d.pop("enabled", UNSET)

        template_barcode = cls(
            barcode_value=barcode_value,
            message_encoding=message_encoding,
            type_=type_,
            alt_text=alt_text,
            enabled=enabled,
        )

        template_barcode.additional_properties = d
        return template_barcode

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
