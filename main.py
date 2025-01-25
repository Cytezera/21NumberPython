def playerTurn(currentValue):
    while True: 
        userInput = int(input("From a range from 1 - 3, how much you would like to put? "))
        if (0 < userInput < 4 ):
            print (f"Your input: {userInput}")
            return (currentValue + userInput)  
        print ("Invalid input. Please try again" ) 
def computerTurn(currentValue):
    compInput =  
def determineMove(currentValue,turn):
    if turn == player: 
        plyaerTurn(currentValue)
    else:
        computerTurn(currentValue)
    return currentValue
def chooseTurn():
    while True:
        userInput = input("Would you like to be first or second") 
        if userInput == "first" or input == "second":
            return "player" if userInput == "first" else "comp" 
        print ("Invalid input, please try again " ) 
def playGame():
    currentValue = 1 
    turn = chooseTurn()
    while currentValue < 21:
        currentValue = determineMove(currentValue,turn)
          
def menu():
	while True: 
        choice = int(input("What would you like to do? \n1.Play\n2.Exit"))
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
