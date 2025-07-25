from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.template_data_field_v1_formatter import TemplateDataFieldV1Formatter
from ..models.template_data_field_v1_front_end_mapping_item import TemplateDataFieldV1FrontEndMappingItem
from ..models.template_usage_v1_item import TemplateUsageV1Item
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.template_data_field_v1_apple_field_settings import TemplateDataFieldV1AppleFieldSettings
    from ..models.template_data_field_v1_form_field_settings import TemplateDataFieldV1FormFieldSettings
    from ..models.template_data_field_v1_google_field_settings import TemplateDataFieldV1GoogleFieldSettings
    from ..models.template_data_field_v1_samsung_field_settings import TemplateDataFieldV1SamsungFieldSettings


T = TypeVar("T", bound="TemplateDataFieldV1")


@_attrs_define
class TemplateDataFieldV1:
    """Data field object

    Attributes:
        key (str): Unique key Example: firstName.
        label (str): The label of the field on the card/form Default: ''. Example: Member Since.
        usage (list[TemplateUsageV1Item]): List of strings to indicate where a field is rendered
        user_can_edit (bool): Value is true if the field appears on the form Example: True.
        default_country_code (Union[Unset, str]): Default country code for phone number field Example: au.
        date_format (Union[Unset, str]): If field is a date data type and it is to be displayed on the pass. Use this
            key to determine the date format using dayjs syntax Example: DD/MM/YYYY.
        default_value (Union[None, Unset, float, str]): Set a default value if you want a static value for this field.
            Overridden, if dataField[].value is set Example: 10.
        help_text (Union[None, Unset, str]): Help text to be displayed next to the field label Example: Date the member
            joined.
        description (Union[Unset, str]): Description of the field Example: This is the full name.
        formatter (Union[Unset, TemplateDataFieldV1Formatter]): Formatter to be used for the field Example: currency.
        currency_code (Union[Unset, str]): ISO 4217 currency code Example: AUD.
        apple_field_settings (Union[Unset, TemplateDataFieldV1AppleFieldSettings]):
        google_field_settings (Union[Unset, TemplateDataFieldV1GoogleFieldSettings]): Google wallet settings
        samsung_field_settings (Union[Unset, TemplateDataFieldV1SamsungFieldSettings]): Samsung field settings
        form_field_settings (Union[Unset, TemplateDataFieldV1FormFieldSettings]): Form field settings (Used for
            Litecard's Web UI based card creation workflow)
        front_end_mapping (Union[Unset, list[TemplateDataFieldV1FrontEndMappingItem]]): List to decide that decide
            whether the field should be rendered in the Litecard UI on scan previews or table views Example: ['SCAN'].
        unique_value (Union[Unset, bool]): Only used for segment keys - segment1, segment2 etc. Default: false Example:
            True.
    """

    key: str
    usage: list[TemplateUsageV1Item]
    user_can_edit: bool
    label: str = ""
    default_country_code: Union[Unset, str] = UNSET
    date_format: Union[Unset, str] = UNSET
    default_value: Union[None, Unset, float, str] = UNSET
    help_text: Union[None, Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    formatter: Union[Unset, TemplateDataFieldV1Formatter] = UNSET
    currency_code: Union[Unset, str] = UNSET
    apple_field_settings: Union[Unset, "TemplateDataFieldV1AppleFieldSettings"] = UNSET
    google_field_settings: Union[Unset, "TemplateDataFieldV1GoogleFieldSettings"] = UNSET
    samsung_field_settings: Union[Unset, "TemplateDataFieldV1SamsungFieldSettings"] = UNSET
    form_field_settings: Union[Unset, "TemplateDataFieldV1FormFieldSettings"] = UNSET
    front_end_mapping: Union[Unset, list[TemplateDataFieldV1FrontEndMappingItem]] = UNSET
    unique_value: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        label = self.label

        usage = []
        for componentsschemas_template_usage_v1_item_data in self.usage:
            componentsschemas_template_usage_v1_item = componentsschemas_template_usage_v1_item_data.value
            usage.append(componentsschemas_template_usage_v1_item)

        user_can_edit = self.user_can_edit

        default_country_code = self.default_country_code

        date_format = self.date_format

        default_value: Union[None, Unset, float, str]
        if isinstance(self.default_value, Unset):
            default_value = UNSET
        else:
            default_value = self.default_value

        help_text: Union[None, Unset, str]
        if isinstance(self.help_text, Unset):
            help_text = UNSET
        else:
            help_text = self.help_text

        description = self.description

        formatter: Union[Unset, str] = UNSET
        if not isinstance(self.formatter, Unset):
            formatter = self.formatter.value

        currency_code = self.currency_code

        apple_field_settings: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.apple_field_settings, Unset):
            apple_field_settings = self.apple_field_settings.to_dict()

        google_field_settings: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.google_field_settings, Unset):
            google_field_settings = self.google_field_settings.to_dict()

        samsung_field_settings: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.samsung_field_settings, Unset):
            samsung_field_settings = self.samsung_field_settings.to_dict()

        form_field_settings: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.form_field_settings, Unset):
            form_field_settings = self.form_field_settings.to_dict()

        front_end_mapping: Union[Unset, list[str]] = UNSET
        if not isinstance(self.front_end_mapping, Unset):
            front_end_mapping = []
            for front_end_mapping_item_data in self.front_end_mapping:
                front_end_mapping_item = front_end_mapping_item_data.value
                front_end_mapping.append(front_end_mapping_item)

        unique_value = self.unique_value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "label": label,
                "usage": usage,
                "userCanEdit": user_can_edit,
            }
        )
        if default_country_code is not UNSET:
            field_dict["defaultCountryCode"] = default_country_code
        if date_format is not UNSET:
            field_dict["dateFormat"] = date_format
        if default_value is not UNSET:
            field_dict["defaultValue"] = default_value
        if help_text is not UNSET:
            field_dict["helpText"] = help_text
        if description is not UNSET:
            field_dict["description"] = description
        if formatter is not UNSET:
            field_dict["formatter"] = formatter
        if currency_code is not UNSET:
            field_dict["currencyCode"] = currency_code
        if apple_field_settings is not UNSET:
            field_dict["appleFieldSettings"] = apple_field_settings
        if google_field_settings is not UNSET:
            field_dict["googleFieldSettings"] = google_field_settings
        if samsung_field_settings is not UNSET:
            field_dict["samsungFieldSettings"] = samsung_field_settings
        if form_field_settings is not UNSET:
            field_dict["formFieldSettings"] = form_field_settings
        if front_end_mapping is not UNSET:
            field_dict["frontEndMapping"] = front_end_mapping
        if unique_value is not UNSET:
            field_dict["uniqueValue"] = unique_value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.template_data_field_v1_apple_field_settings import TemplateDataFieldV1AppleFieldSettings
        from ..models.template_data_field_v1_form_field_settings import TemplateDataFieldV1FormFieldSettings
        from ..models.template_data_field_v1_google_field_settings import TemplateDataFieldV1GoogleFieldSettings
        from ..models.template_data_field_v1_samsung_field_settings import TemplateDataFieldV1SamsungFieldSettings

        d = dict(src_dict)
        key = d.pop("key")

        label = d.pop("label")

        usage = []
        _usage = d.pop("usage")
        for componentsschemas_template_usage_v1_item_data in _usage:
            componentsschemas_template_usage_v1_item = TemplateUsageV1Item(
                componentsschemas_template_usage_v1_item_data
            )

            usage.append(componentsschemas_template_usage_v1_item)

        user_can_edit = d.pop("userCanEdit")

        default_country_code = d.pop("defaultCountryCode", UNSET)

        date_format = d.pop("dateFormat", UNSET)

        def _parse_default_value(data: object) -> Union[None, Unset, float, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float, str], data)

        default_value = _parse_default_value(d.pop("defaultValue", UNSET))

        def _parse_help_text(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        help_text = _parse_help_text(d.pop("helpText", UNSET))

        description = d.pop("description", UNSET)

        _formatter = d.pop("formatter", UNSET)
        formatter: Union[Unset, TemplateDataFieldV1Formatter]
        if isinstance(_formatter, Unset):
            formatter = UNSET
        else:
            formatter = TemplateDataFieldV1Formatter(_formatter)

        currency_code = d.pop("currencyCode", UNSET)

        _apple_field_settings = d.pop("appleFieldSettings", UNSET)
        apple_field_settings: Union[Unset, TemplateDataFieldV1AppleFieldSettings]
        if isinstance(_apple_field_settings, Unset):
            apple_field_settings = UNSET
        else:
            apple_field_settings = TemplateDataFieldV1AppleFieldSettings.from_dict(_apple_field_settings)

        _google_field_settings = d.pop("googleFieldSettings", UNSET)
        google_field_settings: Union[Unset, TemplateDataFieldV1GoogleFieldSettings]
        if isinstance(_google_field_settings, Unset):
            google_field_settings = UNSET
        else:
            google_field_settings = TemplateDataFieldV1GoogleFieldSettings.from_dict(_google_field_settings)

        _samsung_field_settings = d.pop("samsungFieldSettings", UNSET)
        samsung_field_settings: Union[Unset, TemplateDataFieldV1SamsungFieldSettings]
        if isinstance(_samsung_field_settings, Unset):
            samsung_field_settings = UNSET
        else:
            samsung_field_settings = TemplateDataFieldV1SamsungFieldSettings.from_dict(_samsung_field_settings)

        _form_field_settings = d.pop("formFieldSettings", UNSET)
        form_field_settings: Union[Unset, TemplateDataFieldV1FormFieldSettings]
        if isinstance(_form_field_settings, Unset):
            form_field_settings = UNSET
        else:
            form_field_settings = TemplateDataFieldV1FormFieldSettings.from_dict(_form_field_settings)

        front_end_mapping = []
        _front_end_mapping = d.pop("frontEndMapping", UNSET)
        for front_end_mapping_item_data in _front_end_mapping or []:
            front_end_mapping_item = TemplateDataFieldV1FrontEndMappingItem(front_end_mapping_item_data)

            front_end_mapping.append(front_end_mapping_item)

        unique_value = d.pop("uniqueValue", UNSET)

        template_data_field_v1 = cls(
            key=key,
            label=label,
            usage=usage,
            user_can_edit=user_can_edit,
            default_country_code=default_country_code,
            date_format=date_format,
            default_value=default_value,
            help_text=help_text,
            description=description,
            formatter=formatter,
            currency_code=currency_code,
            apple_field_settings=apple_field_settings,
            google_field_settings=google_field_settings,
            samsung_field_settings=samsung_field_settings,
            form_field_settings=form_field_settings,
            front_end_mapping=front_end_mapping,
            unique_value=unique_value,
        )

        template_data_field_v1.additional_properties = d
        return template_data_field_v1

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
