from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.template_barcode_v1 import TemplateBarcodeV1
    from ..models.template_card_expiry_v1_type_0 import TemplateCardExpiryV1Type0
    from ..models.template_card_expiry_v1_type_1 import TemplateCardExpiryV1Type1
    from ..models.template_card_expiry_v1_type_2 import TemplateCardExpiryV1Type2
    from ..models.template_card_expiry_v1_type_3 import TemplateCardExpiryV1Type3
    from ..models.template_colours_v1 import TemplateColoursV1
    from ..models.template_data_field_v1 import TemplateDataFieldV1
    from ..models.template_images_v1 import TemplateImagesV1
    from ..models.template_link_v1 import TemplateLinkV1
    from ..models.template_locations_v1_item import TemplateLocationsV1Item
    from ..models.tier_template_settings_google_wallet_settings import TierTemplateSettingsGoogleWalletSettings


T = TypeVar("T", bound="TierTemplateSettings")


@_attrs_define
class TierTemplateSettings:
    """The unique settings for each membership tier

    Attributes:
        default (bool): default tier when tier isn't provided during card creation. There must be only 1
        card_expiry (Union['TemplateCardExpiryV1Type0', 'TemplateCardExpiryV1Type1', 'TemplateCardExpiryV1Type2',
            'TemplateCardExpiryV1Type3', Unset]): Card Expiry field on Template that details how cards created by the
            template will expire
        colours (Union[Unset, TemplateColoursV1]): Colours of the template
        images (Union[Unset, TemplateImagesV1]): Images of the template
        barcode (Union[Unset, TemplateBarcodeV1]): Barcode Fields of the template
        locations (Union[Unset, list['TemplateLocationsV1Item']]): List of locations to be stored on the pass, used by
            Apple for Geo-Location messages. Max of 10 locations for apple passes.
        links (Union[Unset, list['TemplateLinkV1']]): Template Links
        data_fields (Union[Unset, list['TemplateDataFieldV1']]): Data Fields of the template
        google_wallet_settings (Union[Unset, TierTemplateSettingsGoogleWalletSettings]): Google Wallet Settings for the
            tier
    """

    default: bool
    card_expiry: Union[
        "TemplateCardExpiryV1Type0",
        "TemplateCardExpiryV1Type1",
        "TemplateCardExpiryV1Type2",
        "TemplateCardExpiryV1Type3",
        Unset,
    ] = UNSET
    colours: Union[Unset, "TemplateColoursV1"] = UNSET
    images: Union[Unset, "TemplateImagesV1"] = UNSET
    barcode: Union[Unset, "TemplateBarcodeV1"] = UNSET
    locations: Union[Unset, list["TemplateLocationsV1Item"]] = UNSET
    links: Union[Unset, list["TemplateLinkV1"]] = UNSET
    data_fields: Union[Unset, list["TemplateDataFieldV1"]] = UNSET
    google_wallet_settings: Union[Unset, "TierTemplateSettingsGoogleWalletSettings"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.template_card_expiry_v1_type_0 import TemplateCardExpiryV1Type0
        from ..models.template_card_expiry_v1_type_1 import TemplateCardExpiryV1Type1
        from ..models.template_card_expiry_v1_type_2 import TemplateCardExpiryV1Type2

        default = self.default

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

        colours: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.colours, Unset):
            colours = self.colours.to_dict()

        images: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.images, Unset):
            images = self.images.to_dict()

        barcode: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.barcode, Unset):
            barcode = self.barcode.to_dict()

        locations: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.locations, Unset):
            locations = []
            for componentsschemas_template_locations_v1_item_data in self.locations:
                componentsschemas_template_locations_v1_item = (
                    componentsschemas_template_locations_v1_item_data.to_dict()
                )
                locations.append(componentsschemas_template_locations_v1_item)

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

        google_wallet_settings: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.google_wallet_settings, Unset):
            google_wallet_settings = self.google_wallet_settings.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "default": default,
            }
        )
        if card_expiry is not UNSET:
            field_dict["cardExpiry"] = card_expiry
        if colours is not UNSET:
            field_dict["colours"] = colours
        if images is not UNSET:
            field_dict["images"] = images
        if barcode is not UNSET:
            field_dict["barcode"] = barcode
        if locations is not UNSET:
            field_dict["locations"] = locations
        if links is not UNSET:
            field_dict["links"] = links
        if data_fields is not UNSET:
            field_dict["dataFields"] = data_fields
        if google_wallet_settings is not UNSET:
            field_dict["googleWalletSettings"] = google_wallet_settings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.template_barcode_v1 import TemplateBarcodeV1
        from ..models.template_card_expiry_v1_type_0 import TemplateCardExpiryV1Type0
        from ..models.template_card_expiry_v1_type_1 import TemplateCardExpiryV1Type1
        from ..models.template_card_expiry_v1_type_2 import TemplateCardExpiryV1Type2
        from ..models.template_card_expiry_v1_type_3 import TemplateCardExpiryV1Type3
        from ..models.template_colours_v1 import TemplateColoursV1
        from ..models.template_data_field_v1 import TemplateDataFieldV1
        from ..models.template_images_v1 import TemplateImagesV1
        from ..models.template_link_v1 import TemplateLinkV1
        from ..models.template_locations_v1_item import TemplateLocationsV1Item
        from ..models.tier_template_settings_google_wallet_settings import TierTemplateSettingsGoogleWalletSettings

        d = dict(src_dict)
        default = d.pop("default")

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

        _colours = d.pop("colours", UNSET)
        colours: Union[Unset, TemplateColoursV1]
        if isinstance(_colours, Unset):
            colours = UNSET
        else:
            colours = TemplateColoursV1.from_dict(_colours)

        _images = d.pop("images", UNSET)
        images: Union[Unset, TemplateImagesV1]
        if isinstance(_images, Unset):
            images = UNSET
        else:
            images = TemplateImagesV1.from_dict(_images)

        _barcode = d.pop("barcode", UNSET)
        barcode: Union[Unset, TemplateBarcodeV1]
        if isinstance(_barcode, Unset):
            barcode = UNSET
        else:
            barcode = TemplateBarcodeV1.from_dict(_barcode)

        locations = []
        _locations = d.pop("locations", UNSET)
        for componentsschemas_template_locations_v1_item_data in _locations or []:
            componentsschemas_template_locations_v1_item = TemplateLocationsV1Item.from_dict(
                componentsschemas_template_locations_v1_item_data
            )

            locations.append(componentsschemas_template_locations_v1_item)

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

        _google_wallet_settings = d.pop("googleWalletSettings", UNSET)
        google_wallet_settings: Union[Unset, TierTemplateSettingsGoogleWalletSettings]
        if isinstance(_google_wallet_settings, Unset):
            google_wallet_settings = UNSET
        else:
            google_wallet_settings = TierTemplateSettingsGoogleWalletSettings.from_dict(_google_wallet_settings)

        tier_template_settings = cls(
            default=default,
            card_expiry=card_expiry,
            colours=colours,
            images=images,
            barcode=barcode,
            locations=locations,
            links=links,
            data_fields=data_fields,
            google_wallet_settings=google_wallet_settings,
        )

        tier_template_settings.additional_properties = d
        return tier_template_settings

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
