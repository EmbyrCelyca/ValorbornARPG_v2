import pygame
import importlib
from attributes import Attributes  # Import the Attributes class
from SkillHandler import SkillHandler

class Player:
    def __init__(self, player_x=0, player_y=0):
        self.x = player_x  # Player's x-coordinate in the world
        self.y = player_y  # Player's y-coordinate in the world
        self.attributes = Attributes()
        self.skills = self.initialize_skills()  # Initialize skills
        self.skill_handler = SkillHandler(self)  # Initialize SkillHandler
        self.hotkeys = {
            pygame.K_SPACE: 'dash',
            # Add more hotkeys here
        }
    def update(self):
        pass
    
    def initialize_skills(self):
        player_skill_names = ['dash']  # This list can be dynamic
        skills = {}
        for skill_name in player_skill_names:
            # Dynamically import the skill class
            SkillClass = importlib.import_module(f"{skill_name}_skill").__dict__[skill_name.capitalize() + "Skill"]
            skills[skill_name] = SkillClass(self)
        return skills

    def draw(self, screen):
        screen_center_x = screen.get_width() // 2
        screen_center_y = screen.get_height() // 2
        pygame.draw.circle(screen, (0, 0, 255), (screen_center_x, screen_center_y), 10)