from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.email_reminders_request_body_email_template import EmailRemindersRequestBodyEmailTemplate
from ..types import UNSET, Unset

T = TypeVar("T", bound="EmailRemindersRequestBody")


@_attrs_define
class EmailRemindersRequestBody:
    """
    Attributes:
        email_template (EmailRemindersRequestBodyEmailTemplate): Select which email template option to use. Example:
            litecardpass.
        template_id (Union[Unset, str]): Template of the cards you want to send reminder to. If value not provided, will
            send to all passes that haven't been activated. Example: test_business.
    """

    email_template: EmailRemindersRequestBodyEmailTemplate
    template_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email_template = self.email_template.value

        template_id = self.template_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "emailTemplate": email_template,
            }
        )
        if template_id is not UNSET:
            field_dict["templateId"] = template_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        email_template = EmailRemindersRequestBodyEmailTemplate(d.pop("emailTemplate"))

        template_id = d.pop("templateId", UNSET)

        email_reminders_request_body = cls(
            email_template=email_template,
            template_id=template_id,
        )

        email_reminders_request_body.additional_properties = d
        return email_reminders_request_body

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
