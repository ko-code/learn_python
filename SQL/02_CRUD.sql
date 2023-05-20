-- Crud de datos
-- Create, Insert, Update, Delete

-- Create
INSERT INTO tabla (campo1, campo2, ..., campo_n )
    VALUES (valor_1, valor_2, ..., valor_n);

INSERT INTO tabla
    SET campo1 = 'valor_1', campo2 = 'valor_2', ..., campo_n = 'valor_n';

-- Insertar varios registros
INSERT INTO tabla (campo1, campo2, ..., campo_n ) VALUES
    (valor_1, valor_2, ..., valor_n),
    (valor_1, valor_2, ..., valor_n),
    (valor_1, valor_2, ..., valor_n),
    (valor_1, valor_2, ..., valor_n);

-- Read o leer los campos de una tabla
SELECT * FROM tabla;

-- Leer algunos campos de la tabla
SELECT campo1, campo2, campo_n FROM tabla;

-- Saber cuantos registros tiene la tabla
SELECT COUNT(*) FROM tabla;

-- Leer un registro en particular, buscando el valor de un campo

SELECT * FROM tabla WHERE campo1 = 'valor_1';

-- Leer un registro en particular buscando diferentes valores en un campo

SELECT * FROM tabla WHERE campo1 IN ('valor_1', 'valor_2','valor_n');

-- leer un registro en particular buscando el valor similar en un campo
SELECT * FROM tabla WHERE campo1 LIKE '%valor_1';
SELECT * FROM tabla WHERE campo1 LIKE 'valor_1%';
SELECT * FROM tabla WHERE campo1 LIKE '%valor_1%';

-- Leer un registro en particular buscando el valor con operadores logicos

SELECT * FROM tabla WHERE campo1 = 'valor_1' AND campo2 = 'valor_2';
SELECT * FROM tabla WHERE campo1 = 'valor_1' OR campo2 = 'valor_2';
SELECT * FROM tabla WHERE NOT campo1 = 'valor_1'; 
SELECT * FROM tabla WHERE campo1 != 'valor_1';


-- Update(simpre es recomendable agregar la clausula WHERE para no actualizar toda la tabla)

UPDATE tabla
    SET campo1 = 'valor_1', campo2 = 'valor_2', ..., campo_n = 'valor_n'
    WHERE campo = valor;

-- delete (siempre es recomendar agregar la clausula WHERE para no eliminar toda la tabla)
DELETE FROM tabla WHERE campo = valor;