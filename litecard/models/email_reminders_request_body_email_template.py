from enum import Enum


class EmailRemindersRequestBodyEmailTemplate(str, Enum):
    CX3 = "cx3"
    LITECARDPASS = "litecardpass"
    MUBC = "mubc"
    MUTTC = "muttc"
    TABLE_TENNIS = "table-tennis"
    TARFISH = "tarfish"
    TARFISH_FORM = "tarfish-form"
    TT_REMINDER = "tt-reminder"

    def __str__(self) -> str:
        return str(self.value)
