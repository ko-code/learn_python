### Loops ####

# while

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 1
else: #else es opcional 
    print("Mi condicion es mayor o igual ue 10")

print("la ejecucion continua")

# my_condition = 0 

while my_condition < 20:
    my_condition +=1
    if my_condition == 15:
        print("Se detiene la ejecucion")
        break
    
    print(my_condition)
    
### for ###

# sirve para iterar un listado de elementos

my_list = [35, 40, 50, 70, 21, 29]

for element in my_list:
    print(element)

print("tupla recorrida")
my_tuple = (35, 1.78, "Cristian", "Rojas")

for elem in my_tuple:
    print(elem)

print("sets recorridos")
my_other_set = {"Cristian", "Rojas", 28}

for st in my_other_set:
    print(st)


print("recorrrer un string: Hola")
a =  "hola"
# recorrer un string
for i in range(len(a)):
    print(a[i])

print("dicts recorridos")

my_dict = {
    'first_name':'Cristian',
    'last_name':'Rojas',
    'nick_name':'Kove',
    'age': 28,
    'Lenguajes': {'Python', 'JavaScritp', 'TypeScritp'},
}

for key in my_dict:
    print(key)

for key, value in my_dict.items():
    print(key, value)