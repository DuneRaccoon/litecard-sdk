from enum import Enum


class TableColumnUsageItem(str, Enum):
    CSV = "CSV"
    UI = "UI"

    def __str__(self) -> str:
        return str(self.value)
