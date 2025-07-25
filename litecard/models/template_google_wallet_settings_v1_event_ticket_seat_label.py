from enum import Enum


class TemplateGoogleWalletSettingsV1EventTicketSeatLabel(str, Enum):
    SEAT = "SEAT"
    SEAT_LABEL_UNSPECIFIED = "SEAT_LABEL_UNSPECIFIED"

    def __str__(self) -> str:
        return str(self.value)
