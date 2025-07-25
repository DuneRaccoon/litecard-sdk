from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.form_v1_mailchimp_settings_merge_field_format import FormV1MailchimpSettingsMergeFieldFormat
    from ..models.form_v1_mailchimp_settings_merge_field_mapping import FormV1MailchimpSettingsMergeFieldMapping
    from ..models.mailchimp_tag_settings import MailchimpTagSettings


T = TypeVar("T", bound="FormV1MailchimpSettings")


@_attrs_define
class FormV1MailchimpSettings:
    """Form specific mailchimp settings

    Attributes:
        enabled (Union[Unset, bool]): Enable mailchimp invitation emails
        event_name (Union[Unset, str]): journey to trigger in mailchimp Example: my_event.
        merge_field_mapping (Union[Unset, FormV1MailchimpSettingsMergeFieldMapping]): Additional merge field mappings to
            card data
        merge_field_format (Union[Unset, FormV1MailchimpSettingsMergeFieldFormat]): Format of the merge fields, For
            example MM/DD for birthday type data in mailchimp
        tags (Union[Unset, list['MailchimpTagSettings']]):
    """

    enabled: Union[Unset, bool] = UNSET
    event_name: Union[Unset, str] = UNSET
    merge_field_mapping: Union[Unset, "FormV1MailchimpSettingsMergeFieldMapping"] = UNSET
    merge_field_format: Union[Unset, "FormV1MailchimpSettingsMergeFieldFormat"] = UNSET
    tags: Union[Unset, list["MailchimpTagSettings"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        event_name = self.event_name

        merge_field_mapping: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.merge_field_mapping, Unset):
            merge_field_mapping = self.merge_field_mapping.to_dict()

        merge_field_format: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.merge_field_format, Unset):
            merge_field_format = self.merge_field_format.to_dict()

        tags: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = []
            for tags_item_data in self.tags:
                tags_item = tags_item_data.to_dict()
                tags.append(tags_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if event_name is not UNSET:
            field_dict["eventName"] = event_name
        if merge_field_mapping is not UNSET:
            field_dict["mergeFieldMapping"] = merge_field_mapping
        if merge_field_format is not UNSET:
            field_dict["mergeFieldFormat"] = merge_field_format
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.form_v1_mailchimp_settings_merge_field_format import FormV1MailchimpSettingsMergeFieldFormat
        from ..models.form_v1_mailchimp_settings_merge_field_mapping import FormV1MailchimpSettingsMergeFieldMapping
        from ..models.mailchimp_tag_settings import MailchimpTagSettings

        d = dict(src_dict)
        enabled = d.pop("enabled", UNSET)

        event_name = d.pop("eventName", UNSET)

        _merge_field_mapping = d.pop("mergeFieldMapping", UNSET)
        merge_field_mapping: Union[Unset, FormV1MailchimpSettingsMergeFieldMapping]
        if isinstance(_merge_field_mapping, Unset):
            merge_field_mapping = UNSET
        else:
            merge_field_mapping = FormV1MailchimpSettingsMergeFieldMapping.from_dict(_merge_field_mapping)

        _merge_field_format = d.pop("mergeFieldFormat", UNSET)
        merge_field_format: Union[Unset, FormV1MailchimpSettingsMergeFieldFormat]
        if isinstance(_merge_field_format, Unset):
            merge_field_format = UNSET
        else:
            merge_field_format = FormV1MailchimpSettingsMergeFieldFormat.from_dict(_merge_field_format)

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = MailchimpTagSettings.from_dict(tags_item_data)

            tags.append(tags_item)

        form_v1_mailchimp_settings = cls(
            enabled=enabled,
            event_name=event_name,
            merge_field_mapping=merge_field_mapping,
            merge_field_format=merge_field_format,
            tags=tags,
        )

        form_v1_mailchimp_settings.additional_properties = d
        return form_v1_mailchimp_settings

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
