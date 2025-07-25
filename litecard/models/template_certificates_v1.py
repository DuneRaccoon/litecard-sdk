from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.template_certificates_v1_apple_settings import TemplateCertificatesV1AppleSettings
    from ..models.template_certificates_v1_google_settings import TemplateCertificatesV1GoogleSettings
    from ..models.template_certificates_v1_nfc import TemplateCertificatesV1Nfc


T = TypeVar("T", bound="TemplateCertificatesV1")


@_attrs_define
class TemplateCertificatesV1:
    """
    Attributes:
        apple_settings (Union[Unset, TemplateCertificatesV1AppleSettings]): Apple specific settings
        google_settings (Union[Unset, TemplateCertificatesV1GoogleSettings]): Google specific settings
        nfc (Union[Unset, TemplateCertificatesV1Nfc]): NFC settings
    """

    apple_settings: Union[Unset, "TemplateCertificatesV1AppleSettings"] = UNSET
    google_settings: Union[Unset, "TemplateCertificatesV1GoogleSettings"] = UNSET
    nfc: Union[Unset, "TemplateCertificatesV1Nfc"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        apple_settings: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.apple_settings, Unset):
            apple_settings = self.apple_settings.to_dict()

        google_settings: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.google_settings, Unset):
            google_settings = self.google_settings.to_dict()

        nfc: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.nfc, Unset):
            nfc = self.nfc.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if apple_settings is not UNSET:
            field_dict["appleSettings"] = apple_settings
        if google_settings is not UNSET:
            field_dict["googleSettings"] = google_settings
        if nfc is not UNSET:
            field_dict["nfc"] = nfc

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.template_certificates_v1_apple_settings import TemplateCertificatesV1AppleSettings
        from ..models.template_certificates_v1_google_settings import TemplateCertificatesV1GoogleSettings
        from ..models.template_certificates_v1_nfc import TemplateCertificatesV1Nfc

        d = dict(src_dict)
        _apple_settings = d.pop("appleSettings", UNSET)
        apple_settings: Union[Unset, TemplateCertificatesV1AppleSettings]
        if isinstance(_apple_settings, Unset):
            apple_settings = UNSET
        else:
            apple_settings = TemplateCertificatesV1AppleSettings.from_dict(_apple_settings)

        _google_settings = d.pop("googleSettings", UNSET)
        google_settings: Union[Unset, TemplateCertificatesV1GoogleSettings]
        if isinstance(_google_settings, Unset):
            google_settings = UNSET
        else:
            google_settings = TemplateCertificatesV1GoogleSettings.from_dict(_google_settings)

        _nfc = d.pop("nfc", UNSET)
        nfc: Union[Unset, TemplateCertificatesV1Nfc]
        if isinstance(_nfc, Unset):
            nfc = UNSET
        else:
            nfc = TemplateCertificatesV1Nfc.from_dict(_nfc)

        template_certificates_v1 = cls(
            apple_settings=apple_settings,
            google_settings=google_settings,
            nfc=nfc,
        )

        template_certificates_v1.additional_properties = d
        return template_certificates_v1

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
