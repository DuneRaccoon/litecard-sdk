from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.set_template_status_body_status import SetTemplateStatusBodyStatus

T = TypeVar("T", bound="SetTemplateStatusBody")


@_attrs_define
class SetTemplateStatusBody:
    """
    Attributes:
        status (SetTemplateStatusBodyStatus): Template status Example: ACTIVE.
    """

    status: SetTemplateStatusBodyStatus
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = SetTemplateStatusBodyStatus(d.pop("status"))

        set_template_status_body = cls(
            status=status,
        )

        set_template_status_body.additional_properties = d
        return set_template_status_body

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
