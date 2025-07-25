from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_pass_template_response_body_card_details import CreatePassTemplateResponseBodyCardDetails


T = TypeVar("T", bound="CreatePassTemplateResponseBody")


@_attrs_define
class CreatePassTemplateResponseBody:
    """
    Attributes:
        card_details (Union[Unset, CreatePassTemplateResponseBodyCardDetails]):
        success (Union[Unset, bool]): Returns whether the request was successful Example: True.
        template_id (Union[Unset, str]): Identifier for the template used to create the card Example: test_business.
        form_id (Union[Unset, str]): Id for field input form Example: V1StGXR8_Z5jdHi6B-myT.
    """

    card_details: Union[Unset, "CreatePassTemplateResponseBodyCardDetails"] = UNSET
    success: Union[Unset, bool] = UNSET
    template_id: Union[Unset, str] = UNSET
    form_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        card_details: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.card_details, Unset):
            card_details = self.card_details.to_dict()

        success = self.success

        template_id = self.template_id

        form_id = self.form_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if card_details is not UNSET:
            field_dict["cardDetails"] = card_details
        if success is not UNSET:
            field_dict["success"] = success
        if template_id is not UNSET:
            field_dict["templateId"] = template_id
        if form_id is not UNSET:
            field_dict["formId"] = form_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_pass_template_response_body_card_details import CreatePassTemplateResponseBodyCardDetails

        d = dict(src_dict)
        _card_details = d.pop("cardDetails", UNSET)
        card_details: Union[Unset, CreatePassTemplateResponseBodyCardDetails]
        if isinstance(_card_details, Unset):
            card_details = UNSET
        else:
            card_details = CreatePassTemplateResponseBodyCardDetails.from_dict(_card_details)

        success = d.pop("success", UNSET)

        template_id = d.pop("templateId", UNSET)

        form_id = d.pop("formId", UNSET)

        create_pass_template_response_body = cls(
            card_details=card_details,
            success=success,
            template_id=template_id,
            form_id=form_id,
        )

        create_pass_template_response_body.additional_properties = d
        return create_pass_template_response_body

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
