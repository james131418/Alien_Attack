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

        #