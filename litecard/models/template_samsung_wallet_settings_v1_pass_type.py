from enum import Enum


class TemplateSamsungWalletSettingsV1PassType(str, Enum):
    BOARDING_PASS = "BOARDING_PASS"
    COUPON = "COUPON"
    EVENT_TICKET = "EVENT_TICKET"
    GIFT_CARD = "GIFT_CARD"
    ID = "ID"
    LOYALTY = "LOYALTY"

    def __str__(self) -> str:
        return str(self.value)
