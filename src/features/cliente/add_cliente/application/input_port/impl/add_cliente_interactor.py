from typing import final

from src.features.cliente.add_cliente.application.assembler.impl.add_cliente_dto_assembler_impl import (
    AddClienteDTOAssemblerImpl,
)
from src.features.cliente.add_cliente.application.input_port.dto.add_cliente_dto import (
    AddClienteDTO,
)
from src.features.cliente.add_cliente.application.use_case.add_cliente_use_case import (
    AddClienteUseCase,
)


@final
class AddClienteInteractor:
    def __init__(self, use_case: AddClienteUseCase) -> None:
        self._use_case = use_case

    def execute(self, data: AddClienteDTO) -> None:
        domain = AddClienteDTOAssemblerImpl.to_domain(data)
        self._use_case.execute(domain)
