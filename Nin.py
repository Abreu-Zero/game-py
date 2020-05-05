def ShowRules():
    print("The game is based on the number of pieces in the board,")
    print("every tunr each player removes 1 oe 2 pieces") 
    print("based on the rules settled at the beggining")
    print("the game is won by the player that removes the last piece on the board")
    return

def StartGame():
    pieces = int(input("Please select the number of pieces: "))

    while pieces < 1:
       pieces = int(input("Please select the number of pieces: "))
    
    print("Ok lets go!\n", pieces, "pieces!")
    
    return pieces

def RemoveCounter():
    remove = int(input("\nPlease select the number of pieces to remove per turn: 1 or 2: "))

    while remove <= 0 or remove > 2:
        if remove <= 0:
            remove = int(input("\nPlease don't select zero or a negative number: "))
        if remove > 2:
            remove = int(input("\nPlease don't select a number bigger than 2: "))
            
    print("Nice\n", remove, "pieces!")
    return remove

def CalculateTurn(number, rem):
    if pieces == rem:
        turn = 1
    elif pieces % rem != 0:
        turn = 1
    else:
        turn = 2

print("Welcome to YCNW 1.0")
print("-------------------\n")



option = int(input("Please select an option:\n1- Play Game\n2- Rules\n"))

while option != 1 and option != 2:
    option = int(input("\nPlease select an option:\n1- Play Game\n2- Rules\n"))

if option == 2:
    ShowRules()
    option = int(input("\nWant to start the game now? I want to play!\n1- Yes\n2- No\n"))

if option == 1:
    pieces = StartGame()
    remove = RemoveCounter()
    
    turn = CalculateTurn(pieces, remove)

    while pieces > 0:
        if turn == 1:
            print ("\nCPU's turn")
            if pieces - remove >= remove + 1:
                print("\nCPU removed" ,remove , "pieces")
                pieces -= remove
            elif pieces == remove:
                print("\nCPU removed" ,remove , "pieces")
                pieces -= remove
            else:
                print("\nCPU removed 1 piece")
                pieces -= 1

            print("Total pieces =", pieces)
            
            if pieces > 0:
                print("\nYour turn")
                playerRemove = int(input("Please type how many pieces you want to remove: "))
            
                while playerRemove > remove or playerRemove <= 0:
                    playerRemove = int(input("You cant remove that much, Player: "))
                    
                print("\nPlayer removed", playerRemove)
                pieces -= playerRemove

                print("Total pieces =", pieces)

        if turn == 2:
            print("\nYour turn")
            playerRemove = int(input("Please type how many pieces you want to remove: "))
            
            while playerRemove > remove or playerRemove <= 0:
                 playerRemove = int(input("You cant remove that much,Player: "))
            print("\nPlayer removed", playerRemove)
            pieces -= playerRemove

            print("Total pieces =", pieces)

            print ("\nCPU's turn")
            if pieces - remove >= remove + 1:
                print("\nCPU removed" ,remove , "pieces")
                pieces -= remove
            elif pieces == remove:
                print("\nCPU removed" ,remove , "pieces")
                pieces -= remove
            else:
                print("\nCPU removed 1 piece")
                pieces -= 1

            print("Total pieces =", pieces)     

    if pieces == 0:
        print("CPU won!")

if option ==2:
    print("ok, good bye :(")
    



    

