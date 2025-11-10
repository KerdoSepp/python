number1 = int(input("Sisesta Number1: "))
number2 = int(input("Sisesta Number2: "))
number3 = int(input("Sisesta Number3: "))
vastus = int

if number1 > number2 and number3:
    vastus = number1
else:
    if number2 > number1 and number3:
        vastus = number2
    else:
        if number3 > number1 and number2:
            vastus = number3




print(vastus)