from enum import Enum


class TechnicalMessagesEnum(Enum):
    # ─── EMPLEADO ───────────────────────────────────────────────────────────
    EMPLEADO_ID_INVALIDO = "El id del empleado llegó con valor por defecto o nulo"
    EMPLEADO_DOCUMENTO_INVALIDO = (
        "Campo 'numeroDocumento' de Empleado llegó vacío o nulo"
    )
    EMPLEADO_DOCUMENTO_LONGITUD_INVALIDA = (
        "Campo 'numeroDocumento' de Empleado no cumple longitud entre 7 y 10 caracteres"
    )
    EMPLEADO_DOCUMENTO_FORMATO_INVALIDO = (
        "Campo 'numeroDocumento' de Empleado no cumple patrón de solo dígitos"
    )
    EMPLEADO_NOMBRE_INVALIDO = "Campo 'nombre' de Empleado llegó vacío o nulo"
    EMPLEADO_NOMBRE_LONGITUD_INVALIDA = (
        "Campo 'nombre' de Empleado no cumple longitud entre 2 y 50 caracteres"
    )
    EMPLEADO_NOMBRE_FORMATO_INVALIDO = "Campo 'nombre' de Empleado no cumple patrón de solo letras y caracteres especiales permitidos"
    EMPLEADO_PRIMER_APELLIDO_INVALIDO = (
        "Campo 'primerApellido' de Empleado llegó vacío o nulo"
    )
    EMPLEADO_PRIMER_APELLIDO_LONGITUD_INVALIDA = (
        "Campo 'primerApellido' de Empleado no cumple longitud entre 2 y 50 caracteres"
    )
    EMPLEADO_PRIMER_APELLIDO_FORMATO_INVALIDO = "Campo 'primerApellido' de Empleado no cumple patrón de solo letras y caracteres especiales permitidos"
    EMPLEADO_SEGUNDO_APELLIDO_LONGITUD_INVALIDA = (
        "Campo 'segundoApellido' de Empleado no cumple longitud entre 2 y 50 caracteres"
    )
    EMPLEADO_SEGUNDO_APELLIDO_FORMATO_INVALIDO = "Campo 'segundoApellido' de Empleado no cumple patrón de solo letras y caracteres especiales permitidos"
    EMPLEADO_TELEFONO_INVALIDO = "Campo 'telefono' de Empleado llegó vacío o nulo"
    EMPLEADO_TELEFONO_LONGITUD_INVALIDA = (
        "Campo 'telefono' de Empleado no cumple longitud exacta de 10 caracteres"
    )
    EMPLEADO_TELEFONO_FORMATO_INVALIDO = (
        "Campo 'telefono' de Empleado no cumple patrón de 10 dígitos"
    )
    EMPLEADO_DOCUMENTO_DUPLICADO = (
        "Violación de unicidad: Empleado.numeroDocumento ya existe en BD"
    )
    EMPLEADO_TELEFONO_DUPLICADO = (
        "Violación de unicidad: Empleado.telefono ya existe en BD"
    )
    EMPLEADO_NO_ENCONTRADO = "No se encontró Empleado con el id proporcionado en BD"
    EMPLEADO_EN_USO_EN_PEDIDOS = (
        "No se puede eliminar Empleado porque está referenciado en registros de pedidos"
    )
    EMPLEADO_CUENTA_ACTIVA_NO_ELIMINABLE = (
        "No se puede eliminar Empleado porque su estado de cuenta sigue activo"
    )

    # ─── CLIENTE ────────────────────────────────────────────────────────────
    CLIENTE_ID_INVALIDO = "El id del cliente llegó con valor por defecto o nulo"
    CLIENTE_DOCUMENTO_INVALIDO = "Campo 'numeroDocumento' de Cliente llegó vacío o nulo"
    CLIENTE_DOCUMENTO_LONGITUD_INVALIDA = (
        "Campo 'numeroDocumento' de Cliente no cumple longitud entre 7 y 10 caracteres"
    )
    CLIENTE_DOCUMENTO_FORMATO_INVALIDO = (
        "Campo 'numeroDocumento' de Cliente no cumple patrón de solo dígitos"
    )
    CLIENTE_NOMBRE_COMPLETO_INVALIDO = (
        "Campo 'nombreCompleto' de Cliente llegó vacío o nulo"
    )
    CLIENTE_NOMBRE_COMPLETO_LONGITUD_INVALIDA = (
        "Campo 'nombreCompleto' de Cliente no cumple longitud entre 2 y 50 caracteres"
    )
    CLIENTE_NOMBRE_COMPLETO_FORMATO_INVALIDO = "Campo 'nombreCompleto' de Cliente no cumple patrón de solo letras y caracteres especiales permitidos"
    CLIENTE_TELEFONO_INVALIDO = "Campo 'telefono' de Cliente llegó vacío o nulo"
    CLIENTE_TELEFONO_LONGITUD_INVALIDA = (
        "Campo 'telefono' de Cliente no cumple longitud exacta de 10 caracteres"
    )
    CLIENTE_TELEFONO_FORMATO_INVALIDO = (
        "Campo 'telefono' de Cliente no cumple patrón de 10 dígitos"
    )
    CLIENTE_DOCUMENTO_DUPLICADO = (
        "Violación de unicidad: Cliente.numeroDocumento ya existe en BD"
    )
    CLIENTE_TELEFONO_DUPLICADO = (
        "Violación de unicidad: Cliente.telefono ya existe en BD"
    )
    CLIENTE_NO_ENCONTRADO = "No se encontró Cliente con el id proporcionado en BD"
    CLIENTE_EN_USO_EN_PEDIDOS = (
        "No se puede eliminar Cliente porque está referenciado en registros de pedidos"
    )

    # ─── ADMINISTRADOR ──────────────────────────────────────────────────────
    ADMINISTRADOR_ID_INVALIDO = (
        "El id del administrador llegó con valor por defecto o nulo"
    )
    ADMINISTRADOR_EMPLEADO_INVALIDO = (
        "Campo 'empleado' de Administrador llegó con valor por defecto o nulo"
    )
    ADMINISTRADOR_EMPLEADO_DUPLICADO = (
        "Violación de unicidad: Administrador.empleado ya existe en BD"
    )
    ADMINISTRADOR_NO_ENCONTRADO = (
        "No se encontró Administrador con el id proporcionado en BD"
    )
    ADMINISTRADOR_UNICO_ACTIVO = (
        "No se puede inactivar el único Administrador activo del sistema"
    )
    ADMINISTRADOR_CUENTA_ACTIVA_REQUERIDA = (
        "El Administrador no tiene la cuenta activa para realizar esta operación"
    )

    # ─── RECEPCIONISTA ──────────────────────────────────────────────────────
    RECEPCIONISTA_ID_INVALIDO = (
        "El id del recepcionista llegó con valor por defecto o nulo"
    )
    RECEPCIONISTA_EMPLEADO_INVALIDO = (
        "Campo 'empleado' de Recepcionista llegó con valor por defecto o nulo"
    )
    RECEPCIONISTA_EMPLEADO_DUPLICADO = (
        "Violación de unicidad: Recepcionista.empleado ya existe en BD"
    )
    RECEPCIONISTA_NO_ENCONTRADO = (
        "No se encontró Recepcionista con el id proporcionado en BD"
    )
    RECEPCIONISTA_CUENTA_INACTIVA = (
        "El Recepcionista no tiene la cuenta activa para realizar esta operación"
    )

    # ─── DOMICILIARIO ───────────────────────────────────────────────────────
    DOMICILIARIO_ID_INVALIDO = (
        "El id del domiciliario llegó con valor por defecto o nulo"
    )
    DOMICILIARIO_EMPLEADO_INVALIDO = (
        "Campo 'empleado' de Domiciliario llegó con valor por defecto o nulo"
    )
    DOMICILIARIO_EMPLEADO_DUPLICADO = (
        "Violación de unicidad: Domiciliario.empleado ya existe en BD"
    )
    DOMICILIARIO_NO_ENCONTRADO = (
        "No se encontró Domiciliario con el id proporcionado en BD"
    )
    DOMICILIARIO_CUENTA_INACTIVA = (
        "El Domiciliario no tiene la cuenta activa para realizar esta operación"
    )

    # ─── MOTO ───────────────────────────────────────────────────────────────
    MOTO_ID_INVALIDO = "El id de la moto llegó con valor por defecto o nulo"
    MOTO_PLACA_INVALIDA = "Campo 'placa' de Moto llegó vacío o nulo"
    MOTO_PLACA_LONGITUD_INVALIDA = (
        "Campo 'placa' de Moto no cumple longitud exacta de 6 caracteres"
    )
    MOTO_PLACA_FORMATO_INVALIDO = (
        "Campo 'placa' de Moto no cumple patrón ^[A-Z]{3}\\d{2}[A-Z]$"
    )
    MOTO_DESCRIPCION_INVALIDA = "Campo 'descripcion' de Moto llegó vacío o nulo"
    MOTO_DESCRIPCION_LONGITUD_INVALIDA = (
        "Campo 'descripcion' de Moto no cumple longitud entre 5 y 500 caracteres"
    )
    MOTO_PROPIETARIO_INVALIDO = (
        "Campo 'propietario' de Moto llegó con valor por defecto o nulo"
    )
    MOTO_PLACA_DUPLICADA = "Violación de unicidad: Moto.placa ya existe en BD"
    MOTO_NO_ENCONTRADA = "No se encontró Moto con el id proporcionado en BD"
    MOTO_MINIMO_UNA_POR_DOMICILIARIO = (
        "No se puede eliminar la única moto de un Domiciliario con cuenta activa"
    )

    # ─── PEDIDO ─────────────────────────────────────────────────────────────
    PEDIDO_ID_INVALIDO = "El id del pedido llegó con valor por defecto o nulo"
    PEDIDO_ORDEN_INVALIDA = "Campo 'ordenPedido' de Pedido llegó vacío o nulo"
    PEDIDO_ORDEN_DUPLICADA = "Violación de unicidad: Pedido.ordenPedido ya existe en BD"
    PEDIDO_CLIENTE_INVALIDO = (
        "Campo 'cliente' de Pedido llegó con valor por defecto o nulo"
    )
    PEDIDO_CLIENTE_NO_ENCONTRADO = "No se encontró Cliente referenciado en Pedido en BD"
    PEDIDO_RECEPCIONISTA_INVALIDO = (
        "Campo 'asesor' de Pedido llegó con valor por defecto o nulo"
    )
    PEDIDO_RECEPCIONISTA_NO_ENCONTRADO = (
        "No se encontró Recepcionista referenciado en Pedido en BD"
    )
    PEDIDO_DESCRIPCION_LONGITUD_INVALIDA = (
        "Campo 'descripcion' de Pedido no cumple longitud máxima de 500 caracteres"
    )
    PEDIDO_VALOR_INVALIDO = "Campo 'valor' de Pedido llegó con valor negativo o nulo"
    PEDIDO_VALOR_RANGO_INVALIDO = "Campo 'valor' de Pedido no es múltiplo de 1000"
    PEDIDO_FECHA_INVALIDA = "Campo 'fechaCreacion' de Pedido llegó nulo"
    PEDIDO_YA_ASIGNADO = "No se puede modificar o eliminar Pedido porque ya fue asignado a un Domiciliario"
    PEDIDO_YA_FINALIZADO = "No se puede modificar Pedido porque ya fue finalizado"
    PEDIDO_NO_ENCONTRADO = "No se encontró Pedido con el id proporcionado en BD"

    # ─── DIRECCION ──────────────────────────────────────────────────────────
    DIRECCION_ID_INVALIDA = "El id de la dirección llegó con valor por defecto o nulo"
    DIRECCION_TEXTO_INVALIDO = "Campo 'direccion' de Direccion llegó vacío o nulo"
    DIRECCION_TEXTO_LONGITUD_INVALIDA = (
        "Campo 'direccion' de Direccion no cumple longitud entre 10 y 100 caracteres"
    )
    DIRECCION_CIUDAD_INVALIDA = (
        "Campo 'ciudad' de Direccion llegó con valor por defecto o nulo"
    )
    DIRECCION_CIUDAD_NO_ENCONTRADA = (
        "No se encontró Ciudad referenciada en Direccion en BD"
    )
    DIRECCION_DUPLICADA_EN_CIUDAD = (
        "Violación de unicidad: Direccion.direccion + Direccion.ciudad ya existe en BD"
    )
    DIRECCION_NO_ENCONTRADA = "No se encontró Direccion con el id proporcionado en BD"
    DIRECCION_EN_USO_EN_PEDIDOS = "No se puede eliminar Direccion porque está referenciada en registros de pedidos"

    # ─── DIRECCION_PEDIDO ───────────────────────────────────────────────────
    DIRECCION_PEDIDO_ID_INVALIDO = (
        "El id de DireccionPedido llegó con valor por defecto o nulo"
    )
    DIRECCION_PEDIDO_PEDIDO_INVALIDO = (
        "Campo 'pedido' de DireccionPedido llegó con valor por defecto o nulo"
    )
    DIRECCION_PEDIDO_PEDIDO_NO_ENCONTRADO = (
        "No se encontró Pedido referenciado en DireccionPedido en BD"
    )
    DIRECCION_PEDIDO_ORDEN_INVALIDA = (
        "Campo 'ordenDireccion' de DireccionPedido llegó con valor menor a 1"
    )
    DIRECCION_PEDIDO_ORDEN_DUPLICADA = "Violación de unicidad: DireccionPedido.ordenDireccion ya existe para ese Pedido en BD"
    DIRECCION_PEDIDO_DIRECCION_INVALIDA = (
        "Campo 'direccion' de DireccionPedido llegó con valor por defecto o nulo"
    )
    DIRECCION_PEDIDO_DIRECCION_NO_ENCONTRADA = (
        "No se encontró Direccion referenciada en DireccionPedido en BD"
    )
    DIRECCION_PEDIDO_TIPO_INVALIDO = (
        "Campo 'tipoDireccion' de DireccionPedido llegó con valor por defecto o nulo"
    )
    DIRECCION_PEDIDO_PRIMERA_PARADA_DEBE_SER_RECOGIDA = "Regla de negocio: la primera parada de un Pedido siempre debe ser de tipo Recogida"
    DIRECCION_PEDIDO_PEDIDO_FINALIZADO = (
        "No se pueden modificar paradas de un Pedido que ya fue finalizado"
    )
    DIRECCION_PEDIDO_NO_ENCONTRADO = (
        "No se encontró DireccionPedido con el id proporcionado en BD"
    )
    DIRECCION_PEDIDO_SIN_PARADAS = (
        "El Pedido seleccionado no tiene ninguna parada registrada"
    )

    # ─── PEDIDO_DOMICILIARIO ────────────────────────────────────────────────
    PEDIDO_DOMICILIARIO_ID_INVALIDO = (
        "El id de PedidoDomiciliario llegó con valor por defecto o nulo"
    )
    PEDIDO_DOMICILIARIO_PEDIDO_INVALIDO = (
        "Campo 'pedido' de PedidoDomiciliario llegó con valor por defecto o nulo"
    )
    PEDIDO_DOMICILIARIO_PEDIDO_NO_ENCONTRADO = (
        "No se encontró Pedido referenciado en PedidoDomiciliario en BD"
    )
    PEDIDO_DOMICILIARIO_DOMICILIARIO_INVALIDO = "Campo 'domiciliarioEncargado' de PedidoDomiciliario llegó con valor por defecto o nulo"
    PEDIDO_DOMICILIARIO_DOMICILIARIO_NO_ENCONTRADO = (
        "No se encontró Domiciliario referenciado en PedidoDomiciliario en BD"
    )
    PEDIDO_DOMICILIARIO_FECHA_INVALIDA = (
        "Campo 'fechaAsignacion' de PedidoDomiciliario llegó nulo"
    )
    PEDIDO_DOMICILIARIO_ESTADO_INVALIDO = (
        "Campo 'estadoPedido' de PedidoDomiciliario llegó con valor por defecto o nulo"
    )
    PEDIDO_DOMICILIARIO_ESTADO_TRANSICION_INVALIDA = "Regla de negocio: la transición de estado solicitada no es válida dentro del ciclo del Pedido"
    PEDIDO_DOMICILIARIO_DOMICILIARIO_DUPLICADO = "Violación de unicidad: PedidoDomiciliario.domiciliarioEncargado ya existe para ese Pedido en BD"
    PEDIDO_DOMICILIARIO_PEDIDO_FINALIZADO = (
        "No se puede modificar PedidoDomiciliario porque el Pedido ya fue finalizado"
    )
    PEDIDO_DOMICILIARIO_PEDIDO_CANCELADO = (
        "No se puede modificar PedidoDomiciliario porque el Pedido fue cancelado"
    )
    PEDIDO_DOMICILIARIO_NO_ENCONTRADO = (
        "No se encontró PedidoDomiciliario con el id proporcionado en BD"
    )

    # ─── COMISION ───────────────────────────────────────────────────────────
    COMISION_ID_INVALIDA = "El id de la comisión llegó con valor por defecto o nulo"
    COMISION_PEDIDO_DOMICILIARIO_INVALIDO = "Campo 'pedidoDomiciliarioEncargado' de Comision llegó con valor por defecto o nulo"
    COMISION_PEDIDO_DOMICILIARIO_NO_ENCONTRADO = (
        "No se encontró PedidoDomiciliario referenciado en Comision en BD"
    )
    COMISION_FECHA_INVALIDA = "Campo 'fechaFinalizacion' de Comision llegó nulo"
    COMISION_VALOR_INVALIDO = (
        "Campo 'valor' de Comision llegó con valor negativo o nulo"
    )
    COMISION_YA_PAGA = "No se puede modificar Comision porque ya fue marcada como paga"
    COMISION_NO_ENCONTRADA = "No se encontró Comision con el id proporcionado en BD"

    # ─── CIUDAD ─────────────────────────────────────────────────────────────
    CIUDAD_ID_INVALIDA = "El id de la ciudad llegó con valor por defecto o nulo"
    CIUDAD_NOMBRE_INVALIDO = "Campo 'nombre' de Ciudad llegó vacío o nulo"
    CIUDAD_NOMBRE_LONGITUD_INVALIDA = (
        "Campo 'nombre' de Ciudad no cumple longitud entre 2 y 50 caracteres"
    )
    CIUDAD_DEPARTAMENTO_INVALIDO = (
        "Campo 'departamento' de Ciudad llegó con valor por defecto o nulo"
    )
    CIUDAD_DUPLICADA_EN_DEPARTAMENTO = (
        "Violación de unicidad: Ciudad.nombre + Ciudad.departamento ya existe en BD"
    )
    CIUDAD_NO_ENCONTRADA = "No se encontró Ciudad con el id proporcionado en BD"

    # ─── DEPARTAMENTO ───────────────────────────────────────────────────────
    DEPARTAMENTO_ID_INVALIDO = (
        "El id del departamento llegó con valor por defecto o nulo"
    )
    DEPARTAMENTO_NOMBRE_INVALIDO = "Campo 'nombre' de Departamento llegó vacío o nulo"
    DEPARTAMENTO_NOMBRE_LONGITUD_INVALIDA = (
        "Campo 'nombre' de Departamento no cumple longitud entre 2 y 50 caracteres"
    )
    DEPARTAMENTO_NO_ENCONTRADO = (
        "No se encontró Departamento con el id proporcionado en BD"
    )

    # ─── ESTADO_PEDIDO ──────────────────────────────────────────────────────
    ESTADO_PEDIDO_ID_INVALIDO = (
        "El id del estado de pedido llegó con valor por defecto o nulo"
    )
    ESTADO_PEDIDO_NOMBRE_INVALIDO = "Campo 'nombre' de EstadoPedido llegó vacío o nulo"
    ESTADO_PEDIDO_NO_ENCONTRADO = (
        "No se encontró EstadoPedido con el id proporcionado en BD"
    )

    # ─── TIPO_DIRECCION ─────────────────────────────────────────────────────
    TIPO_DIRECCION_ID_INVALIDO = (
        "El id del tipo de dirección llegó con valor por defecto o nulo"
    )
    TIPO_DIRECCION_NOMBRE_INVALIDO = (
        "Campo 'nombre' de TipoDireccion llegó vacío o nulo"
    )
    TIPO_DIRECCION_NO_ENCONTRADO = (
        "No se encontró TipoDireccion con el id proporcionado en BD"
    )

    # ─── EMPLEADO_IDENTIDAD (Auth0) ─────────────────────────────────────────
    IDENTIDAD_PROVEEDOR_ID_INVALIDO = (
        "Campo 'proveedor_id' de EmpleadoIdentidad llegó vacío o nulo"
    )
    IDENTIDAD_EMPLEADO_INVALIDO = (
        "Campo 'empleado' de EmpleadoIdentidad llegó con valor por defecto o nulo"
    )
    IDENTIDAD_TOKEN_INVALIDO = "El token JWT recibido no es válido o está mal formado"
    IDENTIDAD_TOKEN_EXPIRADO = "El token JWT recibido ha expirado"
    IDENTIDAD_SIN_PERMISOS = (
        "El token JWT no contiene los permisos requeridos para esta operación"
    )
    IDENTIDAD_EMPLEADO_INACTIVO = (
        "El empleado asociado al token JWT tiene la cuenta inactiva"
    )
    IDENTIDAD_NO_ENCONTRADA = (
        "No se encontró EmpleadoIdentidad asociada al proveedor_id del token en BD"
    )

    # ─── INFRAESTRUCTURA ────────────────────────────────────────────────────
    CACHE_ERROR_CONEXION = (
        "Error al intentar conectar con el servidor de caché: {proveedor}"
    )
    CACHE_ERROR_LECTURA = (
        "Error al intentar leer el valor '{clave}' del caché: {proveedor}"
    )
    CACHE_ERROR_ESCRITURA = (
        "Error al intentar escribir el valor '{clave}' en el caché: {proveedor}"
    )
    NOTIFICACION_ERROR_ENVIO = "Error al intentar enviar notificación al destinatario '{destinatario}' a través del proveedor: {proveedor}"
    PARAMETRO_NO_ENCONTRADO = "No se encontró el parámetro '{clave}' en el catálogo de parámetros: {proveedor}"
    PARAMETRO_VALOR_INVALIDO = "El valor retornado para el parámetro '{clave}' no es válido en el catálogo de parámetros: {proveedor}"
    MENSAJE_CLAVE_NO_ENCONTRADA = (
        "No se encontró la clave '{clave}' en el catálogo de mensajes: {proveedor}"
    )
