from typing import final
from uuid import UUID

from src.crosscuting.domain import Domain
from src.crosscuting.helpers.text_helper import TextHelper
from src.crosscuting.helpers.uuid_helper import UUIDHelper


@final
class AddClienteDomain(Domain):
    def __init__(
        self,
        id: UUID | None = None,
        numero_documento: str = "",
        nombre_completo: str = "",
        telefono: str = "",
    ) -> None:
        super().__init__(id if id is not None else UUIDHelper.generate_new_uuid())
        self.numero_documento = numero_documento
        self.nombre_completo = nombre_completo
        self.telefono = telefono

    @property
    def numero_documento(self) -> str:
        return self._numero_documento

    @numero_documento.setter
    def numero_documento(self, value: str) -> None:
        self._numero_documento = TextHelper.get_default_with_strip(value)

    @property
    def nombre_completo(self) -> str:
        return self._nombre_completo

    @nombre_completo.setter
    def nombre_completo(self, value: str) -> None:
        self._nombre_completo = TextHelper.get_default_with_strip(value)

    @property
    def telefono(self) -> str:
        return self._telefono

    @telefono.setter
    def telefono(self, value: str) -> None:
        self._telefono = TextHelper.get_default_with_strip(value)
