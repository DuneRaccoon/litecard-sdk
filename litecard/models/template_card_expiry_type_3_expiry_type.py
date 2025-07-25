from enum import Enum


class TemplateCardExpiryType3ExpiryType(str, Enum):
    FIXED_SCANS = "FIXED_SCANS"

    def __str__(self) -> str:
        return str(self.value)
