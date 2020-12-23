import pygame
from main import screen_size, screen

pygame.init()

def show_menu():
    screen = pygame.display.set_mode((screen_size[0] // 2, screen_size[1] // 2))
    screen_size = ((screen_size[0] // 2, screen_size[1] // 2))