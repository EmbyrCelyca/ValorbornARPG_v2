import pygame
from base_skill import Skill  # Import the base Skill class

class DashSkill(Skill):
    def __init__(self, owner, distance=100, cooldown=2.0, stored_uses=2, cast_time=0.2):
        super().__init__(owner)
        self.distance = distance
        self.cooldown = cooldown
        self.stored_uses = stored_uses
        self.cast_time = cast_time
        self.is_dashing = False 
        self.last_dash_time = 0

    def can_use(self):
        return super().can_use() and self.stored_uses > 0

    def use(self, screen, start_pos, end_pos):
        if not self.can_use():
            return

        self.last_used_time = pygame.time.get_ticks() / 1000.0  # Update last used time
        self.last_dash_time = pygame.time.get_ticks() / 1000.0  # Update last dash time
        self.stored_uses -= 1  # Consume a stored use

        # Calculate the direction vector
        dx = end_pos[0] - start_pos[0]
        dy = end_pos[1] - start_pos[1]

        # Normalize the direction vector
        length = (dx ** 2 + dy ** 2) ** 0.5
        if length > 0:
            dx /= length
            dy /= length

        # Calculate the new position
        new_x = start_pos[0] + dx * self.distance
        new_y = start_pos[1] + dy * self.distance
        
        # Indicator line and circle
        pygame.draw.line(screen, (255, 0, 0), start_pos, (new_x, new_y), 2)
        pygame.draw.circle(screen, (0, 0, 255), (new_x, new_y), 10)

        # Update the owner's position (this is just an example; you'll need to integrate this into your actual game logic)
        self.owner.x = new_x
        self.owner.y = new_y

    def update(self):
        current_time = pygame.time.get_ticks() / 1000.0
        time_since_last_dash = current_time - self.last_dash_time

        # Regenerate a stored use if enough time has passed
        if time_since_last_dash >= self.cooldown:
            self.stored_uses = min(self.stored_uses + 1, 3)  # Cap at 3 stored uses
            self.last_dash_time = current_time  # Reset the last dash time