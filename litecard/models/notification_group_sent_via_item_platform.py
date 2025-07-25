from enum import Enum


class NotificationGroupSentViaItemPlatform(str, Enum):
    APPLE = "apple"
    GOOGLE = "google"

    def __str__(self) -> str:
        return str(self.value)
