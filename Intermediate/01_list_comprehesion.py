### List Comprehension ####


my_original_list = [35, 40, 50, 70, 21, 29]
print(my_original_list)

my_list = [i for i in range(7)]

print(my_list)

my_range = range(8)
print(list(my_range))

my_list = [i + 1 for i in range(7)]
print(my_list)

my_list = [i * i for i in range(7)]
print(my_list)


# si queremos convertir una cadena a una lista de caracteres usamos lo siguiente 
# primera forma 
lenguaje = 'Python'
lst = list(lenguaje)
print(lst)

# segunda forma
lst = [i for i in lenguaje]
print(lst)

# si desea generar una lista de numeros
numbers = [i for i in range(11)]
print(numbers)

numbers = [i + 2 for i in range(11)]
print(numbers)

# tambien es posible crear una lista de tuplas
numbers = [(i, i*2) for i in range(11)]
print(numbers)

# la comprension de listas puede conbinar con la expresion if

numeros_pares =  [i for i in range(21) if(i % 2 == 0)]
print(numeros_pares)

numeros_impares = [i for i in range(21) if(i % 2 != 0)]
print(numeros_impares)

numbers = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
filter_positive = [i for i in numbers if(i % 2 == 0)and(i > 0)]
print(filter_positive)

# recorrer una lista tridimensional
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
lista_plana = [number for row in list_of_lists for number in row]

print(lista_plana)