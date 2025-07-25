from enum import Enum


class SignUpOptionsSourceEmail(str, Enum):
    DONOTREPLYSHAKEWELLWALLET_COM = "donotreply@shakewellwallet.com"
    NOREPLYLUNE_LITECARD_IO = "noreply@lune.litecard.io"
    TARFISHLITECARD_IO = "tarfish@litecard.io"

    def __str__(self) -> str:
        return str(self.value)
