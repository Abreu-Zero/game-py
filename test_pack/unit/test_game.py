import unittest
from unittest.mock import patch
import game


class UnitTest(unittest.TestCase):

    def new_game(self):
        new_game = game.Game()

        return new_game

    def test_show_rules(self):
        test = self.new_game()

        ### shoud return the rules to be print at main_menu

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

    def test_computer_turn(self):
        test = self.new_game()

        ##CPU needs to keep the number of pieces not divisible by the number the player can remove
        ##CPU needs to try to be the one to reach 0 pieces
        ##CPU cant remove 0 pieces or a negative number
        ##CPU should not remove more pieces than available nor than settled at remove_counter()

        ##Valid inputs
        self.assertEqual(test.computer_turn(1, 2), 0)  ##case 1 pieces < remove
        self.assertEqual(test.computer_turn(4, 2), 3)  ##case 2 pieces - remove == pieces - remove + 1
        self.assertEqual(test.computer_turn(8, 3), 5)  ##case 3 pieces - remove > pieces - remove + 1
        self.assertEqual(test.computer_turn(8, 8), 0)  ##case 4 pieces == remove

    def test_computer_turn_invalid_input(self):
        test = self.new_game()

        ##Invalid inputs

        self.assertRaises(Exception, test.computer_turn, 5, 0) ##case 5 invalid input 0
        self.assertRaises(Exception, test.computer_turn, 5, -1) ##case 6 invalid input negative

    def test_pieces_counter(self):
        test = self.new_game()
        invalid_promt = "Please select the number of pieces: "

        ##User will input number of pieces to game
        ##Input needs to be a positive number
        ##System should not accept input <= 0

        #case 1 valid input
        with patch("builtins.input", return_value="1") as mocked_input:
            with patch("builtins.print") as mocked_print:
                test.pieces_counter()
                mocked_print.assert_called_with("Ok lets go! 1 pieces!")

        #case 2 invalid input 0
        with patch("builtins.input") as mocked_input:
            mocked_input.side_effect = 0, 1
            test.pieces_counter()
            mocked_input.assert_called_with(invalid_promt)

        #case 3 invalid input -1
        with patch("builtins.input") as mocked_input:
            mocked_input.side_effect = -1, 1
            test.pieces_counter()
            mocked_input.assert_called_with(invalid_promt)

    def test_remove_counter(self):
        test = self.new_game()
        invalid_promt = "\nPlease don't select zero or a negative number: "

        ##User will input number of pieces to that can be removed
        ##Input needs to be a positive number
        ##System should not accept input <= 0

        # case 1 valid input
        with patch("builtins.input", return_value="1") as mocked_input:
            with patch("builtins.print") as mocked_print:
                test.remove_counter()
                mocked_print.assert_called_with("Nice, 1 pieces!")

        # case 2 invalid input 0
        with patch("builtins.input") as mocked_input:
            mocked_input.side_effect = 0, 1
            test.remove_counter()
            mocked_input.assert_called_with(invalid_promt)

        # case 3 invalid input -1
        with patch("builtins.input") as mocked_input:
            mocked_input.side_effect = -1, 1
            test.remove_counter()
            mocked_input.assert_called_with(invalid_promt)
