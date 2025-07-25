from enum import Enum


class TemplateCardExpiryV1Type0ExpiryType(str, Enum):
    NEVER = "NEVER"

    def __str__(self) -> str:
        return str(self.value)
