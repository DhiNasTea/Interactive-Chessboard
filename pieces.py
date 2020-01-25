import pygame
import mouse_coordinates as mc
import verify_move as vm
import sys


def get_pixel_position(abscisse, ordonnee):
    """Translate the coordinates in pixels"""
    x_pixels = 60 + (abscisse - 1) * 60 + 30
    y_pixels = 60 + (-ordonnee + 8) * 60 + 30
    pixels = (x_pixels, y_pixels)

    return pixels


class Bishop():
    """A representation of a bishop"""
    def __init__(self, screen, color, abscisse, ordonnee):
        self.abscisse = abscisse
        self.ordonnee = ordonnee
        self.color = color
        self.following_mouse = False
        self.screen = screen

        """Show a bishop at the screen."""

        # Load the bishop and get its rectangle.
        if self.color == 'black':
            self.image = pygame.image.load('images_2/fou_noir.png').convert_alpha()
        else:
            self.image = pygame.image.load('images_2/fou_blanc.png').convert_alpha()
        self.rect_piece = self.image.get_rect()

        position = get_pixel_position(self.abscisse, self.ordonnee)
        self.rect_piece.centerx, self.rect_piece.centery = position

        self.xcenter = float(self.rect_piece.centerx)
        self.ycenter = float(self.rect_piece.centery)
        self.rectangle_draging = False

        self.xbefore = float(self.rect_piece.centerx)
        self.ybefore = float(self.rect_piece.centery)
        self.mouse_touch_piece = False

    def show(self):
        """Show a bishop at the screen."""
        self.screen.blit(self.image, self.rect_piece)

    def update_click(self, event_pos):
        """"""
        global offset_x, offset_y
        global initial_x, initial_y
        global final_x, final_y
        if self.rect_piece.collidepoint(event_pos):
            self.mouse_touch_piece = True
            self.rectangle_draging = True
            mouse_x, mouse_y = event_pos
            offset_x = self.xcenter - mouse_x
            offset_y = self.ycenter - mouse_y
            initial_pos = mc.mouse_coordinates_click(mouse_x, mouse_y)
            if initial_pos:
                initial_x, initial_y = initial_pos
            self.rect_piece.centerx = self.xcenter
            self.rect_piece.centery = self.ycenter

    def update_release(self, event_pos):
        """"""
        global offset_x, offset_y
        global initial_x, initial_y
        global final_x, final_y
        if self.mouse_touch_piece:
            mouse_x, mouse_y = event_pos
            self.rectangle_draging = False
            final_pos = mc.mouse_coordinates_release(mouse_x, mouse_y)
            if final_pos:
                final_x, final_y = final_pos
                position = vm.move_legal_bishop(initial_x, initial_y, final_x, final_y)

                if position:
                    x, y = position
                    pixels = get_pixel_position(x, y)
                    self.xcenter, self.ycenter = pixels
                    self.xbefore, self.ybefore = self.xcenter, self.ycenter
                else:
                    self.xcenter, self.ycenter = self.xbefore, self.ybefore
            else:
                self.xcenter, self.ycenter = self.xbefore, self.ybefore
        self.mouse_touch_piece = False
        self.rect_piece.centerx = self.xcenter
        self.rect_piece.centery = self.ycenter

    def update_motion(self, event_pos):
        """"""
        global offset_x, offset_y
        global initial_x, initial_y
        global final_x, final_y
        if self.rectangle_draging:
            mouse_x, mouse_y = event_pos
            self.xcenter = mouse_x + offset_x
            self.ycenter = mouse_y + offset_y

        self.rect_piece.centerx = self.xcenter
        self.rect_piece.centery = self.ycenter


