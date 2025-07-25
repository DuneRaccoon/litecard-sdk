from enum import Enum


class TemplateGoogleWalletSettingsV1EventTicketSectionLabel(str, Enum):
    SECTION = "SECTION"
    THEATER = "THEATER"

    def __str__(self) -> str:
        return str(self.value)
