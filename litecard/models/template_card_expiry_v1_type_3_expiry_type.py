from enum import Enum


class TemplateCardExpiryV1Type3ExpiryType(str, Enum):
    FIXED_SCANS = "FIXED_SCANS"

    def __str__(self) -> str:
        return str(self.value)
