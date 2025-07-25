from enum import Enum


class SettingsV1ExternalProvider(str, Enum):
    CIRCLES = "CIRCLES"
    LITECARD = "LITECARD"
    SHOPIFY = "SHOPIFY"
    SQUARE = "SQUARE"
    ZII_POS = "ZII_POS"

    def __str__(self) -> str:
        return str(self.value)
