from enum import Enum


class FormFieldUsageItem(str, Enum):
    EXTERNAL = "EXTERNAL"
    PRIVATE = "PRIVATE"
    PUBLIC = "PUBLIC"

    def __str__(self) -> str:
        return str(self.value)
