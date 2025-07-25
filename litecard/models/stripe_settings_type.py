from enum import Enum


class StripeSettingsType(str, Enum):
    LINKED = "LINKED"
    STANDARD = "STANDARD"

    def __str__(self) -> str:
        return str(self.value)
