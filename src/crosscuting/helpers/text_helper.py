from typing import final


@final
class TextHelper:
    EMPTY: str = ""

    def __init__(self) -> None:
        raise RuntimeError("TextHelper no puede ser instanciado")

    @staticmethod
    def get_default(value: str | None) -> str:
        return value if value is not None else TextHelper.EMPTY

    @staticmethod
    def get_default_with_strip(value: str | None) -> str:
        return TextHelper.get_default(value).strip()

    @staticmethod
    def is_empty(value: str | None) -> bool:
        return TextHelper.get_default(value) == TextHelper.EMPTY

    @staticmethod
    def is_empty_with_strip(value: str | None) -> bool:
        return TextHelper.get_default_with_strip(value) == TextHelper.EMPTY

    @staticmethod
    def is_length_valid(
        value: str | None, min_length: int, max_length: int, apply_trim: bool
    ) -> bool:
        text = (
            TextHelper.get_default_with_strip(value)
            if apply_trim
            else TextHelper.get_default(value)
        )
        return min_length <= len(text) <= max_length

    @staticmethod
    def is_length_valid_with_trim(
        value: str | None, min_length: int, max_length: int
    ) -> bool:
        return TextHelper.is_length_valid(value, min_length, max_length, True)
