class Game:
    def show_rules(self):
        ## print the rules
        text = ("The game is based on the number of pieces in the board,\n"
                "every turn each player removes pieces\n"
                "based on the rules settled at the beggining\n"
                "the game is won by the player that removes the last piece on the board")

        return text

    def pieces_counter(self):
        ## define the number of pieces to start a game
        pieces = int(input("Please select the number of pieces: "))

        while pieces < 1:
            pieces = int(input("Please select the number of pieces: "))

        print("Ok lets go!", pieces, "pieces!")

        return pieces

    def remove_counter(self):
        ## input the amount of pieces to be removed per turn
        remove = int(input("\nPlease select the number of pieces to remove per turn: "))

        while remove <= 0:
            if remove <= 0:
                remove = int(input("\nPlease don't select zero or a negative number: "))

        print("Nice,", remove, "pieces!")
        return remove

    def calculate_turn(self, number, rem):
        ## calculates if CPU should let the player go first to win

        if number % (rem + 1) == 0:
            turn = 2
        else:
            turn = 1
        return turn

    def computer_turn(self, pieces, remove):
        print("\nCPU's turn")
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

    def player_turn(self, pieces, remove):
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

    def update(self, turn, pieces, remove):
        ## order the turns, feeds the game
        if turn == 1:
            piecesGame = self.computer_turn(pieces, remove)
            piecesGame = self.player_turn(piecesGame, remove)

        if turn == 2:
            piecesGame = self.player_turn(pieces, remove)
            piecesGame = self.computer_turn(piecesGame, remove)

        return piecesGame

    def start_game(self):

        print("Game Starting...")
        print("-------------------\n")

        piecesInGame = self.pieces_counter()
        removeInGame = self.remove_counter()

        turn = self.calculate_turn(piecesInGame, removeInGame)

        while piecesInGame > 0:
            piecesInGame = self.update(turn, piecesInGame, removeInGame)

            if piecesInGame == 0:
                print("CPU won!")
