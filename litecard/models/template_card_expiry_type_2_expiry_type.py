from enum import Enum


class TemplateCardExpiryType2ExpiryType(str, Enum):
    FROM_ACTIVATION = "FROM_ACTIVATION"

    def __str__(self) -> str:
        return str(self.value)
