import random
num = random.randint(0, 100)
print(num)

def guess():
    guessint = int(input("Arva arv 0-100: "))
    if guessint == num:
        print("Õige")
    elif guessint<= num:
        print("Arv on suurem")
        guess()
    elif guessint>= num:
        print("Arv on väiksem")
        guess()


guess()