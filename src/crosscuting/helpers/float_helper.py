from typing import final


@final
class FloatHelper:
    DEFAULT: float = 0.0

    def __init__(self) -> None:
        raise RuntimeError("FloatHelper no puede ser instanciado")

    @staticmethod
    def get_default(value: float | None = None) -> float:
        return value if value is not None else FloatHelper.DEFAULT

    @staticmethod
    def is_non_negative(value: float | None) -> bool:
        return FloatHelper.get_default(value) >= 0.0

    @staticmethod
    def approximate_to_nearest_hundred(value: float | None) -> float:
        safe_value = FloatHelper.get_default(value)
        if safe_value < 0.0:
            return FloatHelper.DEFAULT
        return round(safe_value / 100.0) * 100.0

    @staticmethod
    def approximate_to_nearest_thousand(value: float | None) -> float:
        safe_value = FloatHelper.get_default(value)
        if safe_value < 0.0:
            return FloatHelper.DEFAULT
        return round(safe_value / 1000.0) * 1000.0
