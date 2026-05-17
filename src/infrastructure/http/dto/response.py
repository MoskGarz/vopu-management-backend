from typing import Generic, TypeVar

from pydantic import BaseModel

T = TypeVar("T")


class Response(BaseModel, Generic[T]):
    succeeded: bool = True
    messages: list[str] = []
    data: T | None = None

    @staticmethod
    def ok(data: T | None = None) -> "Response[T]":
        return Response(succeeded=True, data=data, messages=[])

    @staticmethod
    def error(messages: list[str]) -> "Response":
        return Response(succeeded=False, data=None, messages=messages)
