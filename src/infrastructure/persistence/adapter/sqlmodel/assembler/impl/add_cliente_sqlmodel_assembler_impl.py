from typing import final

from src.infrastructure.persistence.adapter.sqlmodel.model.cliente_sqlmodel import (
    ClienteSQLModel,
)
from src.infrastructure.persistence.repository.entity.cliente_entity import (
    ClienteEntity,
)


@final
class AddClienteSQLModelAssemblerImpl:
    def __init__(self) -> None:
        raise RuntimeError("AddClienteSQLModelAssemblerImpl no puede ser instanciado")

    @staticmethod
    def to_sqlmodel(entity: ClienteEntity | None) -> ClienteSQLModel:
        safe_entity = entity if entity is not None else ClienteEntity()
        return ClienteSQLModel(
            id=safe_entity.id,
            numero_documento=safe_entity.numero_documento,
            nombre_completo=safe_entity.nombre_completo,
            telefono=safe_entity.telefono,
        )

    @staticmethod
    def to_entity(model: ClienteSQLModel | None) -> ClienteEntity:
        if model is None:
            return ClienteEntity()
        return ClienteEntity(
            id=model.id,
            numero_documento=model.numero_documento,
            nombre_completo=model.nombre_completo,
            telefono=model.telefono,
        )

    @staticmethod
    def to_sqlmodel_list(
        entity_list: list[ClienteEntity] | None,
    ) -> list[ClienteSQLModel]:
        safe_list = entity_list if entity_list is not None else []
        return [
            AddClienteSQLModelAssemblerImpl.to_sqlmodel(entity) for entity in safe_list
        ]

    @staticmethod
    def to_entity_list(model_list: list[ClienteSQLModel] | None) -> list[ClienteEntity]:
        safe_list = model_list if model_list is not None else []
        return [AddClienteSQLModelAssemblerImpl.to_entity(model) for model in safe_list]
