from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.apple_date_time_style_v1 import AppleDateTimeStyleV1
from ..models.apple_number_style_v1 import AppleNumberStyleV1
from ..models.template_data_field_v1_apple_field_settings_apple_field_type import (
    TemplateDataFieldV1AppleFieldSettingsAppleFieldType,
)
from ..models.template_data_field_v1_apple_field_settings_text_alignment import (
    TemplateDataFieldV1AppleFieldSettingsTextAlignment,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="TemplateDataFieldV1AppleFieldSettings")


@_attrs_define
class TemplateDataFieldV1AppleFieldSettings:
    """
    Attributes:
        position (int): The position in the pass structure array. e.g. For a secondary field, a position of 0 means it
            is first in order to be rendered in that section. Positions start from 0. Example: 1.
        location (TemplateDataFieldV1AppleFieldSettingsAppleFieldType): The pass structure locations, each value
            pertains to a certain region/part of the apple pass Example: HEADER_FIELD.
        attributed_value (Union[Unset, str]): Overrides the apple field value key, can contain HTML a tags Example: <a
            href='http://google.com'>Google</a>.
        change_message (Union[Unset, str]): This is the formatted string, that will be shown as a push notification
            message. The format string must contain %@, which is replaced with the field's new content. If no change message
            is set, the user isn't notified when the field changes. Example: Gate changed to %@.
        date_style (Union[Unset, AppleDateTimeStyleV1]): Style of the time to be displayed

            SHORT - 11/23/37” or “3:30 PM”.

            MEDIUM “Nov 23, 1937” or “3:30:32 PM”.

            LONG - “November 23, 1937” or “3:30:32 PM PST”

            FULL - “Tuesday, April 12, 1952 AD” or “3:30:42 PM Pacific Standard Time”

             Example: SHORT.
        time_style (Union[Unset, AppleDateTimeStyleV1]): Style of the time to be displayed

            SHORT - 11/23/37” or “3:30 PM”.

            MEDIUM “Nov 23, 1937” or “3:30:32 PM”.

            LONG - “November 23, 1937” or “3:30:32 PM PST”

            FULL - “Tuesday, April 12, 1952 AD” or “3:30:42 PM Pacific Standard Time”

             Example: SHORT.
        number_style (Union[Unset, AppleNumberStyleV1]): Style for the number to be displayed see
            https://developer.apple.com/documentation/foundation/nsnumberformatterstyle Example: DECIMAL.
        text_alignment (Union[Unset, TemplateDataFieldV1AppleFieldSettingsTextAlignment]): Optional argument that sets
            the text alignment of the field text. This value is not allowed on primary or back fields. Example:
            PKTextAlignmentRight.
        ignore_time_zone (Union[Unset, bool]): Optional. Always display the time and date in the given time zone, not in
            the user’s current time zone. The default value is false. Example: True.
        is_relative_date (Union[Unset, bool]): Optional. If true, the label’s value is displayed as a relative date;
            otherwise, it is displayed as an absolute date. The default value is false. Example: True.
    """

    position: int
    location: TemplateDataFieldV1AppleFieldSettingsAppleFieldType
    attributed_value: Union[Unset, str] = UNSET
    change_message: Union[Unset, str] = UNSET
    date_style: Union[Unset, AppleDateTimeStyleV1] = UNSET
    time_style: Union[Unset, AppleDateTimeStyleV1] = UNSET
    number_style: Union[Unset, AppleNumberStyleV1] = UNSET
    text_alignment: Union[Unset, TemplateDataFieldV1AppleFieldSettingsTextAlignment] = UNSET
    ignore_time_zone: Union[Unset, bool] = UNSET
    is_relative_date: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        position = self.position

        location = self.location.value

        attributed_value = self.attributed_value

        change_message = self.change_message

        date_style: Union[Unset, str] = UNSET
        if not isinstance(self.date_style, Unset):
            date_style = self.date_style.value

        time_style: Union[Unset, str] = UNSET
        if not isinstance(self.time_style, Unset):
            time_style = self.time_style.value

        number_style: Union[Unset, str] = UNSET
        if not isinstance(self.number_style, Unset):
            number_style = self.number_style.value

        text_alignment: Union[Unset, str] = UNSET
        if not isinstance(self.text_alignment, Unset):
            text_alignment = self.text_alignment.value

        ignore_time_zone = self.ignore_time_zone

        is_relative_date = self.is_relative_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "position": position,
                "location": location,
            }
        )
        if attributed_value is not UNSET:
            field_dict["attributedValue"] = attributed_value
        if change_message is not UNSET:
            field_dict["changeMessage"] = change_message
        if date_style is not UNSET:
            field_dict["dateStyle"] = date_style
        if time_style is not UNSET:
            field_dict["timeStyle"] = time_style
        if number_style is not UNSET:
            field_dict["numberStyle"] = number_style
        if text_alignment is not UNSET:
            field_dict["textAlignment"] = text_alignment
        if ignore_time_zone is not UNSET:
            field_dict["ignoreTimeZone"] = ignore_time_zone
        if is_relative_date is not UNSET:
            field_dict["isRelativeDate"] = is_relative_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        position = d.pop("position")

        location = TemplateDataFieldV1AppleFieldSettingsAppleFieldType(d.pop("location"))

        attributed_value = d.pop("attributedValue", UNSET)

        change_message = d.pop("changeMessage", UNSET)

        _date_style = d.pop("dateStyle", UNSET)
        date_style: Union[Unset, AppleDateTimeStyleV1]
        if isinstance(_date_style, Unset):
            date_style = UNSET
        else:
            date_style = AppleDateTimeStyleV1(_date_style)

        _time_style = d.pop("timeStyle", UNSET)
        time_style: Union[Unset, AppleDateTimeStyleV1]
        if isinstance(_time_style, Unset):
            time_style = UNSET
        else:
            time_style = AppleDateTimeStyleV1(_time_style)

        _number_style = d.pop("numberStyle", UNSET)
        number_style: Union[Unset, AppleNumberStyleV1]
        if isinstance(_number_style, Unset):
            number_style = UNSET
        else:
            number_style = AppleNumberStyleV1(_number_style)

        _text_alignment = d.pop("textAlignment", UNSET)
        text_alignment: Union[Unset, TemplateDataFieldV1AppleFieldSettingsTextAlignment]
        if isinstance(_text_alignment, Unset):
            text_alignment = UNSET
        else:
            text_alignment = TemplateDataFieldV1AppleFieldSettingsTextAlignment(_text_alignment)

        ignore_time_zone = d.pop("ignoreTimeZone", UNSET)

        is_relative_date = d.pop("isRelativeDate", UNSET)

        template_data_field_v1_apple_field_settings = cls(
            position=position,
            location=location,
            attributed_value=attributed_value,
            change_message=change_message,
            date_style=date_style,
            time_style=time_style,
            number_style=number_style,
            text_alignment=text_alignment,
            ignore_time_zone=ignore_time_zone,
            is_relative_date=is_relative_date,
        )

        template_data_field_v1_apple_field_settings.additional_properties = d
        return template_data_field_v1_apple_field_settings

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
