from settings import screen, screen_size, pg, best_font

button_image = pg.image.load('textures/button.png')
button_rect = button_image.get_rect()

bg_image = pg.image.load('textures/bg_image.png')

mouse_rect = pg.rect((0, 0, 1, 1))

class Button():
    def __init__(self, x, y):
        self.rect = pg.Rect((x, y, button_rect.width, button_rect.height))
        self.image = button_image


def show_menu():
    screen.blit(bg_image, (0, 0))

    pg.display.update()

show_menu()

