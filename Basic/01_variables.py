# Variables 
# se usa por convencion snake_case con minuscula todo y con _ entre medio o al inicio de la variable
#lo correcto es: 
my_string_variable = "My string variable"
print(my_string_variable)

# Lo incorreco es
"""
first-name
first@name
first$name
num-1
1num

"""

# Ejemplos de Variables

first_name = "Cristian"
last_name  = "Rojas"

my_string_variable = "My string variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)


my_bool_variable = True
print(my_bool_variable)

my_int_to_str = str(my_int_variable)
print(my_int_to_str)
print(type(my_int_to_str))

# Concatenacion de variables en un print
print(my_string_variable, my_int_variable)
print("Este es el valor de: ", my_bool_variable)
# Algunas funciones del sistema 

#len() devuelve el largo de la cadena
print(len(my_string_variable))


#Variables en una sola linea. Cuidado con abusar de esta sintaxis

name, surename, alias, edad = "Cristian", "Rojas", "Kovek", 28

print("Me llamo: ", name, surename, "mi edad es: ", edad, "y mi alias es:", alias);


# Inputs 
# name = input('Cual es tu nombre?: ')
# edad = input('Cuantos años tienes? ')

print(name)
print(edad)

# Cambiemos su tipo
name = 35
age = "Rojas"
print(name)
print(age)

# Forzar el tipo

address: str = "Miraflores"
address = 32
print(type(address));