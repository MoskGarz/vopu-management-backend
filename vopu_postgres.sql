-- ============================================================
-- Vopu Management — Esquema PostgreSQL
-- Migrado desde MySQL 8.0 con las siguientes correcciones:
--   · Tipos nativos: UUID, BOOLEAN, TIMESTAMPTZ
--   · cliente.telefono marcado como UNIQUE
--   · moto.placa corregida a VARCHAR(6) sin espacio
--   · iniciosesion eliminada (reemplazada por Auth0)
--   · empleado_identidad como tabla auxiliar de autenticación
--   · Restricciones UNIQUE explícitas donde el modelo las define
-- ============================================================

-- Extensión para UUID autogenerado
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- ------------------------------------------------------------
-- CATÁLOGOS (datos predefinidos, solo lectura)
-- ------------------------------------------------------------

CREATE TABLE departamento (
    id      UUID        PRIMARY KEY DEFAULT uuid_generate_v4(),
    nombre  VARCHAR(50) NOT NULL,
    CONSTRAINT uq_departamento_nombre UNIQUE (nombre)
);

CREATE TABLE ciudad (
    id           UUID        PRIMARY KEY DEFAULT uuid_generate_v4(),
    nombre       VARCHAR(50) NOT NULL,
    departamento UUID        NOT NULL REFERENCES departamento(id),
    CONSTRAINT uq_ciudad_nombre_departamento UNIQUE (nombre, departamento)
);

CREATE TABLE estado_pedido (
    id     UUID        PRIMARY KEY DEFAULT uuid_generate_v4(),
    nombre VARCHAR(32) NOT NULL,
    CONSTRAINT uq_estado_pedido_nombre UNIQUE (nombre)
);

CREATE TABLE tipo_direccion (
    id     UUID        PRIMARY KEY DEFAULT uuid_generate_v4(),
    nombre VARCHAR(15) NOT NULL,
    CONSTRAINT uq_tipo_direccion_nombre UNIQUE (nombre)
);

-- ------------------------------------------------------------
-- EMPLEADOS Y ROLES
-- ------------------------------------------------------------

CREATE TABLE empleado (
    id                UUID        PRIMARY KEY DEFAULT uuid_generate_v4(),
    numero_documento  VARCHAR(10) NOT NULL,
    nombre            VARCHAR(50) NOT NULL,
    primer_apellido   VARCHAR(50) NOT NULL,
    segundo_apellido  VARCHAR(50),
    telefono          VARCHAR(10) NOT NULL,
    CONSTRAINT uq_empleado_numero_documento UNIQUE (numero_documento),
    CONSTRAINT uq_empleado_telefono         UNIQUE (telefono)
);

-- Tabla auxiliar de autenticación (desacoplada del proveedor)
CREATE TABLE empleado_identidad (
    id           UUID         PRIMARY KEY DEFAULT uuid_generate_v4(),
    empleado     UUID         NOT NULL REFERENCES empleado(id),
    proveedor    VARCHAR(50)  NOT NULL,   -- 'auth0', 'cognito', 'keycloak', etc.
    proveedor_id VARCHAR(128) NOT NULL,   -- el sub/user_id del proveedor
    activo       BOOLEAN      NOT NULL DEFAULT TRUE,
    CONSTRAINT uq_empleado_identidad_empleado    UNIQUE (empleado),
    CONSTRAINT uq_empleado_identidad_proveedor_id UNIQUE (proveedor, proveedor_id)
);

CREATE TABLE administrador (
    id            UUID    PRIMARY KEY DEFAULT uuid_generate_v4(),
    empleado      UUID    NOT NULL REFERENCES empleado(id),
    estado_cuenta BOOLEAN NOT NULL DEFAULT TRUE,
    CONSTRAINT uq_administrador_empleado UNIQUE (empleado)
);

CREATE TABLE recepcionista (
    id            UUID    PRIMARY KEY DEFAULT uuid_generate_v4(),
    empleado      UUID    NOT NULL REFERENCES empleado(id),
    estado_cuenta BOOLEAN NOT NULL DEFAULT TRUE,
    CONSTRAINT uq_recepcionista_empleado UNIQUE (empleado)
);

CREATE TABLE domiciliario (
    id            UUID    PRIMARY KEY DEFAULT uuid_generate_v4(),
    empleado      UUID    NOT NULL REFERENCES empleado(id),
    estado_cuenta BOOLEAN NOT NULL DEFAULT TRUE,
    CONSTRAINT uq_domiciliario_empleado UNIQUE (empleado)
);

