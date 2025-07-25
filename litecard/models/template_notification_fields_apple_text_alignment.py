from enum import Enum


class TemplateNotificationFieldsAppleTextAlignment(str, Enum):
    PKTEXTALIGNMENTCENTER = "PKTextAlignmentCenter"
    PKTEXTALIGNMENTLEFT = "PKTextAlignmentLeft"
    PKTEXTALIGNMENTNATURAL = "PKTextAlignmentNatural"
    PKTEXTALIGNMENTRIGHT = "PKTextAlignmentRight"

    def __str__(self) -> str:
        return str(self.value)
