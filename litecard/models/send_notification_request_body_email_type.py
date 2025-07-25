from enum import Enum


class SendNotificationRequestBodyEmailType(str, Enum):
    MARKETING = "MARKETING"
    STANDARD = "STANDARD"

    def __str__(self) -> str:
        return str(self.value)
