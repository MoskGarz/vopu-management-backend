from datetime import datetime, timezone
from typing import final


@final
class DateTimeHelper:
    def __init__(self) -> None:
        raise RuntimeError("DateTimeHelper no puede ser instanciado")

    @staticmethod
    def get_default(value: datetime | None = None) -> datetime:
        return value if value is not None else datetime.now(timezone.utc)

    @staticmethod
    def format(value: datetime | None = None) -> str:
        return DateTimeHelper.get_default(value).strftime("%d/%m/%Y %H:%M")