-- ------------------------------------------------------------
-- CLIENTES
-- ------------------------------------------------------------

CREATE TABLE cliente (
    id               UUID        PRIMARY KEY DEFAULT uuid_generate_v4(),
    numero_documento VARCHAR(10) NOT NULL,
    nombre_completo  VARCHAR(50) NOT NULL,
    telefono         VARCHAR(10) NOT NULL,
    CONSTRAINT uq_cliente_numero_documento UNIQUE (numero_documento),
    CONSTRAINT uq_cliente_telefono         UNIQUE (telefono)
);

-- ------------------------------------------------------------
-- MOTOS
-- ------------------------------------------------------------

CREATE TABLE moto (
    id          UUID         PRIMARY KEY DEFAULT uuid_generate_v4(),
    propietario UUID         NOT NULL REFERENCES domiciliario(id),
    placa       VARCHAR(6)   NOT NULL,
    descripcion VARCHAR(500) NOT NULL,
    CONSTRAINT uq_moto_placa UNIQUE (placa)
);

-- ------------------------------------------------------------
-- DIRECCIONES
-- ------------------------------------------------------------

CREATE TABLE direccion (
    id        UUID         PRIMARY KEY DEFAULT uuid_generate_v4(),
    ciudad    UUID         NOT NULL REFERENCES ciudad(id),
    direccion VARCHAR(100) NOT NULL,
    CONSTRAINT uq_direccion_texto_ciudad UNIQUE (direccion, ciudad)
);

-- ------------------------------------------------------------
-- PEDIDOS
-- ------------------------------------------------------------

CREATE TABLE pedido (
    id            UUID         PRIMARY KEY DEFAULT uuid_generate_v4(),
    cliente       UUID         NOT NULL REFERENCES cliente(id),
    asesor        UUID         NOT NULL REFERENCES recepcionista(id),
    orden_pedido  VARCHAR(12)  NOT NULL,
    descripcion   VARCHAR(500),
    valor         INTEGER      NOT NULL,
    fecha_creacion TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    CONSTRAINT uq_pedido_orden_pedido UNIQUE (orden_pedido)
);

CREATE TABLE direccion_pedido (
    id                   UUID         PRIMARY KEY DEFAULT uuid_generate_v4(),
    pedido               UUID         NOT NULL REFERENCES pedido(id),
    direccion            UUID         NOT NULL REFERENCES direccion(id),
    tipo_direccion       UUID         NOT NULL REFERENCES tipo_direccion(id),
    orden_direccion      INTEGER      NOT NULL,
    informacion_adicional VARCHAR(500),
    CONSTRAINT uq_direccion_pedido_orden UNIQUE (pedido, direccion, orden_direccion)
);

-- ------------------------------------------------------------
-- ASIGNACIONES Y ESTADOS
-- ------------------------------------------------------------

CREATE TABLE pedido_domiciliario (
    id                     UUID        PRIMARY KEY DEFAULT uuid_generate_v4(),
    pedido                 UUID        NOT NULL REFERENCES pedido(id),
    domiciliario_encargado UUID        NOT NULL REFERENCES domiciliario(id),
    estado_pedido          UUID        NOT NULL REFERENCES estado_pedido(id),
    fecha_asignacion       TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    CONSTRAINT uq_pedido_domiciliario UNIQUE (pedido, domiciliario_encargado)
);

-- ------------------------------------------------------------
-- COMISIONES
-- ------------------------------------------------------------

CREATE TABLE comision (
    id                           UUID        PRIMARY KEY DEFAULT uuid_generate_v4(),
    pedido_domiciliario_encargado UUID       NOT NULL REFERENCES pedido_domiciliario(id),
    fecha_finalizacion           TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    valor                        INTEGER     NOT NULL,
    esta_paga                    BOOLEAN     NOT NULL DEFAULT FALSE,
    CONSTRAINT uq_comision_pedido_domiciliario UNIQUE (pedido_domiciliario_encargado)
);

-- ------------------------------------------------------------
-- ÍNDICES para columnas usadas frecuentemente en filtros
-- ------------------------------------------------------------

