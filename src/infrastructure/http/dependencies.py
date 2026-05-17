from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.features.cliente.add_cliente.application.input_port.impl.add_cliente_interactor import (
    AddClienteInteractor,
)
from src.features.cliente.add_cliente.application.use_case.impl.add_cliente_use_case_impl import (
    AddClienteUseCaseImpl,
)
from src.infrastructure.persistence.adapter.sqlmodel.cliente_sqlmodel_adapter import (
    ClienteSQLModelAdapter,
)
from src.infrastructure.persistence.config.database import get_session


def get_cliente_interactor(
    session: AsyncSession = Depends(get_session),
) -> AddClienteInteractor:
    repository = ClienteSQLModelAdapter(session)
    use_case = AddClienteUseCaseImpl(repository)
    return AddClienteInteractor(use_case)
