### Dictionaries ###

my_dict = dict()
print(type(my_dict))

my_other_dict = {}
print(type(my_other_dict))

my_other_dict = {
    'firs_name':'Cristian',
    'last_name':'Rojas',
    'nick_name':'Kove',
    'age': 28,
    1: 'Python'

}

my_dict = {
    'first_name':'Cristian',
    'last_name':'Rojas',
    'nick_name':'Kove',
    'age': 28,
    'Lenguajes': {'Python', 'JavaScritp', 'TypeScritp'},
}

print(my_other_dict)
print(my_dict)
print(len(my_dict)) #len devuelve la cantidad de pares clave:valor 

print(my_dict['first_name'])
 
my_dict['first_name'] = 'Gabriel'
print(my_dict)

my_dict[0] = 'Francisca'
print(my_dict)

print(my_dict.get('first_name'))
print(my_dict.get('AL')) #retorna none porque no existe la clave

del my_dict[0] #borra el elemento del diccionario que le estoy pasando
print(my_dict)

my_dict.pop('Lenguajes') # remueve el elemento que le paso por parametro
print(my_dict)

my_dict.popitem() # remueve el ultimo elemento
print(my_dict)

print('Gabriel' in my_dict)

new_dict = my_dict.copy()
print(new_dict)

print(my_dict.items())
print(my_dict.values())
print(my_dict.keys())

my_list = ['Nombre', 1, 'Piso']


my_last_dict = dict.fromkeys(my_list)
print(my_last_dict)

my_last_dict = dict.fromkeys(my_other_dict)
print(my_last_dict)

my_last_dict = dict.fromkeys(my_other_dict, ['Cristian', 'Rojas'])
print(my_last_dict)