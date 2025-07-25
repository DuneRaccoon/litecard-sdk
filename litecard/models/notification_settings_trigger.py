from enum import Enum


class NotificationSettingsTrigger(str, Enum):
    AFTER_CREATION = "AFTER_CREATION"

    def __str__(self) -> str:
        return str(self.value)
