#NIMGRAB.py
#nimGrab game!
# Natasha Mills         March 4, 2025
#Assignment #3
#COM S 127 /2

#This is the nimGrab game! This program runs a game that first asks whether you want to play against a human or a computer, and then it 
#runs the game! You try not to be the last person to take an item from the randomized list
#or you lose!


import random
#creating inventory of items
itemInventory = ["bunny", "train", "book", "plane", "brick", "submarine", "drink", "burger", "taco", "gum", "chips", "lotion", "napkins", "paperclip", "yo-yo", "lamp", "hammer", "tape", "rope", "pillow", "blanket", "hotdog", "calculator", "pencil", "fan"]
#getting a random amount between 20-25 of items
numberItems = random.randint(20,25)
itemInventory = random.sample(itemInventory, numberItems)

randlist = []

def human1():
    global itemInventory #access iteminventory
    print(itemInventory) 
    print(len(itemInventory))
    if len(itemInventory) > 1: #if the length of item inventory is over 1
        choice = int(input('Player 1: How many items would you like to take from [1 to 5]? '))
        if 1 <= choice <= 5: #if choice is withing range
            if len(itemInventory) >= choice:  #if there is enough items
                take = itemInventory[:choice] #take number of items out
                itemInventory = itemInventory[choice:] #append list
                print(f'You took {choice} items.')
                print('Items left: ', len(itemInventory)) #print remaining items
                if len(itemInventory) == 1:
                    print('You win!')
            
            else:
                print(f'Theres only {len(itemInventory)} items left! Try again!')
        else:
            print('How many items would you like to take from [1 to 5]? ')
def human2():
    global itemInventory #access itemInventory
    if len(itemInventory) > 1: #if there is more than 1 items left
        choice = int(input('Player 2: How many items would you like to take from [1 to 5]? '))
        if 1 <= choice <= 5: #if choice is within range
            if len(itemInventory) >= choice: #if the choice is less than the amount of items left
                take = itemInventory[:choice] #take number of items out
                itemInventory = itemInventory[choice:] #append list
                print(f'You took {choice} items.')
                print('Items left: ', len(itemInventory)) #print remaining items
                if len(itemInventory) == 1: #if there is one item left you win!
                    print('You win!')  
            else:
                print(f'Theres only {len(itemInventory)} items left! Try again!')
        else:
            print('How many items would you like to take from [1 to 5]? ')

def computer():
    global itemInventory #access itemInventory
    print(itemInventory)
    print(len(itemInventory))
    while len(itemInventory) > 1: #while inventory is >1
        choice = int(input('Player 1: How many items would you like to take from [1 to 5]? '))
        if 1 <= choice <= 5: #if choice is between 1 and 5
            while len(itemInventory) >= choice: #while inventory > input
                    if len(itemInventory) > 1: #and if it is > 1
                        take = itemInventory[:choice] #take chosen number out
                        itemInventory = itemInventory[choice:] #append itemInventory
                        print('You took', choice, 'items')
                        print('Items left: ', len(itemInventory))
                        if len(itemInventory) > 1: #while theres more than 1 item left
                            computerTake = random.randrange(1, 5) #computer generates random amount to take
                            if 1 <= computerTake <= 5: #if computer chooses an amount between 1 to 5
                                if len(itemInventory) >= computerTake: #and the inventory allows it
                                    take = itemInventory[:computerTake] #take out the amount 
                                    itemInventory = itemInventory[computerTake:] #and append the list
                                    print('The computer took', computerTake, 'items')
                                    print('Items left: ', len(itemInventory))
                                    choice = int(input('Player 1: How many items would you like to take from [1 to 5]? '))
                                    take = itemInventory[:choice] #take chosen number out
                                    itemInventory = itemInventory[choice:] #append itemInventory
                                    if len(itemInventory) == 1:
                                        print('You win!')
                                    if len(itemInventory) == 0:
                                        print('You lose!')
                                else:
                                    print('You lose!')
                        else:
                            print('You win!')
                    



def game(): #game function creation
    global itemInventory #access global inventory
    if gameMode == 'h': #if human gamemode is chosen
        if len(itemInventory) > 1: #only allows if inventory is >1
                human1()
                if len(itemInventory) > 1:
                    human2()
                    if len(itemInventory) > 1: #only allows if inventory is >1
                        human1()
                        if len(itemInventory) > 1:
                            human2()
                            if len(itemInventory) > 1: #only allows if inventory is >1
                                human1()
                                if len(itemInventory) > 1:
                                    human2()
                                    if len(itemInventory) > 1: #only allows if inventory is >1
                                        human1()
                                        if len(itemInventory) > 1:
                                            human2()
    if gameMode == 'c': #if gamemode chosen is computer
        while len (itemInventory) > 1: #and there's more than 1 item left
            computer()


def rules(): #print rules of the game
    print('The rules of this game are as follows:\n'
          '1. Players take turn removing items from the row of items\n'
          '2. When it is your turn, you can choose to take between 1'
          'and 5 items\n'
          '3. You do NOT want to be the last person to take an item! or you lose!')

print('This is the NIMGRAB game!')
gameChoice = input('Would you like to [p]lay, read the [r]ules, or [q]uit?: ')
if gameChoice == 'p': #if game choice is play
    gameMode = input('Would you like to play against a [h]uman or a [c]omputer?: ')
    game()
elif gameChoice == 'r': #if game choice is read rules
    rules()
elif gameChoice == 'q': #if game choice is quit
    print('Good game!')