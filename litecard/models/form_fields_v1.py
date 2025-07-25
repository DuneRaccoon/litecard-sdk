from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.form_field_usage_item import FormFieldUsageItem
from ..models.form_fields_v1_mapping_type import FormFieldsV1MappingType
from ..models.form_fields_v1_rules_item import FormFieldsV1RulesItem
from ..models.form_fields_v1_type import FormFieldsV1Type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.form_fields_v1_options_item import FormFieldsV1OptionsItem


T = TypeVar("T", bound="FormFieldsV1")


@_attrs_define
class FormFieldsV1:
    """
    Attributes:
        type_ (FormFieldsV1Type):
        label (str): The label of the field on the card/form Example: First Name.
        name (str): Unique key Example: firstName.
        rules (list[FormFieldsV1RulesItem]): Validation rules that will be run on this field
        format_ (Union[None, Unset, str]): Format of the field Example: DD/MM/YYYY for date inputs.
        help_text (Union[None, Unset, str]): Help text to be displayed next to the field label Example: Date the member
            joined.
        usage (Union[Unset, list[FormFieldUsageItem]]): Usage of the form field
        mapping_type (Union[Unset, FormFieldsV1MappingType]): Determines if this field is mapped from form to card or
            cardowner or both Example: True.
        value (Union[Unset, float, str]):
        placeholder (Union[Unset, str]): Place holder text Example: Full Name.
        default_country_code (Union[Unset, str]): Default country code for phone number Example: au.
        options (Union[Unset, list['FormFieldsV1OptionsItem']]): List of options for drop down list
    """

    type_: FormFieldsV1Type
    label: str
    name: str
    rules: list[FormFieldsV1RulesItem]
    format_: Union[None, Unset, str] = UNSET
    help_text: Union[None, Unset, str] = UNSET
    usage: Union[Unset, list[FormFieldUsageItem]] = UNSET
    mapping_type: Union[Unset, FormFieldsV1MappingType] = UNSET
    value: Union[Unset, float, str] = UNSET
    placeholder: Union[Unset, str] = UNSET
    default_country_code: Union[Unset, str] = UNSET
    options: Union[Unset, list["FormFieldsV1OptionsItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        label = self.label

        name = self.name

        rules = []
        for rules_item_data in self.rules:
            rules_item = rules_item_data.value
            rules.append(rules_item)

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

        mapping_type: Union[Unset, str] = UNSET
        if not isinstance(self.mapping_type, Unset):
            mapping_type = self.mapping_type.value

        value: Union[Unset, float, str]
        if isinstance(self.value, Unset):
            value = UNSET
        else:
            value = self.value

        placeholder = self.placeholder

        default_country_code = self.default_country_code

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
        if mapping_type is not UNSET:
            field_dict["mappingType"] = mapping_type
        if value is not UNSET:
            field_dict["value"] = value
        if placeholder is not UNSET:
            field_dict["placeholder"] = placeholder
        if default_country_code is not UNSET:
            field_dict["defaultCountryCode"] = default_country_code
        if options is not UNSET:
            field_dict["options"] = options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.form_fields_v1_options_item import FormFieldsV1OptionsItem

        d = dict(src_dict)
        type_ = FormFieldsV1Type(d.pop("type"))

        label = d.pop("label")

        name = d.pop("name")

        rules = []
        _rules = d.pop("rules")
        for rules_item_data in _rules:
            rules_item = FormFieldsV1RulesItem(rules_item_data)

            rules.append(rules_item)

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

        _mapping_type = d.pop("mappingType", UNSET)
        mapping_type: Union[Unset, FormFieldsV1MappingType]
        if isinstance(_mapping_type, Unset):
            mapping_type = UNSET
        else:
            mapping_type = FormFieldsV1MappingType(_mapping_type)

        def _parse_value(data: object) -> Union[Unset, float, str]:
            if isinstance(data, Unset):
                return data
            return cast(Union[Unset, float, str], data)

        value = _parse_value(d.pop("value", UNSET))

        placeholder = d.pop("placeholder", UNSET)

        default_country_code = d.pop("defaultCountryCode", UNSET)

        options = []
        _options = d.pop("options", UNSET)
        for options_item_data in _options or []:
            options_item = FormFieldsV1OptionsItem.from_dict(options_item_data)

            options.append(options_item)

        form_fields_v1 = cls(
            type_=type_,
            label=label,
            name=name,
            rules=rules,
            format_=format_,
            help_text=help_text,
            usage=usage,
            mapping_type=mapping_type,
            value=value,
            placeholder=placeholder,
            default_country_code=default_country_code,
            options=options,
        )

        form_fields_v1.additional_properties = d
        return form_fields_v1

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
