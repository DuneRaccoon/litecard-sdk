import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.business_mailchimp import BusinessMailchimp
    from ..models.ui_config import UIConfig


T = TypeVar("T", bound="Business")


@_attrs_define
class Business:
    """Information about a business entity

    Attributes:
        id (Union[Unset, str]): Unique identifier for the business Example: L3ZrB748fLxlFD8ZjFVgX.
        apple_team_identifier (Union[Unset, str]): Team identifier for Apple services Example: F5MB9WT9BZ.
        business_name (Union[Unset, str]): Name of the business Example: Billing.
        card_count (Union[Unset, int]): Number of cards associated with the business Example: 60.
        card_limit (Union[Unset, int]): Maximum number of cards allowed for the business (-1 for unlimited) Example: -1.
        card_owner_count (Union[Unset, int]): Number of card owners associated with the business Example: 8.
        cert_id (Union[Unset, str]): Identifier for the certificate used by the business Example: freetier.
        created_at (Union[Unset, datetime.datetime]): Timestamp of when the business record was created Example:
            2022-09-08T06:37:44.803Z.
        email (Union[Unset, str]): Contact email for the business Example: billing_analytics@litecard.com.au.
        logo_url (Union[Unset, str]): URL to the business's logo Example: https://assets.litecard.io/Litecard_Badge.png.
        mailchimp (Union[Unset, BusinessMailchimp]): Mailchimp configuration details for the business
        pass_type_identifier (Union[Unset, str]): Pass type identifier for mobile wallet services Example:
            pass.au.com.lc.dev.freetier.
        template_count (Union[Unset, int]): Number of templates created by the business Example: 2.
        template_limit (Union[Unset, int]): Maximum number of templates allowed for the business (-1 for unlimited)
            Example: -1.
        tier (Union[Unset, str]): Tier or plan level of the business Example: FREE.
        updated_at (Union[Unset, datetime.datetime]): Timestamp of the last update to the business's record Example:
            2023-02-15T04:39:05.239Z.
        ui_config (Union[Unset, UIConfig]): Configuration for the UI
    """

    id: Union[Unset, str] = UNSET
    apple_team_identifier: Union[Unset, str] = UNSET
    business_name: Union[Unset, str] = UNSET
    card_count: Union[Unset, int] = UNSET
    card_limit: Union[Unset, int] = UNSET
    card_owner_count: Union[Unset, int] = UNSET
    cert_id: Union[Unset, str] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    email: Union[Unset, str] = UNSET
    logo_url: Union[Unset, str] = UNSET
    mailchimp: Union[Unset, "BusinessMailchimp"] = UNSET
    pass_type_identifier: Union[Unset, str] = UNSET
    template_count: Union[Unset, int] = UNSET
    template_limit: Union[Unset, int] = UNSET
    tier: Union[Unset, str] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    ui_config: Union[Unset, "UIConfig"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        apple_team_identifier = self.apple_team_identifier

        business_name = self.business_name

        card_count = self.card_count

        card_limit = self.card_limit

        card_owner_count = self.card_owner_count

        cert_id = self.cert_id

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        email = self.email

        logo_url = self.logo_url

        mailchimp: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.mailchimp, Unset):
            mailchimp = self.mailchimp.to_dict()

        pass_type_identifier = self.pass_type_identifier

        template_count = self.template_count

        template_limit = self.template_limit

        tier = self.tier

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        ui_config: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.ui_config, Unset):
            ui_config = self.ui_config.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if apple_team_identifier is not UNSET:
            field_dict["appleTeamIdentifier"] = apple_team_identifier
        if business_name is not UNSET:
            field_dict["businessName"] = business_name
        if card_count is not UNSET:
            field_dict["cardCount"] = card_count
        if card_limit is not UNSET:
            field_dict["cardLimit"] = card_limit
        if card_owner_count is not UNSET:
            field_dict["cardOwnerCount"] = card_owner_count
        if cert_id is not UNSET:
            field_dict["certId"] = cert_id
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if email is not UNSET:
            field_dict["email"] = email
        if logo_url is not UNSET:
            field_dict["logoUrl"] = logo_url
        if mailchimp is not UNSET:
            field_dict["mailchimp"] = mailchimp
        if pass_type_identifier is not UNSET:
            field_dict["passTypeIdentifier"] = pass_type_identifier
        if template_count is not UNSET:
            field_dict["templateCount"] = template_count
        if template_limit is not UNSET:
            field_dict["templateLimit"] = template_limit
        if tier is not UNSET:
            field_dict["tier"] = tier
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if ui_config is not UNSET:
            field_dict["uiConfig"] = ui_config

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.business_mailchimp import BusinessMailchimp
        from ..models.ui_config import UIConfig

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        apple_team_identifier = d.pop("appleTeamIdentifier", UNSET)

        business_name = d.pop("businessName", UNSET)

        card_count = d.pop("cardCount", UNSET)

        card_limit = d.pop("cardLimit", UNSET)

        card_owner_count = d.pop("cardOwnerCount", UNSET)

        cert_id = d.pop("certId", UNSET)

        _created_at = d.pop("createdAt", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        email = d.pop("email", UNSET)

        logo_url = d.pop("logoUrl", UNSET)

        _mailchimp = d.pop("mailchimp", UNSET)
        mailchimp: Union[Unset, BusinessMailchimp]
        if isinstance(_mailchimp, Unset):
            mailchimp = UNSET
        else:
            mailchimp = BusinessMailchimp.from_dict(_mailchimp)

        pass_type_identifier = d.pop("passTypeIdentifier", UNSET)

        template_count = d.pop("templateCount", UNSET)

        template_limit = d.pop("templateLimit", UNSET)

        tier = d.pop("tier", UNSET)

        _updated_at = d.pop("updatedAt", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        _ui_config = d.pop("uiConfig", UNSET)
        ui_config: Union[Unset, UIConfig]
        if isinstance(_ui_config, Unset):
            ui_config = UNSET
        else:
            ui_config = UIConfig.from_dict(_ui_config)

        business = cls(
            id=id,
            apple_team_identifier=apple_team_identifier,
            business_name=business_name,
            card_count=card_count,
            card_limit=card_limit,
            card_owner_count=card_owner_count,
            cert_id=cert_id,
            created_at=created_at,
            email=email,
            logo_url=logo_url,
            mailchimp=mailchimp,
            pass_type_identifier=pass_type_identifier,
            template_count=template_count,
            template_limit=template_limit,
            tier=tier,
            updated_at=updated_at,
            ui_config=ui_config,
        )

        business.additional_properties = d
        return business

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