class Pawn():
    """A representation of a pawn"""

    def __init__(self, screen, color, abscisse, ordonnee):
        self.abscisse = abscisse
        self.ordonnee = ordonnee
        self.color = color
        self.following_mouse = False
        self.screen = screen

        """Show a pawn at the screen."""

        # Load the pawn and get its rectangle.
        if self.color == 'black':
            self.image = pygame.image.load('images_2/pion_noir.png').convert_alpha()
        else:
            self.image = pygame.image.load('images_2/pion_blanc.png').convert_alpha()
        self.rect_piece = self.image.get_rect()

        position = get_pixel_position(self.abscisse, self.ordonnee)
        self.rect_piece.centerx, self.rect_piece.centery = position

        self.xcenter = float(self.rect_piece.centerx)
        self.ycenter = float(self.rect_piece.centery)
        self.rectangle_draging = False

        self.xbefore = float(self.rect_piece.centerx)
        self.ybefore = float(self.rect_piece.centery)
        self.mouse_touch_piece = False

    def show(self):
        """Show a pawn at the screen."""
        self.screen.blit(self.image, self.rect_piece)

    def update_click(self, event_pos):
        """"""
        global offset_x, offset_y
        global initial_x, initial_y
        global final_x, final_y
        if self.rect_piece.collidepoint(event_pos):
            self.mouse_touch_piece = True
            self.rectangle_draging = True
            mouse_x, mouse_y = event_pos
            offset_x = self.xcenter - mouse_x
            offset_y = self.ycenter - mouse_y
            initial_pos = mc.mouse_coordinates_click(mouse_x, mouse_y)
            if initial_pos:
                initial_x, initial_y = initial_pos
            self.rect_piece.centerx = self.xcenter
            self.rect_piece.centery = self.ycenter

    def update_release(self, event_pos):
        """"""
        global offset_x, offset_y
        global initial_x, initial_y
        global final_x, final_y
        if self.mouse_touch_piece:
            mouse_x, mouse_y = event_pos
            self.rectangle_draging = False
            final_pos = mc.mouse_coordinates_release(mouse_x, mouse_y)
            if final_pos:
                final_x, final_y = final_pos
                position = vm.move_legal_pawn(initial_x, initial_y, final_x, final_y, self.color)

                if position:
                    x, y = position
                    pixels = get_pixel_position(x, y)
                    self.xcenter, self.ycenter = pixels
                    self.xbefore, self.ybefore = self.xcenter, self.ycenter
                else:
                    self.xcenter, self.ycenter = self.xbefore, self.ybefore
            else:
                self.xcenter, self.ycenter = self.xbefore, self.ybefore
        self.mouse_touch_piece = False
        self.rect_piece.centerx = self.xcenter
        self.rect_piece.centery = self.ycenter

    def update_motion(self, event_pos):
        """"""
        global offset_x, offset_y
        global initial_x, initial_y
        global final_x, final_y
        if self.rectangle_draging:
            mouse_x, mouse_y = event_pos
            self.xcenter = mouse_x + offset_x
            self.ycenter = mouse_y + offset_y

        self.rect_piece.centerx = self.xcenter
        self.rect_piece.centery = self.ycenter


