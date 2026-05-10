from abc import ABC
from uuid import UUID

from src.crosscuting.helpers.uuid_helper import UUIDHelper


class Domain(ABC):
    def __init__(self, id: UUID | None = None) -> None:
        self._id = UUIDHelper.get_default(id)

    @property
    def id(self) -> UUID:
        return self._id

    @id.setter
    def id(self, value: UUID | None) -> None:
        self._id = UUIDHelper.get_default(value)
