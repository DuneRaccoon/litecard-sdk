from enum import Enum


class TemplateDataFieldV1Formatter(str, Enum):
    INITIALS = "initials"

    def __str__(self) -> str:
        return str(self.value)
