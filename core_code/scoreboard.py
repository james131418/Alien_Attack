import pygame.font
from pygame.sprite import Group
from fighter import Fighter

class Scoreboard():
    """A class to display score"""
    def __init__(self, f_settings, screen, stats, fighter):
        """Initialize scorekeeping attributes"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.f_settings = f_settings
        self.stats = stats
        self.fighter = fighter

        #Font settings for score image
        self.text_color = (40, 40, 40)
        self.font = pygame.font.SysFont(None, 48)

        #Prepare the initial score image
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_fighters()

    def prep_score(self):
        """Turn score into an image and place score on the up-right corner"""
        rounded_score = int(round(self.stats.score, -1))
        str_score = "{:,}".format(rounded_score)
        self.score_image = self.font.render(str_score, True, self.text_color, self.f_settings.screen_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 100
        self.score_rect.top = 5

    def prep_high_score(self):
        """Turn high score into an image and place score on the up-right corner next to score"""
        rounded_score = int(round(self.stats.high_score, -1))
        str_score = "{:,}".format(rounded_score)
        self.high_score_image = self.font.render(str_score, True, self.text_color, self.f_settings.screen_color)
        self.high_score_rect = self.score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = 5

    def prep_level(self):
        """Turn level into an image and place score on the up_right corner"""
        self.level_image = self.font.render(str(self.stats.level), True, self.text_color, self.f_settings.screen_color)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.screen_rect.right - 25
        self.level_rect.top = 5

    def prep_fighters(self):
        self.fighters = Group()
        """Show how many fighters left"""
        for fighter_number in range(self.stats.fighter_left):
            prep_fighter = Fighter(self.f_settings, self.screen)
            prep_fighter.rect.x = 15 + fighter_number * prep_fighter.rect.width
            prep_fighter.rect.y = 5
            self.fighters.add(prep_fighter)


    def draw_score(self):
        """Draw score to the screen"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        # Draw fighters
        self.fighters.draw(self.screen)