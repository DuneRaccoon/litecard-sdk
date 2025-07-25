from enum import Enum


class SettingsV1PrimaryContact(str, Enum):
    EMAIL = "EMAIL"
    EMAIL_SMS = "EMAIL_SMS"
    SMS = "SMS"

    def __str__(self) -> str:
        return str(self.value)
