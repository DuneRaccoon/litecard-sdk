from enum import Enum


class TemplateUsageV1Item(str, Enum):
    APPLE_WALLET = "APPLE_WALLET"
    GOOGLE_WALLET = "GOOGLE_WALLET"
    NOT_USED = "NOT_USED"
    SAMSUNG_WALLET = "SAMSUNG_WALLET"

    def __str__(self) -> str:
        return str(self.value)
