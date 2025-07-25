from enum import Enum


class TemplateColoursV1SamsungFont(str, Enum):
    VALUE_0 = "#000000"
    VALUE_1 = "#ffffff"

    def __str__(self) -> str:
        return str(self.value)
