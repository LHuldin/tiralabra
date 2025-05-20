import unittest
from game import Game
from unittest.mock import patch, MagicMock
from config import TILESIZE

class TestGame(unittest.TestCase):

    @patch("pygame.transform.scale")
    @patch("pygame.image.load")
    def test_game_starts(self, mock_load, mock_scale):

        mock_img = MagicMock()
        mock_img.convert_alpha.return_value = mock_img
        mock_img.get_size.return_value = (TILESIZE, TILESIZE)
        mock_load.return_value = mock_img
        mock_scale.return_value = mock_img

        game = Game()
        self.assertTrue(game.running)


    