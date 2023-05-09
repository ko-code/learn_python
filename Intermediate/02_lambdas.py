# lambda es una funcion anonima sin nombre, puede tomar cualquier numero de argumentos, pero solo puede tener una exprecion 
'''
Syntax
x = lambda param1, param2, param3: param1 + param2 + param3

'''
# Ejemplo

def suma_numeros(a, b):
    return a + b

print(suma_numeros(5,6))

# transformamos a lambda

suma_numeros2 = lambda a, b: a + b
print(suma_numeros2(5,6))

# autoinvocacion
print((lambda a, b: a * b)(5,2))

square = lambda x : x**2
print(square(3))

cube = lambda x: x ** 3
print(cube(6))

# multiples variables
multiples_variables = lambda a, b, c: a ** 2 - 3 * b + 4 * c
print(multiples_variables (5,5,3))

# funcion lambda dentro de otra fucnion 
def power(x):
    return lambda n: x**n

cube = power(2)(3)
print(cube)

# Filtre solo negativo y cero en la lista usando la comprensión de lista
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

filtro = [i for i in numbers if(i <= 0)]
print(filtro)

# Aplane la siguiente lista de listas de listas a una lista unidimensional:

# # lista = [expresión for elemento in iterable]
# lista_plana = [number for row in list_of_lists for number in row]
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

limpiar = [number for row in list_of_lists for number in row ]
lista = [number for row in limpiar for number in row]
print(lista)

# Utilizando la comprensión de listas, cree la siguiente lista de tuplas:
'''
[(0, 1, 0, 0, 0, 0, 0),
(1, 1, 1, 1, 1, 1, 1),
(2, 1, 2, 4, 8, 16, 32),
(3, 1, 3, 9, 27, 81, 243),
(4, 1, 4, 16, 64, 256, 1024),
(5, 1, 5, 25, 125, 625, 3125),
(6, 1, 6, 36, 216, 1296, 7776),
(7, 1, 7, 49, 343, 2401, 16807),
(8, 1, 8, 64, 512, 4096, 32768),
(9, 1, 9, 81, 729, 6561, 59049),
(10, 1, 10, 100, 1000, 10000, 100000)]
'''
list_of_tuples = [(i, i*i) for i in range(11)]
print(list_of_tuples)



