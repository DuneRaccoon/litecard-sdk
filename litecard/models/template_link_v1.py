from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.template_link_v1_type import TemplateLinkV1Type
from ..models.template_usage_v1_item import TemplateUsageV1Item
from ..types import UNSET, Unset

T = TypeVar("T", bound="TemplateLinkV1")


@_attrs_define
class TemplateLinkV1:
    """Links

    Attributes:
        id (Union[Unset, str]): Link ID
        uri (Union[Unset, str]): URI
        hyperlink_text (Union[Unset, str]): Add block of text with hyperlink by surrounding text with ${}, used by Apple
            Only Example: Click ${here} to visit the litecard website.
        title (Union[Unset, str]): Link title
        type_ (Union[Unset, TemplateLinkV1Type]): Type of link, used by Google Only
        usage (Union[Unset, list[TemplateUsageV1Item]]): List of strings to indicate where a field is rendered
        position (Union[Unset, float]): Order of the links. The order will be sorted in ascending order e.g. 1,2,3
    """

    id: Union[Unset, str] = UNSET
    uri: Union[Unset, str] = UNSET
    hyperlink_text: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    type_: Union[Unset, TemplateLinkV1Type] = UNSET
    usage: Union[Unset, list[TemplateUsageV1Item]] = UNSET
    position: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        uri = self.uri

        hyperlink_text = self.hyperlink_text

        title = self.title

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        usage: Union[Unset, list[str]] = UNSET
        if not isinstance(self.usage, Unset):
            usage = []
            for componentsschemas_template_usage_v1_item_data in self.usage:
                componentsschemas_template_usage_v1_item = componentsschemas_template_usage_v1_item_data.value
                usage.append(componentsschemas_template_usage_v1_item)

        position = self.position

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if uri is not UNSET:
            field_dict["uri"] = uri
        if hyperlink_text is not UNSET:
            field_dict["hyperlinkText"] = hyperlink_text
        if title is not UNSET:
            field_dict["title"] = title
        if type_ is not UNSET:
            field_dict["type"] = type_
        if usage is not UNSET:
            field_dict["usage"] = usage
        if position is not UNSET:
            field_dict["position"] = position

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        uri = d.pop("uri", UNSET)

        hyperlink_text = d.pop("hyperlinkText", UNSET)

        title = d.pop("title", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, TemplateLinkV1Type]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = TemplateLinkV1Type(_type_)

        usage = []
        _usage = d.pop("usage", UNSET)
        for componentsschemas_template_usage_v1_item_data in _usage or []:
            componentsschemas_template_usage_v1_item = TemplateUsageV1Item(
                componentsschemas_template_usage_v1_item_data
            )

            usage.append(componentsschemas_template_usage_v1_item)

        position = d.pop("position", UNSET)

        template_link_v1 = cls(
            id=id,
            uri=uri,
            hyperlink_text=hyperlink_text,
            title=title,
            type_=type_,
            usage=usage,
            position=position,
        )

        template_link_v1.additional_properties = d
        return template_link_v1

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
