from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.webhook_registration_request_body_auth_type import WebhookRegistrationRequestBodyAuthType
from ..models.webhook_registration_request_body_events_item import WebhookRegistrationRequestBodyEventsItem
from ..models.webhook_registration_request_body_method import WebhookRegistrationRequestBodyMethod
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.webhook_registration_request_body_auth_config import WebhookRegistrationRequestBodyAuthConfig


T = TypeVar("T", bound="WebhookRegistrationRequestBody")


@_attrs_define
class WebhookRegistrationRequestBody:
    """
    Attributes:
        webhook_url (str): The endpoint for Litecard to send the download data Example: https://example.com/webhook.
        method (WebhookRegistrationRequestBodyMethod): Method to use Example: POST.
        events (list[WebhookRegistrationRequestBodyEventsItem]): Types of events the webhook supports
        auth_type (Union[Unset, WebhookRegistrationRequestBodyAuthType]): The type of Auth to use for the webhook
        auth_config (Union[Unset, WebhookRegistrationRequestBodyAuthConfig]): The properties we need to use for
            Authentication
        provider (Union[Unset, str]): To determine the schema of payloads for the events
    """

    webhook_url: str
    method: WebhookRegistrationRequestBodyMethod
    events: list[WebhookRegistrationRequestBodyEventsItem]
    auth_type: Union[Unset, WebhookRegistrationRequestBodyAuthType] = UNSET
    auth_config: Union[Unset, "WebhookRegistrationRequestBodyAuthConfig"] = UNSET
    provider: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        webhook_url = self.webhook_url

        method = self.method.value

        events = []
        for events_item_data in self.events:
            events_item = events_item_data.value
            events.append(events_item)

        auth_type: Union[Unset, str] = UNSET
        if not isinstance(self.auth_type, Unset):
            auth_type = self.auth_type.value

        auth_config: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.auth_config, Unset):
            auth_config = self.auth_config.to_dict()

        provider = self.provider

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "webhookUrl": webhook_url,
                "method": method,
                "events": events,
            }
        )
        if auth_type is not UNSET:
            field_dict["authType"] = auth_type
        if auth_config is not UNSET:
            field_dict["authConfig"] = auth_config
        if provider is not UNSET:
            field_dict["provider"] = provider

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.webhook_registration_request_body_auth_config import WebhookRegistrationRequestBodyAuthConfig

        d = dict(src_dict)
        webhook_url = d.pop("webhookUrl")

        method = WebhookRegistrationRequestBodyMethod(d.pop("method"))

        events = []
        _events = d.pop("events")
        for events_item_data in _events:
            events_item = WebhookRegistrationRequestBodyEventsItem(events_item_data)

            events.append(events_item)

        _auth_type = d.pop("authType", UNSET)
        auth_type: Union[Unset, WebhookRegistrationRequestBodyAuthType]
        if isinstance(_auth_type, Unset):
            auth_type = UNSET
        else:
            auth_type = WebhookRegistrationRequestBodyAuthType(_auth_type)

        _auth_config = d.pop("authConfig", UNSET)
        auth_config: Union[Unset, WebhookRegistrationRequestBodyAuthConfig]
        if isinstance(_auth_config, Unset):
            auth_config = UNSET
        else:
            auth_config = WebhookRegistrationRequestBodyAuthConfig.from_dict(_auth_config)

        provider = d.pop("provider", UNSET)

        webhook_registration_request_body = cls(
            webhook_url=webhook_url,
            method=method,
            events=events,
            auth_type=auth_type,
            auth_config=auth_config,
            provider=provider,
        )

        webhook_registration_request_body.additional_properties = d
        return webhook_registration_request_body

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
