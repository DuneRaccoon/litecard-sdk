from enum import Enum


class TemplateGoogleWalletSettingsV1MultipleDevicesAndUsersStatus(str, Enum):
    MULTIPLE_HOLDERS = "MULTIPLE_HOLDERS"
    ONE_USER_ALL_DEVICES = "ONE_USER_ALL_DEVICES"
    ONE_USER_ONE_DEVICE = "ONE_USER_ONE_DEVICE"

    def __str__(self) -> str:
        return str(self.value)
