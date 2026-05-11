from typing import Protocol

from src.features.cliente.add_cliente.application.input_port.dto.add_cliente_dto import (
    AddClienteDTO,
)


class AddClienteInputPort(Protocol):
    def execute(self, data: AddClienteDTO) -> None: ...
