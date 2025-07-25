from enum import Enum


class CardStatus(str, Enum):
    ACTIVE = "ACTIVE"
    DELETED = "DELETED"
    ERROR = "ERROR"
    INACTIVE = "INACTIVE"
    RESERVED = "RESERVED"

    def __str__(self) -> str:
        return str(self.value)
