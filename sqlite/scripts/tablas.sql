.open Unidad2.db

CREATE TABLE clientes
(
  id NUMBER(4) not null,
  nombre VARCHAR(20) not null,
  apellidos VARCHAR(20) not null,
  rfc VARCHAR(12) not null,
  email VARCHAR(30),
  telefono number(10),
  CONSTRAINT pkIdClientes PRIMARY KEY(id)
);

CREATE TABLE sucursales
(
  id number(15) not null,
  nombre VARCHAR(30) not null,
  direccion VARCHAR(40) not null,
  latitud NUMBER(15) not null,
  longitud NUMBER(15) not null,
  CONSTRAINT pkIdSucursales PRIMARY KEY(id)
);

CREATE TABLE productos  
(
  id VARCHAR(15) not null,
  nombre VARCHAR(30) not null,
  unidadMedida VARCHAR(15) not null,
  precioUnitario NUMBER(10) not null,
  CONSTRAINT pkIdProductos PRIMARY KEY(id)
);

CREATE TABLE ventas
(
  id NUMBER(7) not null,
  sucursalId NUMBER(4) not null,
  clientesId number(15) not null,
  fecha DATE not null,
  CONSTRAINT pkIdVentas PRIMARY KEY(id),
  CONSTRAINT fkIdSucursal FOREIGN KEY (sucursalId) REFERENCES sucursales (id),
  CONSTRAINT fkIdCleintes FOREIGN KEY (clientesId) REFERENCES clientes (id)
);

CREATE TABLE detalles
(
  id number(15) not null,
  ventasId NUMBER(7) not null,
  productosId VARCHAR(15) not null,
  cantidad NUMBER(4) not null,
  CONSTRAINT pkIdDetalles PRIMARY KEY (id),
  CONSTRAINT fkIdVentas FOREIGN KEY (ventasId) REFERENCES ventas (id),
  CONSTRAINT fkIdProductos FOREIGN KEY (productosId) REFERENCES productos (id)
);