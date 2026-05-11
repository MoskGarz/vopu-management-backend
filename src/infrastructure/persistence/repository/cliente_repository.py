from typing import Protocol
from uuid import UUID

from src.features.cliente.add_cliente.application.use_case.domain.add_cliente_domain import (
    AddClienteDomain,
)


class ClienteRepository(Protocol):
    def save(self, domain: AddClienteDomain) -> None: ...

    def exists_by_numero_documento(self, numero_documento: str) -> bool: ...

    def exists_by_telefono(self, telefono: str) -> bool: ...

    def find_by_id(self, id: UUID) -> AddClienteDomain | None: ...
