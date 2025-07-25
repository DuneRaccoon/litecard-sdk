from enum import Enum


class RateLimitV1Type1RuleDateLimitMeasurement(str, Enum):
    DAYS = "DAYS"
    MONTHS = "MONTHS"
    YEARS = "YEARS"

    def __str__(self) -> str:
        return str(self.value)
