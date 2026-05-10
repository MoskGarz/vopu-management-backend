import re
from typing import final

from src.crosscuting.helpers.text_helper import TextHelper


@final
class PlateHelper:
    DEFAULT: str = "AAA00A"
    _PATTERN: re.Pattern = re.compile(r"^[A-Z]{3}\d{2}[A-Z]$")

    def __init__(self) -> None:
        raise RuntimeError("PlateHelper no puede ser instanciado")

    @staticmethod
    def get_default(value: str | None = None) -> str:
        sanitized = PlateHelper.sanitize(value)
        return (
            sanitized if PlateHelper.is_format_valid(sanitized) else PlateHelper.DEFAULT
        )

    @staticmethod
    def sanitize(value: str | None) -> str:
        return (
            TextHelper.get_default_with_strip(value)
            .upper()
            .replace(" ", "")
            .replace("-", "")
        )

    @staticmethod
    def is_format_valid(value: str | None) -> bool:
        return bool(PlateHelper._PATTERN.match(TextHelper.get_default(value)))
