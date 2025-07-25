from enum import Enum


class AuthenticateXUserTenant(str, Enum):
    LITECARD = "litecard"
    SHAKEWELL = "shakewell"

    def __str__(self) -> str:
        return str(self.value)
