class Settings():
    """A class to store all the settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Parametres de l'écran
        self.screen_width = 960
        self.screen_height = 600
        self.bg_color = (50, 50, 50)

        # Parametres des cases
        self.case_width = 60
        self.case_height = 60

        self.case_dark_color = (200, 150, 100)
        self.case_bright_color = (247, 238, 203)

        # Parametres des buttons
        self.button_width = 100
        self.button_height = 55
        self.button_color = (70, 70, 70)
        self.space_between = 15
