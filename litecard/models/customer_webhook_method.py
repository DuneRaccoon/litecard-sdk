from enum import Enum


class CustomerWebhookMethod(str, Enum):
    POST = "POST"

    def __str__(self) -> str:
        return str(self.value)
