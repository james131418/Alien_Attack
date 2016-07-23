import pygame.font

class Button():
    def __init__(self, f_settings, screen, msg):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Design button attributes
        self.width, self.height = 200, 60
        self.button_color = (0, 0, 128)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont("comicsansms", 48)

        # Build the button rect
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # The button message needs to be prepped only once
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """Turn msg into an image and center text on the button"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.screen_rect.center

    def draw_button(self):
        """Draw button and msg"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

