from enum import Enum


class ImageContentImageType(str, Enum):
    ICON = "icon"
    LOGO = "logo"
    STRIP = "strip"
    THUMBNAIL = "thumbnail"

    def __str__(self) -> str:
        return str(self.value)
