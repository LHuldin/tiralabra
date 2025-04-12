import unittest
import pygame
from character import Character
from game import *

class TestCharacter(unittest.TestCase):

    def setUp(self):
        pygame.init()
        self.char = Character(0, 0)
        self.walkable_tiles = {(0, 0), (1, 0)}

    def test_initial_position(self):
        self.assertEqual((self.char.x, self.char.y), (0, 0))
        self.assertEqual(self.char.color, (255, 0, 0))

    

