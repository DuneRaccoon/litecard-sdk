from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.customer_webhook import CustomerWebhook
    from ..models.sub_business_roles import SubBusinessRoles
    from ..models.sub_business_summary import SubBusinessSummary
    from ..models.table_config import TableConfig
    from ..models.ui_config import UIConfig


T = TypeVar("T", bound="Profile")


@_attrs_define
class Profile:
    """
    Attributes:
        id (Union[Unset, str]): Business Id Example: CryoGym.
        business_name (Union[Unset, str]): Business name Example: Cryo gym.
        sub_business_name (Union[Unset, str]): Name to show on sub business selection Example: Cryo gym - Sub 1.
        email (Union[Unset, str]): Business email Example: Ankus Fang.
        post_code (Union[Unset, str]): Business postcode Example: CryoGym.
        state (Union[Unset, str]): Business state Example: AHVW1qv4I_Teqdu4VjwMA.
        logo_url (Union[Unset, str]): Business logo image file Example: https://assets.dev.litecard.io/Logo-Badge_3.png.
        template_count (Union[Unset, float]): Current total number of templates a user has. Example: 3.
        template_limit (Union[Unset, float]): Maximum amount of templates this user can have. A templateLimit of -1
            means the user can have unlimited templates. Example: 12.
        card_count (Union[Unset, float]): Active passes count Example: 12.
        total_card_count (Union[Unset, float]): Total passes count Example: 12.
        downloaded_apple_pass_count (Union[Unset, float]): Current total number of apple pass downloads a business has.
            Example: 12.
        downloaded_google_pass_count (Union[Unset, float]): Current total number of google pass downloads a business
            has. Example: 12.
        card_limit (Union[Unset, float]): Card limit left Example: 12.
        card_owner_count (Union[Unset, float]): Current total number of card owners a user has. Example: 100.
        tier (Union[Unset, str]): tier for the business Example: BUSINESS.
        created_at (Union[Unset, str]): Date when pass was first created, in ISO-8601 format Example:
            2021-08-11T03:15:56.860Z.
        updated_at (Union[Unset, str]): Date when pass was last updated, in ISO-8601 format Example:
            2021-08-1T03:15:56.860Z.
        stripe_customer_id (Union[Unset, str]): User's stripe customer account Example: cus_KozWy3MZchR5DY.
        table_config (Union[Unset, TableConfig]):
        is_master_business (Union[Unset, bool]): Is the account a master account Example: True.
        master_business_id (Union[Unset, str]): Master business id Example: master-business-id.
        sub_businesses (Union[Unset, list['SubBusinessSummary']]): Sub businesses
        sub_business_roles (Union[Unset, SubBusinessRoles]): An object where keys are business IDs and values are lists
            of roles Example: {'businessId1': ['admin', 'editor'], 'businessId2': ['viewer']}.
        ui_config (Union[Unset, UIConfig]): Configuration for the UI
        bulk_pass_invites_sent_at (Union[Unset, str]): Date when bulk pass invites were last sent, in ISO-8601 format
            Example: 2021-08-11T03:15:56.860Z.
        webhooks (Union[Unset, list['CustomerWebhook']]):
        use_enhanced_notification_send (Union[Unset, bool]): Whether to use the enhanced notification sender for sending
            notifications Example: True.
    """

    id: Union[Unset, str] = UNSET
    business_name: Union[Unset, str] = UNSET
    sub_business_name: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    post_code: Union[Unset, str] = UNSET
    state: Union[Unset, str] = UNSET
    logo_url: Union[Unset, str] = UNSET
    template_count: Union[Unset, float] = UNSET
    template_limit: Union[Unset, float] = UNSET
    card_count: Union[Unset, float] = UNSET
    total_card_count: Union[Unset, float] = UNSET
    downloaded_apple_pass_count: Union[Unset, float] = UNSET
    downloaded_google_pass_count: Union[Unset, float] = UNSET
    card_limit: Union[Unset, float] = UNSET
    card_owner_count: Union[Unset, float] = UNSET
    tier: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    stripe_customer_id: Union[Unset, str] = UNSET
    table_config: Union[Unset, "TableConfig"] = UNSET
    is_master_business: Union[Unset, bool] = UNSET
    master_business_id: Union[Unset, str] = UNSET
    sub_businesses: Union[Unset, list["SubBusinessSummary"]] = UNSET
    sub_business_roles: Union[Unset, "SubBusinessRoles"] = UNSET
    ui_config: Union[Unset, "UIConfig"] = UNSET
    bulk_pass_invites_sent_at: Union[Unset, str] = UNSET
    webhooks: Union[Unset, list["CustomerWebhook"]] = UNSET
    use_enhanced_notification_send: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        business_name = self.business_name

        sub_business_name = self.sub_business_name

        email = self.email

        post_code = self.post_code

        state = self.state

        logo_url = self.logo_url

        template_count = self.template_count

        template_limit = self.template_limit

        card_count = self.card_count

        total_card_count = self.total_card_count

        downloaded_apple_pass_count = self.downloaded_apple_pass_count

        downloaded_google_pass_count = self.downloaded_google_pass_count

        card_limit = self.card_limit

        card_owner_count = self.card_owner_count

        tier = self.tier

        created_at = self.created_at

        updated_at = self.updated_at

        stripe_customer_id = self.stripe_customer_id

        table_config: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.table_config, Unset):
            table_config = self.table_config.to_dict()

        is_master_business = self.is_master_business

        master_business_id = self.master_business_id

        sub_businesses: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.sub_businesses, Unset):
            sub_businesses = []
            for sub_businesses_item_data in self.sub_businesses:
                sub_businesses_item = sub_businesses_item_data.to_dict()
                sub_businesses.append(sub_businesses_item)

        sub_business_roles: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.sub_business_roles, Unset):
            sub_business_roles = self.sub_business_roles.to_dict()

        ui_config: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.ui_config, Unset):
            ui_config = self.ui_config.to_dict()

        bulk_pass_invites_sent_at = self.bulk_pass_invites_sent_at

        webhooks: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.webhooks, Unset):
            webhooks = []
            for webhooks_item_data in self.webhooks:
                webhooks_item = webhooks_item_data.to_dict()
                webhooks.append(webhooks_item)

        use_enhanced_notification_send = self.use_enhanced_notification_send

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if business_name is not UNSET:
            field_dict["businessName"] = business_name
        if sub_business_name is not UNSET:
            field_dict["subBusinessName"] = sub_business_name
        if email is not UNSET:
            field_dict["email"] = email
        if post_code is not UNSET:
            field_dict["postCode"] = post_code
        if state is not UNSET:
            field_dict["state"] = state
        if logo_url is not UNSET:
            field_dict["logoUrl"] = logo_url
        if template_count is not UNSET:
            field_dict["templateCount"] = template_count
        if template_limit is not UNSET:
            field_dict["templateLimit"] = template_limit
        if card_count is not UNSET:
            field_dict["cardCount"] = card_count
        if total_card_count is not UNSET:
            field_dict["totalCardCount"] = total_card_count
        if downloaded_apple_pass_count is not UNSET:
            field_dict["downloadedApplePassCount"] = downloaded_apple_pass_count
        if downloaded_google_pass_count is not UNSET:
            field_dict["downloadedGooglePassCount"] = downloaded_google_pass_count
        if card_limit is not UNSET:
            field_dict["cardLimit"] = card_limit
        if card_owner_count is not UNSET:
            field_dict["cardOwnerCount"] = card_owner_count
        if tier is not UNSET:
            field_dict["tier"] = tier
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if stripe_customer_id is not UNSET:
            field_dict["stripeCustomerId"] = stripe_customer_id
        if table_config is not UNSET:
            field_dict["tableConfig"] = table_config
        if is_master_business is not UNSET:
            field_dict["isMasterBusiness"] = is_master_business
        if master_business_id is not UNSET:
            field_dict["masterBusinessId"] = master_business_id
        if sub_businesses is not UNSET:
            field_dict["subBusinesses"] = sub_businesses
        if sub_business_roles is not UNSET:
            field_dict["subBusinessRoles"] = sub_business_roles
        if ui_config is not UNSET:
            field_dict["uiConfig"] = ui_config
        if bulk_pass_invites_sent_at is not UNSET:
            field_dict["bulkPassInvitesSentAt"] = bulk_pass_invites_sent_at
        if webhooks is not UNSET:
            field_dict["webhooks"] = webhooks
        if use_enhanced_notification_send is not UNSET:
            field_dict["useEnhancedNotificationSend"] = use_enhanced_notification_send

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.customer_webhook import CustomerWebhook
        from ..models.sub_business_roles import SubBusinessRoles
        from ..models.sub_business_summary import SubBusinessSummary
        from ..models.table_config import TableConfig
        from ..models.ui_config import UIConfig

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        business_name = d.pop("businessName", UNSET)

        sub_business_name = d.pop("subBusinessName", UNSET)

        email = d.pop("email", UNSET)

        post_code = d.pop("postCode", UNSET)

        state = d.pop("state", UNSET)

        logo_url = d.pop("logoUrl", UNSET)

        template_count = d.pop("templateCount", UNSET)

        template_limit = d.pop("templateLimit", UNSET)

        card_count = d.pop("cardCount", UNSET)

        total_card_count = d.pop("totalCardCount", UNSET)

        downloaded_apple_pass_count = d.pop("downloadedApplePassCount", UNSET)

        downloaded_google_pass_count = d.pop("downloadedGooglePassCount", UNSET)

        card_limit = d.pop("cardLimit", UNSET)

        card_owner_count = d.pop("cardOwnerCount", UNSET)

        tier = d.pop("tier", UNSET)

        created_at = d.pop("createdAt", UNSET)

        updated_at = d.pop("updatedAt", UNSET)

        stripe_customer_id = d.pop("stripeCustomerId", UNSET)

        _table_config = d.pop("tableConfig", UNSET)
        table_config: Union[Unset, TableConfig]
        if isinstance(_table_config, Unset):
            table_config = UNSET
        else:
            table_config = TableConfig.from_dict(_table_config)

        is_master_business = d.pop("isMasterBusiness", UNSET)

        master_business_id = d.pop("masterBusinessId", UNSET)

        sub_businesses = []
        _sub_businesses = d.pop("subBusinesses", UNSET)
        for sub_businesses_item_data in _sub_businesses or []:
            sub_businesses_item = SubBusinessSummary.from_dict(sub_businesses_item_data)

            sub_businesses.append(sub_businesses_item)

        _sub_business_roles = d.pop("subBusinessRoles", UNSET)
        sub_business_roles: Union[Unset, SubBusinessRoles]
        if isinstance(_sub_business_roles, Unset):
            sub_business_roles = UNSET
        else:
            sub_business_roles = SubBusinessRoles.from_dict(_sub_business_roles)

        _ui_config = d.pop("uiConfig", UNSET)
        ui_config: Union[Unset, UIConfig]
        if isinstance(_ui_config, Unset):
            ui_config = UNSET
        else:
            ui_config = UIConfig.from_dict(_ui_config)

        bulk_pass_invites_sent_at = d.pop("bulkPassInvitesSentAt", UNSET)

        webhooks = []
        _webhooks = d.pop("webhooks", UNSET)
        for webhooks_item_data in _webhooks or []:
            webhooks_item = CustomerWebhook.from_dict(webhooks_item_data)

            webhooks.append(webhooks_item)

        use_enhanced_notification_send = d.pop("useEnhancedNotificationSend", UNSET)

        profile = cls(
            id=id,
            business_name=business_name,
            sub_business_name=sub_business_name,
            email=email,
            post_code=post_code,
            state=state,
            logo_url=logo_url,
            template_count=template_count,
            template_limit=template_limit,
            card_count=card_count,
            total_card_count=total_card_count,
            downloaded_apple_pass_count=downloaded_apple_pass_count,
            downloaded_google_pass_count=downloaded_google_pass_count,
            card_limit=card_limit,
            card_owner_count=card_owner_count,
            tier=tier,
            created_at=created_at,
            updated_at=updated_at,
            stripe_customer_id=stripe_customer_id,
            table_config=table_config,
            is_master_business=is_master_business,
            master_business_id=master_business_id,
            sub_businesses=sub_businesses,
            sub_business_roles=sub_business_roles,
            ui_config=ui_config,
            bulk_pass_invites_sent_at=bulk_pass_invites_sent_at,
            webhooks=webhooks,
            use_enhanced_notification_send=use_enhanced_notification_send,
        )

        profile.additional_properties = d
        return profile

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
