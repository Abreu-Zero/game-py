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

        print("Ok lets go! {} pieces!".format(pieces))

        return pieces

    def remove_counter(self):
        ## input the amount of pieces to be removed per turn
        remove = int(input("\nPlease select the number of pieces to remove per turn: "))

        while remove <= 0:
            if remove <= 0:
                remove = int(input("\nPlease don't select zero or a negative number: "))

        print("Nice, {} pieces!".format(remove))
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

        if(remove <= 0):
            raise Exception("remove cant be < 0")

        cpu_move = 1
        moved = False
        if pieces > 0:
            while cpu_move < remove:
                ## loops through the amount of pieces that it can remove to choose the best move
                ## too keep player from winning
                if (pieces - cpu_move) % (remove + 1) == 0:
                    print("\nCPU removed", cpu_move)
                    pieces -= cpu_move
                    moved = True
                else:
                    cpu_move += 1

            if not moved:
                print("\nCPU removed", cpu_move)
                pieces -= cpu_move

            print("Total pieces =", pieces)
            cpu_move = 1
            moved = False
            return pieces

    def player_turn(self, pieces, remove):
        ## Inputs player movements
        if pieces > 0:
            print("\nYour turn")
            player_remove = int(input("Please type how many pieces you want to remove: "))

            while player_remove > remove or player_remove <= 0 or pieces - player_remove < 0:
                player_remove = int(input("You cant remove that much, Player: "))

            print("\nPlayer removed", player_remove)
            pieces -= player_remove

            print("Total pieces =", pieces)

        return pieces

    def update(self, turn, pieces, remove):
        ## order the turns, feeds the game
        if turn == 1:
            pieces_game = self.computer_turn(pieces, remove)
            pieces_game = self.player_turn(pieces_game, remove)

        if turn == 2:
            pieces_game = self.player_turn(pieces, remove)
            pieces_game = self.computer_turn(pieces_game, remove)

        return pieces_game

    def start_game(self):

        print("Game Starting...")
        print("-------------------\n")

        pieces_in_game = self.pieces_counter()
        remove_in_game = self.remove_counter()

        turn = self.calculate_turn(pieces_in_game, remove_in_game)

        while pieces_in_game > 0:
            pieces_in_game = self.update(turn, pieces_in_game, remove_in_game)

            if pieces_in_game == 0:
                print("CPU won!")
