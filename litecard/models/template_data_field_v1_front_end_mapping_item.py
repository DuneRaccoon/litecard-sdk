from enum import Enum


class TemplateDataFieldV1FrontEndMappingItem(str, Enum):
    MEMBER_TABLE = "MEMBER_TABLE"
    SCAN = "SCAN"
    SCAN_TABLE = "SCAN_TABLE"

    def __str__(self) -> str:
        return str(self.value)
