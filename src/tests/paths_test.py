import unittest
from paths import * #Point, Edge, Triangle, prim_mst, distance

class TestPaths(unittest.TestCase):

    def test_edge_equality_and_hashing(self):
        """Test that Edge equality and hashing works regardless of point order."""
        a = Point(0, 0)
        b = Point(1, 1)
        edge1 = Edge(a, b)
        edge2 = Edge(b, a)

        self.assertEqual(edge1, edge2)
        self.assertEqual(hash(edge1), hash(edge2))

        # Test set behavior (no duplicates)
        edge_set = {edge1, edge2}
        self.assertEqual(len(edge_set), 1)

    def test_triangle_circumcircle(self):
        a = Point(0, 0)
        b = Point(4, 0)
        c = Point(0, 3)
        triangle = Triangle(a, b, c)
        center, radius_sq = triangle.circumcircle()
    
        self.assertAlmostEqual(center.x, 2.0)
        self.assertAlmostEqual(center.y, 1.5)
        self.assertAlmostEqual(radius_sq, 6.25)

    def test_bowyer_watson(self):
        """ Test that the Bowyer-Watson algorithm returns the correct triangulation
        for a square point configuration. Ensures:
        - All returned items are Triangle instances.
        - Exactly two triangles are created (as expected for a square).
        - All original points are present in the resulting triangles.
        """
        points = [Point(0, 0), Point(1, 0), Point(0, 1), Point(1, 1)]
        triangles = bowyer_watson(points)
        self.assertTrue(all(isinstance(tri, Triangle) for tri in triangles))
        
        self.assertEqual(len(triangles), 2)  
        all_points = [p for tri in triangles for p in tri.points]
        for pt in points:
            self.assertIn(pt, all_points)

    def test_remove_super_triangle(self):
        """Test that triangles with vertices from the super triangle are removed correctly."""
        points = [Point(0, 0), Point(1, 0), Point(0, 1)]
        super_triangle = create_super_triangle(points)
        triangles = [super_triangle]
        filtered = remove_super_triangle(triangles, super_triangle)
        self.assertEqual(len(filtered), 0)

    def test_bowyer_watson_collinear_points(self):
        """
        Test Bowyer-Watson algorithm with collinear points.

        Ensures that the algorithm correctly handles the edge case where all points 
        are collinear (lying on a single straight line). Expected that
        no triangles are formed, as it's geometrically impossible to create a valid 
        Delaunay triangulation from collinear points.
        """
        points = [Point(0, 0), Point(1, 1), Point(2, 2)]
        triangles = bowyer_watson(points)
        self.assertEqual(len(triangles), 0)

    def test_triangle_circumcircle_degenerate(self):
        """
        Test that circumcircle() returns None for degenerate (collinear) triangles.

        This ensures the method properly detects when the three points do not form
        a valid triangle (i.e., they are collinear) and handles it gracefully by 
        returning None.
        """
        a = Point(0, 0)
        b = Point(1, 1)
        c = Point(2, 2)  # All points lie on the same line
        triangle = Triangle(a, b, c)
        
        result = triangle.circumcircle()
        self.assertIsNone(result)
        

    def test_prim_mst(self):
        """Test that Prim's MST returns the correct number of minimal connecting edges."""
        a = Point(0, 0)
        b = Point(2, 0)
        c = Point(2, 2)
        d = Point(0, 2)
        e = Point(1, 1)
        
    
        edges = [(a, b), (a, d), (a, e),
            (b, c), (b, e),
            (c, d), (c, e),
            (d, e)]
    
        mst = prim_mst([a, b, c, d, e], edges)
    
        self.assertEqual(len(mst), 4)

        #frozenset ignores edge direction
        expected_edges = {frozenset((a, e)), frozenset((b, e)), frozenset((c, e)), frozenset((d, e))}
        
        mst_edges = {frozenset(edge) for edge in mst}
        
        self.assertEqual(mst_edges, expected_edges)

    def test_distance(self):
        """Test that distance function returns the correct Euclidean distance."""
        a = Point(0, 0)
        b = Point(3, 4)
        dist = distance(a, b)
        self.assertAlmostEqual(dist, 5.0)

    def test_prim_mst_empty_input(self):
        """
        Test that prim_mst returns an empty list when given no points.

        Ensures the function handles empty input gracefully without errors
        and returns an empty minimum spanning tree.
        """
        result = prim_mst([], [])
        self.assertEqual(result, [])

    def test_calculate_paths_empty_input(self):
        """
        Test that calculate_paths returns an empty list when given no room points.

        Ensures graceful handling of empty input and that no exception is raised.
        """
        result = calculate_paths([])
        self.assertEqual(result, [])

