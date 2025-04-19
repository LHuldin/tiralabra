import unittest
from config import *
import pygame
from character import Character
from game import *
from unittest.mock import * #patch, MagicMock

class TestCharacter(unittest.TestCase):

    def setUp(self):
        pygame.init()

    @patch("pygame.transform.scale")
    @patch("pygame.image.load")
    def test_initial_position(self, mock_load, mock_scale):
        mock_img = MagicMock()
        mock_img.convert_alpha.return_value = mock_img
        mock_img.get_size.return_value = (TILESIZE, TILESIZE) 
        mock_load.return_value = mock_img
        mock_scale.return_value = mock_img

        char = Character(0, 0)

        self.assertEqual((char.x, char.y), (0, 0))
        self.assertEqual(char.color, (255, 0, 0))
        self.assertIsNotNone(char.image)
        
    
    

