from typing import final

from src.features.cliente.add_cliente.application.use_case.domain.add_cliente_domain import (
    AddClienteDomain,
)
from src.infrastructure.persistence.repository.entity.cliente_entity import (
    ClienteEntity,
)


@final
class AddClienteEntityAssemblerImpl:
    def __init__(self) -> None:
        raise RuntimeError("AddClienteEntityAssemblerImpl no puede ser instanciado")

    @staticmethod
    def to_entity(domain: AddClienteDomain | None) -> ClienteEntity:
        safe_domain = domain if domain is not None else AddClienteDomain()
        return ClienteEntity(
            id=safe_domain.id,
            numero_documento=safe_domain.numero_documento,
            nombre_completo=safe_domain.nombre_completo,
            telefono=safe_domain.telefono,
        )

    @staticmethod
    def to_domain(entity: ClienteEntity | None) -> AddClienteDomain:
        safe_entity = entity if entity is not None else ClienteEntity()
        return AddClienteDomain(
            id=safe_entity.id,
            numero_documento=safe_entity.numero_documento,
            nombre_completo=safe_entity.nombre_completo,
            telefono=safe_entity.telefono,
        )

    @staticmethod
    def to_entity_list(
        domain_list: list[AddClienteDomain] | None,
    ) -> list[ClienteEntity]:
        safe_list = domain_list if domain_list is not None else []
        return [AddClienteEntityAssemblerImpl.to_entity(domain) for domain in safe_list]

    @staticmethod
    def to_domain_list(
        entity_list: list[ClienteEntity] | None,
    ) -> list[AddClienteDomain]:
        safe_list = entity_list if entity_list is not None else []
        return [AddClienteEntityAssemblerImpl.to_domain(entity) for entity in safe_list]
