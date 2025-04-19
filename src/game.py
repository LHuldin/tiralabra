import pygame
from config import * #WINDOW_WIDTH, WINDOW_HEIGHT, FPS, TILESIZE, UI_HEIGHT
from dungeon import Dungeon
from character import Character
from paths import *

class Game:
    
    def __init__(self):
        """Initializes the game window, clock, buttons and running state."""
        self.display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT + UI_HEIGHT))
        pygame.display.set_caption("Dungeon Runner")

        #self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT + UI_HEIGHT))  # ADDED UI HEIGHT TO WINDOW SIZE
        
        self.surface = pygame.Surface((MAP_WIDTH, MAP_HEIGHT))  # CREATES GAME AREA, LARGER THAN WINDOW
        self.camera = pygame.Rect(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)  # CAMERA DEFINES VISIBLE AREA



        self.dungeon = Dungeon()

        self.walls = set()
        self.create_walls()
        #self.paths = Paths(self.dungeon.rooms)

        

        
        
        self.grid_button_rect = pygame.Rect(160, WINDOW_HEIGHT + 10, 120, 30)
        self.quit_button_rect = pygame.Rect(WINDOW_WIDTH - 140, WINDOW_HEIGHT + 10, 120, 30)
        self.new_map_button_rect = pygame.Rect(20, WINDOW_HEIGHT + 10, 120, 30)
        self.paths_button_rect = pygame.Rect(300, WINDOW_HEIGHT + 10, 120, 30)
        self.all_paths_button_rect = pygame.Rect(440, WINDOW_HEIGHT + 10, 120, 30)
        
        #self.show_paths = False
        self.path_display_mode = 0  # 0 = none, 1 = triangulation, 2 = MST
        self.show_all_paths = False
        self.show_grid = False
        self.clock = pygame.time.Clock()
        self.running = True

        self.walkable_tiles = self.get_walkable_tiles()
        start_tile = self.dungeon.room_start_points[0]
        start_x, start_y = start_tile[0] * TILESIZE, start_tile[1] * TILESIZE
        self.character = Character(x=start_x, y=start_y)



    def run(self):
        """Runs the main game loop.

        Continuously handles events and updates the game state
        until the game is no longer running.
        """
        while self.running:
            self.handle_events()
            self.update()
            self.render()
            #pygame.display.flip()
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
                    self.create_walls()
                    self.walkable_tiles = self.get_walkable_tiles()
                    start_tile = self.dungeon.room_start_points[0]
                    start_x, start_y = start_tile[0] * TILESIZE, start_tile[1] * TILESIZE
                    self.character = Character(x=start_x, y=start_y)
                    self.camera.topleft = (0, 0)
                elif self.grid_button_rect.collidepoint(event.pos):
                    self.show_grid = not self.show_grid
                #elif self.paths_button_rect.collidepoint(event.pos):
                #    self.show_paths = not self.show_paths
                elif self.paths_button_rect.collidepoint(event.pos):
                    self.path_display_mode = (self.path_display_mode + 1) % 3
                elif self.all_paths_button_rect.collidepoint(event.pos):
                    self.show_all_paths = not self.show_all_paths

        keys = pygame.key.get_pressed()
        self.character.handle_input(keys, self.walkable_tiles)

    def update(self):
        """Updates the game state.

        """
        #pass
        


        keys = pygame.key.get_pressed()
        camera_speed = 10

        if keys[pygame.K_a]:
            self.camera.x -= camera_speed
        if keys[pygame.K_d]:
            self.camera.x += camera_speed
        if keys[pygame.K_w]:
            self.camera.y -= camera_speed
        if keys[pygame.K_s]:
            self.camera.y += camera_speed

        """ Prevent camera from going outside game area """
        self.camera.x = max(0, min(self.camera.x, self.surface.get_width() - self.camera.width))  # CAMERA BOUNDARY X
        self.camera.y = max(0, min(self.camera.y, self.surface.get_height() - self.camera.height))  # CAMERA BOUNDARY Y
        

    def render(self):
        """Renders dungeon rooms and blocks onto the display."""
        self.display.fill((0, 0, 0))
        self.surface.fill((30, 30, 30))
        for room in self.dungeon.rooms:
            for block in room.blocks:
                pygame.draw.rect(self.surface, room.color, 
                                 (block.position.x * TILESIZE, block.position.y * TILESIZE, TILESIZE, TILESIZE))
        
        for (x, y) in self.dungeon.corridor_positions_mst:
            pygame.draw.rect(self.surface, (255, 255, 255), (x * TILESIZE, y * TILESIZE, TILESIZE, TILESIZE))
        #self.display.blit(self.surface, (0, 0), self.camera)  # DRAW ONLY CAMERA'S VIEW OF GAME AREA

        self.draw_walls(self.surface)

        self.character.draw(self.surface)

        """Renders grid over display."""        
        if self.show_grid:
            for x in range(0, MAP_WIDTH, TILESIZE):
                pygame.draw.line(self.surface, (60, 60, 60), (x, 0), (x, MAP_HEIGHT))
            for y in range(0, MAP_HEIGHT, TILESIZE):
                pygame.draw.line(self.surface, (60, 60, 60), (0, y), (MAP_WIDTH, y))

        
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
        
        if self.show_all_paths:
            points = self.dungeon.room_start_points
            for i in range(len(points)):
                for j in range(i + 1, len(points)):
                    pygame.draw.line(
                        self.surface, (255, 255, 0),
                        (points[i][0] * TILESIZE, points[i][1] * TILESIZE),
                        (points[j][0] * TILESIZE, points[j][1] * TILESIZE), 2)
                   
        
        #if self.show_paths:
        #    for path in self.dungeon.paths:
        #        start = (path[0][0] * TILESIZE, path[0][1] * TILESIZE)
        #        end = (path[1][0] * TILESIZE, path[1][1] * TILESIZE)
        #        pygame.draw.line(self.surface, (255, 0, 0), start, end, 2)

        """

        room_points = [(p[0] * TILESIZE, p[1] * TILESIZE) for p in self.dungeon.room_start_points]

        if self.path_display_mode == 1:
            # Näytä Delaunay-triangulaatio
            edges = calculate_paths(room_points)
            for p1, p2 in edges:
                pygame.draw.line(self.surface, (0, 255, 255), (p1.x, p1.y), (p2.x, p2.y), 2)

        elif self.path_display_mode == 2:
            # Näytä MST
            edges = calculate_paths(room_points)
            points = [Point(x, y) for x, y in room_points]
            mst = prim_mst(points, edges)
            for p1, p2 in mst:
                pygame.draw.line(self.surface, (255, 0, 255), (p1.x, p1.y), (p2.x, p2.y), 2)

        """

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
        
        #for path in self.dungeon.paths:
        #    occupied |= set(path)  

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        for x, y in occupied:
            for dx, dy in directions:
                neighbor = (x + dx, y + dy)
                if neighbor not in occupied:
                    self.walls.add(neighbor)

    def draw_walls(self, surface):
        for x, y in self.walls:
            pygame.draw.rect(surface, (100, 100, 100), (x * TILESIZE, y * TILESIZE, TILESIZE, TILESIZE))