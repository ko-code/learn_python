### Sets ###

my_set = set()
 
print(type(my_set))
my_other_set = {}

print(type(my_other_set)) # esto nos dice que inicialmente es un diccionario

my_other_set = {"Cristian", "Rojas", 28}

print(type(my_other_set))
print(len(my_other_set))

my_other_set.add("R3tr0D3v")

print(my_other_set) #un set no es una estructura ordenada
my_other_set.add("R3tr0D3v") # un set no admite elementos repetidos
print(my_other_set)

# para saber si un elemento existe dentro del set

print("existe el elemento R3tr0D3v", 'R3tr0D3v' in my_other_set)
print('R3tr0D3v' in my_other_set)

my_other_set.remove("R3tr0D3v")
print(my_other_set)

#podemos agregar varios elementos al set usando update, pero se deben pasar los elementos como si fueran una lista
my_other_set.update(["R3tr0", "Kovek", "Ko-code"])
print(my_other_set)

# elimina un elemento de forma aleatoria y lo devuelve

pop_item = my_other_set.pop()
print(pop_item)
print(my_other_set)

#no es recomendable hacer esta conversion ya que al crear set este es variable en posiciones
my_set = {"Cristian", "Rojas", 28}
my_list =list(my_set)
print(my_list)

#unir sets
my_other_set = {"Python", "JavaScript", "TypeScript"}
my_new_set = my_set.union(my_other_set)
print(my_new_set)
#otra forma seria con update
# my_set.update(my_other_set)
# print(my_set)

print(my_new_set.difference(my_set))

#del elimina el objeto 
# del my_other_set
# print(my_other_set)

# deja vacio el set
my_other_set.clear()
print(len(my_other_set))