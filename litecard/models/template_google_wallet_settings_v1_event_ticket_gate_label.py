from enum import Enum


class TemplateGoogleWalletSettingsV1EventTicketGateLabel(str, Enum):
    DOORS = "DOORS"
    ENTRANCE = "ENTRANCE"
    GATE = "GATE"

    def __str__(self) -> str:
        return str(self.value)
