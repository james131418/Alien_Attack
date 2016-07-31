import pygame
from pygame.sprite import Sprite

class Fighter(Sprite):
    def __init__(self, f_settings, screen):
        """Initialize the ship and set its starting position."""
        super(Fighter, self).__init__()
        self.screen = screen
        self.f_settings = f_settings

        # load the ship image and get its rect.
        self.image = pygame.image.load('images/fighter.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Store a decimal value for the fighter's center and back-n-forth position
        self.center = float(self.rect.centerx)
        self.up_down = float(self.rect.bottom)
        # Movement flag
        self.move_right = False
        self.move_left = False
        self.move_up = False
        self.move_down = False

    def position(self):
        """Update the fighter's position"""
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.center += self.f_settings.speed
        if self.move_left and self.rect.left > 0:
            self.center -= self.f_settings.speed
        if self.move_up and self.rect.top > 0:
            self.up_down -= self.f_settings.speed
        if self.move_down and self.rect.bottom < self.screen_rect.bottom:
            self.up_down += self.f_settings.speed

        # Update rect object's position
        self.rect.centerx = self.center
        self.rect.bottom = self.up_down

    def center_bottom_fighter(self):
        """Recenter the fighter"""
        self.center = self.screen_rect.centerx
        self.up_down = self.screen_rect.bottom

    def blitme(self):
        """Draw the fighter at its current location"""
        self.screen.blit(self.image, self.rect)