from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.form_request_status import FormRequestStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.form_fields import FormFields
    from ..models.form_request_style import FormRequestStyle


T = TypeVar("T", bound="FormRequest")


@_attrs_define
class FormRequest:
    """
    Attributes:
        fields (Union[Unset, list['FormFields']]):
        form_name (Union[Unset, str]): Name of the form Example: test form.
        created_by (Union[Unset, str]): Auth0 Id of the user who created this instance Example: V1StGXR8_Z5jdHi6B-myT.
        business_id (Union[Unset, str]): Id for the Business that this entity belongs to Example: LiteCard.
        user_type (Union[Unset, str]): user type Example: staff.
        ttl_enabled (Union[Unset, bool]): Enable ttl Example: true.
        ttl_period (Union[Unset, float]): Set ttl period Example: 10.
        password_enabled (Union[Unset, bool]): Enable password Default: False. Example: true.
        logo (Union[Unset, str]): logo image link url Example: https://assets-dev.litecard.io/logo.png.
        title (Union[Unset, str]): Title of the form Example: LiteCard.
        description (Union[Unset, str]): Description of the form Example: Make your move with LiteCard today..
        style (Union[Unset, FormRequestStyle]):
        connect_id_enabled (Union[Unset, bool]): Enable ConnectID Verification Example: false.
        is_internal (Union[Unset, bool]): Public Visibility of the form Example: True.
        template_id (Union[Unset, str]): Id for the template used to create the card Example: test_business.
        status (Union[Unset, FormRequestStatus]): Status of the form Example: ACTIVE.
    """

    fields: Union[Unset, list["FormFields"]] = UNSET
    form_name: Union[Unset, str] = UNSET
    created_by: Union[Unset, str] = UNSET
    business_id: Union[Unset, str] = UNSET
    user_type: Union[Unset, str] = UNSET
    ttl_enabled: Union[Unset, bool] = UNSET
    ttl_period: Union[Unset, float] = UNSET
    password_enabled: Union[Unset, bool] = False
    logo: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    style: Union[Unset, "FormRequestStyle"] = UNSET
    connect_id_enabled: Union[Unset, bool] = UNSET
    is_internal: Union[Unset, bool] = UNSET
    template_id: Union[Unset, str] = UNSET
    status: Union[Unset, FormRequestStatus] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.form_fields import FormFields
        from ..models.form_request_style import FormRequestStyle

        d = dict(src_dict)
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

        password_enabled = d.pop("passwordEnabled", UNSET)

        logo = d.pop("logo", UNSET)

        title = d.pop("title", UNSET)

        description = d.pop("description", UNSET)

        _style = d.pop("style", UNSET)
        style: Union[Unset, FormRequestStyle]
        if isinstance(_style, Unset):
            style = UNSET
        else:
            style = FormRequestStyle.from_dict(_style)

        connect_id_enabled = d.pop("connectIDEnabled", UNSET)

        is_internal = d.pop("isInternal", UNSET)

        template_id = d.pop("templateId", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, FormRequestStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = FormRequestStatus(_status)

        form_request = cls(
            fields=fields,
            form_name=form_name,
            created_by=created_by,
            business_id=business_id,
            user_type=user_type,
            ttl_enabled=ttl_enabled,
            ttl_period=ttl_period,
            password_enabled=password_enabled,
            logo=logo,
            title=title,
            description=description,
            style=style,
            connect_id_enabled=connect_id_enabled,
            is_internal=is_internal,
            template_id=template_id,
            status=status,
        )

        form_request.additional_properties = d
        return form_request

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
