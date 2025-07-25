from enum import Enum


class TemplateCardExpiryV1Type2FromActivationTimezone(str, Enum):
    AUSTRALIAADELAIDE = "Australia/Adelaide"
    AUSTRALIABRISBANE = "Australia/Brisbane"
    AUSTRALIADARWIN = "Australia/Darwin"
    AUSTRALIAHOBART = "Australia/Hobart"
    AUSTRALIAMELBOURNE = "Australia/Melbourne"
    AUSTRALIAPERTH = "Australia/Perth"
    AUSTRALIASYDNEY = "Australia/Sydney"

    def __str__(self) -> str:
        return str(self.value)
