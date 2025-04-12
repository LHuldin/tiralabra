import unittest
from game import Game

class TestGame(unittest.TestCase):
    def test_game_starts(self):
        game = Game()
        self.assertTrue(game.running)

    #def test_hello_world(self):
    #    self.assertEqual("Hello world", "Hello world")

    