from typing import Any, Protocol


class Rule(Protocol):
    @staticmethod
    def execute(*args: Any) -> None: ...
