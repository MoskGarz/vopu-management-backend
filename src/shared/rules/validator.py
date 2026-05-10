from typing import Any, Protocol


class Validator(Protocol):
    @staticmethod
    def validate(*args: Any) -> None: ...
