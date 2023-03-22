### Operadores ###

# Operadores aritmeticos
print (3 + 4)
print (3 - 4)
print (3 * 4)
print (3 / 4)
print ( 10 % 2)
print (10 // 3) # flor division, quiere decir que al darnos un numero decimal intentara aproximar el resultado
print ( 2 ** 3) #calcular un exponente, 2 elevado a 3

print ("Hola" + " " + "Python")
print ("Hola" + " " + str(5))
print ("Hola" + " ", 5)
print ("Hola" * 5 )
print ("Hola" * (2 ** 3))


# Operadores Comparativos #

print (3 > 4) 
print (3 < 4)
print (3 >= 4)
print (3 <= 4)
print (3 == 4)
print (3 != 4)

print ("Hola" > "Python") 
print ("Hola" < "Python")
print ("aaaa" >= "abaa") # Orden alfabetico ASCII
print (len("aaaa") >= len("abaa")) # Cuenta caracteres
print ("Hola" <= "Python")
print ("Hola" == "Python")
print ("Hola" != "Python")

## Operadores Logicos ##

print(3 > 4 and  "Hola" > "Python")
print(3 > 4 or  "Hola" > "Python")
print(not(3 > 4))