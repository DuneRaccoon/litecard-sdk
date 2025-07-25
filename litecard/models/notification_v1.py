from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.notification_segments import NotificationSegments
    from ..models.notification_v1_notification import NotificationV1Notification
    from ..models.notification_v1_options import NotificationV1Options


T = TypeVar("T", bound="NotificationV1")


@_attrs_define
class NotificationV1:
    """
    Attributes:
        card_ids (list[str]): Array of cardIds to send push notifications to
        notification (NotificationV1Notification):
        segments (Union[Unset, NotificationSegments]):
        template_ids (Union[Unset, list[str]]): Array of card template ids to send notifications to
        options (Union[Unset, NotificationV1Options]):
    """

    card_ids: list[str]
    notification: "NotificationV1Notification"
    segments: Union[Unset, "NotificationSegments"] = UNSET
    template_ids: Union[Unset, list[str]] = UNSET
    options: Union[Unset, "NotificationV1Options"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        card_ids = self.card_ids

        notification = self.notification.to_dict()

        segments: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.segments, Unset):
            segments = self.segments.to_dict()

        template_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.template_ids, Unset):
            template_ids = self.template_ids

        options: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.options, Unset):
            options = self.options.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cardIds": card_ids,
                "notification": notification,
            }
        )
        if segments is not UNSET:
            field_dict["segments"] = segments
        if template_ids is not UNSET:
            field_dict["templateIds"] = template_ids
        if options is not UNSET:
            field_dict["options"] = options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.notification_segments import NotificationSegments
        from ..models.notification_v1_notification import NotificationV1Notification
        from ..models.notification_v1_options import NotificationV1Options

        d = dict(src_dict)
        card_ids = cast(list[str], d.pop("cardIds"))

        notification = NotificationV1Notification.from_dict(d.pop("notification"))

        _segments = d.pop("segments", UNSET)
        segments: Union[Unset, NotificationSegments]
        if isinstance(_segments, Unset):
            segments = UNSET
        else:
            segments = NotificationSegments.from_dict(_segments)

        template_ids = cast(list[str], d.pop("templateIds", UNSET))

        _options = d.pop("options", UNSET)
        options: Union[Unset, NotificationV1Options]
        if isinstance(_options, Unset):
            options = UNSET
        else:
            options = NotificationV1Options.from_dict(_options)

        notification_v1 = cls(
            card_ids=card_ids,
            notification=notification,
            segments=segments,
            template_ids=template_ids,
            options=options,
        )

        notification_v1.additional_properties = d
        return notification_v1

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
