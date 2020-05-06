def ShowRules():
    print("The game is based on the number of pieces in the board,")
    print("every turn each player removes pieces") 
    print("based on the rules settled at the beggining")
    print("the game is won by the player that removes the last piece on the board")
    return

def StartGame():
    pieces = int(input("Please select the number of pieces: "))

    while pieces < 1:
       pieces = int(input("Please select the number of pieces: "))
    
    print("Ok lets go!", pieces, "pieces!")
    
    return pieces

def RemoveCounter():
    remove = int(input("\nPlease select the number of pieces to remove per turn: 1 or 2: "))

    while remove <= 0:
        if remove <= 0:
            remove = int(input("\nPlease don't select zero or a negative number: "))
        
            
    print("Nice,",remove, "pieces!")
    return remove

def CalculateTurn(number, rem):

    if pieces % (rem + 1)  == 0:
        turn = 2
    else:
        turn = 1
    return turn

def ComputerTurn(pieces, remove):
    print ("\nCPU's turn")
    cpuMove = 1
    moved = False
    if pieces > 0:
        while cpuMove < remove:
            if (pieces - cpuMove) % (remove + 1) == 0:
                print("\nCPU removed", cpuMove, "pieces")
                pieces -= cpuMove
                moved = True
            else:
                cpuMove += 1
                
        if not moved:
            print("\nCPU removed", cpuMove, "pieces")
            pieces -= cpuMove

        print("Total pieces =", pieces)
        cpuMove = 1
        moved = False
        return pieces

def PlayerTurn(pieces, remove):
    if pieces > 0:
            print("\nYour turn")
            playerRemove = int(input("Please type how many pieces you want to remove: "))
            
            while playerRemove > remove or playerRemove <= 0 or pieces - playerRemove < 0:
                 playerRemove = int(input("You cant remove that much, Player: "))
                    
            print("\nPlayer removed", playerRemove)
            pieces -= playerRemove

            print("Total pieces =", pieces)

    return pieces

def Game(turn, pieces, remove):
    if turn == 1:
        piecesGame = ComputerTurn(pieces, remove)
        piecesGame = PlayerTurn(piecesGame, remove)
            
            
    if turn == 2:
        piecesGame = PlayerTurn(pieces, remove)
        piecesGame = ComputerTurn(piecesGame, remove)
        
    return piecesGame

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
        pieces = Game(turn, pieces, remove)

    if pieces == 0:
        print("CPU won!")

if option ==2:
    print("ok, good bye :(")
    



    

