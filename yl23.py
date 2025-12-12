import random
cards = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10] * 4

def pullCard():
    random.shuffle(cards)
    randomCard = cards.pop()
    ##randomCard = random.choice(cards)
    return randomCard

def addUpCards(deck):
    sum = 0
    for card in deck:
        if card != "A":
            sum += card
        else:
            if sum + 11 >=21:
                sum +=1
            else:
                sum +=11
    return sum

def startGame():
    playerDeck = []
    pcDeck = []

    pcDeck.append(pullCard())
    pcDeck.append(pullCard())
    playerDeck.append(pullCard())
    playerDeck.append(pullCard())

    def restart():
        restartC = input("Kas tahad uuesti mängida yes/no: ")
        if restartC == "yes":
            startGame()
        else:
            return


    def winCondition():
        if addUpCards(pcDeck) >= addUpCards(playerDeck) and addUpCards(pcDeck) <= 21:
            print("Player:", addUpCards(playerDeck), "Dealer:", addUpCards(pcDeck))
            print("Dealer võitis")
            restart()
        elif addUpCards(pcDeck) <= addUpCards(playerDeck) and addUpCards(playerDeck) <= 21:
         if addUpCards(pcDeck) <= 17:
            pcDeck.append(pullCard())
            winCondition()
         else:
            print("Player:", addUpCards(playerDeck), "Dealer:", addUpCards(pcDeck))
            print("Sa võitsid")
            restart()
        elif addUpCards(playerDeck) >= 21:
            print(addUpCards(playerDeck))
            print("Sa läksid üle 21")
            print("Dealer võitis")
            restart()
        elif addUpCards(pcDeck) >= 21:
            print(addUpCards(pcDeck))
            print("Dealer läks üle 21")
            print("Sa võitsid")
            restart()



    def loop():
        if addUpCards(playerDeck) >= 21:
            winCondition()
        else:
            print("Sinu deck:",playerDeck,addUpCards(playerDeck))
            print("Arvuti deck: ""[""hidden,",pcDeck[0],"]", pcDeck[0])
            choice = input("hit, stand: ")
            if choice == "hit":
                playerDeck.append(pullCard())
                loop()
            elif choice == "stand":
              winCondition()

    loop()

startGame()