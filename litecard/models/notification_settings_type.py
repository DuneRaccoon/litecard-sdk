from enum import Enum


class NotificationSettingsType(str, Enum):
    PN = "PN"

    def __str__(self) -> str:
        return str(self.value)
