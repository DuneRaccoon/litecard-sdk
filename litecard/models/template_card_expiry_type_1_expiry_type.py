from enum import Enum


class TemplateCardExpiryType1ExpiryType(str, Enum):
    FIXED_DATE = "FIXED_DATE"

    def __str__(self) -> str:
        return str(self.value)
