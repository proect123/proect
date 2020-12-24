import sys
from settings import screen, screen_size, screen_width, screen_height, pg, best_font

button_image = pg.image.load('proect/textures/button.png')
button_rect = button_image.get_rect()

bg_image = pg.image.load('proect/textures/bg_image.png')

mouse_rect = pg.Rect((0, 0, 1, 1))

class Button():
    def __init__(self, x, y):
        self.rect = pg.Rect((x, y, button_rect.width, button_rect.height))
        self.image = button_image
        self.text = ''
        self.text_color = (0, 0, 0)

    def update(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))
        screen.blit(best_font.render(self.text, True, self.text_color),\
                    (self.rect.x + self.rect.width // 2 - best_font.size(self.text)[0] // 2,\
                    self.rect.y + self.rect.height // 2 - best_font.size(self.text)[1] // 2))

button_list = []
for i in range(3):
    button_list.append(Button(screen_width - button_rect.width - 50, screen_height - 100 - i * (button_rect.height + 10)))
button_list[-1].text = 'START'
button_list[-2].text = 'SETTINGS'
button_list[-3].text = 'QUIT'


def show_menu():
    global mouse_rect
    screen.blit(bg_image, (0, 0))

    mouse_rect.x = pg.mouse.get_pos()[0]
    mouse_rect.y = pg.mouse.get_pos()[1]

    for i, btn in enumerate(button_list):
        if mouse_rect.colliderect(btn.rect):
            btn.text_color = (240, 100, 100)
            if pg.mouse.get_pressed()[0]:
                if i == 0:
                    sys.exit(0)
        else:
            btn.text_color = (0, 0, 0)

        btn.update()

    pg.display.update()

while True:
    for e in pg.event.get():
        if e.type == pg.KEYDOWN:
            if e.key == pg.K_ESCAPE:
                sys.exit(0)

    show_menu()

