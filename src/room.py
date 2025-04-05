from config import TILESIZE
import random
from typing import Set, Tuple, Optional, List

class Room:
    """Represents a room composed of blocks in a dungeon."""

    def __init__(self):
        """Initialize a room with empty blocks, positions, random color, and no starting position."""
        self.blocks = set()
        self.positions = set()
        self.color = self.random_color()
        self.starting_position = None

    def random_color(self):
        return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def add_block(self, position):
        """Add a new block to the room at the given position if it's not already occupied."""
        if position not in self.positions:
            self.blocks.add(Block(position))
            self.positions.add(position)

    def expand(self):
        """Expand the room by adding a block at a randomly selected neighboring position."""
        candidates = set()
        for pos in self.positions:
            for neighbor in pos.neighbors():
                if neighbor not in self.positions:
                    candidates.add(neighbor)
        if candidates:
            self.add_block(random.choice(list(candidates)))

    """

    def all_borders(self):
        borders = []
        for block in self.blocks:
            borders.extend(block.borders())
        return borders
    """
    
class Block:
    def __init__(self, position):
        self.position = position

    """
    def borders(self):
        x, y = self.position.x, self.position.y
        return [((x, y), (x+1, y)), ((x+1, y), (x+1, y+1)),
                ((x+1, y+1), (x, y+1)), ((x, y+1), (x, y))]
    """
    
class Position:
    """Represents a 2D position on the grid."""

    def __init__(self, x, y, z=0):
        self.x = x
        self.y = y
        self.z = z

    def neighbors(self) -> List["Position"]:
        return [Position(self.x+1, self.y), 
                Position(self.x-1, self.y),
                Position(self.x, self.y+1), 
                Position(self.x, self.y-1)
            ]

    def __eq__(self, other):
        return (self.x, self.y, self.z) == (other.x, other.y, other.z)

    def __hash__(self):
        return hash((self.x, self.y, self.z))

    """
    def __init__(self, x, y):
        self.x, self.y = x, y

    
    def neighbors(self):
        return [Position(self.x+1, self.y), Position(self.x-1, self.y),
                Position(self.x, self.y+1), Position(self.x, self.y-1)]
    

    def __eq__(self, other):
        return isinstance(other, Position) and self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))
    """