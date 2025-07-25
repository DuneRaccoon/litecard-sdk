from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.template_usage_v1_item import TemplateUsageV1Item
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.template_locations_v1_item_apple import TemplateLocationsV1ItemApple
    from ..models.template_locations_v1_item_samsung import TemplateLocationsV1ItemSamsung


T = TypeVar("T", bound="TemplateLocationsV1Item")


@_attrs_define
class TemplateLocationsV1Item:
    """Location

    Attributes:
        id (Union[Unset, str]): Location ID
        lat (Union[Unset, str]): Latitude value Example: -37.8140000.
        lon (Union[Unset, str]): Longitude value Example: 144.9633200.
        apple (Union[Unset, TemplateLocationsV1ItemApple]): Apple specific location fields
        beacon_id (Union[Unset, str]): proximityUUID of the Beacon. This is an alternative to long/lat Example:
            F8F589E9-C07E-58B0-AEAB-A36BE4D48FAC.
        samsung (Union[Unset, TemplateLocationsV1ItemSamsung]): Location details
        order (Union[Unset, float]): Order of the locations. The order will be sorted in ascending order e.g. 1,2,3
        usage (Union[Unset, list[TemplateUsageV1Item]]): List of strings to indicate where a field is rendered
    """

    id: Union[Unset, str] = UNSET
    lat: Union[Unset, str] = UNSET
    lon: Union[Unset, str] = UNSET
    apple: Union[Unset, "TemplateLocationsV1ItemApple"] = UNSET
    beacon_id: Union[Unset, str] = UNSET
    samsung: Union[Unset, "TemplateLocationsV1ItemSamsung"] = UNSET
    order: Union[Unset, float] = UNSET
    usage: Union[Unset, list[TemplateUsageV1Item]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        lat = self.lat

        lon = self.lon

        apple: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.apple, Unset):
            apple = self.apple.to_dict()

        beacon_id = self.beacon_id

        samsung: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.samsung, Unset):
            samsung = self.samsung.to_dict()

        order = self.order

        usage: Union[Unset, list[str]] = UNSET
        if not isinstance(self.usage, Unset):
            usage = []
            for componentsschemas_template_usage_v1_item_data in self.usage:
                componentsschemas_template_usage_v1_item = componentsschemas_template_usage_v1_item_data.value
                usage.append(componentsschemas_template_usage_v1_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if lat is not UNSET:
            field_dict["lat"] = lat
        if lon is not UNSET:
            field_dict["lon"] = lon
        if apple is not UNSET:
            field_dict["apple"] = apple
        if beacon_id is not UNSET:
            field_dict["beaconId"] = beacon_id
        if samsung is not UNSET:
            field_dict["samsung"] = samsung
        if order is not UNSET:
            field_dict["order"] = order
        if usage is not UNSET:
            field_dict["usage"] = usage

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.template_locations_v1_item_apple import TemplateLocationsV1ItemApple
        from ..models.template_locations_v1_item_samsung import TemplateLocationsV1ItemSamsung

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        lat = d.pop("lat", UNSET)

        lon = d.pop("lon", UNSET)

        _apple = d.pop("apple", UNSET)
        apple: Union[Unset, TemplateLocationsV1ItemApple]
        if isinstance(_apple, Unset):
            apple = UNSET
        else:
            apple = TemplateLocationsV1ItemApple.from_dict(_apple)

        beacon_id = d.pop("beaconId", UNSET)

        _samsung = d.pop("samsung", UNSET)
        samsung: Union[Unset, TemplateLocationsV1ItemSamsung]
        if isinstance(_samsung, Unset):
            samsung = UNSET
        else:
            samsung = TemplateLocationsV1ItemSamsung.from_dict(_samsung)

        order = d.pop("order", UNSET)

        usage = []
        _usage = d.pop("usage", UNSET)
        for componentsschemas_template_usage_v1_item_data in _usage or []:
            componentsschemas_template_usage_v1_item = TemplateUsageV1Item(
                componentsschemas_template_usage_v1_item_data
            )

            usage.append(componentsschemas_template_usage_v1_item)

        template_locations_v1_item = cls(
            id=id,
            lat=lat,
            lon=lon,
            apple=apple,
            beacon_id=beacon_id,
            samsung=samsung,
            order=order,
            usage=usage,
        )

        template_locations_v1_item.additional_properties = d
        return template_locations_v1_item

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
