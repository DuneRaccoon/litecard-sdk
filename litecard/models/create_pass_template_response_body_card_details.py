from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreatePassTemplateResponseBodyCardDetails")


@_attrs_define
class CreatePassTemplateResponseBodyCardDetails:
    """
    Attributes:
        card_id (Union[Unset, str]): Id of created card Example: abc123.
        card_owner_id (Union[Unset, str]): Id of created card owner Example: efg345.
        download_id (Union[Unset, str]): Id used for hosted litecard landing page e.g.
            https://app.dev.litecard.io/welcome/?id=5c_Wc9h-WCng0oxe8nHNn Example: 5c_Wc9h-WCng0oxe8nHNn.
        apple_link (Union[Unset, str]): URL apple wallet card Example: https://litecard-demo-pkpass.s3-ap-
            southeast-2.amazonaws.com/coldbrew.pkpass.
        google_link (Union[Unset, str]): URL google wallet card Example: https://pay.google.com/gp/v/save/eyJhbGciOiJSUz
            I1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJsaXRlY2FyZC10ZXN0QGNsZXZlci1hYmJleS0zMDg1MDcuaWFtLmdzZXJ2aWNlYWNjb3VudC5jb20iL
            CJhdWQiOiJnb29nbGUiLCJ0eXAiOiJzYXZldG9hbmRyb2lkcGF5IiwiaWF0IjoxNjIwMTE0NDkxLCJwYXlsb2FkIjp7ImxveWFsdHlPYmplY3RzI
            jpbeyJpZCI6IjMzODgwMDAwMDAwMTA2MDYyNDEuTE9ZQUxUWV9PQkpFQ1RfNTRkYmMwNTUtOWRlMy00YWZjLTg0YmUtZDhiNTZjN2U5Mzc5IiwiY
            2xhc3NJZCI6IjMzODgwMDAwMDAwMTA2MDYyNDEuTE9ZQUxUWV9DTEFTU185OTliOTVlYi00ZDVjLTQzZDEtOGFhOC05Zjg1ZjI0YzlmODQiLCJzd
            GF0ZSI6IkFDVElWRSIsImFjY291bnROYW1lIjoiSmFzb24iLCJhY2NvdW50SWQiOiIxMjMxMjMiLCJiYXJjb2RlIjp7ImFsdGVybmF0ZVRleHQiO
            iIxMjMxMjMiLCJ2YWx1ZSI6IjEyMzEyMyIsInR5cGUiOiJDT0RFXzEyOCJ9LCJsb2NhdGlvbnMiOlt7ImxhdGl0dWRlIjoiLTM3LjgwNjIzMTU2O
            DQyODgxIiwibG9uZ2l0dWRlIjoiMTQ0Ljk4OTkwMjQwODE0ODcifV0sInZhbGlkVGltZUludGVydmFsIjp7InN0YXJ0Ijp7ImRhdGUiOiIyMDIxL
            TA0LTIwVDAwOjAwOjAwLjAwKzEwOjAwIn0sImVuZCI6eyJkYXRlIjoiMjAyNS0wNC0yMFQyMzo1OTowMC4wMCsxMDowMCJ9fSwibGlua3NNb2R1b
            GVEYXRhIjp7InVyaXMiOlt7InVyaSI6InRlbDo2NTA1NTU1NTU1IiwiZGVzY3JpcHRpb24iOiJNb2JpbGUgTnVtYmVyIn0seyJ1cmkiOiJtYWlsd
            G86am9obmRvZUBsaXRlY2FyZC5jb20uYXUiLCJkZXNjcmlwdGlvbiI6IkVtYWlsIn1dfX1dfSwib3JpZ2lucyI6WyJodHRwOi8vbG9jYWxob3N0O
            jgwODAiXX0.bR5nSNqMPH6KUwiaqMP-E-
            nlyjzllOR9-rxUCVgPhqvra_qZ54kc3ZHX64LyViABgSbLIqFEG_EsfA9FCVunAs3ikr1yB5Tk3WiwQ13zt-
            rH7443_XTI078mtzESl930AL5mVhyrteTMfrhHHV0rrzChXDPgqBjPzsaqs4oGIeW7bVu7S1SC_M8EC-pxTUwqkvvv17xpBVBY_BKzDaK1uEykqd
            Qp2XFHjjRT_esBc6xbiMTDGz11sp395v0RO-9jpp4z-L5igi7prFDgm7ZWBcbSZSKMBckp1lzctLIZ3jidJ9pg-
            lwgaZyyksmWWnDkVFKE0CWAQV3wFg6M2PXXyA.
        payment_required (Union[Unset, bool]): Require payment after form submission
    """

    card_id: Union[Unset, str] = UNSET
    card_owner_id: Union[Unset, str] = UNSET
    download_id: Union[Unset, str] = UNSET
    apple_link: Union[Unset, str] = UNSET
    google_link: Union[Unset, str] = UNSET
    payment_required: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        card_id = self.card_id

        card_owner_id = self.card_owner_id

        download_id = self.download_id

        apple_link = self.apple_link

        google_link = self.google_link

        payment_required = self.payment_required

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if card_id is not UNSET:
            field_dict["cardId"] = card_id
        if card_owner_id is not UNSET:
            field_dict["cardOwnerId"] = card_owner_id
        if download_id is not UNSET:
            field_dict["downloadId"] = download_id
        if apple_link is not UNSET:
            field_dict["appleLink"] = apple_link
        if google_link is not UNSET:
            field_dict["googleLink"] = google_link
        if payment_required is not UNSET:
            field_dict["paymentRequired"] = payment_required

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        card_id = d.pop("cardId", UNSET)

        card_owner_id = d.pop("cardOwnerId", UNSET)

        download_id = d.pop("downloadId", UNSET)

        apple_link = d.pop("appleLink", UNSET)

        google_link = d.pop("googleLink", UNSET)

        payment_required = d.pop("paymentRequired", UNSET)

        create_pass_template_response_body_card_details = cls(
            card_id=card_id,
            card_owner_id=card_owner_id,
            download_id=download_id,
            apple_link=apple_link,
            google_link=google_link,
            payment_required=payment_required,
        )

        create_pass_template_response_body_card_details.additional_properties = d
        return create_pass_template_response_body_card_details

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
