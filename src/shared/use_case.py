from typing import Any, Protocol


class UseCase(Protocol):
    def execute(self, data: Any) -> Any: ...
