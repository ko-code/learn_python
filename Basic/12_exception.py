

try:
    print(10 + '55')
except:
    print("Debes sumar con numeros enteros y no con strings")

# try:
#     name = input('Ingresa tu nombre: ')
#     year_born = input('Ingresa año de nacimiento: ')
#     age = 2023 - year_born #si quiero parsear a int uso int(year_born)
#     print(f"Tu eres {name}. y tu edad es: {age}")
# except TypeError:
#     print('Type error occured')

# except ValueError:
#     print('Value error occured')

# except ZeroDivisionError:
#     print('ZeroDivision error occured')


# Forma larga

# try:
#     name = input('Ingresa tu nombre: ')
#     year_born = input('Ingresa año de nacimiento: ')
#     age = 2023 - int(year_born) #si quiero parsear a int uso int(year_born)
#     print(f"Tu eres {name}. y tu edad es: {age}")
# except TypeError:
#     print('Type error occured')

# except ValueError:
#     print('Value error occured')

# except ZeroDivisionError:
#     print('ZeroDivision error occured')

# else:
#     print('Normalmente corre con el block de intento')

# finally:
#     print('Siempre corre')

# Forma Crota ####

# try:
#     name = input('Ingresa tu nombre: ')
#     year_born = input('Ingresa año de nacimiento: ')
#     age = 2023 - int(year_born) #si quiero parsear a int uso int(year_born)
#     print(f"Tu eres {name}. y tu edad es: {age}")
# except Exception as e:
#     print(e)

###### Desenpaquetando listas ######

def suma_de_cinco_numeros(a,b,c,d,e):
    return a + b + c + d + e

lst = [1,2,3,4,5]
print(suma_de_cinco_numeros(*lst))

# tambien se puede desempaquetar en rango

# numeros = range(2, 7) 
# print(list(numeros))

args = [2, 7]
numeros = range(*args)
print(*numeros)

paises = ['Chile', 'Argentina', 'Brazil', 'Venezuela', 'Colombia']

cl, ar, br, *rest = paises

print(cl, ar, br, rest)

numeros = [1,2,3,4,5,6]
one,*two_numbers, four, five, six = numeros
print(one, two_numbers, four, five, six)

### desempaquetado de diccionarios ####

def desempaquetado_persona (name, country, city, age):
    return f'{name} lives in {country}, {city}. he is {age} years old'

dct = {
    'name':'Cristian',
    'country':'Chile',
    'city':'Santiago',
    'age': 28
}


print(desempaquetado_persona(**dct))

