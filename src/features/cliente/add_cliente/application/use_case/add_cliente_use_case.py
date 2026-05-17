from typing import Protocol

from src.features.cliente.add_cliente.application.use_case.domain.add_cliente_domain import (
    AddClienteDomain,
)


class AddClienteUseCase(Protocol):
    async def execute(self, data: AddClienteDomain) -> None: ...
