import pygame, sys
from box import Box
pygame.init()

# COLORS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (255, 0, 255)
YELLOW = (255, 255, 0)

FPS = 60

# Sets the screen size
SIZE = WIDTH, HEIGHT = 500, 500

# Initializes the screen
SCREEN = pygame.display.set_mode(SIZE)

SimonsBox = Box(SCREEN, GREEN, 100, 100, 200, 200)

fpsClock = pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # elif event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_UP:
        #         SimonsBox.move_up(5)
        #     elif event.key == pygame.K_DOWN:
        #         SimonsBox.move_down(5)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        SimonsBox.move_up(5)
    elif keys[pygame.K_DOWN]:
        SimonsBox.move_down(5)
    elif keys[pygame.K_RIGHT]:
        SimonsBox.move_right(5)
    elif keys[pygame.K_LEFT]:
        SimonsBox.move_left(5)

    SCREEN.fill(PURPLE)

    SimonsBox.tick()

    fpsClock.tick(FPS)
    pygame.display.update()


    