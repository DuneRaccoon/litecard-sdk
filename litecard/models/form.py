from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.custom_form_design_schema import CustomFormDesignSchema
    from ..models.form_fields import FormFields
    from ..models.form_mailchimp_settings import FormMailchimpSettings
    from ..models.form_style import FormStyle
    from ..models.ui_config import UIConfig


T = TypeVar("T", bound="Form")


@_attrs_define
class Form:
    """
    Attributes:
        id (Union[Unset, str]): Id for field input form Example: -jJWhjZ1a.
        created_at (Union[Unset, str]): Create date of the form Example: 2021-08-11T03:15:56.860Z.
        fields (Union[Unset, list['FormFields']]):
        form_name (Union[Unset, str]): Name of the form Example: test form.
        created_by (Union[Unset, str]): Auth0 Id of the user who created this instance Example: V1StGXR8_Z5jdHi6B-myT.
        business_id (Union[Unset, str]): Id for the Business that this entity belongs to Example: LiteCard.
        user_type (Union[Unset, str]): user type Example: staff.
        ttl_enabled (Union[Unset, bool]): Enable ttl Example: true.
        ttl_period (Union[Unset, float]): Set ttl period Example: 10.
        updated_at (Union[Unset, str]): Update date of the form Example: 2021-08-11T03:15:56.860Z.
        password_enabled (Union[Unset, bool]): Enable password Example: true.
        logo (Union[Unset, str]): logo image link url Example: https://assets-dev.litecard.io/logo.png.
        title (Union[Unset, str]): Title of the form Example: LiteCard.
        description (Union[Unset, str]): Description of the form Example: Make your move with LiteCard today..
        style (Union[Unset, FormStyle]):
        connect_id_enabled (Union[Unset, bool]): Enable ConnectID Verification Example: false.
        is_internal (Union[Unset, bool]): Public Visibility of the form Example: True.
        template_id (Union[Unset, str]): Id for the template used to create the card Example: test_business.
        status (Union[Unset, str]): Status of the form Example: Deleted.
        mailchimp_settings (Union[Unset, FormMailchimpSettings]): Form specific mailchimp settings
        tac_url (Union[Unset, str]): URL of terms and conditions page Example: https://example.com.
        sms_enabled (Union[Unset, bool]): Flag to determine if we are to send SMS invitation or not Example: True.
        payment_required (Union[Unset, bool]): Whether this form belongs to a template that requires stripe payment
        hide_form (Union[Unset, bool]): Filter to hide form from private sign up
        ui_config (Union[Unset, UIConfig]): Configuration for the UI
        custom_design (Union[Unset, CustomFormDesignSchema]): Sign-up page configuration object
    """

    id: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    fields: Union[Unset, list["FormFields"]] = UNSET
    form_name: Union[Unset, str] = UNSET
    created_by: Union[Unset, str] = UNSET
    business_id: Union[Unset, str] = UNSET
    user_type: Union[Unset, str] = UNSET
    ttl_enabled: Union[Unset, bool] = UNSET
    ttl_period: Union[Unset, float] = UNSET
    updated_at: Union[Unset, str] = UNSET
    password_enabled: Union[Unset, bool] = UNSET
    logo: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    style: Union[Unset, "FormStyle"] = UNSET
    connect_id_enabled: Union[Unset, bool] = UNSET
    is_internal: Union[Unset, bool] = UNSET
    template_id: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    mailchimp_settings: Union[Unset, "FormMailchimpSettings"] = UNSET
    tac_url: Union[Unset, str] = UNSET
    sms_enabled: Union[Unset, bool] = UNSET
    payment_required: Union[Unset, bool] = UNSET
    hide_form: Union[Unset, bool] = UNSET
    ui_config: Union[Unset, "UIConfig"] = UNSET
    custom_design: Union[Unset, "CustomFormDesignSchema"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        created_at = self.created_at

        fields: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.fields, Unset):
            fields = []
            for fields_item_data in self.fields:
                fields_item = fields_item_data.to_dict()
                fields.append(fields_item)

        form_name = self.form_name

        created_by = self.created_by

        business_id = self.business_id

        user_type = self.user_type

        ttl_enabled = self.ttl_enabled

        ttl_period = self.ttl_period

        updated_at = self.updated_at

        password_enabled = self.password_enabled

        logo = self.logo

        title = self.title

        description = self.description

        style: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.style, Unset):
            style = self.style.to_dict()

        connect_id_enabled = self.connect_id_enabled

        is_internal = self.is_internal

        template_id = self.template_id

        status = self.status

        mailchimp_settings: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.mailchimp_settings, Unset):
            mailchimp_settings = self.mailchimp_settings.to_dict()

        tac_url = self.tac_url

        sms_enabled = self.sms_enabled

        payment_required = self.payment_required

        hide_form = self.hide_form

        ui_config: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.ui_config, Unset):
            ui_config = self.ui_config.to_dict()

        custom_design: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.custom_design, Unset):
            custom_design = self.custom_design.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if fields is not UNSET:
            field_dict["fields"] = fields
        if form_name is not UNSET:
            field_dict["formName"] = form_name
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if business_id is not UNSET:
            field_dict["businessId"] = business_id
        if user_type is not UNSET:
            field_dict["userType"] = user_type
        if ttl_enabled is not UNSET:
            field_dict["ttlEnabled"] = ttl_enabled
        if ttl_period is not UNSET:
            field_dict["ttlPeriod"] = ttl_period
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if password_enabled is not UNSET:
            field_dict["passwordEnabled"] = password_enabled
        if logo is not UNSET:
            field_dict["logo"] = logo
        if title is not UNSET:
            field_dict["title"] = title
        if description is not UNSET:
            field_dict["description"] = description
        if style is not UNSET:
            field_dict["style"] = style
        if connect_id_enabled is not UNSET:
            field_dict["connectIDEnabled"] = connect_id_enabled
        if is_internal is not UNSET:
            field_dict["isInternal"] = is_internal
        if template_id is not UNSET:
            field_dict["templateId"] = template_id
        if status is not UNSET:
            field_dict["status"] = status
        if mailchimp_settings is not UNSET:
            field_dict["mailchimpSettings"] = mailchimp_settings
        if tac_url is not UNSET:
            field_dict["tacURL"] = tac_url
        if sms_enabled is not UNSET:
            field_dict["smsEnabled"] = sms_enabled
        if payment_required is not UNSET:
            field_dict["paymentRequired"] = payment_required
        if hide_form is not UNSET:
            field_dict["hideForm"] = hide_form
        if ui_config is not UNSET:
            field_dict["uiConfig"] = ui_config
        if custom_design is not UNSET:
            field_dict["customDesign"] = custom_design

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.custom_form_design_schema import CustomFormDesignSchema
        from ..models.form_fields import FormFields
        from ..models.form_mailchimp_settings import FormMailchimpSettings
        from ..models.form_style import FormStyle
        from ..models.ui_config import UIConfig

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        created_at = d.pop("createdAt", UNSET)

        fields = []
        _fields = d.pop("fields", UNSET)
        for fields_item_data in _fields or []:
            fields_item = FormFields.from_dict(fields_item_data)

            fields.append(fields_item)

        form_name = d.pop("formName", UNSET)

        created_by = d.pop("createdBy", UNSET)

        business_id = d.pop("businessId", UNSET)

        user_type = d.pop("userType", UNSET)

        ttl_enabled = d.pop("ttlEnabled", UNSET)

        ttl_period = d.pop("ttlPeriod", UNSET)

        updated_at = d.pop("updatedAt", UNSET)

        password_enabled = d.pop("passwordEnabled", UNSET)

        logo = d.pop("logo", UNSET)

        title = d.pop("title", UNSET)

        description = d.pop("description", UNSET)

        _style = d.pop("style", UNSET)
        style: Union[Unset, FormStyle]
        if isinstance(_style, Unset):
            style = UNSET
        else:
            style = FormStyle.from_dict(_style)

        connect_id_enabled = d.pop("connectIDEnabled", UNSET)

        is_internal = d.pop("isInternal", UNSET)

        template_id = d.pop("templateId", UNSET)

        status = d.pop("status", UNSET)

        _mailchimp_settings = d.pop("mailchimpSettings", UNSET)
        mailchimp_settings: Union[Unset, FormMailchimpSettings]
        if isinstance(_mailchimp_settings, Unset):
            mailchimp_settings = UNSET
        else:
            mailchimp_settings = FormMailchimpSettings.from_dict(_mailchimp_settings)

        tac_url = d.pop("tacURL", UNSET)

        sms_enabled = d.pop("smsEnabled", UNSET)

        payment_required = d.pop("paymentRequired", UNSET)

        hide_form = d.pop("hideForm", UNSET)

        _ui_config = d.pop("uiConfig", UNSET)
        ui_config: Union[Unset, UIConfig]
        if isinstance(_ui_config, Unset):
            ui_config = UNSET
        else:
            ui_config = UIConfig.from_dict(_ui_config)

        _custom_design = d.pop("customDesign", UNSET)
        custom_design: Union[Unset, CustomFormDesignSchema]
        if isinstance(_custom_design, Unset):
            custom_design = UNSET
        else:
            custom_design = CustomFormDesignSchema.from_dict(_custom_design)

        form = cls(
            id=id,
            created_at=created_at,
            fields=fields,
            form_name=form_name,
            created_by=created_by,
            business_id=business_id,
            user_type=user_type,
            ttl_enabled=ttl_enabled,
            ttl_period=ttl_period,
            updated_at=updated_at,
            password_enabled=password_enabled,
            logo=logo,
            title=title,
            description=description,
            style=style,
            connect_id_enabled=connect_id_enabled,
            is_internal=is_internal,
            template_id=template_id,
            status=status,
            mailchimp_settings=mailchimp_settings,
            tac_url=tac_url,
            sms_enabled=sms_enabled,
            payment_required=payment_required,
            hide_form=hide_form,
            ui_config=ui_config,
            custom_design=custom_design,
        )

        form.additional_properties = d
        return form

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
