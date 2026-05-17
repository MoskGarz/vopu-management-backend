from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status

from src.crosscuting.exception.vopu_exception import VopuException
from src.features.cliente.add_cliente.application.input_port.dto.add_cliente_dto import (
    AddClienteDTO,
)
from src.features.cliente.add_cliente.application.input_port.impl.add_cliente_interactor import (
    AddClienteInteractor,
)
from src.infrastructure.http.dependencies import get_cliente_interactor
from src.infrastructure.http.dto.add_cliente_request import AddClienteRequest
from src.infrastructure.http.dto.response import Response

router = APIRouter(prefix="/api/v1/clientes", tags=["Clientes"])


@router.post("", status_code=status.HTTP_201_CREATED)
async def add_cliente(
    request: AddClienteRequest,
    interactor: Annotated[AddClienteInteractor, Depends(get_cliente_interactor)],
) -> Response:
    try:
        dto = AddClienteDTO(
            numero_documento=request.numero_documento,
            nombre_completo=request.nombre_completo,
            telefono=request.telefono,
        )
        await interactor.execute(dto)
        return Response.ok()
    except VopuException as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=Response.error([e.user_message_key]).model_dump(),
        )
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=Response.error(["infraestructura.error_inesperado"]).model_dump(),
        )
