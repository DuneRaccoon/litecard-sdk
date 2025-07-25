from enum import Enum


class DateTimeStyle(str, Enum):
    FULL = "FULL"
    LONG = "LONG"
    MEDIUM = "MEDIUM"
    NONE = "NONE"
    NOT_USED = "NOT_USED"
    SHORT = "SHORT"

    def __str__(self) -> str:
        return str(self.value)
