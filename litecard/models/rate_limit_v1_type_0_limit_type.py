from enum import Enum


class RateLimitV1Type0LimitType(str, Enum):
    INTERVAL = "INTERVAL"

    def __str__(self) -> str:
        return str(self.value)
