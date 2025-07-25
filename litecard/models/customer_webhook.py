from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.customer_webhook_auth_type import CustomerWebhookAuthType
from ..models.customer_webhook_events_item import CustomerWebhookEventsItem
from ..models.customer_webhook_method import CustomerWebhookMethod
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.customer_webhook_auth_config import CustomerWebhookAuthConfig


T = TypeVar("T", bound="CustomerWebhook")


@_attrs_define
class CustomerWebhook:
    """
    Attributes:
        webhook_url (Union[Unset, str]): The endpoint for Litecard to send the download data Example:
            https://example.com/webhook.
        method (Union[Unset, CustomerWebhookMethod]): Method to use Example: POST.
        auth_type (Union[Unset, CustomerWebhookAuthType]): The type of Auth to use for the webhook
        auth_config (Union[Unset, CustomerWebhookAuthConfig]): The properties we need to use for Authentication
        events (Union[Unset, list[CustomerWebhookEventsItem]]): Types of events the webhook supports
    """

    webhook_url: Union[Unset, str] = UNSET
    method: Union[Unset, CustomerWebhookMethod] = UNSET
    auth_type: Union[Unset, CustomerWebhookAuthType] = UNSET
    auth_config: Union[Unset, "CustomerWebhookAuthConfig"] = UNSET
    events: Union[Unset, list[CustomerWebhookEventsItem]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        webhook_url = self.webhook_url

        method: Union[Unset, str] = UNSET
        if not isinstance(self.method, Unset):
            method = self.method.value

        auth_type: Union[Unset, str] = UNSET
        if not isinstance(self.auth_type, Unset):
            auth_type = self.auth_type.value

        auth_config: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.auth_config, Unset):
            auth_config = self.auth_config.to_dict()

        events: Union[Unset, list[str]] = UNSET
        if not isinstance(self.events, Unset):
            events = []
            for events_item_data in self.events:
                events_item = events_item_data.value
                events.append(events_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if webhook_url is not UNSET:
            field_dict["webhookUrl"] = webhook_url
        if method is not UNSET:
            field_dict["method"] = method
        if auth_type is not UNSET:
            field_dict["authType"] = auth_type
        if auth_config is not UNSET:
            field_dict["authConfig"] = auth_config
        if events is not UNSET:
            field_dict["events"] = events

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.customer_webhook_auth_config import CustomerWebhookAuthConfig

        d = dict(src_dict)
        webhook_url = d.pop("webhookUrl", UNSET)

        _method = d.pop("method", UNSET)
        method: Union[Unset, CustomerWebhookMethod]
        if isinstance(_method, Unset):
            method = UNSET
        else:
            method = CustomerWebhookMethod(_method)

        _auth_type = d.pop("authType", UNSET)
        auth_type: Union[Unset, CustomerWebhookAuthType]
        if isinstance(_auth_type, Unset):
            auth_type = UNSET
        else:
            auth_type = CustomerWebhookAuthType(_auth_type)

        _auth_config = d.pop("authConfig", UNSET)
        auth_config: Union[Unset, CustomerWebhookAuthConfig]
        if isinstance(_auth_config, Unset):
            auth_config = UNSET
        else:
            auth_config = CustomerWebhookAuthConfig.from_dict(_auth_config)

        events = []
        _events = d.pop("events", UNSET)
        for events_item_data in _events or []:
            events_item = CustomerWebhookEventsItem(events_item_data)

            events.append(events_item)

        customer_webhook = cls(
            webhook_url=webhook_url,
            method=method,
            auth_type=auth_type,
            auth_config=auth_config,
            events=events,
        )

        customer_webhook.additional_properties = d
        return customer_webhook

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
