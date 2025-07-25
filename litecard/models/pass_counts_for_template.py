from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.pass_counts_for_template_duration import PassCountsForTemplateDuration
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pass_count_details_for_template import PassCountDetailsForTemplate


T = TypeVar("T", bound="PassCountsForTemplate")


@_attrs_define
class PassCountsForTemplate:
    """Schema for retrieving pass counts for a specific template over a specified duration.

    Attributes:
        template_id (Union[Unset, str]): Id of the template for which the pass counts are retrieved Example:
            template-123.
        duration (Union[Unset, PassCountsForTemplateDuration]): Duration for which the pass counts are retrieved
        pass_counts (Union[Unset, PassCountDetailsForTemplate]): Statistics for a business or template related to pass
            counts.
    """

    template_id: Union[Unset, str] = UNSET
    duration: Union[Unset, PassCountsForTemplateDuration] = UNSET
    pass_counts: Union[Unset, "PassCountDetailsForTemplate"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        template_id = self.template_id

        duration: Union[Unset, str] = UNSET
        if not isinstance(self.duration, Unset):
            duration = self.duration.value

        pass_counts: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pass_counts, Unset):
            pass_counts = self.pass_counts.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if template_id is not UNSET:
            field_dict["templateId"] = template_id
        if duration is not UNSET:
            field_dict["duration"] = duration
        if pass_counts is not UNSET:
            field_dict["passCounts"] = pass_counts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pass_count_details_for_template import PassCountDetailsForTemplate

        d = dict(src_dict)
        template_id = d.pop("templateId", UNSET)

        _duration = d.pop("duration", UNSET)
        duration: Union[Unset, PassCountsForTemplateDuration]
        if isinstance(_duration, Unset):
            duration = UNSET
        else:
            duration = PassCountsForTemplateDuration(_duration)

        _pass_counts = d.pop("passCounts", UNSET)
        pass_counts: Union[Unset, PassCountDetailsForTemplate]
        if isinstance(_pass_counts, Unset):
            pass_counts = UNSET
        else:
            pass_counts = PassCountDetailsForTemplate.from_dict(_pass_counts)

        pass_counts_for_template = cls(
            template_id=template_id,
            duration=duration,
            pass_counts=pass_counts,
        )

        pass_counts_for_template.additional_properties = d
        return pass_counts_for_template

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
