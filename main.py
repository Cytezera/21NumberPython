import random
def playerTurn(currentValue):
    while True: 
        userInput = int(input("From a range from 1 - 3, how much you would like to put? "))
        if (0 < userInput < 4 ):
            print (f"Your input: {userInput}")
            return (currentValue + userInput)  
        print ("Invalid input. Please try again" ) 
def computerTurn(currentValue):
    if (currentValue % 4 > 0) : 
        computerInput = 4 - (currentValue % 4 ) 
    else : 
        computerInput = random.choice([1,2,3])
    print (f"Computer's chocie: {computerInput}")
    return (currentValue + computerInput)

def determineMove(currentValue,turn):
    if turn == "player": 
        currentValue = playerTurn(currentValue)
    else:
        currentValue = computerTurn(currentValue)
    
    return currentValue if currentValue <22 else 21 
def chooseTurn():
    while True:
        userInput = input("Would you like to be first or second \n") 
        if userInput == "first" or userInput == "second":
            return "player" if userInput == "first" else "comp" 
        print ("Invalid input, please try again " ) 
def displayGame(turn,currentValue):
    print (f"Currenet Value: {currentValue}")
    if turn == "player":
        print ("Player's turn" )
    else : 
        print ("Computer's turn")
def changeTurns(turn):
    if turn == "player":
        turn = "comp"
    else:
        turn = "player"
    return turn 
def showResult(turn):
    if turn == "player":
        print ("Comoputer wins!") 
    else : 
        print ("Player wins!") 

def playGame():
    currentValue = 1 
    turn = chooseTurn()
    while currentValue < 21:
        displayGame(turn, currentValue)      
        currentValue = determineMove(currentValue,turn)
        if (currentValue == 21): 
            showResult(turn)
        turn = changeTurns(turn)
def menu():
    while True:
        choice = int(input("What would you like to do ? \n1.Play\n2.Exit"))
        match choice:
            case 1:
                playGame()
            case 2:
                print("Goodbye")
                return 
            case _: 
                print("Invalid input") 
def main():
	menu()

main()
