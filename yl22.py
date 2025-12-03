import random
table = [
    "Kivi",
    "Paber",
    "Käärid",
]

def fetchWord(num):
    word = table[num-1]
    return word

def game():
    num = random.randint(1, 3)
    playerInput = int(input("Kivi:1, Paber:2, Käärid:3 Lõpeta mäng:4 Sisesta number mida soovid mängida: "))
    if playerInput == 4:
        return
    elif num == playerInput:
        print("Viik")
    elif num==1 and playerInput ==3:
        print("Sa kaotasid")
    elif num==3 and playerInput ==1:
        print("Sa võitsid")
    elif num<= playerInput:
        print("Sa võitsid")
    elif num>= playerInput:
        print("Sa kaotasid")
    print("Arvuti valis:",fetchWord(num), "Sina valisin",fetchWord(playerInput))
    game()

game()