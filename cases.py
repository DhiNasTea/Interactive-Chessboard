import pygame
from create_squares import create_squares


class Cases():
    """Une classe représentant les cases"""

    def __init__(self, settings, screen):
        """Créer une case à un endroit donné."""
        self.screen = screen

        # Create 64 squares for the chessboard
        self.squares = create_squares()

        self.squares_rect = []

        for square in self.squares:
            # Create the squares and positioning them depending on the value of their coordinates.
            #  We want them to be one next to each other
            square_x = settings.screen_width / 16 + (square['abscisse'] - 1) * settings.case_width
            square_y = settings.screen_height / 10 + (square['ordonnée'] - 1) * settings.case_height

            square['rect'] = pygame.Rect(square_x, square_y, settings.case_width,
                                         settings.case_height)

            if square['color'] == 'black':
                square['color'] = settings.case_dark_color
            else:
                square['color'] = settings.case_bright_color

            self.squares_rect.append(square)

    def draw_squares(self):
        """Draw each square in the screen."""
        for square in self.squares_rect:
            pygame.draw.rect(self.screen, square['color'], square['rect'])







