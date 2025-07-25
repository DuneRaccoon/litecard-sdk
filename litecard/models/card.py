from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.card_status import CardStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.card_card_owner_copy import CardCardOwnerCopy
    from ..models.card_data_fields import CardDataFields


T = TypeVar("T", bound="Card")


@_attrs_define
class Card:
    """
    Attributes:
        template_id (str): Id for the template used to create the card Example: test_business.
        form_id (str): Id for field input form Example: 00000001.
        id (Union[Unset, str]): ID of the Pass Example: 7048582966.
        download_id (Union[Unset, str]): DownloadId used for landing page Example: V1StGXR8_Z5jdHi6B-myT.
        apple_link (Union[Unset, str]): Url for the apple pass Example: https://litecard-demo-pkpass.s3-ap-
            southeast-2.amazonaws.com/coldbrew.pkpass.
        business_id (Union[Unset, str]): ID of the Business Example: business123.
        user_type (Union[Unset, str]): Type of User Example: employee.
        created_at (Union[Unset, str]): Date Time card was created Example: 2021-11-05T04:25:42.676Z.
        google_pass_id (Union[Unset, str]): Id of google pass Example: 1231244.
        auth_token (Union[Unset, str]): Internal Use Only. Apple Device Auth Token Example: dscxdsf234.
        pass_type (Union[Unset, str]): Mobile wallet pass type Example: VISIT.
        google_link (Union[Unset, str]): Url of google pass Example: https://pay.google.com....
        samsung_link (Union[Unset, str]): Url of samsung pass Example:
            https://a.swallet.link/atw/656147182764415319#Clip?pdata=sIgHCzIwM9g.
        data_fields (Union[Unset, CardDataFields]):
        updated_at (Union[Unset, str]):  Example: 2021-11-05T04:25:42.676Z.
        pk_pass_id (Union[Unset, str]): Id of Apple Pass Example: pass.au.com.litecard.dev.q124234.
        barcode_value (Union[Unset, str]): what the barcode value is Example: 5434435.
        apple_status (Union[Unset, str]): Status of card inside of Apple Wallet Example: ACTIVE.
        google_status (Union[Unset, str]): Status of card inside of Google Wallet Example: INACTIVE.
        card_owner_id (Union[Unset, str]): Id of the card owner Example: asb123.
        status (Union[Unset, CardStatus]): Activation Status of the card Example: INACTIVE.
        expiry (Union[Unset, str]): Expiry of card, in ISO-8601 format Example: 2021-08-11T03:15:56.860Z.
        barcode_link (Union[Unset, str]): Link to the barcode image Example: https://example.com/blah.png.
        card_owner_copy (Union[Unset, CardCardOwnerCopy]): A copy of the card owner's information
        disable_qr (Union[Unset, bool]): Disable QR code on Welcome Page Example: True.
        stripe_customer_id (Union[Unset, str]): stripeCustomerId for subscription passes Example: str_123.
        disable_download (Union[Unset, bool]): Disable download link if pass is already activated. Default: false
            Example: True.
    """

    template_id: str
    form_id: str
    id: Union[Unset, str] = UNSET
    download_id: Union[Unset, str] = UNSET
    apple_link: Union[Unset, str] = UNSET
    business_id: Union[Unset, str] = UNSET
    user_type: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    google_pass_id: Union[Unset, str] = UNSET
    auth_token: Union[Unset, str] = UNSET
    pass_type: Union[Unset, str] = UNSET
    google_link: Union[Unset, str] = UNSET
    samsung_link: Union[Unset, str] = UNSET
    data_fields: Union[Unset, "CardDataFields"] = UNSET
    updated_at: Union[Unset, str] = UNSET
    pk_pass_id: Union[Unset, str] = UNSET
    barcode_value: Union[Unset, str] = UNSET
    apple_status: Union[Unset, str] = UNSET
    google_status: Union[Unset, str] = UNSET
    card_owner_id: Union[Unset, str] = UNSET
    status: Union[Unset, CardStatus] = UNSET
    expiry: Union[Unset, str] = UNSET
    barcode_link: Union[Unset, str] = UNSET
    card_owner_copy: Union[Unset, "CardCardOwnerCopy"] = UNSET
    disable_qr: Union[Unset, bool] = UNSET
    stripe_customer_id: Union[Unset, str] = UNSET
    disable_download: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        template_id = self.template_id

        form_id = self.form_id

        id = self.id

        download_id = self.download_id

        apple_link = self.apple_link

        business_id = self.business_id

        user_type = self.user_type

        created_at = self.created_at

        google_pass_id = self.google_pass_id

        auth_token = self.auth_token

        pass_type = self.pass_type

        google_link = self.google_link

        samsung_link = self.samsung_link

        data_fields: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.data_fields, Unset):
            data_fields = self.data_fields.to_dict()

        updated_at = self.updated_at

        pk_pass_id = self.pk_pass_id

        barcode_value = self.barcode_value

        apple_status = self.apple_status

        google_status = self.google_status

        card_owner_id = self.card_owner_id

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        expiry = self.expiry

        barcode_link = self.barcode_link

        card_owner_copy: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.card_owner_copy, Unset):
            card_owner_copy = self.card_owner_copy.to_dict()

        disable_qr = self.disable_qr

        stripe_customer_id = self.stripe_customer_id

        disable_download = self.disable_download

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "templateId": template_id,
                "formId": form_id,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if download_id is not UNSET:
            field_dict["downloadId"] = download_id
        if apple_link is not UNSET:
            field_dict["appleLink"] = apple_link
        if business_id is not UNSET:
            field_dict["businessId"] = business_id
        if user_type is not UNSET:
            field_dict["userType"] = user_type
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if google_pass_id is not UNSET:
            field_dict["googlePassId"] = google_pass_id
        if auth_token is not UNSET:
            field_dict["authToken"] = auth_token
        if pass_type is not UNSET:
            field_dict["passType"] = pass_type
        if google_link is not UNSET:
            field_dict["googleLink"] = google_link
        if samsung_link is not UNSET:
            field_dict["samsungLink"] = samsung_link
        if data_fields is not UNSET:
            field_dict["dataFields"] = data_fields
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if pk_pass_id is not UNSET:
            field_dict["pkPassId"] = pk_pass_id
        if barcode_value is not UNSET:
            field_dict["barcodeValue"] = barcode_value
        if apple_status is not UNSET:
            field_dict["appleStatus"] = apple_status
        if google_status is not UNSET:
            field_dict["googleStatus"] = google_status
        if card_owner_id is not UNSET:
            field_dict["cardOwnerId"] = card_owner_id
        if status is not UNSET:
            field_dict["status"] = status
        if expiry is not UNSET:
            field_dict["expiry"] = expiry
        if barcode_link is not UNSET:
            field_dict["barcodeLink"] = barcode_link
        if card_owner_copy is not UNSET:
            field_dict["cardOwnerCopy"] = card_owner_copy
        if disable_qr is not UNSET:
            field_dict["disableQR"] = disable_qr
        if stripe_customer_id is not UNSET:
            field_dict["stripeCustomerId"] = stripe_customer_id
        if disable_download is not UNSET:
            field_dict["disableDownload"] = disable_download

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.card_card_owner_copy import CardCardOwnerCopy
        from ..models.card_data_fields import CardDataFields

        d = dict(src_dict)
        template_id = d.pop("templateId")

        form_id = d.pop("formId")

        id = d.pop("id", UNSET)

        download_id = d.pop("downloadId", UNSET)

        apple_link = d.pop("appleLink", UNSET)

        business_id = d.pop("businessId", UNSET)

        user_type = d.pop("userType", UNSET)

        created_at = d.pop("createdAt", UNSET)

        google_pass_id = d.pop("googlePassId", UNSET)

        auth_token = d.pop("authToken", UNSET)

        pass_type = d.pop("passType", UNSET)

        google_link = d.pop("googleLink", UNSET)

        samsung_link = d.pop("samsungLink", UNSET)

        _data_fields = d.pop("dataFields", UNSET)
        data_fields: Union[Unset, CardDataFields]
        if isinstance(_data_fields, Unset):
            data_fields = UNSET
        else:
            data_fields = CardDataFields.from_dict(_data_fields)

        updated_at = d.pop("updatedAt", UNSET)

        pk_pass_id = d.pop("pkPassId", UNSET)

        barcode_value = d.pop("barcodeValue", UNSET)

        apple_status = d.pop("appleStatus", UNSET)

        google_status = d.pop("googleStatus", UNSET)

        card_owner_id = d.pop("cardOwnerId", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, CardStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = CardStatus(_status)

        expiry = d.pop("expiry", UNSET)

        barcode_link = d.pop("barcodeLink", UNSET)

        _card_owner_copy = d.pop("cardOwnerCopy", UNSET)
        card_owner_copy: Union[Unset, CardCardOwnerCopy]
        if isinstance(_card_owner_copy, Unset):
            card_owner_copy = UNSET
        else:
            card_owner_copy = CardCardOwnerCopy.from_dict(_card_owner_copy)

        disable_qr = d.pop("disableQR", UNSET)

        stripe_customer_id = d.pop("stripeCustomerId", UNSET)

        disable_download = d.pop("disableDownload", UNSET)

        card = cls(
            template_id=template_id,
            form_id=form_id,
            id=id,
            download_id=download_id,
            apple_link=apple_link,
            business_id=business_id,
            user_type=user_type,
            created_at=created_at,
            google_pass_id=google_pass_id,
            auth_token=auth_token,
            pass_type=pass_type,
            google_link=google_link,
            samsung_link=samsung_link,
            data_fields=data_fields,
            updated_at=updated_at,
            pk_pass_id=pk_pass_id,
            barcode_value=barcode_value,
            apple_status=apple_status,
            google_status=google_status,
            card_owner_id=card_owner_id,
            status=status,
            expiry=expiry,
            barcode_link=barcode_link,
            card_owner_copy=card_owner_copy,
            disable_qr=disable_qr,
            stripe_customer_id=stripe_customer_id,
            disable_download=disable_download,
        )

        card.additional_properties = d
        return card

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
