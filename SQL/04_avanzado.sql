/*
En SQL existen varios tipos de indices, los principales son:

UNIQUE: asegura los valores de la columna indexada sean unicos en la tabla
PRIMARY KEY: indice especial que identidica de forma unica cada fila de una tabla
INDEX indice que no tiene restricciones de unicidad y e utuliza mejorar el rendimiento de consultas que involucran columnas indexada
FULLTEXT se utiliza para hacer busquedas de texto completo en columnas de texto grandes, como varchar y text

*/

-- Ejemplo

CREATE TABLE una_tabla(
    campo_id INTEGER UNSIGNED PRIMARY KEY,
    campo_unico VARCHAR(80) UNIQUE,
    campo_index VARCHAR(80),
    campo_3 VARCHAR(80),
    campo_4 VARCHAR(80),
    INDEX i_campo_index(campo_index)
    FULLTEXT INDEX fi_campo_fulltext(campo_3, campo_4)
);

-- Ejecutando una consulta tipo FULLTEXT

SELECT * FROM una_tabla
WHERE MATCH(campo_3, campo_4)
AGAINST('UNA BUSQUEDA' IN BOOLEAN MODE);

-- FOREIGN KEYS o llaves foraneas
-- es un campo o conjunto de campos en una tabla que hacen referencia a una clave unica
-- en otra tabla estableciendo asi una relacion entre ambas tablas
-- se utilizan para mantener la integridad referencial de los datos

-- se define de la siguiente forma en una tabla

FOREIGN KEY (nombre_campo) REFERENCES tabla_referencia(campo_referencia);

-- Ejemplo

CREATE TABLE lenguajes(
    lenguaje_id UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    lenguaje VARCHAR(30) NOT NULL,
);

CREATE TABLE entornos(
    entorno_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    entorno VARCHAR(30) NOT NULL,

);

CREATE TABLE frameworks (
    framework_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    framework VARCHAR(30) NOT NULL,
    lenguaje INT UNSIGNED,
    entorno INT UNSIGNED,
    FOREIGN KEY (lenguaje) REFERENCES lenguajes(lenguaje_id),
    FOREIGN KEY (entorno) REFERENCES entornos(entorno_id)
);

-- JOINS
/*

Los JOINS sirven para combinar filas de dos o mas tablas basandose en un campo comun
entre ellas, devolviendo por tanto datos de diferentes tablas. Un JOIN se produce cuando dos o mas 
tablas se juntan en una sentencia SQL.

Los mas importantes son los siguientes:

INNER JOIN: Devuelve todas las filas cuando hay al menos una coincidencia en ambas tablas.
LEFT JOIN: Devuelve todas las filas de la tabla de la izquierda, y las filas coincidentes de la tabla de la derecha.
RIGHT JOIN: Devuelve todas las filas de la tabla de la derecha, y las filas coincidentes de la tabla de la izquierda.
OUTER JOIN: Devuelve todas las filas de las dos tablas, la izquierda y la derecha, también se llama FULL OUTER JOIN.

*/

SELECT * FROM tabla_1 AS t1
    INNER JOIN tabla_2 AS t2;

SELECT * FROM tabla_1 AS t1
    INNER JOIN tabla_2 AS t2
    ON t1.a_campo = t2.a_campo;

SELECT t1.campo_1, t1.campo_2, t1.campo_3, t2.campo_1, t2.campo_5
    FROM tabla_1 AS t1
    INNER JOIN tabla_2 AS t2
    ON t1.campo_1 = t2.campo_5
    WHERE t1.campo_1 = 'valor'
    ORDER BY t1.campo_3 DESC;

