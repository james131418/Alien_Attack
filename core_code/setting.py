class Setting():
    """A class to store all settings"""
    def __init__(self):
        """initialize the game's setting"""
        # screen setting
        self.screen_width = 1200
        self.screen_height = 768
        self.screen_color = (230, 230, 230)

        # fighter's setting
        self.speed = 3

        # bullets setting
        self.bullet_speed = 10
        self.bullet_height = 16
        self.bullet_width = 3
        self.bullet_color = (50, 50, 50)
        self.bullet_allowed = 3

        # aliens setting
        self.alien_speed = 1
        self.fleet_drop_speed = 12
        # fleet_direction of -1 represents left, 1 represent right
        self.fleet_direction = 1
