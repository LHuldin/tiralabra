import unittest
from dungeon import Dungeon

class TestDungeon(unittest.TestCase):

    def test_dungeon_default_creation(self):
        dungeon = Dungeon()
        
        # Ensure at least one room is created
        self.assertGreater(len(dungeon.rooms), 0, "Dungeon should contain at least one room.")

        # Ensure that each room has a corresponding start point
        self.assertEqual(len(dungeon.room_start_points), len(dungeon.rooms),
                         "Each room should have a corresponding start point.")
        
        # Ensure that paths is a list (even if empty)
        self.assertIsInstance(dungeon.paths, list, "Paths should be a list.")
