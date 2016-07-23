import sys
import pygame
from setting import Setting
from fighter import Fighter
from alien import Alien
import game_function as gf
from pygame.sprite import Group
from game_stats import GamesStats
from button import Button

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

    # Create play button
    play_button = Button(f_settings, screen, "Play")

    # Create an instance to store game stats
    stats = GamesStats(f_settings)

    # Create the fleet of aliens
    gf.create_fleet(f_settings, screen, aliens, fighter)

    # Start the main loop for the game.
    while True:
        gf.check_events(f_settings, screen, aliens, fighter, bullets, play_button, stats)
        if stats.game_active:
            fighter.position()
            gf.update_bullets(f_settings, screen, fighter, bullets, aliens)
            gf.update_aliens(f_settings, screen, aliens, fighter, bullets, stats)
        gf.screen_update(f_settings, screen, fighter, bullets, aliens, stats, play_button)

run_game()