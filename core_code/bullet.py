import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class to manage bullet"""
    def __init__(self, f_settings, screen, fighter):
        """Create a bullet object position"""
        super(Bullet, self).__init__()
        self.screen = screen

        """Create a bullet rect at (0, 0) and then set correct position"""
        self.rect = pygame.Rect(0, 0, f_settings.bullet_width, f_settings.bullet_height)
        self.rect.centerx = fighter.rect.centerx
        self.rect.top = fighter.rect.top

        """Store the bullet postion as a decimal value"""
        self.y = float(self.rect.y)

        """ Bullet's factor"""

        self.color = f_settings.bullet_color
        self.speed = f_settings.bullet_speed

    def update(self):
        """Update the bullet's position"""
        self.y -= self.speed

        """Update the rect position"""
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)