from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="OnboardMailchimpBodyAdditionalMergeFieldsItem")


@_attrs_define
class OnboardMailchimpBodyAdditionalMergeFieldsItem:
    """
    Attributes:
        name (str): Segment Name/Merge Field Example: postCode.
        help_text (str): Helpful text to show in mailchimp UI for Segment Example: The Post Code of the customer.
        tag (str): Tag to use Example: POSTCODE.
    """

    name: str
    help_text: str
    tag: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        help_text = self.help_text

        tag = self.tag

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "helpText": help_text,
                "tag": tag,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        help_text = d.pop("helpText")

        tag = d.pop("tag")

        onboard_mailchimp_body_additional_merge_fields_item = cls(
            name=name,
            help_text=help_text,
            tag=tag,
        )

        onboard_mailchimp_body_additional_merge_fields_item.additional_properties = d
        return onboard_mailchimp_body_additional_merge_fields_item

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
