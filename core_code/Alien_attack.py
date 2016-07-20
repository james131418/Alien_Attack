import sys
import pygame
from setting import Setting
from fighter import Fighter
import game_function as gf
from pygame.sprite import Group

def run_game():
    # initialize game and create a screen object
    pygame.init()
    f_settings = Setting()
    screen = pygame.display.set_mode((f_settings.screen_width, f_settings.screen_height))
    pygame.display.set_caption("Alien Attack!")

    # Create a fighter
    fighter = Fighter(f_settings, screen)
    # Make a group to store bullets
    bullets = Group()

    # Start the main loop for the game.
    while True:
        gf.check_events(f_settings, screen, fighter, bullets)
        fighter.position()
        gf.update_bullets(bullets)
        gf.screen_update(f_settings, screen, fighter, bullets)

run_game()