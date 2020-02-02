import pygame
import sys

show = False
piece = None

def check_button_click(buttons):
    """Check the mouse clicks and react appropriately."""
    global piece
    global show
    import chess as c
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            # Check if a button is clicked
            for button in buttons:
                if button.rect.collidepoint(mouse_x, mouse_y):
                    if button.text == 'bishop':
                        piece = c.bishop
                        show = True
                    elif button.text == 'knight':
                        piece = c.knight
                        show = True
                    elif button.text == 'rook':
                        piece = c.rook
                        show = True
                    elif button.text == 'queen':
                        piece = c.queen
                        show = True
                    elif button.text == 'king':
                        piece = c.king
                        show = True
                    elif button.text == 'w_pawn':
                        piece = c.w_pawn
                        show = True
                    elif button.text == 'b_pawn':
                        piece = c.b_pawn
                        show = True
                    else:
                        pass
            if piece:
                event_pos = mouse_x, mouse_y
                piece.update_click(event_pos)

        elif event.type == pygame.MOUSEMOTION:
            if piece:
                piece.update_motion(event.pos)

        elif event.type == pygame.MOUSEBUTTONUP:
            if piece:
                piece.update_release(event.pos)
        elif event.type == pygame.QUIT:
            sys.exit()

    if piece:
        piece.show()
















