def mouse_coordinates_click(mouse_x, mouse_y):
    """Get the coordinates of the square where the mouse was released"""
    click = mouse_x, mouse_y
    if click:
        x, y = click
        if 60 <= x < 120:
            abscisse = 1
        elif 120 <= x < 180:
            abscisse = 2
        elif 180 <= x < 240:
            abscisse = 3
        elif 240 <= x < 300:
            abscisse = 4
        elif 300 <= x < 360:
            abscisse = 5
        elif 360 <= x < 420:
            abscisse = 6
        elif 420 <= x < 480:
            abscisse = 7
        elif 480 <= x < 540:
            abscisse = 8
        else:
            abscisse = False

        if 60 <= y < 120:
            ordonnee = 8
        elif 120 <= y < 180:
            ordonnee = 7
        elif 180 <= y < 240:
            ordonnee = 6
        elif 240 <= y < 300:
            ordonnee = 5
        elif 300 <= y < 360:
            ordonnee = 4
        elif 360 <= y < 420:
            ordonnee = 3
        elif 420 <= y < 480:
            ordonnee = 2
        elif 480 <= y < 540:
            ordonnee = 1
        else:
            ordonnee = False
        coordinates = abscisse, ordonnee
        if abscisse:
            if ordonnee:
                return coordinates
            else:
                return False


def mouse_coordinates_release(mouse_x, mouse_y):
    """Get the coordinates of the square where the mouse was released"""
    release = mouse_x, mouse_y
    if release:
        x, y = release
        if 60 <= x < 120:
            abscisse = 1
        elif 120 <= x < 180:
            abscisse = 2
        elif 180 <= x < 240:
            abscisse = 3
        elif 240 <= x < 300:
            abscisse = 4
        elif 300 <= x < 360:
            abscisse = 5
        elif 360 <= x < 420:
            abscisse = 6
        elif 420 <= x < 480:
            abscisse = 7
        elif 480 <= x < 540:
            abscisse = 8
        else:
            abscisse = False

        if 60 <= y < 120:
            ordonnee = 8
        elif 120 <= y < 180:
            ordonnee = 7
        elif 180 <= y < 240:
            ordonnee = 6
        elif 240 <= y < 300:
            ordonnee = 5
        elif 300 <= y < 360:
            ordonnee = 4
        elif 360 <= y < 420:
            ordonnee = 3
        elif 420 <= y < 480:
            ordonnee = 2
        elif 480 <= y < 540:
            ordonnee = 1
        else:
            ordonnee = False
        coordinates = abscisse, ordonnee
        if abscisse:
            if ordonnee:
                return coordinates
            else:
                return False
