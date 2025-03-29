from config import TILESIZE
import random

class Room:
    def __init__(self):
        self.blocks = set()
        self.positions = set()
        self.color = self.random_color()

    def random_color(self):
        return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def add_block(self, position):
        if position not in self.positions:
            self.blocks.add(Block(position))
            self.positions.add(position)

    def expand(self):
        candidates = set()
        for pos in self.positions:
            for neighbor in pos.neighbors():
                if neighbor not in self.positions:
                    candidates.add(neighbor)
        if candidates:
            self.add_block(random.choice(list(candidates)))

    def all_borders(self):
        borders = []
        for block in self.blocks:
            borders.extend(block.borders())
        return borders
    
class Block:
    def __init__(self, position):
        self.position = position

    def borders(self):
        x, y = self.position.x, self.position.y
        return [((x, y), (x+1, y)), ((x+1, y), (x+1, y+1)),
                ((x+1, y+1), (x, y+1)), ((x, y+1), (x, y))]
    
class Position:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def neighbors(self):
        return [Position(self.x+1, self.y), Position(self.x-1, self.y),
                Position(self.x, self.y+1), Position(self.x, self.y-1)]

    def __eq__(self, other):
        return isinstance(other, Position) and self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))