from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.template_apple_wallet_settings_v1_pass_type import TemplateAppleWalletSettingsV1PassType
from ..types import UNSET, Unset

T = TypeVar("T", bound="TemplateAppleWalletSettingsV1")


@_attrs_define
class TemplateAppleWalletSettingsV1:
    """Settings specific to apple wallet

    Attributes:
        pass_type (TemplateAppleWalletSettingsV1PassType): Apple wallet card type Example: STORE_CARD.
        hide_logo (Union[Unset, bool]): Hides the logo in the top right of apple wallet cards
        hide_logo_text (Union[Unset, bool]): Hides logo text in the top right of apple wallet cards
        disable_sharing (Union[Unset, bool]): Disables the share button on the apple pass. This does not stop the user
            from taking a screenshot and sharing the pass details.
    """

    pass_type: TemplateAppleWalletSettingsV1PassType
    hide_logo: Union[Unset, bool] = UNSET
    hide_logo_text: Union[Unset, bool] = UNSET
    disable_sharing: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pass_type = self.pass_type.value

        hide_logo = self.hide_logo

        hide_logo_text = self.hide_logo_text

        disable_sharing = self.disable_sharing

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "passType": pass_type,
            }
        )
        if hide_logo is not UNSET:
            field_dict["hideLogo"] = hide_logo
        if hide_logo_text is not UNSET:
            field_dict["hideLogoText"] = hide_logo_text
        if disable_sharing is not UNSET:
            field_dict["disableSharing"] = disable_sharing

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        pass_type = TemplateAppleWalletSettingsV1PassType(d.pop("passType"))

        hide_logo = d.pop("hideLogo", UNSET)

        hide_logo_text = d.pop("hideLogoText", UNSET)

        disable_sharing = d.pop("disableSharing", UNSET)

        template_apple_wallet_settings_v1 = cls(
            pass_type=pass_type,
            hide_logo=hide_logo,
            hide_logo_text=hide_logo_text,
            disable_sharing=disable_sharing,
        )

        template_apple_wallet_settings_v1.additional_properties = d
        return template_apple_wallet_settings_v1

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
