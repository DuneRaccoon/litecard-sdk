from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.form_v1_status import FormV1Status
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.form_fields_v1 import FormFieldsV1
    from ..models.form_v1_mailchimp_settings import FormV1MailchimpSettings
    from ..models.form_v1_style import FormV1Style


T = TypeVar("T", bound="FormV1")


@_attrs_define
class FormV1:
    """
    Attributes:
        id (str): Id of the form Example: -jJWhjZ1a.
        fields (list['FormFieldsV1']):
        form_name (str): Name of the form Example: test form.
        business_id (str): Identifier for the Business that this entity belongs to Example: LiteCard.
        logo (str): logo image link url Example: https://assets-dev.litecard.io/logo.png.
        description (str): Description of the form Example: Make your move with LiteCard today..
        style (FormV1Style):
        is_internal (bool): Public Visibility of the form Example: True.
        template_id (str): Identifier for the template used to create the card Example: test_business.
        status (FormV1Status): Status of the form Example: ACTIVE.
        created_at (Union[Unset, str]): Record creation date Example: 2021-08-11T03:15:56.860Z.
        updated_at (Union[Unset, str]): Record update date Example: 2021-08-1T03:15:56.860Z.
        created_by (Union[Unset, str]): User Id of the creator Example: abc123.
        password_enabled (Union[Unset, bool]): Enable password Default: False. Example: true.
        title (Union[Unset, str]): Title of the form Example: LiteCard.
        connect_id_enabled (Union[Unset, bool]): Enable ConnectID Verification Example: false.
        payment_required (Union[Unset, bool]): Require payment after form submission
        tac_url (Union[Unset, str]): Terms and Condition link to be used
        sms_enabled (Union[Unset, bool]): Flag to send SMS or not. Used by our sign up form
        hide_form (Union[Unset, bool]): Hide form from Private Signup
        mailchimp_settings (Union[Unset, FormV1MailchimpSettings]): Form specific mailchimp settings
    """

    id: str
    fields: list["FormFieldsV1"]
    form_name: str
    business_id: str
    logo: str
    description: str
    style: "FormV1Style"
    is_internal: bool
    template_id: str
    status: FormV1Status
    created_at: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    created_by: Union[Unset, str] = UNSET
    password_enabled: Union[Unset, bool] = False
    title: Union[Unset, str] = UNSET
    connect_id_enabled: Union[Unset, bool] = UNSET
    payment_required: Union[Unset, bool] = UNSET
    tac_url: Union[Unset, str] = UNSET
    sms_enabled: Union[Unset, bool] = UNSET
    hide_form: Union[Unset, bool] = UNSET
    mailchimp_settings: Union[Unset, "FormV1MailchimpSettings"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        fields = []
        for fields_item_data in self.fields:
            fields_item = fields_item_data.to_dict()
            fields.append(fields_item)

        form_name = self.form_name

        business_id = self.business_id

        logo = self.logo

        description = self.description

        style = self.style.to_dict()

        is_internal = self.is_internal

        template_id = self.template_id

        status = self.status.value

        created_at = self.created_at

        updated_at = self.updated_at

        created_by = self.created_by

        password_enabled = self.password_enabled

        title = self.title

        connect_id_enabled = self.connect_id_enabled

        payment_required = self.payment_required

        tac_url = self.tac_url

        sms_enabled = self.sms_enabled

        hide_form = self.hide_form

        mailchimp_settings: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.mailchimp_settings, Unset):
            mailchimp_settings = self.mailchimp_settings.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "fields": fields,
                "formName": form_name,
                "businessId": business_id,
                "logo": logo,
                "description": description,
                "style": style,
                "isInternal": is_internal,
                "templateId": template_id,
                "status": status,
            }
        )
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if password_enabled is not UNSET:
            field_dict["passwordEnabled"] = password_enabled
        if title is not UNSET:
            field_dict["title"] = title
        if connect_id_enabled is not UNSET:
            field_dict["connectIDEnabled"] = connect_id_enabled
        if payment_required is not UNSET:
            field_dict["paymentRequired"] = payment_required
        if tac_url is not UNSET:
            field_dict["tacURL"] = tac_url
        if sms_enabled is not UNSET:
            field_dict["smsEnabled"] = sms_enabled
        if hide_form is not UNSET:
            field_dict["hideForm"] = hide_form
        if mailchimp_settings is not UNSET:
            field_dict["mailchimpSettings"] = mailchimp_settings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.form_fields_v1 import FormFieldsV1
        from ..models.form_v1_mailchimp_settings import FormV1MailchimpSettings
        from ..models.form_v1_style import FormV1Style

        d = dict(src_dict)
        id = d.pop("id")

        fields = []
        _fields = d.pop("fields")
        for fields_item_data in _fields:
            fields_item = FormFieldsV1.from_dict(fields_item_data)

            fields.append(fields_item)

        form_name = d.pop("formName")

        business_id = d.pop("businessId")

        logo = d.pop("logo")

        description = d.pop("description")

        style = FormV1Style.from_dict(d.pop("style"))

        is_internal = d.pop("isInternal")

        template_id = d.pop("templateId")

        status = FormV1Status(d.pop("status"))

        created_at = d.pop("createdAt", UNSET)

        updated_at = d.pop("updatedAt", UNSET)

        created_by = d.pop("createdBy", UNSET)

        password_enabled = d.pop("passwordEnabled", UNSET)

        title = d.pop("title", UNSET)

        connect_id_enabled = d.pop("connectIDEnabled", UNSET)

        payment_required = d.pop("paymentRequired", UNSET)

        tac_url = d.pop("tacURL", UNSET)

        sms_enabled = d.pop("smsEnabled", UNSET)

        hide_form = d.pop("hideForm", UNSET)

        _mailchimp_settings = d.pop("mailchimpSettings", UNSET)
        mailchimp_settings: Union[Unset, FormV1MailchimpSettings]
        if isinstance(_mailchimp_settings, Unset):
            mailchimp_settings = UNSET
        else:
            mailchimp_settings = FormV1MailchimpSettings.from_dict(_mailchimp_settings)

        form_v1 = cls(
            id=id,
            fields=fields,
            form_name=form_name,
            business_id=business_id,
            logo=logo,
            description=description,
            style=style,
            is_internal=is_internal,
            template_id=template_id,
            status=status,
            created_at=created_at,
            updated_at=updated_at,
            created_by=created_by,
            password_enabled=password_enabled,
            title=title,
            connect_id_enabled=connect_id_enabled,
            payment_required=payment_required,
            tac_url=tac_url,
            sms_enabled=sms_enabled,
            hide_form=hide_form,
            mailchimp_settings=mailchimp_settings,
        )

        form_v1.additional_properties = d
        return form_v1

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
