from config import *
from room import *
import random

class Dungeon:
    def __init__(self, num_rooms= ROOMS, max_blocks= BLOCKS):
        self.rooms = []
        self.generate_dungeon(num_rooms, max_blocks)

    """
    def generate_dungeon(self, num_rooms, max_blocks):
        for _ in range(num_rooms):
            room = Room()
            room.add_block(Position(random.randint(0, WINDOW_WIDTH//TILESIZE), 
                                    random.randint(0, WINDOW_HEIGHT//TILESIZE)))
            
            for _ in range(random.randint(1, max_blocks - 1)):
                room.expand()

            self.rooms.append(room)
    """ 

    """ 
    def generate_dungeon(self, num_rooms, max_blocks):
        for _ in range(num_rooms):
            room = Room()

            # Satunnainen vasen yläkulma 2x2 huoneelle
            base_x = random.randint(0, (WINDOW_WIDTH // TILESIZE) - 2)
            base_y = random.randint(0, (WINDOW_HEIGHT // TILESIZE) - 2)

            # Lisää 2x2 lohkot
            starting_positions = [
                Position(base_x, base_y),
                Position(base_x + 1, base_y),
                Position(base_x, base_y + 1),
                Position(base_x + 1, base_y + 1),
            ]

            for pos in starting_positions:
                room.add_block(pos)

            # Laajenna huonetta lopuilla expand-kutsuilla
            expand_count = random.randint(1, max_blocks - len(starting_positions))
            for _ in range(expand_count):
                room.expand() 

            self.rooms.append(room)
    """ 

    def generate_dungeon(self, num_rooms, max_blocks):
        attempts = 0
        max_attempts = num_rooms * 10

        while len(self.rooms) < num_rooms and attempts < max_attempts:
            attempts += 1
            room = Room()

            base_x = random.randint(0, (WINDOW_WIDTH // TILESIZE) - 2)
            base_y = random.randint(0, (WINDOW_HEIGHT // TILESIZE) - 2)

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
                continue  # Hylkää, jos liian lähellä toisia huoneita

            self.rooms.append(room)


    def room_overlaps(self, new_room):
        for existing_room in self.rooms:
            for pos1 in new_room.positions:
                for pos2 in existing_room.positions:
                    dx = abs(pos1.x - pos2.x)
                    dy = abs(pos1.y - pos2.y)
                    if dx <= 3 and dy <= 3:
                        return True  
        return False

            

