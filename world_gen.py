import pygame

class WorldGen:
    def __init__(self):
        self.grid_size = 50  # Size of each grid cell
        self.world_offset_x = 0  # World offset for x-axis
        self.world_offset_y = 0  # World offset for y-axis

    def update(self, player_x, player_y):
        self.world_offset_x = -player_x  # Update world offset based on player position
        self.world_offset_y = -player_y
        print(f"Updated WorldGen offsets: x = {self.world_offset_x}, y = {self.world_offset_y}")  # Debugging line

    def draw(self, screen):
        screen_center_x = screen.get_width() // 2
        screen_center_y = screen.get_height() // 2

        # Calculate the range for drawing grid lines based on player's position
        start_x = int(self.world_offset_x - screen.get_width() // 2)
        end_x = int(self.world_offset_x + screen.get_width() // 2)
        start_y = int(self.world_offset_y - screen.get_height() // 2)
        end_y = int(self.world_offset_y + screen.get_height() // 2)

        # Calculate the first grid line to draw
        first_line_x = start_x - (start_x % self.grid_size)
        first_line_y = start_y - (start_y % self.grid_size)

        for x in range(first_line_x, end_x, self.grid_size):
            pygame.draw.line(screen, (255, 255, 255), (x - self.world_offset_x + screen_center_x, 0), (x - self.world_offset_x + screen_center_x, screen.get_height()))
        for y in range(first_line_y, end_y, self.grid_size):
            pygame.draw.line(screen, (255, 255, 255), (0, y - self.world_offset_y + screen_center_y), (screen.get_width(), y - self.world_offset_y + screen_center_y))
