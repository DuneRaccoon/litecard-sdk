from enum import Enum


class TableColumnFormat(str, Enum):
    CURRENCY = "currency"
    DATE = "date"
    DATETIME = "datetime"
    NUMBER = "number"
    TIME = "time"

    def __str__(self) -> str:
        return str(self.value)
