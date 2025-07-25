from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.template_notification_fields_apple_text_alignment import TemplateNotificationFieldsAppleTextAlignment
from ..types import UNSET, Unset

T = TypeVar("T", bound="TemplateNotificationFields")


@_attrs_define
class TemplateNotificationFields:
    """Notification Fields of the template

    Attributes:
        apple_field_position (Union[Unset, float]): Position of the Apple Field
        user_can_edit (Union[Unset, bool]): User can edit or not Example: True.
        apple_change_message (Union[Unset, str]): Apple Change Message Example: abcde.
        apple_date_style (Union[Unset, str]): Style of the Apple Date Example: NOT_USED.
        field_label (Union[Unset, str]): Label of the Field Example: test label.
        google_field_type (Union[Unset, str]): Field Type in Google Example: MESSAGES.
        apple_time_style (Union[Unset, str]): Style of the apple Time Example: NOT_USED.
        field_value (Union[Unset, str]): Value of the Field Example: test value.
        apple_field_type (Union[Unset, str]): Type of the Apple Field Example: BACK_FIELD.
        apple_attributed_value (Union[Unset, str]): Overrides the apple field value key, can contain HTML a tags
            Example: <a href='http://google.com'>Google</a>.
        apple_ignore_time_zone (Union[Unset, bool]): Optional. Always display the time and date in the given time zone,
            not in the user’s current time zone. The default value is false. Default: False. Example: True.
        apple_is_relative_date (Union[Unset, bool]): Optional. If true, the label’s value is displayed as a relative
            date; otherwise, it is displayed as an absolute date. The default value is false. Default: False. Example: True.
        apple_text_alignment (Union[Unset, TemplateNotificationFieldsAppleTextAlignment]): Optional argument that sets
            the text alignment of the field text. This value is not allowed on primary or back fields. Default:
            TemplateNotificationFieldsAppleTextAlignment.PKTEXTALIGNMENTNATURAL. Example: PKTextAlignmentRight.
    """

    apple_field_position: Union[Unset, float] = UNSET
    user_can_edit: Union[Unset, bool] = UNSET
    apple_change_message: Union[Unset, str] = UNSET
    apple_date_style: Union[Unset, str] = UNSET
    field_label: Union[Unset, str] = UNSET
    google_field_type: Union[Unset, str] = UNSET
    apple_time_style: Union[Unset, str] = UNSET
    field_value: Union[Unset, str] = UNSET
    apple_field_type: Union[Unset, str] = UNSET
    apple_attributed_value: Union[Unset, str] = UNSET
    apple_ignore_time_zone: Union[Unset, bool] = False
    apple_is_relative_date: Union[Unset, bool] = False
    apple_text_alignment: Union[Unset, TemplateNotificationFieldsAppleTextAlignment] = (
        TemplateNotificationFieldsAppleTextAlignment.PKTEXTALIGNMENTNATURAL
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        apple_field_position = self.apple_field_position

        user_can_edit = self.user_can_edit

        apple_change_message = self.apple_change_message

        apple_date_style = self.apple_date_style

        field_label = self.field_label

        google_field_type = self.google_field_type

        apple_time_style = self.apple_time_style

        field_value = self.field_value

        apple_field_type = self.apple_field_type

        apple_attributed_value = self.apple_attributed_value

        apple_ignore_time_zone = self.apple_ignore_time_zone

        apple_is_relative_date = self.apple_is_relative_date

        apple_text_alignment: Union[Unset, str] = UNSET
        if not isinstance(self.apple_text_alignment, Unset):
            apple_text_alignment = self.apple_text_alignment.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if apple_field_position is not UNSET:
            field_dict["appleFieldPosition"] = apple_field_position
        if user_can_edit is not UNSET:
            field_dict["userCanEdit"] = user_can_edit
        if apple_change_message is not UNSET:
            field_dict["appleChangeMessage"] = apple_change_message
        if apple_date_style is not UNSET:
            field_dict["appleDateStyle"] = apple_date_style
        if field_label is not UNSET:
            field_dict["fieldLabel"] = field_label
        if google_field_type is not UNSET:
            field_dict["googleFieldType"] = google_field_type
        if apple_time_style is not UNSET:
            field_dict["appleTimeStyle"] = apple_time_style
        if field_value is not UNSET:
            field_dict["fieldValue"] = field_value
        if apple_field_type is not UNSET:
            field_dict["appleFieldType"] = apple_field_type
        if apple_attributed_value is not UNSET:
            field_dict["appleAttributedValue"] = apple_attributed_value
        if apple_ignore_time_zone is not UNSET:
            field_dict["appleIgnoreTimeZone"] = apple_ignore_time_zone
        if apple_is_relative_date is not UNSET:
            field_dict["appleIsRelativeDate"] = apple_is_relative_date
        if apple_text_alignment is not UNSET:
            field_dict["appleTextAlignment"] = apple_text_alignment

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        apple_field_position = d.pop("appleFieldPosition", UNSET)

        user_can_edit = d.pop("userCanEdit", UNSET)

        apple_change_message = d.pop("appleChangeMessage", UNSET)

        apple_date_style = d.pop("appleDateStyle", UNSET)

        field_label = d.pop("fieldLabel", UNSET)

        google_field_type = d.pop("googleFieldType", UNSET)

        apple_time_style = d.pop("appleTimeStyle", UNSET)

        field_value = d.pop("fieldValue", UNSET)

        apple_field_type = d.pop("appleFieldType", UNSET)

        apple_attributed_value = d.pop("appleAttributedValue", UNSET)

        apple_ignore_time_zone = d.pop("appleIgnoreTimeZone", UNSET)

        apple_is_relative_date = d.pop("appleIsRelativeDate", UNSET)

        _apple_text_alignment = d.pop("appleTextAlignment", UNSET)
        apple_text_alignment: Union[Unset, TemplateNotificationFieldsAppleTextAlignment]
        if isinstance(_apple_text_alignment, Unset):
            apple_text_alignment = UNSET
        else:
            apple_text_alignment = TemplateNotificationFieldsAppleTextAlignment(_apple_text_alignment)

        template_notification_fields = cls(
            apple_field_position=apple_field_position,
            user_can_edit=user_can_edit,
            apple_change_message=apple_change_message,
            apple_date_style=apple_date_style,
            field_label=field_label,
            google_field_type=google_field_type,
            apple_time_style=apple_time_style,
            field_value=field_value,
            apple_field_type=apple_field_type,
            apple_attributed_value=apple_attributed_value,
            apple_ignore_time_zone=apple_ignore_time_zone,
            apple_is_relative_date=apple_is_relative_date,
            apple_text_alignment=apple_text_alignment,
        )

        template_notification_fields.additional_properties = d
        return template_notification_fields

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
