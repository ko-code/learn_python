### Tuples ###
# las tuplas no se pueden mutar son inmutables luego de definirlas 

my_tuple = tuple()
my_other_tuple = ()


my_tuple = (35, 1.78, "Cristian", "Rojas")
my_other_tuple = (35,40,60,30)
print(my_tuple)

print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])

print(my_tuple[1:3])

print(my_tuple.count("Cristian"))

print(my_tuple.index("Rojas"))

# my_tuple[4] = "hola" // no se pueden asiganr valores a las tuplas

# se pueden sumar las tuplas y crear otra
my_sum_tuple = my_tuple + my_other_tuple
# print(my_tuple + my_other_tuple)
print(my_sum_tuple[2:6])

my_tuple = list(my_tuple)
print(type(my_tuple))


my_tuple.insert(1, "black")
my_tuple = tuple(my_tuple)


