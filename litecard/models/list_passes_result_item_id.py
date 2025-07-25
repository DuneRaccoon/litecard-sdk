from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.list_passes_result_item_id_data_fields import ListPassesResultItemIdDataFields


T = TypeVar("T", bound="ListPassesResultItemId")


@_attrs_define
class ListPassesResultItemId:
    """passId

    Example:
        00000001

    Attributes:
        account_name (Union[Unset, str]): Name associated with the pass Example: John Doe.
        download_id (Union[Unset, str]): DownloadId used for landing page Example: V1StGXR8_Z5jdHi6B-myT.
        created_at (Union[Unset, str]): Date when pass was first created, in ISO-8601 format Example:
            2021-07-01T12:13:20.159Z.
        updated_at (Union[Unset, str]): Date when pass was last updated, in ISO-8601 format Example:
            2021-07-08T02:48:50.399Z.
        apple_link (Union[Unset, str]): Link to apple pass Example: https://litecard-demo-pkpass.s3-ap-
            southeast-2.amazonaws.com/coldbrew.pkpass.
        google_link (Union[Unset, str]): Link to google pass Example: https://pay.google.com/gp/v/save/eyJhbGciOiJSUzI1N
            iIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJsaXRlY2FyZC10ZXN0QGNsZXZlci1hYmJleS0zMDg1MDcuaWFtLmdzZXJ2aWNlYWNjb3VudC5jb20iLCJh
            dWQiOiJnb29nbGUiLCJ0eXAiOiJzYXZldG9hbmRyb2lkcGF5IiwiaWF0IjoxNjIwMTE0NDkxLCJwYXlsb2FkIjp7ImxveWFsdHlPYmplY3RzIjpb
            eyJpZCI6IjMzODgwMDAwMDAwMTA2MDYyNDEuTE9ZQUxUWV9PQkpFQ1RfNTRkYmMwNTUtOWRlMy00YWZjLTg0YmUtZDhiNTZjN2U5Mzc5IiwiY2xh
            c3NJZCI6IjMzODgwMDAwMDAwMTA2MDYyNDEuTE9ZQUxUWV9DTEFTU185OTliOTVlYi00ZDVjLTQzZDEtOGFhOC05Zjg1ZjI0YzlmODQiLCJzdGF0
            ZSI6IkFDVElWRSIsImFjY291bnROYW1lIjoiSmFzb24iLCJhY2NvdW50SWQiOiIxMjMxMjMiLCJiYXJjb2RlIjp7ImFsdGVybmF0ZVRleHQiOiIx
            MjMxMjMiLCJ2YWx1ZSI6IjEyMzEyMyIsInR5cGUiOiJDT0RFXzEyOCJ9LCJsb2NhdGlvbnMiOlt7ImxhdGl0dWRlIjoiLTM3LjgwNjIzMTU2ODQy
            ODgxIiwibG9uZ2l0dWRlIjoiMTQ0Ljk4OTkwMjQwODE0ODcifV0sInZhbGlkVGltZUludGVydmFsIjp7InN0YXJ0Ijp7ImRhdGUiOiIyMDIxLTA0
            LTIwVDAwOjAwOjAwLjAwKzEwOjAwIn0sImVuZCI6eyJkYXRlIjoiMjAyNS0wNC0yMFQyMzo1OTowMC4wMCsxMDowMCJ9fSwibGlua3NNb2R1bGVE
            YXRhIjp7InVyaXMiOlt7InVyaSI6InRlbDo2NTA1NTU1NTU1IiwiZGVzY3JpcHRpb24iOiJNb2JpbGUgTnVtYmVyIn0seyJ1cmkiOiJtYWlsdG86
            am9obmRvZUBsaXRlY2FyZC5jb20uYXUiLCJkZXNjcmlwdGlvbiI6IkVtYWlsIn1dfX1dfSwib3JpZ2lucyI6WyJodHRwOi8vbG9jYWxob3N0Ojgw
            ODAiXX0.bR5nSNqMPH6KUwiaqMP-E-
            nlyjzllOR9-rxUCVgPhqvra_qZ54kc3ZHX64LyViABgSbLIqFEG_EsfA9FCVunAs3ikr1yB5Tk3WiwQ13zt-
            rH7443_XTI078mtzESl930AL5mVhyrteTMfrhHHV0rrzChXDPgqBjPzsaqs4oGIeW7bVu7S1SC_M8EC-pxTUwqkvvv17xpBVBY_BKzDaK1uEykqd
            Qp2XFHjjRT_esBc6xbiMTDGz11sp395v0RO-9jpp4z-L5igi7prFDgm7ZWBcbSZSKMBckp1lzctLIZ3jidJ9pg-
            lwgaZyyksmWWnDkVFKE0CWAQV3wFg6M2PXXyA.
        data_fields (Union[Unset, ListPassesResultItemIdDataFields]): Data Fields of the pass
        form_id (Union[Unset, str]): Id for field input form Example: form123.
    """

    account_name: Union[Unset, str] = UNSET
    download_id: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    apple_link: Union[Unset, str] = UNSET
    google_link: Union[Unset, str] = UNSET
    data_fields: Union[Unset, "ListPassesResultItemIdDataFields"] = UNSET
    form_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_name = self.account_name

        download_id = self.download_id

        created_at = self.created_at

        updated_at = self.updated_at

        apple_link = self.apple_link

        google_link = self.google_link

        data_fields: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.data_fields, Unset):
            data_fields = self.data_fields.to_dict()

        form_id = self.form_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_name is not UNSET:
            field_dict["accountName"] = account_name
        if download_id is not UNSET:
            field_dict["downloadId"] = download_id
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if apple_link is not UNSET:
            field_dict["appleLink"] = apple_link
        if google_link is not UNSET:
            field_dict["googleLink"] = google_link
        if data_fields is not UNSET:
            field_dict["dataFields"] = data_fields
        if form_id is not UNSET:
            field_dict["formId"] = form_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_passes_result_item_id_data_fields import ListPassesResultItemIdDataFields

        d = dict(src_dict)
        account_name = d.pop("accountName", UNSET)

        download_id = d.pop("downloadId", UNSET)

        created_at = d.pop("createdAt", UNSET)

        updated_at = d.pop("updatedAt", UNSET)

        apple_link = d.pop("appleLink", UNSET)

        google_link = d.pop("googleLink", UNSET)

        _data_fields = d.pop("dataFields", UNSET)
        data_fields: Union[Unset, ListPassesResultItemIdDataFields]
        if isinstance(_data_fields, Unset):
            data_fields = UNSET
        else:
            data_fields = ListPassesResultItemIdDataFields.from_dict(_data_fields)

        form_id = d.pop("formId", UNSET)

        list_passes_result_item_id = cls(
            account_name=account_name,
            download_id=download_id,
            created_at=created_at,
            updated_at=updated_at,
            apple_link=apple_link,
            google_link=google_link,
            data_fields=data_fields,
            form_id=form_id,
        )

        list_passes_result_item_id.additional_properties = d
        return list_passes_result_item_id

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
