-- Sentencias de agrupamiento

-- GROUP BY se utiliza para agrupar registros en una sola consulta, 
-- basandose en una o mas consultas

SELECT producto, SUM(cantidad) AS total_vendido FROM ventas GROUP BY producto;

-- HAVING se utiliza en sql para filtrar los resultados de una consulta que utiliza GROUP BY 

SELECT producto, SUM(cantidad) AS total_vendido FROM ventas GROUP BY producto HAVING SUM(cantidad) >= 10;


-- DISTINCT se utiliza para eliminar filas duplicadas de un conjunto de resultados

SELECT DISTINCT nombre FROM clientes;
-- esto devolvera solo los nombres unicos sin repetirse

-- ORDER BY 
-- Se utiliza para ordenar datos de forma ascendente o descendente

SELECT * FROM empleados ORDER BY salario ASC;
SELECT * FROM empleados ORDER BY salario DESC;

-- LIMIT se utiliza para limitar el numero de resultados devueltos en una consulta.
-- Permite especificar el numero de filas que se debe devolver de la tabla lo que puede ser util en consultas que devuelven gran cantidad de datos

-- Sintaxis basica 

SELECT columna_1, columna_2, ..., columna_n
    FROM tabla 
    LIMIT cantidad_de_filas;

-- donde cantidad_de_filas es el numero maximo de filas que se deben devolver de la consulta
-- se puede expecifical el punto inicial de donde recuperar las filas 

SELECT columna_1, columna_2, ..., columna_n
    FROM tabla 
    LIMIT indice_inicio, cantidad_de_filas;

-- ejemplos 
-- DEVUELVE LOS PRIMEROS 10 REGISTROS DE LA TABLA CLIENTES
SELECT * FROM clientes
    LIMIT 10;

-- 
SELECT * FROM clientes
    LIMIT 10, 10;
