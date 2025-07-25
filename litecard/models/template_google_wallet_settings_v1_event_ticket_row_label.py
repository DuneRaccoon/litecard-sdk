from enum import Enum


class TemplateGoogleWalletSettingsV1EventTicketRowLabel(str, Enum):
    ROW = "ROW"
    ROW_LABEL_UNSPECIFIED = "ROW_LABEL_UNSPECIFIED"

    def __str__(self) -> str:
        return str(self.value)
