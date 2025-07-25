from enum import Enum


class TemplateDataFieldV1AppleFieldSettingsTextAlignment(str, Enum):
    PKTEXTALIGNMENTCENTER = "PKTextAlignmentCenter"
    PKTEXTALIGNMENTLEFT = "PKTextAlignmentLeft"
    PKTEXTALIGNMENTNATURAL = "PKTextAlignmentNatural"
    PKTEXTALIGNMENTRIGHT = "PKTextAlignmentRight"

    def __str__(self) -> str:
        return str(self.value)
