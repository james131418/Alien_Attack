class GamesStats():
    """Track statistics for Aliens Attack!"""

    def __init__(self, f_settings):
        self.f_settings = f_settings
        self.reset_stats()

    def reset_stats(self):
        """Initialize the stats that can change during the game"""
        self.fighter_left = self.f_settings.fighter_limit

