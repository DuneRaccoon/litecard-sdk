from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="UIPageSchema")


@_attrs_define
class UIPageSchema:
    """
    Attributes:
        logo_url (Union[Unset, str]): URL of the logo Example: https://host/logo.jpg.
        disable_qr_code (Union[Unset, bool]): Disable QR code
        redirect_url (Union[Unset, str]): URL to redirect to after sign up Example: https://host/redirect.
        auto_download_text (Union[Unset, str]): Text for the qrRedirect screen Example: Your download should start
            automatically. Alternatively you can start the download below..
        or_text (Union[Unset, str]): OR text for the qrRedirect screen Example: OR.
        qr_text (Union[Unset, str]): Text for the directing the user to scan the QR code Example: Add to wallet by
            scanning the QR code.
        footer_text (Union[Unset, str]): Text for the directing the user to scan the QR code Example: This QR code is a
            link to download your digital pass, not the pass itself..
        background_colour (Union[Unset, str]): Background colour of the page Example: #FFFFFF.
        text_colour (Union[Unset, str]): Text colour of the page Example: #000000.
        favicon_path (Union[Unset, str]): Path to the favicon image Example: /path/to/favicon.ico.
        document_title (Union[Unset, str]): Title of the document Example: Please enter your title.
    """

    logo_url: Union[Unset, str] = UNSET
    disable_qr_code: Union[Unset, bool] = UNSET
    redirect_url: Union[Unset, str] = UNSET
    auto_download_text: Union[Unset, str] = UNSET
    or_text: Union[Unset, str] = UNSET
    qr_text: Union[Unset, str] = UNSET
    footer_text: Union[Unset, str] = UNSET
    background_colour: Union[Unset, str] = UNSET
    text_colour: Union[Unset, str] = UNSET
    favicon_path: Union[Unset, str] = UNSET
    document_title: Union[Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        logo_url = self.logo_url

        disable_qr_code = self.disable_qr_code

        redirect_url = self.redirect_url

        auto_download_text = self.auto_download_text

        or_text = self.or_text

        qr_text = self.qr_text

        footer_text = self.footer_text

        background_colour = self.background_colour

        text_colour = self.text_colour

        favicon_path = self.favicon_path

        document_title = self.document_title

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if logo_url is not UNSET:
            field_dict["logoUrl"] = logo_url
        if disable_qr_code is not UNSET:
            field_dict["disableQRCode"] = disable_qr_code
        if redirect_url is not UNSET:
            field_dict["redirectUrl"] = redirect_url
        if auto_download_text is not UNSET:
            field_dict["autoDownloadText"] = auto_download_text
        if or_text is not UNSET:
            field_dict["orText"] = or_text
        if qr_text is not UNSET:
            field_dict["qrText"] = qr_text
        if footer_text is not UNSET:
            field_dict["footerText"] = footer_text
        if background_colour is not UNSET:
            field_dict["backgroundColour"] = background_colour
        if text_colour is not UNSET:
            field_dict["textColour"] = text_colour
        if favicon_path is not UNSET:
            field_dict["faviconPath"] = favicon_path
        if document_title is not UNSET:
            field_dict["documentTitle"] = document_title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        logo_url = d.pop("logoUrl", UNSET)

        disable_qr_code = d.pop("disableQRCode", UNSET)

        redirect_url = d.pop("redirectUrl", UNSET)

        auto_download_text = d.pop("autoDownloadText", UNSET)

        or_text = d.pop("orText", UNSET)

        qr_text = d.pop("qrText", UNSET)

        footer_text = d.pop("footerText", UNSET)

        background_colour = d.pop("backgroundColour", UNSET)

        text_colour = d.pop("textColour", UNSET)

        favicon_path = d.pop("faviconPath", UNSET)

        document_title = d.pop("documentTitle", UNSET)

        ui_page_schema = cls(
            logo_url=logo_url,
            disable_qr_code=disable_qr_code,
            redirect_url=redirect_url,
            auto_download_text=auto_download_text,
            or_text=or_text,
            qr_text=qr_text,
            footer_text=footer_text,
            background_colour=background_colour,
            text_colour=text_colour,
            favicon_path=favicon_path,
            document_title=document_title,
        )

        return ui_page_schema
