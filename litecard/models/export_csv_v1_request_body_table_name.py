from enum import Enum


class ExportCsvV1RequestBodyTableName(str, Enum):
    CARDSTABLE = "cardsTable"
    NOTIFICATIONGROUPSTABLE = "notificationGroupsTable"
    SCANSTABLE = "scansTable"
    SCAN_TABLE = "SCAN_TABLE"

    def __str__(self) -> str:
        return str(self.value)
