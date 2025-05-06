from config import *
from room import *
from paths import *
import random
from typing import List, Tuple

class Dungeon:
    """Represents a dungeon composed of multiple rooms and paths."""

    def __init__(self, num_rooms= ROOMS, max_blocks= BLOCKS):
        """Initialize a dungeon with a specified number of rooms and maximum blocks per room."""
        self.rooms = []
        self.room_start_points = []
        self.corridor_positions = []
        self.corridor_positions_mst = []
        self.paths = []
        self.paths_mst = []
        self.generate_dungeon(num_rooms, max_blocks)
        self.paths = calculate_paths(self.room_start_points)
        goal_tile = self.room_start_points[-1]
        self.goal_position = (goal_tile[0] * TILESIZE, goal_tile[1] * TILESIZE)
        

    def generate_dungeon(self, num_rooms, max_blocks):
        """Generate rooms randomly positioned and expanded within dungeon boundaries, avoiding overlaps."""
        attempts = 0
        max_attempts = num_rooms * 10

        while len(self.rooms) < num_rooms and attempts < max_attempts:
            attempts += 1
            room = Room()

            base_x = random.randint(1, (MAP_WIDTH // TILESIZE) - 3)
            base_y = random.randint(1, (MAP_HEIGHT // TILESIZE) - 3)

            starting_positions = [
                Position(base_x, base_y),
                Position(base_x + 1, base_y),
                Position(base_x, base_y + 1),
                Position(base_x + 1, base_y + 1),
            ]

            for pos in starting_positions:
                room.add_block(pos)

            expand_count = random.randint(1, max_blocks - len(starting_positions))
            for _ in range(expand_count):
                room.expand()

            if self.room_overlaps(room):
                continue 

            self.room_start_points.append((base_x, base_y))
            self.rooms.append(room)

        #self.paths = calculate_paths(self.room_start_points)
        
        
        
        """Generate simple corridors between rooms based on Delaunay triangulation"""
        self.paths = calculate_paths([(x, y) for (x, y) in self.room_start_points])

        for p1, p2 in self.paths:
            corridor = []

            # First, draw a horizontal corridor from p1 to p2
            for x in range(min(p1.x, p2.x), max(p1.x, p2.x) + 1):
                corridor.append((x, p1.y))

            # Then, draw a vertical corridor from the end of horizontal segment to p2
            for y in range(min(p1.y, p2.y), max(p1.y, p2.y) + 1):
                corridor.append((p2.x, y))

            # Add all corridor tiles to the dungeon's corridor list  
            self.corridor_positions.extend(corridor)

        

        """Generate paths using Delaunay triangulation and filter them using Prim's algorithm."""
        points = [Point(x, y) for (x, y) in self.room_start_points]
        edges = calculate_paths(self.room_start_points)
        self.paths_mst = prim_mst(points, edges)

        """Create corridors between points in the MST."""
        for p1, p2 in self.paths_mst:
            corridor = []

            # First, draw a horizontal corridor from p1 to p2
            for x in range(min(p1.x, p2.x), max(p1.x, p2.x) + 1):
                corridor.append((x, p1.y))

            # Then, draw a vertical corridor from the end of the horizontal segment to p2
            for y in range(min(p1.y, p2.y), max(p1.y, p2.y) + 1):
                corridor.append((p2.x, y))

            # Add all corridor tiles to the dungeon's corridor list
            self.corridor_positions_mst.extend(corridor)


    def room_overlaps(self, new_room) -> bool:
        """Check whether a newly created room overlaps with existing rooms in the dungeon."""
        for existing_room in self.rooms:
            for pos1 in new_room.positions:
                for pos2 in existing_room.positions:
                    dx = abs(pos1.x - pos2.x)
                    dy = abs(pos1.y - pos2.y)
                    if dx <= 3 and dy <= 3:
                        return True  
        return False

            

