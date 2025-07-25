from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.form_mailchimp_settings_merge_field_mapping import FormMailchimpSettingsMergeFieldMapping


T = TypeVar("T", bound="FormMailchimpSettings")


@_attrs_define
class FormMailchimpSettings:
    """Form specific mailchimp settings

    Attributes:
        enabled (Union[Unset, bool]): Enable mailchimp invitation emails
        event_name (Union[Unset, str]): journey to trigger in mailchimp Example: my_event.
        merge_field_mapping (Union[Unset, FormMailchimpSettingsMergeFieldMapping]): Additional merge field mappings to
            card data
    """

    enabled: Union[Unset, bool] = UNSET
    event_name: Union[Unset, str] = UNSET
    merge_field_mapping: Union[Unset, "FormMailchimpSettingsMergeFieldMapping"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        event_name = self.event_name

        merge_field_mapping: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.merge_field_mapping, Unset):
            merge_field_mapping = self.merge_field_mapping.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if event_name is not UNSET:
            field_dict["eventName"] = event_name
        if merge_field_mapping is not UNSET:
            field_dict["mergeFieldMapping"] = merge_field_mapping

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.form_mailchimp_settings_merge_field_mapping import FormMailchimpSettingsMergeFieldMapping

        d = dict(src_dict)
        enabled = d.pop("enabled", UNSET)

        event_name = d.pop("eventName", UNSET)

        _merge_field_mapping = d.pop("mergeFieldMapping", UNSET)
        merge_field_mapping: Union[Unset, FormMailchimpSettingsMergeFieldMapping]
        if isinstance(_merge_field_mapping, Unset):
            merge_field_mapping = UNSET
        else:
            merge_field_mapping = FormMailchimpSettingsMergeFieldMapping.from_dict(_merge_field_mapping)

        form_mailchimp_settings = cls(
            enabled=enabled,
            event_name=event_name,
            merge_field_mapping=merge_field_mapping,
        )

        form_mailchimp_settings.additional_properties = d
        return form_mailchimp_settings

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
