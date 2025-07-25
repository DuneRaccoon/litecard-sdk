from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.template_v1 import TemplateV1


T = TypeVar("T", bound="ListTemplatesV1Response200")


@_attrs_define
class ListTemplatesV1Response200:
    """
    Attributes:
        templates (Union[Unset, list['TemplateV1']]):
        next_ (Union[Unset, str]): Key used to next set of results
    """

    templates: Union[Unset, list["TemplateV1"]] = UNSET
    next_: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        templates: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.templates, Unset):
            templates = []
            for componentsschemas_list_templates_v1_item_data in self.templates:
                componentsschemas_list_templates_v1_item = componentsschemas_list_templates_v1_item_data.to_dict()
                templates.append(componentsschemas_list_templates_v1_item)

        next_ = self.next_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if templates is not UNSET:
            field_dict["templates"] = templates
        if next_ is not UNSET:
            field_dict["next"] = next_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.template_v1 import TemplateV1

        d = dict(src_dict)
        templates = []
        _templates = d.pop("templates", UNSET)
        for componentsschemas_list_templates_v1_item_data in _templates or []:
            componentsschemas_list_templates_v1_item = TemplateV1.from_dict(
                componentsschemas_list_templates_v1_item_data
            )

            templates.append(componentsschemas_list_templates_v1_item)

        next_ = d.pop("next", UNSET)

        list_templates_v1_response_200 = cls(
            templates=templates,
            next_=next_,
        )

        list_templates_v1_response_200.additional_properties = d
        return list_templates_v1_response_200

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
