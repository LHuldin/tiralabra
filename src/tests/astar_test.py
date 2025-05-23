import unittest
from astar import *


class TestAstar(unittest.TestCase):
    
    def test_manhattan_simple(self):
        """Test Manhattan distance between points with simple coordinates."""
        self.assertEqual(manhattan((0, 0), (1, 1)), 2)
        self.assertEqual(manhattan((3, 4), (0, 0)), 7)
        self.assertEqual(manhattan((5, 5), (5, 5)), 0)

    def test_neighbors_center(self):
        """Test neighbors of a center tile in a grid."""
        walkable = {(4, 5), (6, 5), (5, 4), (5, 6)}
        result = neighbors((5, 5), walkable)
        self.assertEqual(set(result), {(4, 5), (6, 5), (5, 4), (5, 6)})

    def test_neighbors_corner(self):
        """Test neighbors of a corner tile in a grid."""
        walkable = {(1, 0), (0, 1)}
        result = neighbors((0, 0), walkable)
        self.assertEqual(set(result), {(1, 0), (0, 1)})

    def test_build_path_of_five_steps(self):
        """Test building a path of five steps"""
        came_from = {
            (0, 5): (0, 4),
            (0, 4): (0, 3),
            (0, 3): (0, 2),
            (0, 2): (0, 1),
            (0, 1): (0, 0)
        }
        path = build_path(came_from, (0, 5))
        self.assertEqual(path, [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5)])

    def test_astar_simple(self):
        """Test that A* finds a valid path in a small open grid."""
        start = (0, 0)
        goal = (2, 2)
        walkable_tiles = [(x, y) for x in range(3) for y in range(3)]
        path = astar(start, goal, walkable_tiles)
        self.assertEqual(path[0], (0, 0))
        self.assertEqual(path[-1], (2, 2))
        self.assertTrue(all(isinstance(p, tuple) for p in path))

    def test_astar_blocked(self):
        """Test A* returns no path when the goal is blocked by walls."""
        start = (0, 0)
        goal = (2, 2)
        all_tiles = [(x, y) for x in range(3) for y in range(3)]
        walls = [(1, 0), (1, 1), (1, 2)]
        walkable_tiles = [t for t in all_tiles if t not in walls]
        path = astar(start, goal, walkable_tiles)
        self.assertTrue(path == [] or path is None)

    def test_astar_start_is_goal(self):
        """Test A* returns a path with only the start when start equals goal.""" 
        start = (1, 1)
        goal = (1, 1)
        walkable_tiles = [(x, y) for x in range(3) for y in range(3)]
        path = astar(start, goal, walkable_tiles)
        self.assertEqual(path, [(1, 1)])

    