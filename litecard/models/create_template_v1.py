from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_template_v1_type import CreateTemplateV1Type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_template_v1_barcode import CreateTemplateV1Barcode
    from ..models.create_template_v1_colours import CreateTemplateV1Colours
    from ..models.create_template_v1_images import CreateTemplateV1Images
    from ..models.create_template_v1_tiers import CreateTemplateV1Tiers
    from ..models.notification_settings import NotificationSettings
    from ..models.rate_limit_v1_type_0 import RateLimitV1Type0
    from ..models.rate_limit_v1_type_1 import RateLimitV1Type1
    from ..models.settings_v1 import SettingsV1
    from ..models.shopfify_settings import ShopfifySettings
    from ..models.stripe_settings import StripeSettings
    from ..models.template_actions_v1 import TemplateActionsV1
    from ..models.template_app_linking import TemplateAppLinking
    from ..models.template_apple_wallet_settings_v1 import TemplateAppleWalletSettingsV1
    from ..models.template_card_expiry_v1_type_0 import TemplateCardExpiryV1Type0
    from ..models.template_card_expiry_v1_type_1 import TemplateCardExpiryV1Type1
    from ..models.template_card_expiry_v1_type_2 import TemplateCardExpiryV1Type2
    from ..models.template_card_expiry_v1_type_3 import TemplateCardExpiryV1Type3
    from ..models.template_certificates_v1 import TemplateCertificatesV1
    from ..models.template_data_field_v1 import TemplateDataFieldV1
    from ..models.template_google_wallet_settings_v1 import TemplateGoogleWalletSettingsV1
    from ..models.template_link_v1 import TemplateLinkV1
    from ..models.template_locations_v1_item import TemplateLocationsV1Item
    from ..models.template_samsung_wallet_settings_v1 import TemplateSamsungWalletSettingsV1


T = TypeVar("T", bound="CreateTemplateV1")


