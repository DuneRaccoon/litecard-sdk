from enum import Enum


class TemplateGoogleWalletSettingsV1PassType(str, Enum):
    EVENT_TICKET = "EVENT_TICKET"
    FLIGHT = "FLIGHT"
    GENERIC = "GENERIC"
    GIFT_CARD = "GIFT_CARD"
    LOYALTY = "LOYALTY"
    OFFER = "OFFER"
    TRANSIT = "TRANSIT"

    def __str__(self) -> str:
        return str(self.value)
