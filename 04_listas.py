#### Listas ####

my_list = list()
my_other_list = []


print(len(my_list))

my_list = [35, 40, 50, 70, 21, 29]

print(my_list)
print(len(my_list))

my_other_list = [28, 1.78, "Cristian", "Rojas"]
print(my_other_list)
print(len(my_other_list))

print(type(my_other_list))
print(type(my_list))

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-3])
# print(my_other_list[-5]) Error out of range
# print(my_other_list[4]) Error out of range

print(my_other_list.count("Rojas")) #count devuelve el numero de ocurrencias de un valor en la lista

age, height, name, surname = my_other_list;
print(name)

print(my_list + my_other_list) # se pueden concatenar listas

my_other_list.append("R3tr0")
print(my_other_list)
my_other_list.insert(1, "black") ## recibe posisicon y valor para agregar a la lista 
print(my_other_list)

my_other_list.remove("black") ## elimina la primera ocurrencia 
print(my_other_list)

my_list.pop() #quita ppor defecto el ultimo elemento de la lista y lo retorna o tambien de un lugar especifico
print(my_list)

del my_list[2] #lo elimina de la lista derechamente
print(my_list)

my_new_list = my_list.copy()

my_list.clear() #deja vacia la lista 
print(my_list)

print(my_new_list)

my_new_list.reverse()
print(my_new_list)

my_new_list.sort()
print(my_new_list)

my_new_list = my_list.copy()
print
my_list = "Hola Python"
print(type(my_list))