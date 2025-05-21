import os
import pygame
from config import TILESIZE

class Character:
    def __init__(self, x, y, color=(255, 0, 0)):
        """Initializes a new Character."""

        self.x = x
        self.y = y
        self.color = color
        self.radius = TILESIZE // 2
        self.speed = TILESIZE
        self.last_move_time = 0
        base_dir = os.path.dirname(__file__)
        image_path = os.path.join(base_dir, "assets", "hero.png")
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (TILESIZE, TILESIZE))

    def handle_input(self, keys, walkable_tiles): # pragma: no cover
        now = pygame.time.get_ticks()
        if now - self.last_move_time < 150:  # ms
            return

        new_x, new_y = self.x, self.y

        if keys[pygame.K_LEFT]:
            new_x -= self.speed
        elif keys[pygame.K_RIGHT]:
            new_x += self.speed
        elif keys[pygame.K_UP]:
            new_y -= self.speed
        elif keys[pygame.K_DOWN]:
            new_y += self.speed
        else:
            return

        new_tile = (new_x // TILESIZE, new_y // TILESIZE)
        if new_tile in walkable_tiles:
            self.x, self.y = new_x, new_y
            self.last_move_time = now

    def draw(self, surface): # pragma: no cover
        surface.blit(self.image, (self.x, self.y))
