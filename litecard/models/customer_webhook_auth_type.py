from enum import Enum


class CustomerWebhookAuthType(str, Enum):
    API_KEY = "API_KEY"

    def __str__(self) -> str:
        return str(self.value)
