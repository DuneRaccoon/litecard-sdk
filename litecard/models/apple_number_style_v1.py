from enum import Enum


class AppleNumberStyleV1(str, Enum):
    DECIMAL = "DECIMAL"
    NOT_USED = "NOT_USED"
    PERCENT = "PERCENT"
    SCIENTIFIC = "SCIENTIFIC"
    SPELLOUT = "SPELLOUT"

    def __str__(self) -> str:
        return str(self.value)
