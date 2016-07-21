import sys
import pygame
from setting import Setting
from fighter import Fighter
from alien import Alien
import game_function as gf
from pygame.sprite import Group

def run_game():
    # initialize game and create a screen object
    pygame.init()
    f_settings = Setting()
    screen = pygame.display.set_mode((f_settings.screen_width, f_settings.screen_height))
    pygame.display.set_caption("Alien Attack!")
    # Make a fighter, a group of bullets and a group of aliens
    fighter = Fighter(f_settings, screen)
    aliens = Group()
    bullets = Group()

    # Create the fleet of aliens
    gf.create_fleet(f_settings, screen, aliens, fighter)

    # Start the main loop for the game.
    while True:
        gf.check_events(f_settings, screen, fighter, bullets)
        fighter.position()
        gf.update_bullets(bullets)
        gf.update_aliens(f_settings, aliens)
        gf.screen_update(f_settings, screen, fighter, bullets, aliens)

run_game()