class GamesStats():
    """Track statistics for Aliens Attack!"""

    def __init__(self, f_settings):
        self.f_settings = f_settings
        self.reset_stats()
        self.high_score = 0
        # Start Alien_Attack in an inactive state
        self.game_active = False
    def reset_stats(self):
        """Initialize the stats that can change during the game"""
        self.fighter_left = self.f_settings.fighter_limit
        self.score = 0
        self.level = 1
