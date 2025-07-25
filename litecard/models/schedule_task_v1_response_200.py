from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ScheduleTaskV1Response200")


@_attrs_define
class ScheduleTaskV1Response200:
    """
    Attributes:
        message (Union[Unset, str]):
        batch_group (Union[Unset, str]): ID denoting which batch group a task is part of
    """

    message: Union[Unset, str] = UNSET
    batch_group: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message = self.message

        batch_group = self.batch_group

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if message is not UNSET:
            field_dict["message"] = message
        if batch_group is not UNSET:
            field_dict["batchGroup"] = batch_group

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        message = d.pop("message", UNSET)

        batch_group = d.pop("batchGroup", UNSET)

        schedule_task_v1_response_200 = cls(
            message=message,
            batch_group=batch_group,
        )

        schedule_task_v1_response_200.additional_properties = d
        return schedule_task_v1_response_200

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
