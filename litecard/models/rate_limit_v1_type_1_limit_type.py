from enum import Enum


class RateLimitV1Type1LimitType(str, Enum):
    DATE = "DATE"

    def __str__(self) -> str:
        return str(self.value)
