from settings import *

button_image = pg.image.load('textures/button.png')
button_pressed_image = pg.image.load('textures/button_pressed.png')


def show_menu():
    screen.fill((100, 100, 100))
    
    screen.blit(button_image, (0,0))
    screen.blit(button_pressed_image, (100,0))

    pg.display.update()

show_menu()
