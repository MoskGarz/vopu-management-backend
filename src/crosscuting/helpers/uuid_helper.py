from typing import final
from uuid import UUID, uuid4


@final
class UUIDHelper:
    DEFAULT: UUID = UUID("00000000-0000-0000-0000-000000000000")

    def __init__(self) -> None:
        raise RuntimeError("UUIDHelper no puede ser instanciado")

    @staticmethod
    def get_default(value: UUID | None = None) -> UUID:
        return value if value is not None else UUIDHelper.DEFAULT

    @staticmethod
    def generate_new_uuid() -> UUID:
        return uuid4()

    @staticmethod
    def is_default_uuid(value: UUID | None) -> bool:
        return UUIDHelper.get_default(value) == UUIDHelper.DEFAULT

    @staticmethod
    def get_from_string(value: str | None) -> UUID:
        from src.crosscuting.helpers.text_helper import TextHelper

        if TextHelper.is_empty_with_strip(value):
            return UUIDHelper.DEFAULT
        try:
            return UUID(str(value).strip())
        except ValueError:
            return UUIDHelper.DEFAULT
