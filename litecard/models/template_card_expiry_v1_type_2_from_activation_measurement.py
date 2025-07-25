from enum import Enum


class TemplateCardExpiryV1Type2FromActivationMeasurement(str, Enum):
    DAYS = "DAYS"
    MONTHS = "MONTHS"
    YEARS = "YEARS"

    def __str__(self) -> str:
        return str(self.value)
