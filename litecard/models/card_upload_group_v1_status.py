from enum import Enum


class CardUploadGroupV1Status(str, Enum):
    COMPLETED = "COMPLETED"
    PARSING_ERROR = "PARSING_ERROR"
    PENDING = "PENDING"
    RECORD_COUNT_EXCEEDED = "RECORD_COUNT_EXCEEDED"
    VALIDATION_COMPLETE = "VALIDATION_COMPLETE"

    def __str__(self) -> str:
        return str(self.value)
