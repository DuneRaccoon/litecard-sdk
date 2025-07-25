from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cards_upload_csvv1_body_header_mappings import CardsUploadCSVV1BodyHeaderMappings


T = TypeVar("T", bound="CardsUploadCSVV1Body")


@_attrs_define
class CardsUploadCSVV1Body:
    """
    Attributes:
        file (str):  Example: data:text/csv;base64,YXNkLHdlZHcsd2VkZQoxLDIsMwo=.
        template_id (str):  Example: template-1.
        header_mappings (CardsUploadCSVV1BodyHeaderMappings):  Example: {'name': 'Full Name', 'age': 'Years Old',
            'email': 'Email Address'}.
        file_name (str):  Example: cards.csv.
        override_existing (Union[Unset, bool]):  Example: True.
        sms_invitation_enabled (Union[Unset, bool]):  Example: True.
        email_invitation_enabled (Union[Unset, bool]):  Example: True.
    """

    file: str
    template_id: str
    header_mappings: "CardsUploadCSVV1BodyHeaderMappings"
    file_name: str
    override_existing: Union[Unset, bool] = UNSET
    sms_invitation_enabled: Union[Unset, bool] = UNSET
    email_invitation_enabled: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file = self.file

        template_id = self.template_id

        header_mappings = self.header_mappings.to_dict()

        file_name = self.file_name

        override_existing = self.override_existing

        sms_invitation_enabled = self.sms_invitation_enabled

        email_invitation_enabled = self.email_invitation_enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "file": file,
                "templateId": template_id,
                "headerMappings": header_mappings,
                "fileName": file_name,
            }
        )
        if override_existing is not UNSET:
            field_dict["overrideExisting"] = override_existing
        if sms_invitation_enabled is not UNSET:
            field_dict["smsInvitationEnabled"] = sms_invitation_enabled
        if email_invitation_enabled is not UNSET:
            field_dict["emailInvitationEnabled"] = email_invitation_enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cards_upload_csvv1_body_header_mappings import CardsUploadCSVV1BodyHeaderMappings

        d = dict(src_dict)
        file = d.pop("file")

        template_id = d.pop("templateId")

        header_mappings = CardsUploadCSVV1BodyHeaderMappings.from_dict(d.pop("headerMappings"))

        file_name = d.pop("fileName")

        override_existing = d.pop("overrideExisting", UNSET)

        sms_invitation_enabled = d.pop("smsInvitationEnabled", UNSET)

        email_invitation_enabled = d.pop("emailInvitationEnabled", UNSET)

        cards_upload_csvv1_body = cls(
            file=file,
            template_id=template_id,
            header_mappings=header_mappings,
            file_name=file_name,
            override_existing=override_existing,
            sms_invitation_enabled=sms_invitation_enabled,
            email_invitation_enabled=email_invitation_enabled,
        )

        cards_upload_csvv1_body.additional_properties = d
        return cards_upload_csvv1_body

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
