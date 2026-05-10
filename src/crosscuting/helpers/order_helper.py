import re
from typing import final

from src.crosscuting.helpers.text_helper import TextHelper


@final
class OrderHelper:
    DEFAULT: str = "OP - 000000"
    _PATTERN: re.Pattern = re.compile(r"^OP - \d{6}$")

    def __init__(self) -> None:
        raise RuntimeError("OrderHelper no puede ser instanciado")

    @staticmethod
    def get_default(value: str | None = None) -> str:
        return value if value is not None else OrderHelper.DEFAULT

    @staticmethod
    def format(number: int) -> str:
        return f"OP - {number:06d}"

    @staticmethod
    def is_format_valid(value: str | None) -> bool:
        return bool(OrderHelper._PATTERN.match(TextHelper.get_default(value)))

    @staticmethod
    def is_default_value(value: str | None) -> bool:
        return TextHelper.get_default_with_strip(value) == OrderHelper.DEFAULT
