from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.form_field_usage_item import FormFieldUsageItem
from ..models.form_fields_type import FormFieldsType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.form_fields_options_item import FormFieldsOptionsItem


T = TypeVar("T", bound="FormFields")


@_attrs_define
class FormFields:
    """
    Attributes:
        enabled (bool):
        mapping_type (str):
        type_ (FormFieldsType):
        label (str):
        name (str):
        rules (list[str]):
        format_ (Union[None, Unset, str]): Format of the field Example: DD/MM/YYYY for date inputs.
        help_text (Union[None, Unset, str]): Help text to be displayed next to the field label Example: Date the member
            joined.
        usage (Union[Unset, list[FormFieldUsageItem]]): Usage of the form field
        value (Union[Unset, float, str]):
        placeholder (Union[Unset, str]):
        options (Union[Unset, list['FormFieldsOptionsItem']]): List of options for drop down list
    """

    enabled: bool
    mapping_type: str
    type_: FormFieldsType
    label: str
    name: str
    rules: list[str]
    format_: Union[None, Unset, str] = UNSET
    help_text: Union[None, Unset, str] = UNSET
    usage: Union[Unset, list[FormFieldUsageItem]] = UNSET
    value: Union[Unset, float, str] = UNSET
    placeholder: Union[Unset, str] = UNSET
    options: Union[Unset, list["FormFieldsOptionsItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        mapping_type = self.mapping_type

        type_ = self.type_.value

        label = self.label

        name = self.name

        rules = self.rules

        format_: Union[None, Unset, str]
        if isinstance(self.format_, Unset):
            format_ = UNSET
        else:
            format_ = self.format_

        help_text: Union[None, Unset, str]
        if isinstance(self.help_text, Unset):
            help_text = UNSET
        else:
            help_text = self.help_text

        usage: Union[Unset, list[str]] = UNSET
        if not isinstance(self.usage, Unset):
            usage = []
            for componentsschemas_form_field_usage_item_data in self.usage:
                componentsschemas_form_field_usage_item = componentsschemas_form_field_usage_item_data.value
                usage.append(componentsschemas_form_field_usage_item)

        value: Union[Unset, float, str]
        if isinstance(self.value, Unset):
            value = UNSET
        else:
            value = self.value

        placeholder = self.placeholder

        options: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.options, Unset):
            options = []
            for options_item_data in self.options:
                options_item = options_item_data.to_dict()
                options.append(options_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enabled": enabled,
                "mappingType": mapping_type,
                "type": type_,
                "label": label,
                "name": name,
                "rules": rules,
            }
        )
        if format_ is not UNSET:
            field_dict["format"] = format_
        if help_text is not UNSET:
            field_dict["helpText"] = help_text
        if usage is not UNSET:
            field_dict["usage"] = usage
        if value is not UNSET:
            field_dict["value"] = value
        if placeholder is not UNSET:
            field_dict["placeholder"] = placeholder
        if options is not UNSET:
            field_dict["options"] = options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.form_fields_options_item import FormFieldsOptionsItem

        d = dict(src_dict)
        enabled = d.pop("enabled")

        mapping_type = d.pop("mappingType")

        type_ = FormFieldsType(d.pop("type"))

        label = d.pop("label")

        name = d.pop("name")

        rules = cast(list[str], d.pop("rules"))

        def _parse_format_(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        format_ = _parse_format_(d.pop("format", UNSET))

        def _parse_help_text(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        help_text = _parse_help_text(d.pop("helpText", UNSET))

        usage = []
        _usage = d.pop("usage", UNSET)
        for componentsschemas_form_field_usage_item_data in _usage or []:
            componentsschemas_form_field_usage_item = FormFieldUsageItem(componentsschemas_form_field_usage_item_data)

            usage.append(componentsschemas_form_field_usage_item)

        def _parse_value(data: object) -> Union[Unset, float, str]:
            if isinstance(data, Unset):
                return data
            return cast(Union[Unset, float, str], data)

        value = _parse_value(d.pop("value", UNSET))

        placeholder = d.pop("placeholder", UNSET)

        options = []
        _options = d.pop("options", UNSET)
        for options_item_data in _options or []:
            options_item = FormFieldsOptionsItem.from_dict(options_item_data)

            options.append(options_item)

        form_fields = cls(
            enabled=enabled,
            mapping_type=mapping_type,
            type_=type_,
            label=label,
            name=name,
            rules=rules,
            format_=format_,
            help_text=help_text,
            usage=usage,
            value=value,
            placeholder=placeholder,
            options=options,
        )

        form_fields.additional_properties = d
        return form_fields

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
