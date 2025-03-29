import pygame
from config import WINDOW_WIDTH, WINDOW_HEIGHT, FPS, TILESIZE, UI_HEIGHT
from dungeon import Dungeon

class Game:
    
    def __init__(self):
        """Initializes the game window, clock, buttons and running state."""
        self.display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT + UI_HEIGHT))
        pygame.display.set_caption("Dungeon Runner")
        self.dungeon = Dungeon()
        
        self.grid_button_rect = pygame.Rect(160, WINDOW_HEIGHT + 10, 120, 30)
        self.quit_button_rect = pygame.Rect(WINDOW_WIDTH - 140, WINDOW_HEIGHT + 10, 120, 30)
        self.new_map_button_rect = pygame.Rect(20, WINDOW_HEIGHT + 10, 120, 30)
        self.paths_button_rect = pygame.Rect(300, WINDOW_HEIGHT + 10, 120, 30)
        
        self.show_paths = False
        self.show_grid = False
        self.clock = pygame.time.Clock()
        self.running = True

    def run(self):
        """Runs the main game loop.

        Continuously handles events and updates the game state
        until the game is no longer running.
        """
        while self.running:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(FPS)

    def handle_events(self):
        """Processes user input and system events.

        Sets the running to False if the user quit the game.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.quit_button_rect.collidepoint(event.pos):
                    self.running = False
                elif self.new_map_button_rect.collidepoint(event.pos):
                    self.dungeon = Dungeon()
                elif self.grid_button_rect.collidepoint(event.pos):
                    self.show_grid = not self.show_grid
                elif self.paths_button_rect.collidepoint(event.pos):
                    self.show_paths = not self.show_paths

        keys = pygame.key.get_pressed()

    def update(self):
        """Updates the game state.

        This method is currently a placeholder and does not perform any updates.
        """
        pass

    def render(self):
        """Renders dungeon rooms and blocks onto the display."""
        self.display.fill((0, 0, 0))
        for room in self.dungeon.rooms:
            for block in room.blocks:
                pygame.draw.rect(self.display, room.color, 
                                 (block.position.x * TILESIZE, block.position.y * TILESIZE, TILESIZE, TILESIZE))

        """Renders grid over display."""        
        if self.show_grid:
            for x in range(0, WINDOW_WIDTH, TILESIZE):
                pygame.draw.line(self.display, (60, 60, 60), (x, 0), (x, WINDOW_HEIGHT))
            for y in range(0, WINDOW_HEIGHT, TILESIZE):
                pygame.draw.line(self.display, (60, 60, 60), (0, y), (WINDOW_WIDTH, y))

        
        """
        points = self.dungeon.room_start_points
        if len(points) > 1:
            for i in range(len(points) - 1):
                pygame.draw.line(
                    self.display, (255, 255, 0), 
                    (points[i][0] * TILESIZE, points[i][1] * TILESIZE), 
                    (points[i+1][0] * TILESIZE, points[i+1][1] * TILESIZE), 2)
        """
        """Renders lines between all the rooms."""
        if self.show_paths:
            points = self.dungeon.room_start_points
            for i in range(len(points)):
                for j in range(i + 1, len(points)):
                    pygame.draw.line(
                        self.display, (255, 255, 0),
                        (points[i][0] * TILESIZE, points[i][1] * TILESIZE),
                        (points[j][0] * TILESIZE, points[j][1] * TILESIZE), 2)

        pygame.draw.rect(self.display, (50, 50, 50), (0, WINDOW_HEIGHT, WINDOW_WIDTH, UI_HEIGHT))
        font = pygame.font.SysFont(None, 24)

        pygame.draw.rect(self.display, (0, 120, 200), self.new_map_button_rect)
        text = font.render("New Map", True, (255, 255, 255))
        text_rect = text.get_rect(center=self.new_map_button_rect.center)
        self.display.blit(text, text_rect)

        pygame.draw.rect(self.display, (0, 180, 100), self.grid_button_rect)
        text = font.render("Show Grid", True, (255, 255, 255))
        text_rect = text.get_rect(center=self.grid_button_rect.center)
        self.display.blit(text, text_rect)

        pygame.draw.rect(self.display, (200, 0, 0), self.quit_button_rect)
        text = font.render("Quit", True, (255, 255, 255))
        text_rect = text.get_rect(center=self.quit_button_rect.center)
        self.display.blit(text, text_rect)

        pygame.draw.rect(self.display, (150, 0, 200), self.paths_button_rect)
        text = font.render("Show All Paths", True, (255, 255, 255))
        text_rect = text.get_rect(center=self.paths_button_rect.center)
        self.display.blit(text, text_rect)


        pygame.display.flip()