@_attrs_define
class CreateTemplateV1:
    """Template used to create apple/google wallet cards

    Attributes:
        name (str): Human readable name of the template Example: Bronze Card.
        description (str): Template Description Example: LiteCard Bronze Card.
        business_name (str): Name of the business Example: LiteCard.
        apple_wallet_settings (TemplateAppleWalletSettingsV1): Settings specific to apple wallet
        google_wallet_settings (TemplateGoogleWalletSettingsV1): Settings specific to google wallet
        colours (CreateTemplateV1Colours): Colours of the template
        images (CreateTemplateV1Images): Images of the template
        barcode (CreateTemplateV1Barcode): Barcode Fields of the template
        card_count (Union[Unset, int]): Number of active cards created using this template Example: 80.
        downloads_count (Union[Unset, int]): Number of cards downloaded Example: 70.
        downloaded_apple_pass_count (Union[Unset, int]): Number of cards downloaded on Apple Wallet Example: 50.
        downloaded_google_pass_count (Union[Unset, int]): Number of cards downloaded on Google Wallet Example: 20.
        is_internal (Union[Unset, bool]): Public Visibility of the template/form
        type_ (Union[Unset, CreateTemplateV1Type]): The Type of Pass
        external_id (Union[Unset, str]): External id mapping to third party system Example: 1234.
        settings (Union[Unset, SettingsV1]):
        stripe_settings (Union[Unset, StripeSettings]):
        samsung_wallet_settings (Union[Unset, TemplateSamsungWalletSettingsV1]): Settings specific to samsung wallet
        locations (Union[Unset, list['TemplateLocationsV1Item']]): List of locations to be stored on the pass, used by
            Apple for Geo-Location messages. Max of 10 locations for apple passes.
        card_expiry (Union['TemplateCardExpiryV1Type0', 'TemplateCardExpiryV1Type1', 'TemplateCardExpiryV1Type2',
            'TemplateCardExpiryV1Type3', Unset]): Card Expiry field on Template that details how cards created by the
            template will expire
        links (Union[Unset, list['TemplateLinkV1']]): Template Links
        data_fields (Union[Unset, list['TemplateDataFieldV1']]): Data Fields of the template
        certificates (Union[Unset, TemplateCertificatesV1]):
        actions (Union[Unset, TemplateActionsV1]):
        rate_limit (Union['RateLimitV1Type0', 'RateLimitV1Type1', Unset]): Card Scan Rate Limits
        app_linking (Union[Unset, TemplateAppLinking]): Template Settings to Allow AppLinking on the pass.
        shopify_settings (Union[Unset, ShopfifySettings]): Shopify specific settings
        notifications (Union[Unset, list['NotificationSettings']]):
        tiers (Union[Unset, CreateTemplateV1Tiers]): Multi tiers Settings
    """

    name: str
    description: str
    business_name: str
    apple_wallet_settings: "TemplateAppleWalletSettingsV1"
    google_wallet_settings: "TemplateGoogleWalletSettingsV1"
    colours: "CreateTemplateV1Colours"
    images: "CreateTemplateV1Images"
    barcode: "CreateTemplateV1Barcode"
    card_count: Union[Unset, int] = UNSET
    downloads_count: Union[Unset, int] = UNSET
    downloaded_apple_pass_count: Union[Unset, int] = UNSET
    downloaded_google_pass_count: Union[Unset, int] = UNSET
    is_internal: Union[Unset, bool] = UNSET
    type_: Union[Unset, CreateTemplateV1Type] = UNSET
    external_id: Union[Unset, str] = UNSET
    settings: Union[Unset, "SettingsV1"] = UNSET
    stripe_settings: Union[Unset, "StripeSettings"] = UNSET
    samsung_wallet_settings: Union[Unset, "TemplateSamsungWalletSettingsV1"] = UNSET
    locations: Union[Unset, list["TemplateLocationsV1Item"]] = UNSET
    card_expiry: Union[
        "TemplateCardExpiryV1Type0",
        "TemplateCardExpiryV1Type1",
        "TemplateCardExpiryV1Type2",
        "TemplateCardExpiryV1Type3",
        Unset,
    ] = UNSET
    links: Union[Unset, list["TemplateLinkV1"]] = UNSET
    data_fields: Union[Unset, list["TemplateDataFieldV1"]] = UNSET
    certificates: Union[Unset, "TemplateCertificatesV1"] = UNSET
    actions: Union[Unset, "TemplateActionsV1"] = UNSET
    rate_limit: Union["RateLimitV1Type0", "RateLimitV1Type1", Unset] = UNSET
    app_linking: Union[Unset, "TemplateAppLinking"] = UNSET
    shopify_settings: Union[Unset, "ShopfifySettings"] = UNSET
    notifications: Union[Unset, list["NotificationSettings"]] = UNSET
    tiers: Union[Unset, "CreateTemplateV1Tiers"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.rate_limit_v1_type_0 import RateLimitV1Type0
        from ..models.template_card_expiry_v1_type_0 import TemplateCardExpiryV1Type0
        from ..models.template_card_expiry_v1_type_1 import TemplateCardExpiryV1Type1
        from ..models.template_card_expiry_v1_type_2 import TemplateCardExpiryV1Type2

        name = self.name

        description = self.description

        business_name = self.business_name

        apple_wallet_settings = self.apple_wallet_settings.to_dict()

        google_wallet_settings = self.google_wallet_settings.to_dict()

        colours = self.colours.to_dict()

        images = self.images.to_dict()

        barcode = self.barcode.to_dict()

        card_count = self.card_count

        downloads_count = self.downloads_count

        downloaded_apple_pass_count = self.downloaded_apple_pass_count

        downloaded_google_pass_count = self.downloaded_google_pass_count

        is_internal = self.is_internal

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        external_id = self.external_id

        settings: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.settings, Unset):
            settings = self.settings.to_dict()

        stripe_settings: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.stripe_settings, Unset):
            stripe_settings = self.stripe_settings.to_dict()

        samsung_wallet_settings: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.samsung_wallet_settings, Unset):
            samsung_wallet_settings = self.samsung_wallet_settings.to_dict()

        locations: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.locations, Unset):
            locations = []
            for componentsschemas_template_locations_v1_item_data in self.locations:
                componentsschemas_template_locations_v1_item = (
                    componentsschemas_template_locations_v1_item_data.to_dict()
                )
                locations.append(componentsschemas_template_locations_v1_item)

        card_expiry: Union[Unset, dict[str, Any]]
        if isinstance(self.card_expiry, Unset):
            card_expiry = UNSET
        elif isinstance(self.card_expiry, TemplateCardExpiryV1Type0):
            card_expiry = self.card_expiry.to_dict()
        elif isinstance(self.card_expiry, TemplateCardExpiryV1Type1):
            card_expiry = self.card_expiry.to_dict()
        elif isinstance(self.card_expiry, TemplateCardExpiryV1Type2):
            card_expiry = self.card_expiry.to_dict()
        else:
            card_expiry = self.card_expiry.to_dict()

        links: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.links, Unset):
            links = []
            for links_item_data in self.links:
                links_item = links_item_data.to_dict()
                links.append(links_item)

        data_fields: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.data_fields, Unset):
            data_fields = []
            for data_fields_item_data in self.data_fields:
                data_fields_item = data_fields_item_data.to_dict()
                data_fields.append(data_fields_item)

        certificates: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.certificates, Unset):
            certificates = self.certificates.to_dict()

        actions: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.actions, Unset):
            actions = self.actions.to_dict()

        rate_limit: Union[Unset, dict[str, Any]]
        if isinstance(self.rate_limit, Unset):
            rate_limit = UNSET
        elif isinstance(self.rate_limit, RateLimitV1Type0):
            rate_limit = self.rate_limit.to_dict()
        else:
            rate_limit = self.rate_limit.to_dict()

        app_linking: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.app_linking, Unset):
            app_linking = self.app_linking.to_dict()

        shopify_settings: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.shopify_settings, Unset):
            shopify_settings = self.shopify_settings.to_dict()

        notifications: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.notifications, Unset):
            notifications = []
            for notifications_item_data in self.notifications:
                notifications_item = notifications_item_data.to_dict()
                notifications.append(notifications_item)

        tiers: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.tiers, Unset):
            tiers = self.tiers.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "description": description,
                "businessName": business_name,
                "appleWalletSettings": apple_wallet_settings,
                "googleWalletSettings": google_wallet_settings,
                "colours": colours,
                "images": images,
                "barcode": barcode,
            }
        )
        if card_count is not UNSET:
            field_dict["cardCount"] = card_count
        if downloads_count is not UNSET:
            field_dict["downloadsCount"] = downloads_count
        if downloaded_apple_pass_count is not UNSET:
            field_dict["downloadedApplePassCount"] = downloaded_apple_pass_count
        if downloaded_google_pass_count is not UNSET:
            field_dict["downloadedGooglePassCount"] = downloaded_google_pass_count
        if is_internal is not UNSET:
            field_dict["isInternal"] = is_internal
        if type_ is not UNSET:
            field_dict["type"] = type_
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if settings is not UNSET:
            field_dict["settings"] = settings
        if stripe_settings is not UNSET:
            field_dict["stripeSettings"] = stripe_settings
        if samsung_wallet_settings is not UNSET:
            field_dict["samsungWalletSettings"] = samsung_wallet_settings
        if locations is not UNSET:
            field_dict["locations"] = locations
        if card_expiry is not UNSET:
            field_dict["cardExpiry"] = card_expiry
        if links is not UNSET:
            field_dict["links"] = links
        if data_fields is not UNSET:
            field_dict["dataFields"] = data_fields
        if certificates is not UNSET:
            field_dict["certificates"] = certificates
        if actions is not UNSET:
            field_dict["actions"] = actions
        if rate_limit is not UNSET:
            field_dict["rateLimit"] = rate_limit
        if app_linking is not UNSET:
            field_dict["appLinking"] = app_linking
        if shopify_settings is not UNSET:
            field_dict["shopifySettings"] = shopify_settings
        if notifications is not UNSET:
            field_dict["notifications"] = notifications
        if tiers is not UNSET:
            field_dict["tiers"] = tiers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_template_v1_barcode import CreateTemplateV1Barcode
        from ..models.create_template_v1_colours import CreateTemplateV1Colours
        from ..models.create_template_v1_images import CreateTemplateV1Images
        from ..models.create_template_v1_tiers import CreateTemplateV1Tiers
        from ..models.notification_settings import NotificationSettings
        from ..models.rate_limit_v1_type_0 import RateLimitV1Type0
        from ..models.rate_limit_v1_type_1 import RateLimitV1Type1
        from ..models.settings_v1 import SettingsV1
        from ..models.shopfify_settings import ShopfifySettings
        from ..models.stripe_settings import StripeSettings
        from ..models.template_actions_v1 import TemplateActionsV1
        from ..models.template_app_linking import TemplateAppLinking
        from ..models.template_apple_wallet_settings_v1 import TemplateAppleWalletSettingsV1
        from ..models.template_card_expiry_v1_type_0 import TemplateCardExpiryV1Type0
        from ..models.template_card_expiry_v1_type_1 import TemplateCardExpiryV1Type1
        from ..models.template_card_expiry_v1_type_2 import TemplateCardExpiryV1Type2
        from ..models.template_card_expiry_v1_type_3 import TemplateCardExpiryV1Type3
        from ..models.template_certificates_v1 import TemplateCertificatesV1
        from ..models.template_data_field_v1 import TemplateDataFieldV1
        from ..models.template_google_wallet_settings_v1 import TemplateGoogleWalletSettingsV1
        from ..models.template_link_v1 import TemplateLinkV1
        from ..models.template_locations_v1_item import TemplateLocationsV1Item
        from ..models.template_samsung_wallet_settings_v1 import TemplateSamsungWalletSettingsV1

        d = dict(src_dict)
        name = d.pop("name")

        description = d.pop("description")

        business_name = d.pop("businessName")

        apple_wallet_settings = TemplateAppleWalletSettingsV1.from_dict(d.pop("appleWalletSettings"))

        google_wallet_settings = TemplateGoogleWalletSettingsV1.from_dict(d.pop("googleWalletSettings"))

        colours = CreateTemplateV1Colours.from_dict(d.pop("colours"))

        images = CreateTemplateV1Images.from_dict(d.pop("images"))

        barcode = CreateTemplateV1Barcode.from_dict(d.pop("barcode"))

        card_count = d.pop("cardCount", UNSET)

        downloads_count = d.pop("downloadsCount", UNSET)

        downloaded_apple_pass_count = d.pop("downloadedApplePassCount", UNSET)

        downloaded_google_pass_count = d.pop("downloadedGooglePassCount", UNSET)

        is_internal = d.pop("isInternal", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, CreateTemplateV1Type]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = CreateTemplateV1Type(_type_)

        external_id = d.pop("externalId", UNSET)

        _settings = d.pop("settings", UNSET)
        settings: Union[Unset, SettingsV1]
        if isinstance(_settings, Unset):
            settings = UNSET
        else:
            settings = SettingsV1.from_dict(_settings)

        _stripe_settings = d.pop("stripeSettings", UNSET)
        stripe_settings: Union[Unset, StripeSettings]
        if isinstance(_stripe_settings, Unset):
            stripe_settings = UNSET
        else:
            stripe_settings = StripeSettings.from_dict(_stripe_settings)

        _samsung_wallet_settings = d.pop("samsungWalletSettings", UNSET)
        samsung_wallet_settings: Union[Unset, TemplateSamsungWalletSettingsV1]
        if isinstance(_samsung_wallet_settings, Unset):
            samsung_wallet_settings = UNSET
        else:
            samsung_wallet_settings = TemplateSamsungWalletSettingsV1.from_dict(_samsung_wallet_settings)

        locations = []
        _locations = d.pop("locations", UNSET)
        for componentsschemas_template_locations_v1_item_data in _locations or []:
            componentsschemas_template_locations_v1_item = TemplateLocationsV1Item.from_dict(
                componentsschemas_template_locations_v1_item_data
            )

            locations.append(componentsschemas_template_locations_v1_item)

        def _parse_card_expiry(
            data: object,
        ) -> Union[
            "TemplateCardExpiryV1Type0",
            "TemplateCardExpiryV1Type1",
            "TemplateCardExpiryV1Type2",
            "TemplateCardExpiryV1Type3",
            Unset,
        ]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_template_card_expiry_v1_type_0 = TemplateCardExpiryV1Type0.from_dict(data)

                return componentsschemas_template_card_expiry_v1_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_template_card_expiry_v1_type_1 = TemplateCardExpiryV1Type1.from_dict(data)

                return componentsschemas_template_card_expiry_v1_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_template_card_expiry_v1_type_2 = TemplateCardExpiryV1Type2.from_dict(data)

                return componentsschemas_template_card_expiry_v1_type_2
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_template_card_expiry_v1_type_3 = TemplateCardExpiryV1Type3.from_dict(data)

            return componentsschemas_template_card_expiry_v1_type_3

        card_expiry = _parse_card_expiry(d.pop("cardExpiry", UNSET))

        links = []
        _links = d.pop("links", UNSET)
        for links_item_data in _links or []:
            links_item = TemplateLinkV1.from_dict(links_item_data)

            links.append(links_item)

        data_fields = []
        _data_fields = d.pop("dataFields", UNSET)
        for data_fields_item_data in _data_fields or []:
            data_fields_item = TemplateDataFieldV1.from_dict(data_fields_item_data)

            data_fields.append(data_fields_item)

        _certificates = d.pop("certificates", UNSET)
        certificates: Union[Unset, TemplateCertificatesV1]
        if isinstance(_certificates, Unset):
            certificates = UNSET
        else:
            certificates = TemplateCertificatesV1.from_dict(_certificates)

        _actions = d.pop("actions", UNSET)
        actions: Union[Unset, TemplateActionsV1]
        if isinstance(_actions, Unset):
            actions = UNSET
        else:
            actions = TemplateActionsV1.from_dict(_actions)

        def _parse_rate_limit(data: object) -> Union["RateLimitV1Type0", "RateLimitV1Type1", Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_rate_limit_v1_type_0 = RateLimitV1Type0.from_dict(data)

                return componentsschemas_rate_limit_v1_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_rate_limit_v1_type_1 = RateLimitV1Type1.from_dict(data)

            return componentsschemas_rate_limit_v1_type_1

        rate_limit = _parse_rate_limit(d.pop("rateLimit", UNSET))

        _app_linking = d.pop("appLinking", UNSET)
        app_linking: Union[Unset, TemplateAppLinking]
        if isinstance(_app_linking, Unset):
            app_linking = UNSET
        else:
            app_linking = TemplateAppLinking.from_dict(_app_linking)

        _shopify_settings = d.pop("shopifySettings", UNSET)
        shopify_settings: Union[Unset, ShopfifySettings]
        if isinstance(_shopify_settings, Unset):
            shopify_settings = UNSET
        else:
            shopify_settings = ShopfifySettings.from_dict(_shopify_settings)

        notifications = []
        _notifications = d.pop("notifications", UNSET)
        for notifications_item_data in _notifications or []:
            notifications_item = NotificationSettings.from_dict(notifications_item_data)

            notifications.append(notifications_item)

        _tiers = d.pop("tiers", UNSET)
        tiers: Union[Unset, CreateTemplateV1Tiers]
        if isinstance(_tiers, Unset):
            tiers = UNSET
        else:
            tiers = CreateTemplateV1Tiers.from_dict(_tiers)

        create_template_v1 = cls(
            name=name,
            description=description,
            business_name=business_name,
            apple_wallet_settings=apple_wallet_settings,
            google_wallet_settings=google_wallet_settings,
            colours=colours,
            images=images,
            barcode=barcode,
            card_count=card_count,
            downloads_count=downloads_count,
            downloaded_apple_pass_count=downloaded_apple_pass_count,
            downloaded_google_pass_count=downloaded_google_pass_count,
            is_internal=is_internal,
            type_=type_,
            external_id=external_id,
            settings=settings,
            stripe_settings=stripe_settings,
            samsung_wallet_settings=samsung_wallet_settings,
            locations=locations,
            card_expiry=card_expiry,
            links=links,
            data_fields=data_fields,
            certificates=certificates,
            actions=actions,
            rate_limit=rate_limit,
            app_linking=app_linking,
            shopify_settings=shopify_settings,
            notifications=notifications,
            tiers=tiers,
        )

        create_template_v1.additional_properties = d
        return create_template_v1

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
