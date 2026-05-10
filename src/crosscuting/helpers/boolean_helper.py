from typing import final


@final
class BooleanHelper:
    DEFAULT: bool = False

    def __init__(self) -> None:
        raise RuntimeError("BooleanHelper no puede ser instanciado")

    @staticmethod
    def get_default(value: bool | None = None) -> bool:
        return value if value is not None else BooleanHelper.DEFAULT
