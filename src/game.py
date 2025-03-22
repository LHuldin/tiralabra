import pygame
from config import WINDOW_WIDTH, WINDOW_HEIGHT, FPS

class Game:
    def __init__(self):
        """Initializes the game window, clock, and running state."""
        self.display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Dungeon Runner")
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
            self.clock.tick(FPS)

    def handle_events(self):
        """Processes user input and system events.

        Sets the running to False if the user quit the game.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

        keys = pygame.key.get_pressed()

    def update(self):
        """Updates the game state.

        This method is currently a placeholder and does not perform any updates.
        """
        pass
