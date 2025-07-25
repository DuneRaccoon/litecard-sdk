from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ui_config import UIConfig


T = TypeVar("T", bound="WelcomeDetailsResponse")


@_attrs_define
class WelcomeDetailsResponse:
    """Download Urls for welcome page

    Attributes:
        download_id (str): DownloadId used for landing page Example: V1StGXR8_Z5jdHi6B-myT.
        apple_link (str): Link to apple pass Example: https://litecard-demo-pkpass.s3-ap-
            southeast-2.amazonaws.com/coldbrew.pkpass.
        google_link (str): Link to google pass Example: https://pay.google.com/gp/v/save/eyJhbGciOiJSUzI1NiIsInR5cCI6Ikp
            XVCJ9.eyJpc3MiOiJsaXRlY2FyZC10ZXN0QGNsZXZlci1hYmJleS0zMDg1MDcuaWFtLmdzZXJ2aWNlYWNjb3VudC5jb20iLCJhdWQiOiJnb29nbG
            UiLCJ0eXAiOiJzYXZldG9hbmRyb2lkcGF5IiwiaWF0IjoxNjIwMTE0NDkxLCJwYXlsb2FkIjp7ImxveWFsdHlPYmplY3RzIjpbeyJpZCI6IjMzOD
            gwMDAwMDAwMTA2MDYyNDEuTE9ZQUxUWV9PQkpFQ1RfNTRkYmMwNTUtOWRlMy00YWZjLTg0YmUtZDhiNTZjN2U5Mzc5IiwiY2xhc3NJZCI6IjMzOD
            gwMDAwMDAwMTA2MDYyNDEuTE9ZQUxUWV9DTEFTU185OTliOTVlYi00ZDVjLTQzZDEtOGFhOC05Zjg1ZjI0YzlmODQiLCJzdGF0ZSI6IkFDVElWRS
            IsImFjY291bnROYW1lIjoiSmFzb24iLCJhY2NvdW50SWQiOiIxMjMxMjMiLCJiYXJjb2RlIjp7ImFsdGVybmF0ZVRleHQiOiIxMjMxMjMiLCJ2YW
            x1ZSI6IjEyMzEyMyIsInR5cGUiOiJDT0RFXzEyOCJ9LCJsb2NhdGlvbnMiOlt7ImxhdGl0dWRlIjoiLTM3LjgwNjIzMTU2ODQyODgxIiwibG9uZ2
            l0dWRlIjoiMTQ0Ljk4OTkwMjQwODE0ODcifV0sInZhbGlkVGltZUludGVydmFsIjp7InN0YXJ0Ijp7ImRhdGUiOiIyMDIxLTA0LTIwVDAwOjAwOj
            AwLjAwKzEwOjAwIn0sImVuZCI6eyJkYXRlIjoiMjAyNS0wNC0yMFQyMzo1OTowMC4wMCsxMDowMCJ9fSwibGlua3NNb2R1bGVEYXRhIjp7InVyaX
            MiOlt7InVyaSI6InRlbDo2NTA1NTU1NTU1IiwiZGVzY3JpcHRpb24iOiJNb2JpbGUgTnVtYmVyIn0seyJ1cmkiOiJtYWlsdG86am9obmRvZUBsaX
            RlY2FyZC5jb20uYXUiLCJkZXNjcmlwdGlvbiI6IkVtYWlsIn1dfX1dfSwib3JpZ2lucyI6WyJodHRwOi8vbG9jYWxob3N0OjgwODAiXX0.bR5nSN
            qMPH6KUwiaqMP-E-nlyjzllOR9-rxUCVgPhqvra_qZ54kc3ZHX64LyViABgSbLIqFEG_EsfA9FCVunAs3ikr1yB5Tk3WiwQ13zt-
            rH7443_XTI078mtzESl930AL5mVhyrteTMfrhHHV0rrzChXDPgqBjPzsaqs4oGIeW7bVu7S1SC_M8EC-pxTUwqkvvv17xpBVBY_BKzDaK1uEykqd
            Qp2XFHjjRT_esBc6xbiMTDGz11sp395v0RO-9jpp4z-L5igi7prFDgm7ZWBcbSZSKMBckp1lzctLIZ3jidJ9pg-
            lwgaZyyksmWWnDkVFKE0CWAQV3wFg6M2PXXyA.
        barcode_link (Union[Unset, str]): Link to Barcode image Example: https://example.com/blah.
        samsung_link (Union[Unset, str]): Link to samsung pass Example:
            https://a.swallet.link/atw/656147182764415319#Clip?pdata=sIgHCzIwM9g.
        ui_config (Union[Unset, UIConfig]): Configuration for the UI
        disable_qr (Union[Unset, bool]): Disable QR code on Welcome Page Example: True.
    """

    download_id: str
    apple_link: str
    google_link: str
    barcode_link: Union[Unset, str] = UNSET
    samsung_link: Union[Unset, str] = UNSET
    ui_config: Union[Unset, "UIConfig"] = UNSET
    disable_qr: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        download_id = self.download_id

        apple_link = self.apple_link

        google_link = self.google_link

        barcode_link = self.barcode_link

        samsung_link = self.samsung_link

        ui_config: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.ui_config, Unset):
            ui_config = self.ui_config.to_dict()

        disable_qr = self.disable_qr

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "downloadId": download_id,
                "appleLink": apple_link,
                "googleLink": google_link,
            }
        )
        if barcode_link is not UNSET:
            field_dict["barcodeLink"] = barcode_link
        if samsung_link is not UNSET:
            field_dict["samsungLink"] = samsung_link
        if ui_config is not UNSET:
            field_dict["uiConfig"] = ui_config
        if disable_qr is not UNSET:
            field_dict["disableQR"] = disable_qr

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ui_config import UIConfig

        d = dict(src_dict)
        download_id = d.pop("downloadId")

        apple_link = d.pop("appleLink")

        google_link = d.pop("googleLink")

        barcode_link = d.pop("barcodeLink", UNSET)

        samsung_link = d.pop("samsungLink", UNSET)

        _ui_config = d.pop("uiConfig", UNSET)
        ui_config: Union[Unset, UIConfig]
        if isinstance(_ui_config, Unset):
            ui_config = UNSET
        else:
            ui_config = UIConfig.from_dict(_ui_config)

        disable_qr = d.pop("disableQR", UNSET)

        welcome_details_response = cls(
            download_id=download_id,
            apple_link=apple_link,
            google_link=google_link,
            barcode_link=barcode_link,
            samsung_link=samsung_link,
            ui_config=ui_config,
            disable_qr=disable_qr,
        )

        welcome_details_response.additional_properties = d
        return welcome_details_response

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
