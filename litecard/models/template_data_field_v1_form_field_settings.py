from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.form_field_usage_item import FormFieldUsageItem
from ..models.template_data_field_v1_form_field_settings_data_type import TemplateDataFieldV1FormFieldSettingsDataType
from ..models.template_data_field_v1_form_field_settings_external_provider_mapping import (
    TemplateDataFieldV1FormFieldSettingsExternalProviderMapping,
)
from ..models.template_data_field_v1_form_field_settings_rules_item import TemplateDataFieldV1FormFieldSettingsRulesItem
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.template_data_field_v1_form_field_settings_options_item import (
        TemplateDataFieldV1FormFieldSettingsOptionsItem,
    )


T = TypeVar("T", bound="TemplateDataFieldV1FormFieldSettings")


@_attrs_define
class TemplateDataFieldV1FormFieldSettings:
    """Form field settings (Used for Litecard's Web UI based card creation workflow)

    Attributes:
        position (float): Order of the form field, all form fields will be ordered in ascending order (e.g. 1,2,3)
        place_holder_text (str): Place holder text Example: Full Name.
        data_type (TemplateDataFieldV1FormFieldSettingsDataType): Form field data type
        rules (Union[Unset, list[TemplateDataFieldV1FormFieldSettingsRulesItem]]): Validation rules that will be run on
            this field
        usage (Union[Unset, list[FormFieldUsageItem]]): Usage of the form field
        options (Union[Unset, list['TemplateDataFieldV1FormFieldSettingsOptionsItem']]): List of options for drop down
            list
        external_provider_mapping (Union[Unset, TemplateDataFieldV1FormFieldSettingsExternalProviderMapping]): If the
            field is mapped to an external provider, the key of the external provider
        external_mapping_key (Union[Unset, str]): If the field is mapped to an external provider, the key of the field
            in the external provider Example: memberId.
    """

    position: float
    place_holder_text: str
    data_type: TemplateDataFieldV1FormFieldSettingsDataType
    rules: Union[Unset, list[TemplateDataFieldV1FormFieldSettingsRulesItem]] = UNSET
    usage: Union[Unset, list[FormFieldUsageItem]] = UNSET
    options: Union[Unset, list["TemplateDataFieldV1FormFieldSettingsOptionsItem"]] = UNSET
    external_provider_mapping: Union[Unset, TemplateDataFieldV1FormFieldSettingsExternalProviderMapping] = UNSET
    external_mapping_key: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        position = self.position

        place_holder_text = self.place_holder_text

        data_type = self.data_type.value

        rules: Union[Unset, list[str]] = UNSET
        if not isinstance(self.rules, Unset):
            rules = []
            for rules_item_data in self.rules:
                rules_item = rules_item_data.value
                rules.append(rules_item)

        usage: Union[Unset, list[str]] = UNSET
        if not isinstance(self.usage, Unset):
            usage = []
            for componentsschemas_form_field_usage_item_data in self.usage:
                componentsschemas_form_field_usage_item = componentsschemas_form_field_usage_item_data.value
                usage.append(componentsschemas_form_field_usage_item)

        options: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.options, Unset):
            options = []
            for options_item_data in self.options:
                options_item = options_item_data.to_dict()
                options.append(options_item)

        external_provider_mapping: Union[Unset, str] = UNSET
        if not isinstance(self.external_provider_mapping, Unset):
            external_provider_mapping = self.external_provider_mapping.value

        external_mapping_key = self.external_mapping_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "position": position,
                "placeHolderText": place_holder_text,
                "dataType": data_type,
            }
        )
        if rules is not UNSET:
            field_dict["rules"] = rules
        if usage is not UNSET:
            field_dict["usage"] = usage
        if options is not UNSET:
            field_dict["options"] = options
        if external_provider_mapping is not UNSET:
            field_dict["externalProviderMapping"] = external_provider_mapping
        if external_mapping_key is not UNSET:
            field_dict["externalMappingKey"] = external_mapping_key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.template_data_field_v1_form_field_settings_options_item import (
            TemplateDataFieldV1FormFieldSettingsOptionsItem,
        )

        d = dict(src_dict)
        position = d.pop("position")

        place_holder_text = d.pop("placeHolderText")

        data_type = TemplateDataFieldV1FormFieldSettingsDataType(d.pop("dataType"))

        rules = []
        _rules = d.pop("rules", UNSET)
        for rules_item_data in _rules or []:
            rules_item = TemplateDataFieldV1FormFieldSettingsRulesItem(rules_item_data)

            rules.append(rules_item)

        usage = []
        _usage = d.pop("usage", UNSET)
        for componentsschemas_form_field_usage_item_data in _usage or []:
            componentsschemas_form_field_usage_item = FormFieldUsageItem(componentsschemas_form_field_usage_item_data)

            usage.append(componentsschemas_form_field_usage_item)

        options = []
        _options = d.pop("options", UNSET)
        for options_item_data in _options or []:
            options_item = TemplateDataFieldV1FormFieldSettingsOptionsItem.from_dict(options_item_data)

            options.append(options_item)

        _external_provider_mapping = d.pop("externalProviderMapping", UNSET)
        external_provider_mapping: Union[Unset, TemplateDataFieldV1FormFieldSettingsExternalProviderMapping]
        if isinstance(_external_provider_mapping, Unset):
            external_provider_mapping = UNSET
        else:
            external_provider_mapping = TemplateDataFieldV1FormFieldSettingsExternalProviderMapping(
                _external_provider_mapping
            )

        external_mapping_key = d.pop("externalMappingKey", UNSET)

        template_data_field_v1_form_field_settings = cls(
            position=position,
            place_holder_text=place_holder_text,
            data_type=data_type,
            rules=rules,
            usage=usage,
            options=options,
            external_provider_mapping=external_provider_mapping,
            external_mapping_key=external_mapping_key,
        )

        template_data_field_v1_form_field_settings.additional_properties = d
        return template_data_field_v1_form_field_settings

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
