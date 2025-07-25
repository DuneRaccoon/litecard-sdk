from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.card_upload_group_v1_status import CardUploadGroupV1Status

if TYPE_CHECKING:
    from ..models.card_upload_group_v1_count import CardUploadGroupV1Count


T = TypeVar("T", bound="CardUploadGroupV1")


@_attrs_define
class CardUploadGroupV1:
    """Schema for Card Upload Group

    Attributes:
        id (str):  Example: group-id.
        business_id (str):  Example: business-id.
        count (CardUploadGroupV1Count): valid + invalid = total and valid = created + updated + failed + skipped
        created_at (str):  Example: 2024-05-30T06:53:18.700Z.
        file_name (str):  Example: cards.csv.
        override_existing (bool):  Example: True.
        status (CardUploadGroupV1Status):  Example: COMPLETED.
        template_id (str):  Example: template-id.
    """

    id: str
    business_id: str
    count: "CardUploadGroupV1Count"
    created_at: str
    file_name: str
    override_existing: bool
    status: CardUploadGroupV1Status
    template_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        business_id = self.business_id

        count = self.count.to_dict()

        created_at = self.created_at

        file_name = self.file_name

        override_existing = self.override_existing

        status = self.status.value

        template_id = self.template_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "businessId": business_id,
                "count": count,
                "createdAt": created_at,
                "fileName": file_name,
                "overrideExisting": override_existing,
                "status": status,
                "templateId": template_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.card_upload_group_v1_count import CardUploadGroupV1Count

        d = dict(src_dict)
        id = d.pop("id")

        business_id = d.pop("businessId")

        count = CardUploadGroupV1Count.from_dict(d.pop("count"))

        created_at = d.pop("createdAt")

        file_name = d.pop("fileName")

        override_existing = d.pop("overrideExisting")

        status = CardUploadGroupV1Status(d.pop("status"))

        template_id = d.pop("templateId")

        card_upload_group_v1 = cls(
            id=id,
            business_id=business_id,
            count=count,
            created_at=created_at,
            file_name=file_name,
            override_existing=override_existing,
            status=status,
            template_id=template_id,
        )

        card_upload_group_v1.additional_properties = d
        return card_upload_group_v1

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
