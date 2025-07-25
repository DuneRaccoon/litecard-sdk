from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TierTemplateSettingsGoogleWalletSettings")


@_attrs_define
class TierTemplateSettingsGoogleWalletSettings:
    """Google Wallet Settings for the tier

    Attributes:
        title (Union[Unset, str]): Text that appears beside your logo on the pass Example: Litecard.
        header (Union[Unset, str]): Text that appears within your pass before expanding Example: Your membership Pass.
        sub_header (Union[Unset, str]): The Label for the header section Example: Welcome!.
    """

    title: Union[Unset, str] = UNSET
    header: Union[Unset, str] = UNSET
    sub_header: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        header = self.header

        sub_header = self.sub_header

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if header is not UNSET:
            field_dict["header"] = header
        if sub_header is not UNSET:
            field_dict["subHeader"] = sub_header

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        title = d.pop("title", UNSET)

        header = d.pop("header", UNSET)

        sub_header = d.pop("subHeader", UNSET)

        tier_template_settings_google_wallet_settings = cls(
            title=title,
            header=header,
            sub_header=sub_header,
        )

        tier_template_settings_google_wallet_settings.additional_properties = d
        return tier_template_settings_google_wallet_settings

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
