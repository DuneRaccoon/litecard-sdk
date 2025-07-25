from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.custom_form_design_background_styles import CustomFormDesignBackgroundStyles
    from ..models.custom_form_design_common_styles import CustomFormDesignCommonStyles
    from ..models.custom_form_design_footer_section import CustomFormDesignFooterSection
    from ..models.custom_form_design_left_section import CustomFormDesignLeftSection
    from ..models.custom_form_design_right_section import CustomFormDesignRightSection


T = TypeVar("T", bound="CustomFormDesignSchema")


@_attrs_define
class CustomFormDesignSchema:
    """Sign-up page configuration object

    Attributes:
        background_styles (CustomFormDesignBackgroundStyles): Background styling options
        left_section (CustomFormDesignLeftSection): Configuration for the left section of the form
        design_type (Union[Unset, float]): design type id Default: 1.0.
        is_public (Union[Unset, bool]): Flag to indicate if the form is public Default: False.
        document_title (Union[Unset, str]): Title of the document Example: Please enter your title.
        favicon_path (Union[Unset, str]): Path to the favicon image Example: /path/to/favicon.ico.
        facebook_url (Union[Unset, str]): URL to the Facebook page Example: https://www.facebook.com/.
        social_links_text (Union[Unset, str]): Text for the social links section Example: SHARE.
        instagram_url (Union[Unset, str]): URL to the Instagram page Example: https://www.instagram.com/.
        redirection_url (Union[Unset, str]): URL to redirect to after sign up Example: https://www.example.com.
        terms_and_conditions_url (Union[Unset, str]): URL to the terms and conditions Example:
            https://www.example.com/terms.
        terms_link_text (Union[Unset, str]): Text for the terms and conditions link Example: Terms and Conditions.
        home_page_url (Union[Unset, str]): URL to the home page Example: https://www.example.com.
        success_submission_message (Union[Unset, str]): Message displayed on successful form submission Example: Thank
            you for signing up!.
        disable_success_submission_message (Union[Unset, bool]): Flag to disable the success submission message
        right_section (Union[Unset, CustomFormDesignRightSection]): Configuration for the right section of the form
        common_styles (Union[Unset, CustomFormDesignCommonStyles]): Common styles applied throughout the form
        footer_section (Union[Unset, CustomFormDesignFooterSection]): Configuration for the footer section of the form
    """

    background_styles: "CustomFormDesignBackgroundStyles"
    left_section: "CustomFormDesignLeftSection"
    design_type: Union[Unset, float] = 1.0
    is_public: Union[Unset, bool] = False
    document_title: Union[Unset, str] = UNSET
    favicon_path: Union[Unset, str] = UNSET
    facebook_url: Union[Unset, str] = UNSET
    social_links_text: Union[Unset, str] = UNSET
    instagram_url: Union[Unset, str] = UNSET
    redirection_url: Union[Unset, str] = UNSET
    terms_and_conditions_url: Union[Unset, str] = UNSET
    terms_link_text: Union[Unset, str] = UNSET
    home_page_url: Union[Unset, str] = UNSET
    success_submission_message: Union[Unset, str] = UNSET
    disable_success_submission_message: Union[Unset, bool] = UNSET
    right_section: Union[Unset, "CustomFormDesignRightSection"] = UNSET
    common_styles: Union[Unset, "CustomFormDesignCommonStyles"] = UNSET
    footer_section: Union[Unset, "CustomFormDesignFooterSection"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        background_styles = self.background_styles.to_dict()

        left_section = self.left_section.to_dict()

        design_type = self.design_type

        is_public = self.is_public

        document_title = self.document_title

        favicon_path = self.favicon_path

        facebook_url = self.facebook_url

        social_links_text = self.social_links_text

        instagram_url = self.instagram_url

        redirection_url = self.redirection_url

        terms_and_conditions_url = self.terms_and_conditions_url

        terms_link_text = self.terms_link_text

        home_page_url = self.home_page_url

        success_submission_message = self.success_submission_message

        disable_success_submission_message = self.disable_success_submission_message

        right_section: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.right_section, Unset):
            right_section = self.right_section.to_dict()

        common_styles: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.common_styles, Unset):
            common_styles = self.common_styles.to_dict()

        footer_section: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.footer_section, Unset):
            footer_section = self.footer_section.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "backgroundStyles": background_styles,
                "leftSection": left_section,
            }
        )
        if design_type is not UNSET:
            field_dict["designType"] = design_type
        if is_public is not UNSET:
            field_dict["isPublic"] = is_public
        if document_title is not UNSET:
            field_dict["documentTitle"] = document_title
        if favicon_path is not UNSET:
            field_dict["faviconPath"] = favicon_path
        if facebook_url is not UNSET:
            field_dict["facebookURL"] = facebook_url
        if social_links_text is not UNSET:
            field_dict["socialLinksText"] = social_links_text
        if instagram_url is not UNSET:
            field_dict["instagramURL"] = instagram_url
        if redirection_url is not UNSET:
            field_dict["redirectionURL"] = redirection_url
        if terms_and_conditions_url is not UNSET:
            field_dict["termsAndConditionsURL"] = terms_and_conditions_url
        if terms_link_text is not UNSET:
            field_dict["termsLinkText"] = terms_link_text
        if home_page_url is not UNSET:
            field_dict["homePageURL"] = home_page_url
        if success_submission_message is not UNSET:
            field_dict["successSubmissionMessage"] = success_submission_message
        if disable_success_submission_message is not UNSET:
            field_dict["disableSuccessSubmissionMessage"] = disable_success_submission_message
        if right_section is not UNSET:
            field_dict["rightSection"] = right_section
        if common_styles is not UNSET:
            field_dict["commonStyles"] = common_styles
        if footer_section is not UNSET:
            field_dict["footerSection"] = footer_section

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.custom_form_design_background_styles import CustomFormDesignBackgroundStyles
        from ..models.custom_form_design_common_styles import CustomFormDesignCommonStyles
        from ..models.custom_form_design_footer_section import CustomFormDesignFooterSection
        from ..models.custom_form_design_left_section import CustomFormDesignLeftSection
        from ..models.custom_form_design_right_section import CustomFormDesignRightSection

        d = dict(src_dict)
        background_styles = CustomFormDesignBackgroundStyles.from_dict(d.pop("backgroundStyles"))

        left_section = CustomFormDesignLeftSection.from_dict(d.pop("leftSection"))

        design_type = d.pop("designType", UNSET)

        is_public = d.pop("isPublic", UNSET)

        document_title = d.pop("documentTitle", UNSET)

        favicon_path = d.pop("faviconPath", UNSET)

        facebook_url = d.pop("facebookURL", UNSET)

        social_links_text = d.pop("socialLinksText", UNSET)

        instagram_url = d.pop("instagramURL", UNSET)

        redirection_url = d.pop("redirectionURL", UNSET)

        terms_and_conditions_url = d.pop("termsAndConditionsURL", UNSET)

        terms_link_text = d.pop("termsLinkText", UNSET)

        home_page_url = d.pop("homePageURL", UNSET)

        success_submission_message = d.pop("successSubmissionMessage", UNSET)

        disable_success_submission_message = d.pop("disableSuccessSubmissionMessage", UNSET)

        _right_section = d.pop("rightSection", UNSET)
        right_section: Union[Unset, CustomFormDesignRightSection]
        if isinstance(_right_section, Unset):
            right_section = UNSET
        else:
            right_section = CustomFormDesignRightSection.from_dict(_right_section)

        _common_styles = d.pop("commonStyles", UNSET)
        common_styles: Union[Unset, CustomFormDesignCommonStyles]
        if isinstance(_common_styles, Unset):
            common_styles = UNSET
        else:
            common_styles = CustomFormDesignCommonStyles.from_dict(_common_styles)

        _footer_section = d.pop("footerSection", UNSET)
        footer_section: Union[Unset, CustomFormDesignFooterSection]
        if isinstance(_footer_section, Unset):
            footer_section = UNSET
        else:
            footer_section = CustomFormDesignFooterSection.from_dict(_footer_section)

        custom_form_design_schema = cls(
            background_styles=background_styles,
            left_section=left_section,
            design_type=design_type,
            is_public=is_public,
            document_title=document_title,
            favicon_path=favicon_path,
            facebook_url=facebook_url,
            social_links_text=social_links_text,
            instagram_url=instagram_url,
            redirection_url=redirection_url,
            terms_and_conditions_url=terms_and_conditions_url,
            terms_link_text=terms_link_text,
            home_page_url=home_page_url,
            success_submission_message=success_submission_message,
            disable_success_submission_message=disable_success_submission_message,
            right_section=right_section,
            common_styles=common_styles,
            footer_section=footer_section,
        )

        custom_form_design_schema.additional_properties = d
        return custom_form_design_schema

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
