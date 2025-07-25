from enum import Enum


class NotificationGroupSentViaItemType(str, Enum):
    EMAIL = "EMAIL"
    PUSH_NOTIFICATION = "PUSH_NOTIFICATION"

    def __str__(self) -> str:
        return str(self.value)
