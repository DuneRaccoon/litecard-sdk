from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CardUploadGroupV1Count")


@_attrs_define
class CardUploadGroupV1Count:
    """valid + invalid = total and valid = created + updated + failed + skipped

    Attributes:
        failed (Union[Unset, float]):
        invalid (Union[Unset, float]):  Example: 2.
        skipped (Union[Unset, float]):
        created (Union[Unset, float]):  Example: 1.
        updated (Union[Unset, float]):  Example: 1.
        total (Union[Unset, float]):  Example: 3.
        valid (Union[Unset, float]):  Example: 1.
    """

    failed: Union[Unset, float] = UNSET
    invalid: Union[Unset, float] = UNSET
    skipped: Union[Unset, float] = UNSET
    created: Union[Unset, float] = UNSET
    updated: Union[Unset, float] = UNSET
    total: Union[Unset, float] = UNSET
    valid: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        failed = self.failed

        invalid = self.invalid

        skipped = self.skipped

        created = self.created

        updated = self.updated

        total = self.total

        valid = self.valid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if failed is not UNSET:
            field_dict["failed"] = failed
        if invalid is not UNSET:
            field_dict["invalid"] = invalid
        if skipped is not UNSET:
            field_dict["skipped"] = skipped
        if created is not UNSET:
            field_dict["created"] = created
        if updated is not UNSET:
            field_dict["updated"] = updated
        if total is not UNSET:
            field_dict["total"] = total
        if valid is not UNSET:
            field_dict["valid"] = valid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        failed = d.pop("failed", UNSET)

        invalid = d.pop("invalid", UNSET)

        skipped = d.pop("skipped", UNSET)

        created = d.pop("created", UNSET)

        updated = d.pop("updated", UNSET)

        total = d.pop("total", UNSET)

        valid = d.pop("valid", UNSET)

        card_upload_group_v1_count = cls(
            failed=failed,
            invalid=invalid,
            skipped=skipped,
            created=created,
            updated=updated,
            total=total,
            valid=valid,
        )

        card_upload_group_v1_count.additional_properties = d
        return card_upload_group_v1_count

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
