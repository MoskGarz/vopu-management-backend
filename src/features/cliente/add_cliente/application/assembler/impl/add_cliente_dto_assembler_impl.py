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

    @staticmethod
    def to_domain_list(dto_list: list[AddClienteDTO] | None) -> list[AddClienteDomain]:
        safe_list = dto_list if dto_list is not None else []
        return [AddClienteDTOAssemblerImpl.to_domain(dto) for dto in safe_list]

    @staticmethod
    def to_dto_list(domain_list: list[AddClienteDomain] | None) -> list[AddClienteDTO]:
        safe_list = domain_list if domain_list is not None else []
        return [AddClienteDTOAssemblerImpl.to_dto(domain) for domain in safe_list]
