from enum import Enum


class WebhookRegistrationRequestBodyEventsItem(str, Enum):
    PASS_DOWNLOAD = "PASS_DOWNLOAD"
    PASS_REMOVE = "PASS_REMOVE"
    REGISTER_WEBHOOK = "REGISTER_WEBHOOK"

    def __str__(self) -> str:
        return str(self.value)
