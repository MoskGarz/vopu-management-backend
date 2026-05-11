from typing import final

from src.features.cliente.add_cliente.application.input_port.dto.add_cliente_dto import (
    AddClienteDTO,
)
from src.features.cliente.add_cliente.application.use_case.domain.add_cliente_domain import (
    AddClienteDomain,
)


@final
class AddClienteDTOAssemblerImpl:
    def __init__(self) -> None:
        raise RuntimeError("AddClienteDTOAssemblerImpl no puede ser instanciado")

    @staticmethod
    def to_domain(dto: AddClienteDTO | None) -> AddClienteDomain:
        safe_dto = dto if dto is not None else AddClienteDTO()
        return AddClienteDomain(
            numero_documento=safe_dto.numero_documento,
            nombre_completo=safe_dto.nombre_completo,
            telefono=safe_dto.telefono,
        )

    @staticmethod
    def to_dto(domain: AddClienteDomain | None) -> AddClienteDTO:
        safe_domain = domain if domain is not None else AddClienteDomain()
        return AddClienteDTO(
            numero_documento=safe_domain.numero_documento,
            nombre_completo=safe_domain.nombre_completo,
            telefono=safe_domain.telefono,
        )
