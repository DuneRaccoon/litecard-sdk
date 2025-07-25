from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.onboard_mailchimp_body_additional_merge_fields_item import (
        OnboardMailchimpBodyAdditionalMergeFieldsItem,
    )


T = TypeVar("T", bound="OnboardMailchimpBody")


@_attrs_define
class OnboardMailchimpBody:
    """
    Attributes:
        access_token (Union[Unset, str]): Mailchimp access token Example: d657...a926-us14.
        server (Union[Unset, str]): Mailchimp server Example: us14.
        from_email (Union[Unset, str]): Mailchimp email to send from Example: test@example.com.
        audience (Union[Unset, str]): Name of the Mailchimp Audience Example: Litecard.
        additional_merge_fields (Union[Unset, list['OnboardMailchimpBodyAdditionalMergeFieldsItem']]): Business
            customisable merge fields or segments
    """

    access_token: Union[Unset, str] = UNSET
    server: Union[Unset, str] = UNSET
    from_email: Union[Unset, str] = UNSET
    audience: Union[Unset, str] = UNSET
    additional_merge_fields: Union[Unset, list["OnboardMailchimpBodyAdditionalMergeFieldsItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        access_token = self.access_token

        server = self.server

        from_email = self.from_email

        audience = self.audience

        additional_merge_fields: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.additional_merge_fields, Unset):
            additional_merge_fields = []
            for additional_merge_fields_item_data in self.additional_merge_fields:
                additional_merge_fields_item = additional_merge_fields_item_data.to_dict()
                additional_merge_fields.append(additional_merge_fields_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if access_token is not UNSET:
            field_dict["accessToken"] = access_token
        if server is not UNSET:
            field_dict["server"] = server
        if from_email is not UNSET:
            field_dict["fromEmail"] = from_email
        if audience is not UNSET:
            field_dict["audience"] = audience
        if additional_merge_fields is not UNSET:
            field_dict["additionalMergeFields"] = additional_merge_fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.onboard_mailchimp_body_additional_merge_fields_item import (
            OnboardMailchimpBodyAdditionalMergeFieldsItem,
        )

        d = dict(src_dict)
        access_token = d.pop("accessToken", UNSET)

        server = d.pop("server", UNSET)

        from_email = d.pop("fromEmail", UNSET)

        audience = d.pop("audience", UNSET)

        additional_merge_fields = []
        _additional_merge_fields = d.pop("additionalMergeFields", UNSET)
        for additional_merge_fields_item_data in _additional_merge_fields or []:
            additional_merge_fields_item = OnboardMailchimpBodyAdditionalMergeFieldsItem.from_dict(
                additional_merge_fields_item_data
            )

            additional_merge_fields.append(additional_merge_fields_item)

        onboard_mailchimp_body = cls(
            access_token=access_token,
            server=server,
            from_email=from_email,
            audience=audience,
            additional_merge_fields=additional_merge_fields,
        )

        onboard_mailchimp_body.additional_properties = d
        return onboard_mailchimp_body

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
