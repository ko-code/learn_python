### Strings ###

my_strings = "Mi String"
my_other_string = 'Mi otro String'

print(len(my_strings));
print(len(my_other_string));

print(my_strings + " " + my_other_string)

my_new_line__string = "Este es un string\ncon salto de linea"
print(my_new_line__string)

my_tab_line__string = "\tEste es un string con tabulacion"
print(my_tab_line__string)

my_scape_string = "\\tEste es un String \n escapado"
print(my_scape_string)

"""

\n: new line
\t: Tab means(8 spaces)
\\: Back slash
\': Single quote (')
\": Double quote (")

"""

### Formateo de Strings ###

##Old Style 
name, surname, age = "R3tr0", "Ko", 28
print("Mi nombre es %s %s y mi edad es %d" %(name, surname, age))

##New Style ####
print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))

###Interpolacion ####
print(f"Mi nombre es {name} {surname} y mi edad es {age}")


### Desempaquetado de caracteres ###
lenguaje = "python"
a,b,c,d,e,f = lenguaje

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

#  Division

lenguaje_slice = lenguaje[1:3]
print(lenguaje_slice)

lenguaje_slice = lenguaje[-1]
print(lenguaje_slice)

lenguaje_slice = lenguaje[0:6:2]
print(lenguaje_slice)

# reverse 

reversed_lenguaje = lenguaje[::-1]
print(reversed_lenguaje)

# Funciones
print(lenguaje.capitalize()) #la primera letra mayuscula
print(lenguaje.upper())
print(lenguaje.count('t'))
print(lenguaje.isnumeric())
print("1".isnumeric())
print(lenguaje.lower())
print(lenguaje.upper())
print(lenguaje.lower().isupper())
print(lenguaje.startswith("py"))

