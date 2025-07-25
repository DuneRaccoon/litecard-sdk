from enum import Enum


class WebhookRegistrationRequestBodyAuthType(str, Enum):
    API_KEY = "API_KEY"

    def __str__(self) -> str:
        return str(self.value)