class Knight():
    """A representation of a knight"""
    def __init__(self, screen, color, abscisse, ordonnee):
        self.abscisse = abscisse
        self.ordonnee = ordonnee
        self.color = color
        self.following_mouse = False
        self.screen = screen

        """Show a knight at the screen."""

        # Load the knight and get its rectangle.
        if self.color == 'black':
            self.image = pygame.image.load('images_2/cavalier_noir.png').convert_alpha()
        else:
            self.image = pygame.image.load('images_2/cavalier_blanc.png').convert_alpha()
        self.rect_piece = self.image.get_rect()

        position = get_pixel_position(self.abscisse, self.ordonnee)
        self.rect_piece.centerx, self.rect_piece.centery = position

        self.xcenter = float(self.rect_piece.centerx)
        self.ycenter = float(self.rect_piece.centery)
        self.rectangle_draging = False

        self.xbefore = float(self.rect_piece.centerx)
        self.ybefore = float(self.rect_piece.centery)
        self.mouse_touch_piece = False

    def show(self):
        """Show a knight at the screen."""
        self.screen.blit(self.image, self.rect_piece)

    def update_click(self, event_pos):
        """"""
        global offset_x, offset_y
        global initial_x, initial_y
        global final_x, final_y
        if self.rect_piece.collidepoint(event_pos):
            self.mouse_touch_piece = True
            self.rectangle_draging = True
            mouse_x, mouse_y = event_pos
            offset_x = self.xcenter - mouse_x
            offset_y = self.ycenter - mouse_y
            initial_pos = mc.mouse_coordinates_click(mouse_x, mouse_y)
            if initial_pos:
                initial_x, initial_y = initial_pos
            self.rect_piece.centerx = self.xcenter
            self.rect_piece.centery = self.ycenter

    def update_release(self, event_pos):
        """"""
        global offset_x, offset_y
        global initial_x, initial_y
        global final_x, final_y
        if self.mouse_touch_piece:
            mouse_x, mouse_y = event_pos
            self.rectangle_draging = False
            final_pos = mc.mouse_coordinates_release(mouse_x, mouse_y)
            if final_pos:
                final_x, final_y = final_pos
                position = vm.move_legal_knight(initial_x, initial_y, final_x, final_y)

                if position:
                    x, y = position
                    pixels = get_pixel_position(x, y)
                    self.xcenter, self.ycenter = pixels
                    self.xbefore, self.ybefore = self.xcenter, self.ycenter
                else:
                    self.xcenter, self.ycenter = self.xbefore, self.ybefore
            else:
                self.xcenter, self.ycenter = self.xbefore, self.ybefore
        self.mouse_touch_piece = False
        self.rect_piece.centerx = self.xcenter
        self.rect_piece.centery = self.ycenter

    def update_motion(self, event_pos):
        """"""
        global offset_x, offset_y
        global initial_x, initial_y
        global final_x, final_y
        if self.rectangle_draging:
            mouse_x, mouse_y = event_pos
            self.xcenter = mouse_x + offset_x
            self.ycenter = mouse_y + offset_y

        self.rect_piece.centerx = self.xcenter
        self.rect_piece.centery = self.ycenter


class Rook():
    """A representation of a rook"""
    def __init__(self, screen, color, abscisse, ordonnee):
        self.abscisse = abscisse
        self.ordonnee = ordonnee
        self.color = color
        self.following_mouse = False
        self.screen = screen

        """Show a rook at the screen."""

        # Load the knight and get its rectangle.
        if self.color == 'black':
            self.image = pygame.image.load('images_2/tour_noire.png').convert_alpha()
        else:
            self.image = pygame.image.load('images_2/tour_blanche.png').convert_alpha()
        self.rect_piece = self.image.get_rect()

        position = get_pixel_position(self.abscisse, self.ordonnee)
        self.rect_piece.centerx, self.rect_piece.centery = position

        self.xcenter = float(self.rect_piece.centerx)
        self.ycenter = float(self.rect_piece.centery)
        self.rectangle_draging = False

        self.xbefore = float(self.rect_piece.centerx)
        self.ybefore = float(self.rect_piece.centery)
        self.mouse_touch_piece = False

    def show(self):
        """Show a rook at the screen."""
        self.screen.blit(self.image, self.rect_piece)

    def update_click(self, event_pos):
        """"""
        global offset_x, offset_y
        global initial_x, initial_y
        global final_x, final_y
        if self.rect_piece.collidepoint(event_pos):
            self.mouse_touch_piece = True
            self.rectangle_draging = True
            mouse_x, mouse_y = event_pos
            offset_x = self.xcenter - mouse_x
            offset_y = self.ycenter - mouse_y
            initial_pos = mc.mouse_coordinates_click(mouse_x, mouse_y)
            if initial_pos:
                initial_x, initial_y = initial_pos
            self.rect_piece.centerx = self.xcenter
            self.rect_piece.centery = self.ycenter

    def update_release(self, event_pos):
        """"""
        global offset_x, offset_y
        global initial_x, initial_y
        global final_x, final_y
        if self.mouse_touch_piece:
            mouse_x, mouse_y = event_pos
            self.rectangle_draging = False
            final_pos = mc.mouse_coordinates_release(mouse_x, mouse_y)
            if final_pos:
                final_x, final_y = final_pos
                position = vm.move_legal_rook(initial_x, initial_y, final_x, final_y)

                if position:
                    x, y = position
                    pixels = get_pixel_position(x, y)
                    self.xcenter, self.ycenter = pixels
                    self.xbefore, self.ybefore = self.xcenter, self.ycenter
                else:
                    self.xcenter, self.ycenter = self.xbefore, self.ybefore
            else:
                self.xcenter, self.ycenter = self.xbefore, self.ybefore
        self.mouse_touch_piece = False
        self.rect_piece.centerx = self.xcenter
        self.rect_piece.centery = self.ycenter

    def update_motion(self, event_pos):
        """"""
        global offset_x, offset_y
        global initial_x, initial_y
        global final_x, final_y
        if self.rectangle_draging:
            mouse_x, mouse_y = event_pos
            self.xcenter = mouse_x + offset_x
            self.ycenter = mouse_y + offset_y

        self.rect_piece.centerx = self.xcenter
        self.rect_piece.centery = self.ycenter


