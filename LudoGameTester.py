import unittest
from LudoGameRevised import LudoGame

class TestLudoGame(unittest.TestCase):
    def test_case_1(self):
        players = ['A', 'B', 'C', 'D']
        turns = [('A', 6), ('A', 1), ('B', 6), ('B', 2), ('C', 6), ('C', 3), ('D', 6), ('D', 4)]
        game = LudoGame()
        result = game.play_game(players, turns)
        expected = ['1', 'H', '16', 'H', '31', 'H', '46', 'H']
        self.assertEqual(expected, result)

    def test_case_2(self):
        players = ['A', 'B']
        turns = [('B', 6), ('B', 4), ('B', 5), ('B', 4), ('B', 4), ('B', 3), ('B', 4), ('B', 5), ('B', 4), ('B', 4),
                 ('B', 5), ('B', 4), ('B', 1), ('B', 4), ('B', 5), ('B', 5), ('B', 5)]
        game = LudoGame()
        result = game.play_game(players, turns)
        expected = ['H', 'H', 'B6', 'H']
        self.assertEqual(expected, result)

    def test_case_3(self):
        players = ['A', 'B']
        turns = [('A', 6), ('A', 3), ('A', 6), ('A', 3), ('A', 6), ('A', 5), ('A', 4), ('A', 6), ('A', 4)]
        game = LudoGame()
        result = game.play_game(players, turns)
        expected = ['28', '28', 'H', 'H']
        self.assertEqual(expected, result)

    def test_case_4(self):
        players = ['A', 'C']
        turns = [('A', 6), ('A', 4), ('A', 4), ('A', 4), ('A', 5), ('A', 6), ('A', 4), ('A', 6), ('A', 4), ('A', 6),
                 ('A', 6), ('A', 6), ('A', 4), ('A', 6), ('A', 6), ('C', 6), ('C', 4)]
        game = LudoGame()
        result = game.play_game(players, turns)
        expected = ['33', 'H', '32', 'H']
        self.assertEqual(expected, result)

    def test_case_5(self):
        players = ['A', 'B']
        turns = [('A', 6), ('A', 4), ('A', 4), ('A', 4), ('A', 5), ('A', 6), ('A', 4), ('A', 6), ('A', 4), ('A', 6),
                 ('A', 6), ('A', 4), ('A', 6), ('A', 4), ('A', 6), ('A', 6), ('A', 4), ('A', 6), ('A', 6), ('A', 4),
                 ('A', 6), ('A', 6), ('A', 4), ('A', 6), ('A', 3), ('A', 6), ('B', 6), ('A', 6)]
        game = LudoGame()
        result = game.play_game(players, turns)
        expected = ['E', 'E', 'R', 'H']
        self.assertEqual(expected, result)

    def test_case_6(self):
        players = ['A', 'B']
        turns = [('A', 6), ('A', 2), ('A', 2), ('A', 6), ('A', 4), ('A', 5), ('A', 4), ('A', 4), ('B', 6), ('B', 3),
                 ('A', 6), ('A', 3)]
        game = LudoGame()
        result = game.play_game(players, turns)
        expected = ['3', 'H', '17', 'H']
        self.assertEqual(expected, result)

    def test_case_7(self):
        players = ['A', 'B']
        turns = [('A', 6), ('A', 4), ('A', 5), ('A', 4), ('A', 4), ('A', 4), ('A', 5), ('A', 4), ('A', 5), ('A', 5),
                 ('A', 3), ('A', 5), ('A', 3), ('A', 6)]
        game = LudoGame()
        result = game.play_game(players, turns)
        expected = ['A1', 'R', 'H', 'H']
        self.assertEqual(expected, result)

    def test_case_8(self):
        players = ['A', 'B']
        turns = [('A', 6), ('A', 4), ('A', 5), ('A', 4), ('A', 4), ('A', 4), ('A', 5), ('A', 4), ('A', 5), ('A', 5),
                 ('A', 3), ('A', 5), ('A', 5), ('A', 6), ('A', 5), ('A', 5), ('A', 3), ('B', 6), ('B', 3), ('A', 4)]
        game = LudoGame()
        result = game.play_game(players, turns)
        expected = ['E', '13', '17', 'H']
        self.assertEqual(expected, result)

    def test_case_9(self):
        players = ['A', 'B']
        turns = [('A', 6), ('A', 4), ('A', 4), ('A', 4), ('A', 6), ('A', 5), ('A', 3), ('B', 6), ('B', 2), ('A', 2),
                 ('A', 4)]
        game = LudoGame()
        result = game.play_game(players, turns)
        expected = ['16', '10', 'H', 'H']
        self.assertEqual(expected, result)

    def test_case_10(self):
        players = ['A', 'B']
        turns = [('A', 6), ('A', 4), ('A', 5), ('A', 4), ('A', 4), ('A', 3), ('A', 4), ('A', 5), ('A', 4), ('A', 4),
                 ('A', 5), ('A', 4), ('A', 1), ('A', 4), ('A', 5), ('A', 5)]
        game = LudoGame()
        result = game.play_game(players, turns)
        expected = ['A3', 'H', 'H', 'H']
        self.assertEqual(expected, result)

    def test_case_11(self):
        players = ['A', 'B']
        turns = [('A', 6), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5),
                 ('A', 3), ('A', 5)]
        game = LudoGame()
        result = game.play_game(players, turns)
        expected = ['A6', 'H', 'H', 'H']
        self.assertEqual(expected, result)

    def test_case_12(self):
        players = ['A', 'B']
        turns = [('A', 6), ('A', 6), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5),
                 ('A', 2), ('A', 6)]
        game = LudoGame()
        result = game.play_game(players, turns)
        expected = ['A6', 'A6', 'H', 'H']
        self.assertEqual(expected, result)

    def test_case_13(self):
        players = ['A', 'B']
        turns = [('A', 6)]
        game = LudoGame()
        result = game.play_game(players, turns)
        expected = ['R', 'H', 'H', 'H']
        self.assertEqual(expected, result)

    def test_case_14(self):
        players = ['A', 'B']
        turns = [('A', 6), ('A', 6)]
        game = LudoGame()
        result = game.play_game(players, turns)
        expected = ['R', 'R', 'H', 'H']
        self.assertEqual(expected, result)

    def test_case_15(self):
        players = ['A', 'B']
        turns = [('A', 6), ('A', 5), ('A', 6)]
        game = LudoGame()
        result = game.play_game(players, turns)
        expected = ['5', 'R', 'H', 'H']
        self.assertEqual(expected, result)

    def test_case_16(self):
        players = ['A', 'B']
        turns = [('B', 6)]
        game = LudoGame()
        result = game.play_game(players, turns)
        expected = ['H', 'H', 'R', 'H']
        self.assertEqual(expected, result)

    def test_case_17(self):
        players = ['A', 'B']
        turns = [('B', 6), ('B', 6)]
        game = LudoGame()
        result = game.play_game(players, turns)
        expected = ['H', 'H', 'R', 'R']
        self.assertEqual(expected, result)

    def test_case_18(self):
        players = ['A', 'B']
        turns = [('B', 6), ('B', 5), ('B', 6)]
        game = LudoGame()
        result = game.play_game(players, turns)
        expected = ['H', 'H', '19', 'R']
        self.assertEqual(expected, result)

    def test_case_19(self):
        players = ['A', 'B']
        turns = [('A', 6), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5),
                 ('A', 1), ('A', 6)]
        game = LudoGame()
        result = game.play_game(players, turns)
        expected = ['A1', 'R', 'H', 'H']
        self.assertEqual(expected, result)

    def test_case_20(self):
        players = ['A', 'B']
        turns = [('A', 5), ('A', 5)]
        game = LudoGame()
        result = game.play_game(players, turns)
        expected = ['H', 'H', 'H', 'H']
        self.assertEqual(expected, result)
