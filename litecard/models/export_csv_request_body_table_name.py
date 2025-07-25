from enum import Enum


class ExportCsvRequestBodyTableName(str, Enum):
    CARD_TABLE = "CARD_TABLE"
    MEMBER_TABLE = "MEMBER_TABLE"
    SCAN_TABLE = "SCAN_TABLE"

    def __str__(self) -> str:
        return str(self.value)