class Queen():
    """A representation of a queen."""

    def __init__(self, screen, color, abscisse, ordonnee):
        self.abscisse = abscisse
        self.ordonnee = ordonnee
        self.color = color
        self.following_mouse = False
        self.screen = screen

        """Show a queen at the screen."""

        # Load the queen and get its rectangle.
        if self.color == 'black':
            self.image = pygame.image.load('images_2/reine_noire.png').convert_alpha()
        else:
            self.image = pygame.image.load('images_2/reine_blanche.png').convert_alpha()
        self.rect_piece = self.image.get_rect()

        position = get_pixel_position(self.abscisse, self.ordonnee)
        self.rect_piece.centerx, self.rect_piece.centery = position

        self.xcenter = float(self.rect_piece.centerx)
        self.ycenter = float(self.rect_piece.centery)
        self.rectangle_draging = False

        self.xbefore = float(self.rect_piece.centerx)
        self.ybefore = float(self.rect_piece.centery)
        self.mouse_touch_piece = False

    def show(self):
        """Show a queen at the screen."""
        self.screen.blit(self.image, self.rect_piece)

    def update_click(self, event_pos):
        """"""
        global offset_x, offset_y
        global initial_x, initial_y
        global final_x, final_y
        if self.rect_piece.collidepoint(event_pos):
            self.mouse_touch_piece = True
            self.rectangle_draging = True
            mouse_x, mouse_y = event_pos
            offset_x = self.xcenter - mouse_x
            offset_y = self.ycenter - mouse_y
            initial_pos = mc.mouse_coordinates_click(mouse_x, mouse_y)
            if initial_pos:
                initial_x, initial_y = initial_pos
            self.rect_piece.centerx = self.xcenter
            self.rect_piece.centery = self.ycenter

    def update_release(self, event_pos):
        """"""
        global offset_x, offset_y
        global initial_x, initial_y
        global final_x, final_y
        if self.mouse_touch_piece:
            mouse_x, mouse_y = event_pos
            self.rectangle_draging = False
            final_pos = mc.mouse_coordinates_release(mouse_x, mouse_y)
            if final_pos:
                final_x, final_y = final_pos
                position = vm.move_legal_queen(initial_x, initial_y, final_x, final_y)

                if position:
                    x, y = position
                    pixels = get_pixel_position(x, y)
                    self.xcenter, self.ycenter = pixels
                    self.xbefore, self.ybefore = self.xcenter, self.ycenter
                else:
                    self.xcenter, self.ycenter = self.xbefore, self.ybefore
            else:
                self.xcenter, self.ycenter = self.xbefore, self.ybefore
        self.mouse_touch_piece = False
        self.rect_piece.centerx = self.xcenter
        self.rect_piece.centery = self.ycenter

    def update_motion(self, event_pos):
        """"""
        global offset_x, offset_y
        global initial_x, initial_y
        global final_x, final_y
        if self.rectangle_draging:
            mouse_x, mouse_y = event_pos
            self.xcenter = mouse_x + offset_x
            self.ycenter = mouse_y + offset_y

        self.rect_piece.centerx = self.xcenter
        self.rect_piece.centery = self.ycenter


