from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.custom_form_design_right_section_form_styles import CustomFormDesignRightSectionFormStyles


T = TypeVar("T", bound="CustomFormDesignRightSection")


@_attrs_define
class CustomFormDesignRightSection:
    """Configuration for the right section of the form

    Attributes:
        header_logo (Union[Unset, str]): URL of the header logo image Example: /path/to/right-logo.png.
        header (Union[Unset, str]): Header text for the right section Example: Sign up now!.
        content (Union[Unset, str]): Content for the right section Example: Please fill in your details.
        instructions (Union[Unset, str]): Content for the instructions section Example: Please fill in your details.
        header_text_colour (Union[Unset, str]): Colour of the header text Default: '#000000'. Example: #000000.
        submit_button_colour (Union[Unset, str]): Colour of the submit button Default: '#FFFFFF'. Example: #FFFFFF.
        submit_button_text_colour (Union[Unset, str]): Colour of the submit button text Default: '#000000'. Example:
            #000000.
        submit_button_text (Union[Unset, str]): Text displayed on the submit button Default: 'Send'. Example: Send.
        submit_border_colour (Union[Unset, str]): Border color of the submit button Default: 'transparent'. Example:
            transparent.
        header_class_name (Union[Unset, str]): Custom CSS class for the header Example: form-header.
        form_styles (Union[Unset, CustomFormDesignRightSectionFormStyles]): Custom styles for the form
    """

    header_logo: Union[Unset, str] = UNSET
    header: Union[Unset, str] = UNSET
    content: Union[Unset, str] = UNSET
    instructions: Union[Unset, str] = UNSET
    header_text_colour: Union[Unset, str] = "#000000"
    submit_button_colour: Union[Unset, str] = "#FFFFFF"
    submit_button_text_colour: Union[Unset, str] = "#000000"
    submit_button_text: Union[Unset, str] = "Send"
    submit_border_colour: Union[Unset, str] = "transparent"
    header_class_name: Union[Unset, str] = UNSET
    form_styles: Union[Unset, "CustomFormDesignRightSectionFormStyles"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        header_logo = self.header_logo

        header = self.header

        content = self.content

        instructions = self.instructions

        header_text_colour = self.header_text_colour

        submit_button_colour = self.submit_button_colour

        submit_button_text_colour = self.submit_button_text_colour

        submit_button_text = self.submit_button_text

        submit_border_colour = self.submit_border_colour

        header_class_name = self.header_class_name

        form_styles: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.form_styles, Unset):
            form_styles = self.form_styles.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if header_logo is not UNSET:
            field_dict["headerLogo"] = header_logo
        if header is not UNSET:
            field_dict["header"] = header
        if content is not UNSET:
            field_dict["content"] = content
        if instructions is not UNSET:
            field_dict["instructions"] = instructions
        if header_text_colour is not UNSET:
            field_dict["headerTextColour"] = header_text_colour
        if submit_button_colour is not UNSET:
            field_dict["submitButtonColour"] = submit_button_colour
        if submit_button_text_colour is not UNSET:
            field_dict["submitButtonTextColour"] = submit_button_text_colour
        if submit_button_text is not UNSET:
            field_dict["submitButtonText"] = submit_button_text
        if submit_border_colour is not UNSET:
            field_dict["submitBorderColour"] = submit_border_colour
        if header_class_name is not UNSET:
            field_dict["headerClassName"] = header_class_name
        if form_styles is not UNSET:
            field_dict["formStyles"] = form_styles

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.custom_form_design_right_section_form_styles import CustomFormDesignRightSectionFormStyles

        d = dict(src_dict)
        header_logo = d.pop("headerLogo", UNSET)

        header = d.pop("header", UNSET)

        content = d.pop("content", UNSET)

        instructions = d.pop("instructions", UNSET)

        header_text_colour = d.pop("headerTextColour", UNSET)

        submit_button_colour = d.pop("submitButtonColour", UNSET)

        submit_button_text_colour = d.pop("submitButtonTextColour", UNSET)

        submit_button_text = d.pop("submitButtonText", UNSET)

        submit_border_colour = d.pop("submitBorderColour", UNSET)

        header_class_name = d.pop("headerClassName", UNSET)

        _form_styles = d.pop("formStyles", UNSET)
        form_styles: Union[Unset, CustomFormDesignRightSectionFormStyles]
        if isinstance(_form_styles, Unset):
            form_styles = UNSET
        else:
            form_styles = CustomFormDesignRightSectionFormStyles.from_dict(_form_styles)

        custom_form_design_right_section = cls(
            header_logo=header_logo,
            header=header,
            content=content,
            instructions=instructions,
            header_text_colour=header_text_colour,
            submit_button_colour=submit_button_colour,
            submit_button_text_colour=submit_button_text_colour,
            submit_button_text=submit_button_text,
            submit_border_colour=submit_border_colour,
            header_class_name=header_class_name,
            form_styles=form_styles,
        )

        custom_form_design_right_section.additional_properties = d
        return custom_form_design_right_section

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
