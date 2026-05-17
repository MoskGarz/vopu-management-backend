from typing import final

from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

from src.features.cliente.add_cliente.application.assembler.impl.add_cliente_entity_assembler_impl import (
    AddClienteEntityAssemblerImpl,
)
from src.features.cliente.add_cliente.application.use_case.domain.add_cliente_domain import (
    AddClienteDomain,
)
from src.infrastructure.persistence.adapter.sqlmodel.assembler.impl.add_cliente_sqlmodel_assembler_impl import (
    AddClienteSQLModelAssemblerImpl,
)
from src.infrastructure.persistence.adapter.sqlmodel.model.cliente_sqlmodel import (
    ClienteSQLModel,
)
from src.infrastructure.persistence.repository.entity.cliente_entity import (
    ClienteEntity,
)


@final
class ClienteSQLModelAdapter:
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def save(self, domain: AddClienteDomain) -> None:
        entity: ClienteEntity = AddClienteEntityAssemblerImpl.to_entity(domain)
        model: ClienteSQLModel = AddClienteSQLModelAssemblerImpl.to_sqlmodel(entity)
        self._session.add(model)
        await self._session.commit()

    async def exists_by_numero_documento(self, numero_documento: str) -> bool:
        statement = select(ClienteSQLModel).where(
            ClienteSQLModel.numero_documento == numero_documento
        )
        result = await self._session.execute(statement)
        return result.scalars().first() is not None

    async def exists_by_telefono(self, telefono: str) -> bool:
        statement = select(ClienteSQLModel).where(ClienteSQLModel.telefono == telefono)
        result = await self._session.execute(statement)
        return result.scalars().first() is not None

    async def find_by_id(self, id) -> AddClienteDomain | None:
        statement = select(ClienteSQLModel).where(ClienteSQLModel.id == id)
        result = await self._session.execute(statement)
        model = result.scalars().first()
        if model is None:
            return None
        entity = AddClienteSQLModelAssemblerImpl.to_entity(model)
        return AddClienteEntityAssemblerImpl.to_domain(entity)
