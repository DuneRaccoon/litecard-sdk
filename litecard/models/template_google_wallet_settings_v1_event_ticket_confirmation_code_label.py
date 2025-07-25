from enum import Enum


class TemplateGoogleWalletSettingsV1EventTicketConfirmationCodeLabel(str, Enum):
    CONFIRMATION_CODE = "CONFIRMATION_CODE"
    CONFIRMATION_CODE_LABEL_UNSPECIFIED = "CONFIRMATION_CODE_LABEL_UNSPECIFIED"
    CONFIRMATION_NUMBER = "CONFIRMATION_NUMBER"
    ORDER_NUMBER = "ORDER_NUMBER"
    RESERVATION_NUMBER = "RESERVATION_NUMBER"

    def __str__(self) -> str:
        return str(self.value)
