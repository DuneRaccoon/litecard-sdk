from enum import Enum


class TemplateAppleWalletSettingsV1PassType(str, Enum):
    BOARDING_PASS = "BOARDING_PASS"
    COUPON = "COUPON"
    EVENT_TICKET = "EVENT_TICKET"
    GENERIC = "GENERIC"
    STORE_CARD = "STORE_CARD"

    def __str__(self) -> str:
        return str(self.value)
