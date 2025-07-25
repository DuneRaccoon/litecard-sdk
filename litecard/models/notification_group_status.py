from enum import Enum


class NotificationGroupStatus(str, Enum):
    CANCELLED = "CANCELLED"
    FAILED = "FAILED"
    IN_PROGRESS = "IN_PROGRESS"
    PENDING = "PENDING"
    QUEUED = "QUEUED"
    SENT = "SENT"

    def __str__(self) -> str:
        return str(self.value)
