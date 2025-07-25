from enum import Enum


class BaseTemplateV1Type(str, Enum):
    BUSINESS_CARD = "BUSINESS_CARD"
    COUPON = "COUPON"
    EVENT_TICKET = "EVENT_TICKET"
    GENERIC = "GENERIC"

    def __str__(self) -> str:
        return str(self.value)
