# First need to create an empty Pygame window. Starting with the basic structure:

import sys
import pygame
import game_functions as gf
from snail import Snail
from settings import Settings
from pygame.sprite import Group
from mushroom import Mushroom

def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # Make a snail.
    snail = Snail(settings, screen)
    # make a group to store bullets in.
    bullets = Group()
    # Make a mushroom group.
    mushrooms = Group()

    # Create grouping of mushrooms.
    gf.create_fleet(settings, screen, snail, mushrooms)

    # Start the main loop for the game.
    while True:
        gf.check_events(settings, screen, snail, bullets)
        snail.update()
        gf.update_bullets(bullets)
        gf.update_screen(settings, screen, snail, mushrooms, bullets)

run_game()