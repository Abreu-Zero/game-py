def ShowRules():
    ## print the rules
    print("The game is based on the number of pieces in the board,")
    print("every turn each player removes pieces") 
    print("based on the rules settled at the beggining")
    print("the game is won by the player that removes the last piece on the board")
    return

def PiecesCounter():
    ## define the number of pieces to start a game
    pieces = int(input("Please select the number of pieces: "))

    while pieces < 1:
       pieces = int(input("Please select the number of pieces: "))
    
    print("Ok lets go!", pieces, "pieces!")
    
    return pieces

def RemoveCounter():
    ## input the amount of pieces to be removed per turn
    remove = int(input("\nPlease select the number of pieces to remove per turn: "))

    while remove <= 0:
        if remove <= 0:
            remove = int(input("\nPlease don't select zero or a negative number: "))
        
            
    print("Nice,",remove, "pieces!")
    return remove

def CalculateTurn(number, rem):
    ## calculates if CPU should let the player go first to win

    if number % (rem + 1)  == 0:
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
            ## loops through the amount of pieces that it can remove to choose the best move
            ## too keep player from winning
            if (pieces - cpuMove) % (remove + 1) == 0:
                print("\nCPU removed", cpuMove)
                pieces -= cpuMove
                moved = True
            else:
                cpuMove += 1
                
        if not moved:
            print("\nCPU removed", cpuMove)
            pieces -= cpuMove

        print("Total pieces =", pieces)
        cpuMove = 1
        moved = False
        return pieces

def PlayerTurn(pieces, remove):
    ## Inputs player movements
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
    ## order the turns, feeds the game
    if turn == 1:
        piecesGame = ComputerTurn(pieces, remove)
        piecesGame = PlayerTurn(piecesGame, remove)
            
            
    if turn == 2:
        piecesGame = PlayerTurn(pieces, remove)
        piecesGame = ComputerTurn(piecesGame, remove)
        
    return piecesGame

def StartGame():

    print("Game Starting...")
    print("-------------------\n")
    
    piecesInGame = PiecesCounter()
    removeInGame = RemoveCounter()
    
    turn = CalculateTurn(piecesInGame, removeInGame)

    while piecesInGame > 0:
        piecesInGame = Game(turn, piecesInGame, removeInGame)

        if piecesInGame == 0:
            print("CPU won!")


        

print("Welcome to YCNW 1.0")
print("-------------------\n")



option = int(input("Please select an option:\n1- Play Game\n2- Rules\n"))

while option != 1 and option != 2:
    option = int(input("\nPlease select an option:\n1- Play Game\n2- Rules\n"))

if option == 2:
    ShowRules()
    option = int(input("\nWant to start the game now? I want to play!\n1- Yes\n2- No\n"))

while option == 1:

    StartGame()
    option  = int(input("\nWant to Play again?\n1- Yes\n2- No\n"))
        
if option != 1:
    print("ok, good bye :(")
    



    

