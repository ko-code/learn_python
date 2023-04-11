### Funtions ###

def my_funtions ():
    print("Esto es una funcion")


my_funtions()

def sum_two_values (num1, num2):
    print(num1 + num2)

sum_two_values(5,2) 
sum_two_values("5","7") 
sum_two_values(5.33, 2.44) 

def sum_two_values_with_return (num1, num2):
    return num1 + num2

my_result = sum_two_values_with_return(10, 5)

print(my_result)

def print_name (name, surname, alias = "Sin alias" ):
    print(f"{name}, {surname}, {alias} ") 

print_name(surname ='rojas', name ='cristian')

def print_text (text):
    print(text)
print_text("Hola")

def print_upper_texts(*texts):
    print(type(texts))
    for text in texts:
        print(text.upper())

print_upper_texts("hola", "python", "r3troD3v")