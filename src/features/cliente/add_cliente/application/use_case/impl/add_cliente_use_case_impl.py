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

    def execute(self, data: AddClienteDomain) -> None:
        try:
            ValidateAddClienteDataConsistency.validate(data)
            self._validate_unique_documento(data)
            self._validate_unique_telefono(data)
            self._cliente_repository.save(data)
        except VopuException:
            raise
        except Exception as e:
            raise VopuException.create(
                "infraestructura.error_inesperado",
                TechnicalMessagesEnum.CACHE_ERROR_CONEXION.value.format(
                    proveedor="PostgreSQL"
                ),
                e,
            )

    def _validate_unique_documento(self, data: AddClienteDomain) -> None:
        if self._cliente_repository.exists_by_numero_documento(data.numero_documento):
            raise VopuException.create(
                "cliente.documento.duplicado",
                TechnicalMessagesEnum.CLIENTE_DOCUMENTO_DUPLICADO.value,
            )

    def _validate_unique_telefono(self, data: AddClienteDomain) -> None:
        if self._cliente_repository.exists_by_telefono(data.telefono):
            raise VopuException.create(
                "cliente.telefono.duplicado",
                TechnicalMessagesEnum.CLIENTE_TELEFONO_DUPLICADO.value,
            )
