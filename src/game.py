import pygame
from config import * #WINDOW_WIDTH, WINDOW_HEIGHT, FPS, TILESIZE, UI_HEIGHT
from dungeon import Dungeon
from character import Character
from paths import *
from astar import astar

class Game:
    def __init__(self):
        """Initializes the game window, clock, buttons and running state."""
        self.display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT + UI_HEIGHT))
        pygame.display.set_caption("Dungeon Runner")

        #Surface creates game area, camera defines visible area
        self.surface = pygame.Surface((MAP_WIDTH, MAP_HEIGHT))
        self.camera = pygame.Rect(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)

        self.dungeon = Dungeon()

        self.walls = set()
        self.create_walls()

        self.goal_position = self.dungeon.goal_position
        self.game_over = False

        self.grid_button_rect = pygame.Rect(160, WINDOW_HEIGHT + 10, 120, 30)
        self.quit_button_rect = pygame.Rect(WINDOW_WIDTH - 140, WINDOW_HEIGHT + 10, 120, 30)
        self.new_map_button_rect = pygame.Rect(20, WINDOW_HEIGHT + 10, 120, 30)
        self.paths_button_rect = pygame.Rect(300, WINDOW_HEIGHT + 10, 120, 30)
        self.all_paths_button_rect = pygame.Rect(440, WINDOW_HEIGHT + 10, 120, 30)
        self.toggle_color_button_rect = pygame.Rect(20, WINDOW_HEIGHT + 50, 120, 30)
        self.extra_button2 = pygame.Rect(160, WINDOW_HEIGHT + 50, 120, 30)
        self.extra_button3 = pygame.Rect(300, WINDOW_HEIGHT + 50, 120, 30)
        self.extra_button4 = pygame.Rect(440, WINDOW_HEIGHT + 50, 120, 30)

        self.path_display_mode = 0  # 0 = none, 1 = triangulation, 2 = MST
        self.show_all_paths = False
        self.show_grid = False
        self.clock = pygame.time.Clock()
        self.running = True
        self.brown_mode = True
        self.follow_player = True
        self.limited_visibility = True

        for room in self.dungeon.rooms:
            room.color = (181, 101, 29)

        self.corridor_color = (181, 101, 29) if self.brown_mode else (255, 255, 255)

        self.walkable_tiles = self.get_walkable_tiles()
        start_tile = self.dungeon.room_start_points[0]
        start_x, start_y = start_tile[0] * TILESIZE, start_tile[1] * TILESIZE
        self.character = Character(x=start_x, y=start_y)



    def run(self): # pragma: no cover
        """Runs the main game loop.

        Continuously handles events and updates the game state
        until the game is no longer running.
        """
        while self.running:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(FPS)

    def handle_events(self): # pragma: no cover
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
                    for room in self.dungeon.rooms:
                        room.color = (181, 101, 29)
                    self.corridor_color = (181, 101, 29)
                    self.create_walls()
                    self.walkable_tiles = self.get_walkable_tiles()
                    start_tile = self.dungeon.room_start_points[0]
                    start_x, start_y = start_tile[0] * TILESIZE, start_tile[1] * TILESIZE
                    self.character = Character(x=start_x, y=start_y)
                    self.camera.topleft = (0, 0)
                    self.goal_position = self.dungeon.goal_position
                    self.game_over = False
                elif self.grid_button_rect.collidepoint(event.pos):
                    self.show_grid = not self.show_grid
                elif self.paths_button_rect.collidepoint(event.pos):
                    self.path_display_mode = (self.path_display_mode + 1) % 3
                elif self.all_paths_button_rect.collidepoint(event.pos):
                    self.show_all_paths = not self.show_all_paths
                elif self.toggle_color_button_rect.collidepoint(event.pos):
                    self.toggle_dungeon_colors()
                elif self.extra_button2.collidepoint(event.pos):
                    self.follow_player = not self.follow_player
                elif self.extra_button3.collidepoint(event.pos):
                    self.limited_visibility = not self.limited_visibility
        if not self.game_over:
            keys = pygame.key.get_pressed()
            self.character.handle_input(keys, self.walkable_tiles)

    def update(self):  # pragma: no cover
        """Updates the game state.
        """
        keys = pygame.key.get_pressed()
        if self.follow_player:
            self.camera.center = (self.character.x + TILESIZE // 2,
                                  self.character.y + TILESIZE // 2)
        else:
            camera_speed = 10
            if keys[pygame.K_a]:
                self.camera.x -= camera_speed
            if keys[pygame.K_d]:
                self.camera.x += camera_speed
            if keys[pygame.K_w]:
                self.camera.y -= camera_speed
            if keys[pygame.K_s]:
                self.camera.y += camera_speed

        #Prevent camera from going outside game area
        self.camera.x = max(0, min(self.camera.x, self.surface.get_width() - self.camera.width))
        self.camera.y = max(0, min(self.camera.y, self.surface.get_height() - self.camera.height))

        if (self.character.x, self.character.y) == self.goal_position:
            self.end_game(self.display)

    def render(self):  # pragma: no cover
        """Renders dungeon rooms and blocks onto the display."""
        self.display.fill((0, 0, 0))
        self.surface.fill((30, 30, 30))

        player_tile = (self.character.x // TILESIZE, self.character.y // TILESIZE)

        for room in self.dungeon.rooms:
            for block in room.blocks:
                tile_pos = (block.position.x, block.position.y)

                if not self.limited_visibility or (
                    abs(tile_pos[0] - player_tile[0]) <= 8 and
                    abs(tile_pos[1] - player_tile[1]) <= 8
                ):
                    pygame.draw.rect(self.surface,
                        room.color, (block.position.x * TILESIZE, block.position.y * TILESIZE,
                                     TILESIZE, TILESIZE))
        for (x, y) in self.dungeon.corridor_positions_mst:
            if not self.limited_visibility or (
                abs(x - player_tile[0]) <= 8 and abs(y - player_tile[1]) <= 8
            ):
                pygame.draw.rect(self.surface, self.corridor_color, (x * TILESIZE, y * TILESIZE,
                                                                     TILESIZE, TILESIZE))

        self.draw_walls(self.surface)

        goal_x, goal_y = self.goal_position
        goal_tile = (goal_x // TILESIZE, goal_y // TILESIZE)

        time_now = pygame.time.get_ticks()
        color_phase = (time_now // 500) % 3

        if color_phase == 0:
            goal_color = (255, 255, 0)  # yellow
        elif color_phase == 1:
            goal_color = (0, 255, 0)    # green
        else:
            goal_color = (0, 255, 255)  # cyan

        if not self.limited_visibility or (
            abs(goal_tile[0] - player_tile[0]) <= 8 and abs(goal_tile[1] - player_tile[1]) <= 8
        ):
            pygame.draw.rect(
                self.surface,
                goal_color,
                (goal_x, goal_y, TILESIZE, TILESIZE)
            )

        self.character.draw(self.surface)

        """Renders grid over display."""        
        if self.show_grid:
            for x in range(0, MAP_WIDTH, TILESIZE):
                pygame.draw.line(self.surface, (60, 60, 60), (x, 0), (x, MAP_HEIGHT))
            for y in range(0, MAP_HEIGHT, TILESIZE):
                pygame.draw.line(self.surface, (60, 60, 60), (0, y), (MAP_WIDTH, y))

        """Renders lines between all the rooms."""

        if self.show_all_paths:
            points = self.dungeon.room_start_points
            for i in range(len(points)):
                for j in range(i + 1, len(points)):
                    pygame.draw.line(
                        self.surface, (255, 255, 0),
                        (points[i][0] * TILESIZE, points[i][1] * TILESIZE),
                        (points[j][0] * TILESIZE, points[j][1] * TILESIZE), 2)

        if self.path_display_mode == 1:
            for path in self.dungeon.paths:
                start = (path[0][0] * TILESIZE, path[0][1] * TILESIZE)
                end = (path[1][0] * TILESIZE, path[1][1] * TILESIZE)
                pygame.draw.line(self.surface, (255, 0, 0), start, end, 2)

        elif self.path_display_mode == 2:
            for path in self.dungeon.paths_mst:
                start = (path[0][0] * TILESIZE, path[0][1] * TILESIZE)
                end = (path[1][0] * TILESIZE, path[1][1] * TILESIZE)
                pygame.draw.line(self.surface, (255, 0, 255), start, end, 2)


        """DRAW ONLY CAMERA'S VIEW OF Surface"""
        self.display.blit(self.surface, (0, 0), self.camera)

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
        text = font.render("Show Tri/MST", True, (255, 255, 255))
        text_rect = text.get_rect(center=self.paths_button_rect.center)
        self.display.blit(text, text_rect)

        pygame.draw.rect(self.display, (150, 75, 0), self.all_paths_button_rect)
        text = font.render("Show All Paths", True, (255, 255, 255))
        text_rect = text.get_rect(center=self.all_paths_button_rect.center)
        self.display.blit(text, text_rect)

        pygame.draw.rect(self.display, (100, 100, 255), self.toggle_color_button_rect)
        text = font.render("Color", True, (255, 255, 255))
        text_rect = text.get_rect(center=self.toggle_color_button_rect.center)
        self.display.blit(text, text_rect)

        follow_text = "Follow: ON" if self.follow_player else "Follow: OFF"
        pygame.draw.rect(self.display, (100, 100, 255), self.extra_button2)
        text = font.render(follow_text, True, (255, 255, 255))
        text_rect = text.get_rect(center=self.extra_button2.center)
        self.display.blit(text, text_rect)

        visibility_text = "Fog: ON" if self.limited_visibility else "Fog: OFF"
        pygame.draw.rect(self.display, (100, 100, 255), self.extra_button3)
        text = font.render(visibility_text, True, (255, 255, 255))
        text_rect = text.get_rect(center=self.extra_button3.center)
        self.display.blit(text, text_rect)

        if self.game_over:
            font_big = pygame.font.SysFont(None, 28)
            text_surface = font_big.render(
                "Congratulations! You reached the goal. Click 'New Map' to play again.",
                True, (255, 255, 255))
            text_rect = text_surface.get_rect(center=(self.display.get_width() // 2,
                                                      self.display.get_height() // 2))
            self.display.blit(text_surface, text_rect)

        """ Draw A* distance """
        start_tile = (self.character.x // TILESIZE, self.character.y // TILESIZE)
        goal_tile = (self.goal_position[0] // TILESIZE, self.goal_position[1] // TILESIZE)
        path = astar(start_tile, goal_tile, self.walkable_tiles)
        distance = len(path) - 1 if path else -1
        distance_text = font.render(f"Distance to goal: {distance if distance >= 0 else 'N/A'}",
                                    True, (255, 255, 255))
        self.display.blit(distance_text, (WINDOW_WIDTH - 180, WINDOW_HEIGHT + 50, 120, 30))



        pygame.display.flip()

    def get_walkable_tiles(self):
        tiles = set()
        for room in self.dungeon.rooms:
            tiles.update((p.x, p.y) for p in room.positions)
        tiles.update(self.dungeon.corridor_positions_mst)
        return tiles

    def create_walls(self):
        self.walls = set()
        occupied = set()
        for room in self.dungeon.rooms:
            occupied |= {(block.position.x, block.position.y) for block in room.blocks}
        occupied |= set(self.dungeon.corridor_positions_mst)

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        for x, y in occupied:
            for dx, dy in directions:
                neighbor = (x + dx, y + dy)
                if neighbor not in occupied:
                    self.walls.add(neighbor)

    def draw_walls(self, surface): # pragma: no cover
        player_tile = (self.character.x // TILESIZE, self.character.y // TILESIZE)

        for x, y in self.walls:
            if not self.limited_visibility or (
                abs(x - player_tile[0]) <= 8 and abs(y - player_tile[1]) <= 8
            ):
                pygame.draw.rect(surface, (100, 100, 100), (x * TILESIZE, y * TILESIZE,
                                                            TILESIZE, TILESIZE))

    def toggle_dungeon_colors(self): # pragma: no cover
        self.brown_mode = not self.brown_mode
        if self.brown_mode:
            color = (181, 101, 29)
        else:
            color = None

        for room in self.dungeon.rooms:
            if color:
                room.color = color
            else:
                room.color = room.random_color()

        self.corridor_color = color if color else (255, 255, 255)

    def end_game(self, screen): # pragma: no cover
        self.running = True   #False
        self.game_over = True

        font = pygame.font.SysFont(None, 28)
        text_surface = font.render(
            "Congratulations! You reached the goal. Click 'New Map' to play again.",
            True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(screen.get_width() // 2,
                                                  screen.get_height() // 2))
        screen.blit(text_surface, text_rect)
        pygame.display.flip()
