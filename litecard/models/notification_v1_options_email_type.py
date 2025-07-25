from enum import Enum


class NotificationV1OptionsEmailType(str, Enum):
    MARKETING = "MARKETING"
    STANDARD = "STANDARD"

    def __str__(self) -> str:
        return str(self.value)
