from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateTemplateV1Response201")


@_attrs_define
class CreateTemplateV1Response201:
    """
    Attributes:
        template_id (Union[Unset, str]):
        form_id (Union[Unset, str]):
    """

    template_id: Union[Unset, str] = UNSET
    form_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        template_id = self.template_id

        form_id = self.form_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if template_id is not UNSET:
            field_dict["templateId"] = template_id
        if form_id is not UNSET:
            field_dict["formId"] = form_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        template_id = d.pop("templateId", UNSET)

        form_id = d.pop("formId", UNSET)

        create_template_v1_response_201 = cls(
            template_id=template_id,
            form_id=form_id,
        )

        create_template_v1_response_201.additional_properties = d
        return create_template_v1_response_201

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
