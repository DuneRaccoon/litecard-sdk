from enum import Enum


class TemplateLinkV1Type(str, Enum):
    HELP_URI = "HELP_URI"
    HOMEPAGE_URI = "HOMEPAGE_URI"
    NOT_USED = "NOT_USED"
    URI_EMAIL = "URI_EMAIL"
    URI_TEL = "URI_TEL"
    URI_WEB = "URI_WEB"

    def __str__(self) -> str:
        return str(self.value)
