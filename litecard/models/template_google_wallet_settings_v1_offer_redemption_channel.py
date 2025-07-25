from enum import Enum


class TemplateGoogleWalletSettingsV1OfferRedemptionChannel(str, Enum):
    BOTH = "BOTH"
    INSTORE = "INSTORE"
    ONLINE = "ONLINE"
    TEMPORARY_PRICE_REDUCTION = "TEMPORARY_PRICE_REDUCTION"

    def __str__(self) -> str:
        return str(self.value)
