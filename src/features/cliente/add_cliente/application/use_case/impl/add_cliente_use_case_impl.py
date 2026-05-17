from typing import final

from src.crosscuting.exception.vopu_exception import VopuException
from src.crosscuting.messages.technical_messages_enum import TechnicalMessagesEnum
from src.features.cliente.add_cliente.application.use_case.domain.add_cliente_domain import (
    AddClienteDomain,
)
from src.features.cliente.add_cliente.application.use_case.validator.validate_add_cliente_data_consistency import (
    ValidateAddClienteDataConsistency,
)
from src.infrastructure.persistence.repository.cliente_repository import (
    ClienteRepository,
)


@final
class AddClienteUseCaseImpl:
    def __init__(self, cliente_repository: ClienteRepository) -> None:
        self._cliente_repository = cliente_repository

    async def execute(self, data: AddClienteDomain) -> None:
        ValidateAddClienteDataConsistency.validate(data)
        await self._validate_unique_documento(data)
        await self._validate_unique_telefono(data)
        await self._cliente_repository.save(data)

    async def _validate_unique_documento(self, data: AddClienteDomain) -> None:
        if await self._cliente_repository.exists_by_numero_documento(
            data.numero_documento
        ):
            raise VopuException.create(
                "cliente.documento.duplicado",
                TechnicalMessagesEnum.CLIENTE_DOCUMENTO_DUPLICADO.value,
            )

    async def _validate_unique_telefono(self, data: AddClienteDomain) -> None:
        if await self._cliente_repository.exists_by_telefono(data.telefono):
            raise VopuException.create(
                "cliente.telefono.duplicado",
                TechnicalMessagesEnum.CLIENTE_TELEFONO_DUPLICADO.value,
            )
