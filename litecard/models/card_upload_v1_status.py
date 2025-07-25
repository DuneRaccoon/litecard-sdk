from enum import Enum


class CardUploadV1Status(str, Enum):
    CREATED = "CREATED"
    FAILED = "FAILED"
    PROCESSING = "PROCESSING"
    QUEUED = "QUEUED"
    SKIPPED = "SKIPPED"
    UPDATED = "UPDATED"
    VALIDATION_FAILED = "VALIDATION_FAILED"

    def __str__(self) -> str:
        return str(self.value)
