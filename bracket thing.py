
import random

print("Welcome to the Pokemon Deck Matchup Calculator!")

def menu():
    print("1 - Add a new deck\n2 - Display decks\n3 - Generate 9 game day\n")

class WeightedRandomizer:
    def __init__ (self, weights):
        self.__max = .0
        self.__weights = []
        for value, weight in weights.items ():
            self.__max += weight
            self.__weights.append ( (self.__max, value) )

    def random (self):
        r = random.random () * self.__max
        for ceil, value in self.__weights:
            if ceil > r: return value

bastion = 1
decks = {}

while bastion == 1:
    menu()
    option = int(input("\nMenu option: "))

    if (option == 1):
        deckName = str(input("Enter deck name: "))
        deckOdds = float(input("Enter the odds of facing this deck: "))
        decks[deckName] = deckOdds
    
    elif (option == 2):
        print(decks)
    
    elif (option == 3): 
        wr = WeightedRandomizer(decks)
        results = {}
        for key in decks:
            results[key] = 0
        for i in range (9):
            results[wr.random()] +=1
        
        print ("Amount of times you faced each deck that day:")
        print (results)
        
    else:
        print("Not a valid option. Please try again.")
        menu()


