from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.form_fields import FormFields
    from ..models.list_forms_result_item_id_style import ListFormsResultItemIdStyle


T = TypeVar("T", bound="ListFormsResultItemId")


@_attrs_define
class ListFormsResultItemId:
    """formId

    Example:
        -jJWhjZ1a

    Attributes:
        created_at (Union[Unset, str]): Create date of the form Example: 2021-08-11T03:15:56.860Z.
        fields (Union[Unset, list['FormFields']]):
        form_name (Union[Unset, str]): Name of the form Example: test form.
        created_by (Union[Unset, str]): Auth0 Id of the user who created this instance Example: V1StGXR8_Z5jdHi6B-myT.
        business_id (Union[Unset, str]): Id for the Business that this entity belongs to Example: LiteCard.
        ttl_enabled (Union[Unset, bool]): Enable ttl Example: true.
        ttl_period (Union[Unset, float]): Set ttl period Example: 10.
        updated_at (Union[Unset, str]): Update date of the form Example: 2021-08-11T03:15:56.860Z.
        password_enabled (Union[Unset, bool]): Enable password Example: true.
        logo (Union[Unset, str]): logo image link url Example: https://assets-dev.litecard.io/logo.png.
        title (Union[Unset, str]): Title of the form Example: LiteCard.
        description (Union[Unset, str]): Description of the form Example: Make your move with LiteCard today..
        style (Union[Unset, ListFormsResultItemIdStyle]):
        connect_id_enabled (Union[Unset, bool]): Enable ConnectID Verification Example: false.
    """

    created_at: Union[Unset, str] = UNSET
    fields: Union[Unset, list["FormFields"]] = UNSET
    form_name: Union[Unset, str] = UNSET
    created_by: Union[Unset, str] = UNSET
    business_id: Union[Unset, str] = UNSET
    ttl_enabled: Union[Unset, bool] = UNSET
    ttl_period: Union[Unset, float] = UNSET
    updated_at: Union[Unset, str] = UNSET
    password_enabled: Union[Unset, bool] = UNSET
    logo: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    style: Union[Unset, "ListFormsResultItemIdStyle"] = UNSET
    connect_id_enabled: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.form_fields import FormFields
        from ..models.list_forms_result_item_id_style import ListFormsResultItemIdStyle

        d = dict(src_dict)
        created_at = d.pop("createdAt", UNSET)

        fields = []
        _fields = d.pop("fields", UNSET)
        for fields_item_data in _fields or []:
            fields_item = FormFields.from_dict(fields_item_data)

            fields.append(fields_item)

        form_name = d.pop("formName", UNSET)

        created_by = d.pop("createdBy", UNSET)

        business_id = d.pop("businessId", UNSET)

        ttl_enabled = d.pop("ttlEnabled", UNSET)

        ttl_period = d.pop("ttlPeriod", UNSET)

        updated_at = d.pop("updatedAt", UNSET)

        password_enabled = d.pop("passwordEnabled", UNSET)

        logo = d.pop("logo", UNSET)

        title = d.pop("title", UNSET)

        description = d.pop("description", UNSET)

        _style = d.pop("style", UNSET)
        style: Union[Unset, ListFormsResultItemIdStyle]
        if isinstance(_style, Unset):
            style = UNSET
        else:
            style = ListFormsResultItemIdStyle.from_dict(_style)

        connect_id_enabled = d.pop("connectIDEnabled", UNSET)

        list_forms_result_item_id = cls(
            created_at=created_at,
            fields=fields,
            form_name=form_name,
            created_by=created_by,
            business_id=business_id,
            ttl_enabled=ttl_enabled,
            ttl_period=ttl_period,
            updated_at=updated_at,
            password_enabled=password_enabled,
            logo=logo,
            title=title,
            description=description,
            style=style,
            connect_id_enabled=connect_id_enabled,
        )

        list_forms_result_item_id.additional_properties = d
        return list_forms_result_item_id

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
