from pydantic import BaseModel


class AddClienteRequest(BaseModel):
    numero_documento: str = ""
    nombre_completo: str = ""
    telefono: str = ""
