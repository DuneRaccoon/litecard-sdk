from enum import Enum


class FormRequestStatus(str, Enum):
    ACTIVE = "ACTIVE"
    DELETED = "DELETED"
    INACTIVE = "INACTIVE"

    def __str__(self) -> str:
        return str(self.value)
