import pygame
from parametres import Settings
from cases import Cases
from buttons import Button
import game_functionalities as gf
import pieces as p
import rules_display as rd


settings = Settings()
screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))

bishop = p.Bishop(screen, 'black', 4, 4)
queen = p.Queen(screen, 'white', 7, 2)
knight = p.Knight(screen, 'black', 2, 8)
rook = p.Rook(screen, 'white', 7, 8)
king = p.King(screen, 'black', 3, 6)
b_pawn = p.Pawn(screen, 'black', 6, 7)
w_pawn = p.Pawn(screen, 'white', 3, 2)

clock = pygame.time.Clock()

def run_game():
    # Initialize and set up the screen.
    pygame.init()
    pygame.display.set_caption("Échecs")

    cases = Cases(settings, screen)

    bishop_button = Button(screen, "bishop", settings, "Fou", 1)
    knight_button = Button(screen, "knight", settings, "Cavalier", 2)
    king_button = Button(screen, "king", settings, "Roi", 3)
    queen_button = Button(screen, "queen", settings, "Reine", 4)
    rook_button = Button(screen, "rook", settings, "Tour", 5)
    w_pawn_button = Button(screen, "w_pawn", settings, "1er Pion", 6)
    b_pawn_button = Button(screen, "b_pawn", settings, "2e Pion", 7)

    buttons = [bishop_button, knight_button, king_button, queen_button,
               rook_button, w_pawn_button, b_pawn_button]

    # Start main loop.
    while True:
        # Start event loop.

        screen.fill(settings.bg_color)
        cases.draw_squares()
        for button in buttons:
            button.prep_msg()
            button.show_button()
        if p.rule_display:
            rd.show_rule(screen, p.rule_display)
        gf.check_button_click(buttons)

        # Refresh screen.
        pygame.display.flip()


run_game()
