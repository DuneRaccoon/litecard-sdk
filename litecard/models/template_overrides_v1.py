from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.template_barcode_v1 import TemplateBarcodeV1
    from ..models.template_card_expiry_v1_type_0 import TemplateCardExpiryV1Type0
    from ..models.template_card_expiry_v1_type_1 import TemplateCardExpiryV1Type1
    from ..models.template_card_expiry_v1_type_2 import TemplateCardExpiryV1Type2
    from ..models.template_card_expiry_v1_type_3 import TemplateCardExpiryV1Type3
    from ..models.template_images_v1 import TemplateImagesV1
    from ..models.template_link_v1 import TemplateLinkV1
    from ..models.template_locations_v1_item import TemplateLocationsV1Item


T = TypeVar("T", bound="TemplateOverridesV1")


@_attrs_define
class TemplateOverridesV1:
    """Template Overrides

    Attributes:
        images (Union[Unset, TemplateImagesV1]): Images of the template
        barcode (Union[Unset, TemplateBarcodeV1]): Barcode Fields of the template
        locations (Union[Unset, list['TemplateLocationsV1Item']]): List of locations to be stored on the pass, used by
            Apple for Geo-Location messages. Max of 10 locations for apple passes.
        card_expiry (Union['TemplateCardExpiryV1Type0', 'TemplateCardExpiryV1Type1', 'TemplateCardExpiryV1Type2',
            'TemplateCardExpiryV1Type3', Unset]): Card Expiry field on Template that details how cards created by the
            template will expire
        links (Union[Unset, list['TemplateLinkV1']]): Template Links
    """

    images: Union[Unset, "TemplateImagesV1"] = UNSET
    barcode: Union[Unset, "TemplateBarcodeV1"] = UNSET
    locations: Union[Unset, list["TemplateLocationsV1Item"]] = UNSET
    card_expiry: Union[
        "TemplateCardExpiryV1Type0",
        "TemplateCardExpiryV1Type1",
        "TemplateCardExpiryV1Type2",
        "TemplateCardExpiryV1Type3",
        Unset,
    ] = UNSET
    links: Union[Unset, list["TemplateLinkV1"]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.template_card_expiry_v1_type_0 import TemplateCardExpiryV1Type0
        from ..models.template_card_expiry_v1_type_1 import TemplateCardExpiryV1Type1
        from ..models.template_card_expiry_v1_type_2 import TemplateCardExpiryV1Type2

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

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if images is not UNSET:
            field_dict["images"] = images
        if barcode is not UNSET:
            field_dict["barcode"] = barcode
        if locations is not UNSET:
            field_dict["locations"] = locations
        if card_expiry is not UNSET:
            field_dict["cardExpiry"] = card_expiry
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.template_barcode_v1 import TemplateBarcodeV1
        from ..models.template_card_expiry_v1_type_0 import TemplateCardExpiryV1Type0
        from ..models.template_card_expiry_v1_type_1 import TemplateCardExpiryV1Type1
        from ..models.template_card_expiry_v1_type_2 import TemplateCardExpiryV1Type2
        from ..models.template_card_expiry_v1_type_3 import TemplateCardExpiryV1Type3
        from ..models.template_images_v1 import TemplateImagesV1
        from ..models.template_link_v1 import TemplateLinkV1
        from ..models.template_locations_v1_item import TemplateLocationsV1Item

        d = dict(src_dict)
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

        template_overrides_v1 = cls(
            images=images,
            barcode=barcode,
            locations=locations,
            card_expiry=card_expiry,
            links=links,
        )

        return template_overrides_v1
