import unittest
import game


class UnitTest(unittest.TestCase):

    def new_game(self):
        new_game = game.Game()

        return new_game

    def test_show_rules(self):
        test = self.new_game()
        test_string = ("The game is based on the number of pieces in the board,\n"
                       "every turn each player removes pieces\n"
                       "based on the rules settled at the beggining\n"
                       "the game is won by the player that removes the last piece on the board")

        self.assertEqual(test.show_rules(), test_string)

    def test_calculate_turn(self):
        test = self.new_game()

        ## Tests if the calculate_turn method can bring the right turns
        ## if the number of pieces is divisible by the number that the player can remove
        ## then the cpu must move first

        self.assertEqual(test.calculate_turn(5, 5), 1) #positive value returns player
        self.assertEqual(test.calculate_turn(6, 5), 2)  # positive value returns cpu