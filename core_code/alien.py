import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent an alien"""
    def __init__(self, f_settings, screen):
        """initialize the Alien and set its start position"""
        super(Alien, self).__init__()
        self.screen = screen
        self.f_settings = f_settings

        # Load the Alien image
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien image at top-left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the decimal value of alien
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw the alien at its position"""
        self.screen.blit(self.image, self.rect)