class King():
    """A representation of a king"""

    def __init__(self, screen, color, abscisse, ordonnee):
        self.abscisse = abscisse
        self.ordonnee = ordonnee
        self.color = color
        self.following_mouse = False
        self.screen = screen

        """Show a king at the screen."""

        # Load the king and get its rectangle.
        if self.color == 'black':
            self.image = pygame.image.load('images_2/roi_noir.png').convert_alpha()
        else:
            self.image = pygame.image.load('images_2/roi_blanc.png').convert_alpha()
        self.rect_piece = self.image.get_rect()

        position = get_pixel_position(self.abscisse, self.ordonnee)
        self.rect_piece.centerx, self.rect_piece.centery = position

        self.xcenter = float(self.rect_piece.centerx)
        self.ycenter = float(self.rect_piece.centery)
        self.rectangle_draging = False

        self.xbefore = float(self.rect_piece.centerx)
        self.ybefore = float(self.rect_piece.centery)
        self.mouse_touch_piece = False

    def show(self):
        """Show a king at the screen."""
        self.screen.blit(self.image, self.rect_piece)

    def update_click(self, event_pos):
        """"""
        global offset_x, offset_y
        global initial_x, initial_y
        global final_x, final_y
        if self.rect_piece.collidepoint(event_pos):
            self.mouse_touch_piece = True
            self.rectangle_draging = True
            mouse_x, mouse_y = event_pos
            offset_x = self.xcenter - mouse_x
            offset_y = self.ycenter - mouse_y
            initial_pos = mc.mouse_coordinates_click(mouse_x, mouse_y)
            if initial_pos:
                initial_x, initial_y = initial_pos
            self.rect_piece.centerx = self.xcenter
            self.rect_piece.centery = self.ycenter

    def update_release(self, event_pos):
        """"""
        global offset_x, offset_y
        global initial_x, initial_y
        global final_x, final_y
        if self.mouse_touch_piece:
            mouse_x, mouse_y = event_pos
            self.rectangle_draging = False
            final_pos = mc.mouse_coordinates_release(mouse_x, mouse_y)
            if final_pos:
                final_x, final_y = final_pos
                position = vm.move_legal_king(initial_x, initial_y, final_x, final_y)

                if position:
                    x, y = position
                    pixels = get_pixel_position(x, y)
                    self.xcenter, self.ycenter = pixels
                    self.xbefore, self.ybefore = self.xcenter, self.ycenter
                else:
                    self.xcenter, self.ycenter = self.xbefore, self.ybefore
            else:
                self.xcenter, self.ycenter = self.xbefore, self.ybefore
        self.mouse_touch_piece = False
        self.rect_piece.centerx = self.xcenter
        self.rect_piece.centery = self.ycenter

    def update_motion(self, event_pos):
        """"""
        global offset_x, offset_y
        global initial_x, initial_y
        global final_x, final_y
        if self.rectangle_draging:
            mouse_x, mouse_y = event_pos
            self.xcenter = mouse_x + offset_x
            self.ycenter = mouse_y + offset_y

        self.rect_piece.centerx = self.xcenter
        self.rect_piece.centery = self.ycenter



