import unittest
from paths import Point, Edge, Triangle

class TestPaths(unittest.TestCase):

    def test_edge_equality_and_hashing(self):
        a = Point(0, 0)
        b = Point(1, 1)
        edge1 = Edge(a, b)
        edge2 = Edge(b, a)

        self.assertEqual(edge1, edge2)
        self.assertEqual(hash(edge1), hash(edge2))

        # Test set behavior (no duplicates)
        edge_set = {edge1, edge2}
        self.assertEqual(len(edge_set), 1)
