

contador  = 1
while contador <=100:
    if contador % 3 == 0 and contador % 5 == 0:
        print("FizzBuzz")
    elif contador % 5 == 0:
        print("Buzz")
    elif contador % 3 == 0:
        print("Fizz")
    else:
        print(contador)
    contador +=1


    