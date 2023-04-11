### Conditionals ###

my_condition = False

if my_condition:
    print("Se ejecuta la condicion del if")



my_condition = 5*3
if my_condition == 10:
    print("Se ejecuta la condicion del segundo if")

if my_condition > 10 and my_condition < 20:
    print("es mayor que 10 y menor que 20")
elif my_condition == 1:
    print("es igual a 1")
else:
    print("Es menor o igual que 10")
print("la ejecucion continua")

# es importante la tabulacion en python, sobre todo en condicionales
# tambien se pueden usar los operadores logicos and, or y not 