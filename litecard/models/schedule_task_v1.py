from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ScheduleTaskV1")


@_attrs_define
class ScheduleTaskV1:
    """
    Attributes:
        execute_at (str): When to schedule the task
        csv_ids (list[str]): CSV IDs to schedule task for Example: abc.
        google_service_account (Union[Unset, str]): Google Service Account to use for any Google related actions
            Example: google-service-account@litecard-example.iam.gserviceaccount.com.
    """

    execute_at: str
    csv_ids: list[str]
    google_service_account: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        execute_at = self.execute_at

        csv_ids = self.csv_ids

        google_service_account = self.google_service_account

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "executeAt": execute_at,
                "csvIds": csv_ids,
            }
        )
        if google_service_account is not UNSET:
            field_dict["googleServiceAccount"] = google_service_account

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        execute_at = d.pop("executeAt")

        csv_ids = cast(list[str], d.pop("csvIds"))

        google_service_account = d.pop("googleServiceAccount", UNSET)

        schedule_task_v1 = cls(
            execute_at=execute_at,
            csv_ids=csv_ids,
            google_service_account=google_service_account,
        )

        schedule_task_v1.additional_properties = d
        return schedule_task_v1

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
