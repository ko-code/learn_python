-- Gestion de dataBases

SHOW DATABASES;

CREATE DATABASE test_snake;
CREATE DATABASE IF NOT EXISTS test_snake;
DROP DATABASE test_snake;
DROP DATABASE IF EXISTS test_snake;

-- Usuarios y privilegios

CREATE USER 'mi_user'@'servidor' IDENTIFIED BY 'my_password';

SELECT PASSWORD('my_password');

DROP USER 'mi_user'@'servidor';

GRANT ALL PRIVILEGES ON nombre_base.tabla TO 'mi_user'@'servidor' IDENTIFIED BY PASSWORD 'my_password';

FLUSH PRIVILEGES;

SHOW GRANTS FOR 'mi_user'@'servidor';

REVOKE ALL, GRANT OPTION FROM 'mi_user'@'servidor'

-- Gestionando tablas

SHOW TABLES;
DESCRIBE nombre_tabla;
CREATE TABLE nombre_tabla(
    campo1 TIPO_DATO ATRIBUTOS,
    campo2 TIPO_DATO ATRIBUTOS
);

ALTER TABLE nombre_tabla ADD COLUMN nombre_campo TIPO_DATO;
ALTER TABLE nombre_tabla MODIFY nombre_campo TIPO_DATO;
ALTER TABLE nombre_tabla RENAME COLUMN nombre_viejo TO nombre_nuevo;
ALTER TABLE nombre_tabla DROP COLUMN nombre_campo;
DROP TABLE nombre_tabla;

-- Ejemplo Tabla

CREATE TABLE usuarios(
    usuario_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(30) NOT NULL,
    apellido VARCHAR(30) NOT NULL,
    correo VARCHAR(50) UNIQUE,
    direccion VARCHAR(100) DEFAULT 'sin direccion'
    edad INT DEFAULT 0
);

