from enum import Enum


class TemplateCardExpiryType2FromActivationMeasurement(str, Enum):
    DAYS = "DAYS"
    MONTHS = "MONTHS"
    YEARS = "YEARS"

    def __str__(self) -> str:
        return str(self.value)
