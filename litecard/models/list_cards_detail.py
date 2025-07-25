from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.list_cards_detail_data_fields import ListCardsDetailDataFields


T = TypeVar("T", bound="ListCardsDetail")


@_attrs_define
class ListCardsDetail:
    """Fields that are returned for each passId

    Attributes:
        id (str): Id of the card Example: -jJWhjZ1a.
        account_name (str): Name associated with the pass Example: John Doe.
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
        template_id (str): Template id of the card Example: rnb-patron.
        form_id (str): Id for field input form Example: 00000001.
        card_owner_id (str): Card owner Id Example: eJoGyeOMcyd1jnfPSuTvH.
        download_id (Union[Unset, str]): DownloadId used for landing page Example: V1StGXR8_Z5jdHi6B-myT.
        barcode_value (Union[Unset, str]): Barcode Value of the Card Example: eqdu4VjAHVW1qv4I_TwMA.
        pass_type (Union[Unset, str]): Pass Type Example: VISIT.
        data_fields (Union[Unset, ListCardsDetailDataFields]): Data Fields of the pass
    """

    id: str
    account_name: str
    apple_link: str
    google_link: str
    template_id: str
    form_id: str
    card_owner_id: str
    download_id: Union[Unset, str] = UNSET
    barcode_value: Union[Unset, str] = UNSET
    pass_type: Union[Unset, str] = UNSET
    data_fields: Union[Unset, "ListCardsDetailDataFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        account_name = self.account_name

        apple_link = self.apple_link

        google_link = self.google_link

        template_id = self.template_id

        form_id = self.form_id

        card_owner_id = self.card_owner_id

        download_id = self.download_id

        barcode_value = self.barcode_value

        pass_type = self.pass_type

        data_fields: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.data_fields, Unset):
            data_fields = self.data_fields.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "accountName": account_name,
                "appleLink": apple_link,
                "googleLink": google_link,
                "templateId": template_id,
                "formId": form_id,
                "cardOwnerId": card_owner_id,
            }
        )
        if download_id is not UNSET:
            field_dict["downloadId"] = download_id
        if barcode_value is not UNSET:
            field_dict["barcodeValue"] = barcode_value
        if pass_type is not UNSET:
            field_dict["passType"] = pass_type
        if data_fields is not UNSET:
            field_dict["dataFields"] = data_fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_cards_detail_data_fields import ListCardsDetailDataFields

        d = dict(src_dict)
        id = d.pop("id")

        account_name = d.pop("accountName")

        apple_link = d.pop("appleLink")

        google_link = d.pop("googleLink")

        template_id = d.pop("templateId")

        form_id = d.pop("formId")

        card_owner_id = d.pop("cardOwnerId")

        download_id = d.pop("downloadId", UNSET)

        barcode_value = d.pop("barcodeValue", UNSET)

        pass_type = d.pop("passType", UNSET)

        _data_fields = d.pop("dataFields", UNSET)
        data_fields: Union[Unset, ListCardsDetailDataFields]
        if isinstance(_data_fields, Unset):
            data_fields = UNSET
        else:
            data_fields = ListCardsDetailDataFields.from_dict(_data_fields)

        list_cards_detail = cls(
            id=id,
            account_name=account_name,
            apple_link=apple_link,
            google_link=google_link,
            template_id=template_id,
            form_id=form_id,
            card_owner_id=card_owner_id,
            download_id=download_id,
            barcode_value=barcode_value,
            pass_type=pass_type,
            data_fields=data_fields,
        )

        list_cards_detail.additional_properties = d
        return list_cards_detail

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
