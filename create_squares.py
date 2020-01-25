squares = []

def create_squares():
    """Create the 64 squares of the chessboard."""
    x = 1
    y = 1

    flag = True
    for square in range(64):
        square = {'abscisse': x, 'ordonnée': y, 'color': ''}
        if x == 8:
            x = 0
            y += 1
        elif x == 7 and y == 8:
            x = 8
            y = 8
            flag = False
        if flag:
            x += 1
        squares.append(square)

    for square in squares:
        if (square['abscisse'] + square['ordonnée']) % 2 == 0:
            square['color'] = 'white'
        else:
            square['color'] = 'black'

    return squares
