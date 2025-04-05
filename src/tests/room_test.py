import unittest
from room import Room, Block, Position

class TestRoom(unittest.TestCase):

    def test_room_initialization(self):
        room = Room()
        self.assertEqual(len(room.blocks), 0)
        self.assertEqual(len(room.positions), 0)
        self.assertIsNone(room.starting_position)
        self.assertIsInstance(room.color, tuple)
        self.assertEqual(len(room.color), 3)
        for value in room.color:
            self.assertTrue(0 <= value <= 255, "RGB values should be between 0 and 255")


    def test_add_block(self):
        room = Room()
        pos = Position(1, 1)
        room.add_block(pos)

        # Position should now be part of the room
        self.assertIn(pos, room.positions)

        # Exactly one block should be added
        self.assertEqual(len(room.blocks), 1)

        # Block's position should match
        block = next(iter(room.blocks))
        self.assertEqual(block.position, pos)

        # Adding same block again should not duplicate
        room.add_block(pos)
        self.assertEqual(len(room.blocks), 1)

    def test_expand_adds_neighbor(self):
        room = Room()
        start = Position(3, 3)
        room.add_block(start)
        before = len(room.positions)

        room.expand()

        after = len(room.positions)
        self.assertGreaterEqual(after, before)
        self.assertTrue(any(pos != start for pos in room.positions),
                        "expand should add at least one different neighbor position.")
