import unittest
from paths import Point, Edge, Triangle, prim_mst, distance

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

    def test_prim_mst(self):
        a = Point(0, 0)
        b = Point(1, 0)
        c = Point(0, 1)
    
        edges = [(a, b), (b, c), (a, c)]
    
        mst = prim_mst([a, b, c], edges)
    
        self.assertEqual(len(mst), 2)
    
        expected_edges = {(a, b), (a, c), (b, a), (c, a)}
        for i in mst:
            self.assertIn(i, expected_edges)

    def test_distance(self):
        a = Point(0, 0)
        b = Point(3, 4)
        dist = distance(a, b)
        self.assertAlmostEqual(dist, 5.0)
