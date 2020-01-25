import pygame
import pygame.font


class Button:
    """A represantation of an interactive button."""
    def __init__(self, screen, text, settings, piece_reference, number):
        self.screen = screen
        self.text = text
        self.settings = settings
        self.piece = piece_reference
        self.number = number
        self.piece_image_rect = None

        # Create a button at a designated place.
        self.rect = pygame.Rect(0, 0, settings.button_width,
                                settings.button_height)
        self.rect.x = 790
        self.rect.y = 60 + self.settings.button_height * (self.number - 1)
        self.rect.y += self.settings.space_between * (self.number - 1)

        # Create the properties
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 30)
        self.prep_msg()

    def prep_msg(self):
        """Turn msg into a rendered image and center tezt on the button."""
        self.piece_image = self.font.render(self.piece, True, self.text_color,
                                            self.settings.button_color)
        self.piece_image_rect = self.piece_image.get_rect()
        self.piece_image_rect.center = self.rect.center

    def show_button(self):
        """Show the button to the screen"""
        self.screen.fill(self.settings.button_color, self.rect)
        self.screen.blit(self.piece_image, self.piece_image_rect)
