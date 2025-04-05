from collections import namedtuple
from typing import List, Tuple, Set

Point = namedtuple("Point", ["x", "y"])

class Edge:
    def __init__(self, p1: Point, p2: Point):
        """Represents an undirected edge between two points."""
        self.p1 = p1
        self.p2 = p2

    def __eq__(self, other):
        return {self.p1, self.p2} == {other.p1, other.p2}

    def __hash__(self):
        return hash(frozenset((self.p1, self.p2)))

    #def __repr__(self):
    #    return f"Edge({self.p1}, {self.p2})"

class Triangle:
    def __init__(self, p1: Point, p2: Point, p3: Point):
        """Represents a triangle defined by three points."""
        self.points = [p1, p2, p3]
        self.edges = [Edge(p1, p2), Edge(p2, p3), Edge(p3, p1)]
        self.circumcenter, self.radius_sq = self.circumcircle()

    def circumcircle(self) -> Tuple[Point, float]:
        """Calculates the circumcircle center and squared radius of the triangle."""
        A, B, C = self.points
        d = 2 * (A.x * (B.y - C.y) + B.x * (C.y - A.y) + C.x * (A.y - B.y))
        if d == 0:
            return Point(0, 0), float('inf')

        ux = ((A.x**2 + A.y**2)*(B.y - C.y) + (B.x**2 + B.y**2)*(C.y - A.y) + (C.x**2 + C.y**2)*(A.y - B.y)) / d
        uy = ((A.x**2 + A.y**2)*(C.x - B.x) + (B.x**2 + B.y**2)*(A.x - C.x) + (C.x**2 + C.y**2)*(B.x - A.x)) / d
        center = Point(ux, uy)
        radius_sq = (center.x - A.x)**2 + (center.y - A.y)**2
        return center, radius_sq

    def contains_point_in_circumcircle(self, point: Point) -> bool:
        """Checks whether a point lies inside the triangle's circumcircle."""
        dx = self.circumcenter.x - point.x
        dy = self.circumcenter.y - point.y
        return dx * dx + dy * dy < self.radius_sq

def create_super_triangle(points: List[Point]) -> Triangle:
    """Creates a super-triangle that completely encloses all given points.
    
    The triangle is constructed using a scaling factor of 20 * delta_max 
    (where delta_max is the maximum range in x or y direction among the points). 
    This ensures the triangle is large enough to encompass all input points 
    regardless of their distribution.
    """
    min_x, max_x = min(p.x for p in points), max(p.x for p in points)
    min_y, max_y = min(p.y for p in points), max(p.y for p in points)
    dx, dy = max_x - min_x, max_y - min_y
    delta_max = max(dx, dy)
    mid_x, mid_y = (min_x + max_x) / 2, (min_y + max_y) / 2

    p1 = Point(mid_x - 20 * delta_max, mid_y - delta_max)
    p2 = Point(mid_x, mid_y + 20 * delta_max)
    p3 = Point(mid_x + 20 * delta_max, mid_y - delta_max)
    return Triangle(p1, p2, p3)

def find_bad_triangles(triangles: List[Triangle], point: Point) -> List[Triangle]:
    """Finds triangles whose circumcircles contain the given point."""
    return [t for t in triangles if t.contains_point_in_circumcircle(point)]

def find_polygon_edges(bad_triangles: List[Triangle]) -> List[Edge]:
    """Finds the boundary edges of the polygonal hole created by removing bad triangles."""
    polygon: List[Edge] = []
    for tri in bad_triangles:
        for edge in tri.edges:
            if not any(edge in other.edges for other in bad_triangles if other != tri):
                polygon.append(edge)
    return polygon

def retriangulate(triangles: List[Triangle], polygon: List[Edge], point: Point) -> None:
    """Creates new triangles by connecting polygon edges to the given point."""
    for edge in polygon:
        triangles.append(Triangle(edge.p1, edge.p2, point))

def remove_super_triangle(triangles: List[Triangle], super_triangle: Triangle) -> List[Triangle]:
    """Removes triangles that include any vertex of the original super-triangle."""
    return [t for t in triangles if all(p not in super_triangle.points for p in t.points)]

def bowyer_watson(points: List[Point]) -> List[Triangle]:
    """Performs the Bowyer-Watson algorithm to generate a Delaunay triangulation."""
    super_triangle = create_super_triangle(points)
    triangles = [super_triangle]

    for point in points:
        bad_triangles = find_bad_triangles(triangles, point)
        polygon = find_polygon_edges(bad_triangles)

        for tri in bad_triangles:
            triangles.remove(tri)

        retriangulate(triangles, polygon, point)

    return remove_super_triangle(triangles, super_triangle)

def calculate_paths(room_points: List[Tuple[float, float]]) -> List[Tuple[Point, Point]]:
    """Calculates valid paths between rooms using Delaunay triangulation.

    Args:
        room_points: List of (x, y) tuples representing room positions.

    Returns:
        A list of tuples, each containing two Points that form an edge in the path network.
    """
    points = [Point(x, y) for x, y in room_points]
    triangles = bowyer_watson(points)

    edges: Set[Edge] = set()
    for tri in triangles:
        for edge in tri.edges:
            if edge.p1 in points and edge.p2 in points:
                edges.add(edge)

    return [(edge.p1, edge.p2) for edge in edges]


