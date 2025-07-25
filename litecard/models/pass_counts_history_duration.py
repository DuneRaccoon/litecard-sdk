from enum import Enum


class PassCountsHistoryDuration(str, Enum):
    ALL = "ALL"
    PAST_30_DAYS = "PAST_30_DAYS"
    PAST_7_DAYS = "PAST_7_DAYS"

    def __str__(self) -> str:
        return str(self.value)
