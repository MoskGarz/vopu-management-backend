from typing import final


@final
class IntHelper:
    DEFAULT: int = 0
    MIN_VALUE: int = 1

    def __init__(self) -> None:
        raise RuntimeError("IntHelper no puede ser instanciado")

    @staticmethod
    def get_default(value: int | None = None) -> int:
        return value if value is not None else IntHelper.DEFAULT

    @staticmethod
    def is_range_valid(value: int | None, min_value: int, max_value: int) -> bool:
        safe_value = IntHelper.get_default(value)
        return min_value <= safe_value <= max_value

    @staticmethod
    def get_valid_order(value: int | None) -> int:
        safe_value = IntHelper.get_default(value)
        return safe_value if safe_value >= IntHelper.MIN_VALUE else IntHelper.DEFAULT
