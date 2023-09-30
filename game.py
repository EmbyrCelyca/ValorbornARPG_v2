
from typing import Self
import pygame
import sys
from player import Player
from enemy_spawner import EnemySpawner
from world_gen import WorldGen

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Valorborn')

# Initialize game objects
player = Player(0, 0)
enemy_spawner = EnemySpawner()
world_gen = WorldGen()

# Main game loop
left_mouse_button_down = False  # To track the state of the LMB

while True:
    left_mouse_button_down = pygame.mouse.get_pressed()[0]  # [0] is the left mouse button

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Handle Player Movement
    if left_mouse_button_down:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        screen_center_x = screen.get_width() // 2
        screen_center_y = screen.get_height() // 2

        # Update player's world coordinates based on move_speed
        dx = -(mouse_x - screen_center_x) // 10
        dy = -(mouse_y - screen_center_y) // 10
        player.x += dx * player.attributes.get_attribute("move_speed") / 10
        player.y += dy * player.attributes.get_attribute("move_speed") / 10

    print(f"Player x: {player.x}, Player y: {player.y}")  # Debugging line

    # Handle skills
    keys = pygame.key.get_pressed()
    mouse_x, mouse_y = pygame.mouse.get_pos()
    screen_center_x = screen.get_width() // 2
    screen_center_y = screen.get_height() // 2
    player.skill_handler.handle_input(keys, screen, (mouse_x, mouse_y), (screen_center_x, screen_center_y))

    # Update game objects
    player.update()
    enemy_spawner.update()
    world_gen.update(player.x, player.y)
    
    # Update skills
    player.skill_handler.update_skills()

    # Draw game objects
    screen.fill((0, 0, 0))  # Fill screen with black
    player.draw(screen)
    enemy_spawner.draw(screen)
    world_gen.draw(screen)

    pygame.display.update()