CREATE INDEX idx_empleado_numero_documento  ON empleado(numero_documento);
CREATE INDEX idx_empleado_telefono          ON empleado(telefono);
CREATE INDEX idx_cliente_numero_documento   ON cliente(numero_documento);
CREATE INDEX idx_cliente_telefono           ON cliente(telefono);
CREATE INDEX idx_moto_placa                 ON moto(placa);
CREATE INDEX idx_pedido_orden               ON pedido(orden_pedido);
CREATE INDEX idx_pedido_fecha               ON pedido(fecha_creacion);
CREATE INDEX idx_pedido_domiciliario_estado ON pedido_domiciliario(estado_pedido);
CREATE INDEX idx_comision_esta_paga         ON comision(esta_paga);
CREATE INDEX idx_empleado_identidad_proveedor_id ON empleado_identidad(proveedor_id);

-- ------------------------------------------------------------
-- DATOS SEMILLA (catálogos predefinidos)
-- ------------------------------------------------------------

INSERT INTO estado_pedido (id, nombre) VALUES
    ('964fcae4-b047-11f0-8716-00155d7f30d8', 'Confirmado'),
    ('964ff93e-b047-11f0-8716-00155d7f30d8', 'Pendiente por entregar'),
    ('964ffb4a-b047-11f0-8716-00155d7f30d8', 'Pendiente por pagar'),
    ('964ffbaa-b047-11f0-8716-00155d7f30d8', 'Finalizado'),
    ('964ffbfe-b047-11f0-8716-00155d7f30d8', 'Cancelado');

INSERT INTO tipo_direccion (id, nombre) VALUES
    ('9cfedafd-b047-11f0-8716-00155d7f30d8', 'Entrega'),
    ('9cfedec6-b047-11f0-8716-00155d7f30d8', 'Recogida');

INSERT INTO departamento (id, nombre) VALUES
    ('2baef523-b048-11f0-8716-00155d7f30d8', 'Amazonas'),
    ('2baef8f2-b048-11f0-8716-00155d7f30d8', 'Antioquia'),
    ('2baefa0b-b048-11f0-8716-00155d7f30d8', 'Arauca'),
    ('2baefa5b-b048-11f0-8716-00155d7f30d8', 'Atlántico'),
    ('2baefaae-b048-11f0-8716-00155d7f30d8', 'Bolívar'),
    ('2baefafa-b048-11f0-8716-00155d7f30d8', 'Boyacá'),
    ('2baefb44-b048-11f0-8716-00155d7f30d8', 'Caldas'),
    ('2baefba7-b048-11f0-8716-00155d7f30d8', 'Caquetá'),
    ('2baefbfc-b048-11f0-8716-00155d7f30d8', 'Casanare'),
    ('2baefc61-b048-11f0-8716-00155d7f30d8', 'Cauca'),
    ('2baefcc1-b048-11f0-8716-00155d7f30d8', 'Cesar'),
    ('2baefd08-b048-11f0-8716-00155d7f30d8', 'Chocó'),
    ('2baefd51-b048-11f0-8716-00155d7f30d8', 'Córdoba'),
    ('2baefda4-b048-11f0-8716-00155d7f30d8', 'Cundinamarca'),
    ('2baefde8-b048-11f0-8716-00155d7f30d8', 'Guainía'),
    ('2baefe30-b048-11f0-8716-00155d7f30d8', 'Guaviare'),
    ('2baefe79-b048-11f0-8716-00155d7f30d8', 'Huila'),
    ('2baefec4-b048-11f0-8716-00155d7f30d8', 'La Guajira'),
    ('2baeff09-b048-11f0-8716-00155d7f30d8', 'Magdalena'),
    ('2baeff5c-b048-11f0-8716-00155d7f30d8', 'Meta'),
    ('2baeffa3-b048-11f0-8716-00155d7f30d8', 'Nariño'),
    ('2baf0019-b048-11f0-8716-00155d7f30d8', 'Norte de Santander'),
    ('2baf0067-b048-11f0-8716-00155d7f30d8', 'Putumayo'),
    ('2baf00b1-b048-11f0-8716-00155d7f30d8', 'Quindío'),
    ('2baf00fa-b048-11f0-8716-00155d7f30d8', 'Risaralda'),
    ('2baf0141-b048-11f0-8716-00155d7f30d8', 'San Andrés y Providencia'),
    ('2baf0189-b048-11f0-8716-00155d7f30d8', 'Santander'),
    ('2baf01cf-b048-11f0-8716-00155d7f30d8', 'Sucre'),
    ('2baf023c-b048-11f0-8716-00155d7f30d8', 'Tolima'),
    ('2baf0280-b048-11f0-8716-00155d7f30d8', 'Valle del Cauca'),
    ('2baf02c7-b048-11f0-8716-00155d7f30d8', 'Vaupés'),
    ('2baf030e-b048-11f0-8716-00155d7f30d8', 'Vichada');
