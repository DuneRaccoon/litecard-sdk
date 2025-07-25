from enum import Enum


class ScanScanType(str, Enum):
    REDEEM = "REDEEM"
    SCAN = "SCAN"

    def __str__(self) -> str:
        return str(self.value)
