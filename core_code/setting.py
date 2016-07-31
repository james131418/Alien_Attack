class Setting():
    """A class to store all settings"""
    def __init__(self):
        """initialize the game's setting"""
        # screen setting
        self.screen_width = 1200
        self.screen_height = 768
        self.screen_color = (230, 230, 230)

        # fighter's setting
        self.speed = 6
        self.fighter_limit = 3

        # bullets setting
        self.bullet_speed = 10
        self.bullet_height = 16
        self.bullet_width = 300
        self.bullet_color = (50, 50, 50)
        self.bullet_allowed = 3

        # aliens setting
        self.alien_speed = 3
        self.fleet_drop_speed = 12
        # fleet_direction of -1 represents left, 1 represent right
        self.fleet_direction = 1

        # How quick the game speed up
        self.speedup_scale = 1.2
        self.initialize_dynamic_setting()
        # How quickly the score value increases
        self.score_scale = 1.5

    def initialize_dynamic_setting(self):
        # fighter's setting
        self.speed = 6
        # bullets setting
        self.bullet_speed = 10
        # aliens setting
        self.alien_speed = 3
        # fleet_direction of -1 represents left, 1 represent right
        self.fleet_direction = 1
        # Scoring
        self.alien_point = 50


    def increase_speed(self):
        """Increases game speed"""
        self.speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

    def increase_score_value(self):
        """Increase score of hitting aliens"""
        self.alien_point = int(self.alien_point * self.score_scale)








