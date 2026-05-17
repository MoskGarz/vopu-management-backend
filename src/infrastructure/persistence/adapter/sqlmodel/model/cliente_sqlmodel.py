from uuid import UUID, uuid4

from sqlmodel import Field, SQLModel


class ClienteSQLModel(SQLModel, table=True):
    __tablename__ = "cliente"  # type: ignore

    id: UUID = Field(default_factory=uuid4, primary_key=True)
    numero_documento: str = Field(max_length=10, nullable=False, unique=True)
    nombre_completo: str = Field(max_length=50, nullable=False)
    telefono: str = Field(max_length=15, nullable=False, unique=True)
