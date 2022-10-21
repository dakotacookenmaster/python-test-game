from tkinter.tix import DirSelectBox
import pygame
import sys
import random
from box import Box
from direction import Direction
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

PONG = Box(SCREEN, WHITE, 245, 245, 10, 10)
PONG_DIRECTION = Direction.RIGHT
PLAYER_ONE = Box(SCREEN, WHITE, 60, 220, 15, 60)
PLAYER_TWO = Box(SCREEN, WHITE, 425, 220, 15, 60)
MOVE_DISTANCE = 5

fpsClock = pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # Checking for the players key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        PLAYER_ONE.move_up(MOVE_DISTANCE)
    if keys[pygame.K_s]:
        PLAYER_ONE.move_down(MOVE_DISTANCE)
    if keys[pygame.K_UP]:
        PLAYER_TWO.move_up(MOVE_DISTANCE)
    if keys[pygame.K_DOWN]:
        PLAYER_TWO.move_down(MOVE_DISTANCE)


    print(PONG_DIRECTION)
    print(PONG.x, PONG.y)

    ### Pong Movement ###

    # move right
    if PONG_DIRECTION == Direction.RIGHT:
        if PONG.x + PONG.width == PONG.surface_width:
            PONG_DIRECTION = random.choice(
                [Direction.LEFT, Direction.DOWN_AND_LEFT, Direction.UP_AND_LEFT])
        else:
            PONG.move_right(MOVE_DISTANCE)
    # move left
    elif PONG_DIRECTION == Direction.LEFT:
        if PONG.x == 0:
            PONG_DIRECTION = random.choice(
                [Direction.RIGHT, Direction.DOWN_AND_RIGHT, Direction.UP_AND_RIGHT])
        else:
            PONG.move_left(MOVE_DISTANCE)
    # move down + left
    elif PONG_DIRECTION == Direction.DOWN_AND_LEFT:
        if PONG.x == 0 and PONG.y + PONG.height == PONG.surface_height:
            PONG_DIRECTION = Direction.UP_AND_RIGHT
        elif PONG.x == 0:
            PONG_DIRECTION = random.choice(
                [Direction.UP_AND_RIGHT, Direction.RIGHT, Direction.DOWN_AND_RIGHT]
            )
        elif PONG.y + PONG.height == PONG.surface_height:
            PONG_DIRECTION = random.choice(
                [Direction.UP, Direction.UP_AND_LEFT, Direction.UP_AND_RIGHT])
        else:
            PONG.move_left(MOVE_DISTANCE)
            PONG.move_down(MOVE_DISTANCE)
    # move up + left
    elif PONG_DIRECTION == Direction.UP_AND_LEFT:
        if PONG.y == 0 and PONG.x == 0:
            PONG_DIRECTION = Direction.DOWN_AND_RIGHT
        elif PONG.y == 0:
            PONG_DIRECTION = random.choice(
                [Direction.DOWN_AND_LEFT, Direction.DOWN, Direction.DOWN_AND_RIGHT])
        elif PONG.x == 0:
            PONG_DIRECTION = random.choice(
                [Direction.UP_AND_RIGHT, Direction.RIGHT, Direction.DOWN_AND_RIGHT]
            )
        else:
            PONG.move_left(MOVE_DISTANCE)
            PONG.move_up(MOVE_DISTANCE)
    
    #move down + right
    elif PONG_DIRECTION == Direction.DOWN_AND_RIGHT:
        if PONG.x + PONG.width == PONG.surface_width and PONG.y + PONG.height == PONG.surface_height:
            PONG_DIRECTION = Direction.UP_AND_LEFT
        elif PONG.x + PONG.width == PONG.surface_width:
            PONG_DIRECTION = random.choice(
                [Direction.UP_AND_LEFT, Direction.LEFT, Direction.DOWN_AND_LEFT]
            )
        elif PONG.y + PONG.height == PONG.surface_height:
            PONG_DIRECTION = random.choice(
                [Direction.UP_AND_LEFT, Direction.UP, Direction.UP_AND_RIGHT]
            )
        else:
            PONG.move_down(MOVE_DISTANCE)
            PONG.move_right(MOVE_DISTANCE)

    #move up + right
    elif PONG_DIRECTION == Direction.UP_AND_RIGHT:
        if PONG.x + PONG.width == PONG.surface_width and PONG.y == 0:
            PONG_DIRECTION = Direction.DOWN_AND_LEFT
        elif PONG.x + PONG.width == PONG.surface_width:
            PONG_DIRECTION = random.choice(
                [Direction.DOWN_AND_LEFT, Direction.DOWN, Direction.DOWN_AND_RIGHT]
            )
        elif PONG.y == 0:
            PONG_DIRECTION == random.choice(
                [Direction.UP_AND_LEFT, Direction.LEFT, Direction.DOWN_AND_LEFT]
            )
        else:
            PONG.move_up(MOVE_DISTANCE)
            PONG.move_right(MOVE_DISTANCE)
    #move down
    elif PONG_DIRECTION == Direction.DOWN:
        if PONG.y + PONG.height == PONG.surface_height:
            PONG_DIRECTION == random.choice(
                [Direction.UP_AND_LEFT, Direction.UP_AND_RIGHT, Direction.UP]
            )
        else:
            PONG.move_down(MOVE_DISTANCE)
    #move up
    elif PONG_DIRECTION ==  Direction.UP:
        if PONG.y == 0:
            PONG_DIRECTION == random.choice(
                [Direction.DOWN_AND_LEFT, Direction.DOWN, Direction.DOWN_AND_RIGHT]
            )
        else:
            PONG.move_up(MOVE_DISTANCE)

    SCREEN.fill(BLACK)

    PONG.tick()
    PLAYER_ONE.tick()
    PLAYER_TWO.tick()

    fpsClock.tick(FPS)
    pygame.display.update()
