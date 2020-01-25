def move_legal_pawn(initial_x, initial_y, final_x, final_y, color):
    """Decide wetter the move is legal or not."""
    if color == 'white':
        if final_y == 1:
            return False

        elif initial_x == final_x and final_y - initial_y == 1:
            abscisse = final_x
            ordonnee = final_y

            return abscisse, ordonnee

        elif initial_x == final_x and initial_y == 2 and final_y - initial_y == 2:
            abscisse = final_x
            ordonnee = final_y

            return abscisse, ordonnee

        else:
            return False

    if color == 'black':
        if final_y == 8:
            return False

        elif initial_x == final_x and initial_y - final_y == 1:
            abscisse = final_x
            ordonnee = final_y

            return abscisse, ordonnee

        elif initial_x == final_x and initial_y == 7 and initial_y - final_y == 2:
            abscisse = final_x
            ordonnee = final_y

            return abscisse, ordonnee

        else:
            return False


def move_legal_knight(initial_x, initial_y, final_x, final_y):
    """Decide wetter the move is legal or not."""
    if abs(initial_x - final_x) == 2 and abs(initial_y - final_y) == 1:
        abscisse = final_x
        ordonnee = final_y

        return abscisse, ordonnee

    elif abs(initial_y - final_y) == 2 and abs(initial_x - final_x) == 1:
        abscisse = final_x
        ordonnee = final_y

        return abscisse, ordonnee

    else:
        return False


def move_legal_bishop(initial_x, initial_y, final_x, final_y):
    """Decide wetter the move is legal or not."""
    if initial_x == final_x and initial_y == final_y:
        return False

    elif initial_x + initial_y == final_x + final_y:
        abscisse = final_x
        ordonnee = final_y

        return abscisse, ordonnee

    elif initial_x - initial_y == final_x - final_y:
        abscisse = final_x
        ordonnee = final_y

        return abscisse, ordonnee

    else:
        return False


def move_legal_rook(initial_x, initial_y, final_x, final_y):
    """Decide wetter the move is legal or not."""
    if initial_x == final_x:
        abscisse = final_x
        ordonnee = final_y

        return abscisse, ordonnee

    elif initial_y == final_y:
        abscisse = final_x
        ordonnee = final_y

        return abscisse, ordonnee

    else:
        return False


def move_legal_queen(initial_x, initial_y, final_x, final_y):
    """Decide wetter the move is legal or not."""
    if initial_x + initial_y == final_x + final_y:
        abscisse = final_x
        ordonnee = final_y

        return abscisse, ordonnee

    elif initial_x - initial_y == final_x - final_y:
        abscisse = final_x
        ordonnee = final_y

        return abscisse, ordonnee

    elif initial_x == final_x:
        abscisse = final_x
        ordonnee = final_y

        return abscisse, ordonnee

    elif initial_y == final_y:
        abscisse = final_x
        ordonnee = final_y

        return abscisse, ordonnee
    else:
        return False


def move_legal_king(initial_x, initial_y, final_x, final_y):
    """Decide wetter the move is legal or not."""
    if abs(initial_x - final_x) == 1 and abs(initial_y - final_y) == 1:
        abscisse = final_x
        ordonnee = final_y

        return abscisse, ordonnee

    elif abs(initial_x - final_x) == 1 and initial_y == final_y:
        abscisse = final_x
        ordonnee = final_y

        return abscisse, ordonnee

    elif abs(initial_y - final_y) == 1 and initial_x == final_x:
        abscisse = final_x
        ordonnee = final_y

        return abscisse, ordonnee

    else:
        return False
