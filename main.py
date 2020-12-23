import pygame
import sys
from menu import show_menu

pygame.init()

screen_size = screen_width, screen_height = (800, 600)
screen = pygame.display.set_mode(screen_size)

while True:
    screen.fill((50, 180, 130))
    for e in pygame.event.get():
        if e.type == pygame.KEYDOWN:
            show_menu()
    
    pygame.display.update()