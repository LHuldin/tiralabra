from config import *
from room import *
from paths import *
import random

class Dungeon:
    """Represents a dungeon composed of multiple rooms and paths."""

    def __init__(self, num_rooms= ROOMS, max_blocks= BLOCKS):
        """Initialize a dungeon with a specified number of rooms and maximum blocks per room."""
        self.rooms = []
        self.room_start_points = []
        #self.paths = []
        self.generate_dungeon(num_rooms, max_blocks)
        self.paths = calculate_paths(self.room_start_points)

    def generate_dungeon(self, num_rooms, max_blocks):
        """Generate rooms randomly positioned and expanded within dungeon boundaries, avoiding overlaps."""
        attempts = 0
        max_attempts = num_rooms * 10

        while len(self.rooms) < num_rooms and attempts < max_attempts:
            attempts += 1
            room = Room()

            base_x = random.randint(0, (MAP_WIDTH // TILESIZE) - 2)
            base_y = random.randint(0, (MAP_HEIGHT // TILESIZE) - 2)

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


    def room_overlaps(self, new_room):
        """Check whether a newly created room overlaps with existing rooms in the dungeon."""
        for existing_room in self.rooms:
            for pos1 in new_room.positions:
                for pos2 in existing_room.positions:
                    dx = abs(pos1.x - pos2.x)
                    dy = abs(pos1.y - pos2.y)
                    if dx <= 3 and dy <= 3:
                        return True  
        return False

            

