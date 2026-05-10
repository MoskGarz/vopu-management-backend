from typing import Any, Protocol


class InputPort(Protocol):
    def execute(self, data: Any) -> Any: ...
