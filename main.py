import pygame
import sys, time
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
SIZE = WIDTH, HEIGHT = 500, 700

# Initializes the screen
SCREEN = pygame.display.set_mode(SIZE)

START_PONG_X = 245
START_PONG_Y = 245

START_PLAYER_ONE_X = 60
START_PLAYER_ONE_Y = 220

START_PLAYER_TWO_X = 425
START_PLAYER_TWO_Y = 220

player_one_score = 0
player_two_score = 0

GAME_AREA = pygame.surface.Surface((500, 500))

PONG = Box(GAME_AREA, WHITE, START_PONG_X, START_PONG_Y, 10, 10)
PONG_DIRECTION = Direction.RIGHT
PLAYER_ONE = Box(GAME_AREA, WHITE, START_PLAYER_ONE_X, START_PLAYER_ONE_Y, 15, 60)
PLAYER_TWO = Box(GAME_AREA, WHITE, START_PLAYER_TWO_X, START_PLAYER_TWO_Y, 15, 60)
MOVE_DISTANCE = 5

fpsClock = pygame.time.Clock()

def reset_game_state():
    global PONG_DIRECTION
    PONG.x = START_PONG_X
    PONG.y = START_PONG_Y
    PLAYER_ONE.x = START_PLAYER_ONE_X
    PLAYER_ONE.y = START_PLAYER_ONE_Y
    PLAYER_TWO.x = START_PLAYER_TWO_X
    PLAYER_TWO.y = START_PLAYER_TWO_Y
    PONG_DIRECTION = random.choice([Direction.LEFT, Direction.RIGHT])
    time.sleep(2)



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



    ### Pong Movement ###

    # move right
    if PONG_DIRECTION == Direction.RIGHT:
        if PONG.rect.colliderect(PLAYER_TWO.rect):
            PONG_DIRECTION = random.choice(
                [Direction.LEFT, Direction.DOWN_AND_LEFT, Direction.UP_AND_LEFT]
            )
        elif PONG.x + PONG.width == PONG.surface_width:
            #win for player one
            player_one_score += 1
            #reset game state
            reset_game_state()
        else:
            PONG.move_right(MOVE_DISTANCE)
    # move left
    elif PONG_DIRECTION == Direction.LEFT:
        if PONG.rect.colliderect(PLAYER_ONE.rect):
            PONG_DIRECTION = random.choice(
                [Direction.RIGHT, Direction.DOWN_AND_RIGHT, Direction.UP_AND_RIGHT]
            )
        elif PONG.x == 0:
            player_two_score += 1
            reset_game_state()
        else:
            PONG.move_left(MOVE_DISTANCE)
    # move down + left
    elif PONG_DIRECTION == Direction.DOWN_AND_LEFT:
        if PONG.rect.colliderect(PLAYER_ONE.rect):
            PONG_DIRECTION = random.choice(
                [Direction.RIGHT, Direction.DOWN_AND_RIGHT, Direction.UP_AND_RIGHT]
            )
        elif PONG.x == 0 and PONG.y + PONG.height == PONG.surface_height:
            player_two_score += 1
            reset_game_state()
        elif PONG.x == 0:
            player_two_score += 1
            reset_game_state()
        elif PONG.y + PONG.height == PONG.surface_height:
            PONG_DIRECTION = random.choice(
                [Direction.UP, Direction.UP_AND_LEFT, Direction.UP_AND_RIGHT])
        else:
            PONG.move_left(MOVE_DISTANCE)
            PONG.move_down(MOVE_DISTANCE)
    # move up + left
    elif PONG_DIRECTION == Direction.UP_AND_LEFT:
        if PONG.rect.colliderect(PLAYER_ONE.rect):
            PONG_DIRECTION = random.choice(
                [Direction.RIGHT, Direction.DOWN_AND_RIGHT, Direction.UP_AND_RIGHT]
            )
        elif PONG.y == 0 and PONG.x == 0:
            player_two_score += 1
            reset_game_state()
        elif PONG.y == 0:
            PONG_DIRECTION = random.choice(
                [Direction.DOWN_AND_LEFT, Direction.DOWN, Direction.DOWN_AND_RIGHT])
        elif PONG.x == 0:
            player_two_score += 1
            reset_game_state()
        else:
            PONG.move_left(MOVE_DISTANCE)
            PONG.move_up(MOVE_DISTANCE)
    
    #move down + right
    elif PONG_DIRECTION == Direction.DOWN_AND_RIGHT:
        if PONG.rect.colliderect(PLAYER_TWO.rect):
            PONG_DIRECTION = random.choice(
                [Direction.LEFT, Direction.DOWN_AND_LEFT, Direction.UP_AND_LEFT]
            )
        elif PONG.x + PONG.width == PONG.surface_width and PONG.y + PONG.height == PONG.surface_height:
            player_one_score += 1
            reset_game_state()
        elif PONG.x + PONG.width == PONG.surface_width:
            player_one_score += 1
            reset_game_state()
        elif PONG.y + PONG.height == PONG.surface_height:
            PONG_DIRECTION = random.choice(
                [Direction.UP_AND_LEFT, Direction.UP, Direction.UP_AND_RIGHT]
            )
        else:
            PONG.move_down(MOVE_DISTANCE)
            PONG.move_right(MOVE_DISTANCE)

    #move up + right
    elif PONG_DIRECTION == Direction.UP_AND_RIGHT:
        if PONG.rect.colliderect(PLAYER_TWO.rect):
            PONG_DIRECTION = random.choice(
                [Direction.LEFT, Direction.DOWN_AND_LEFT, Direction.UP_AND_LEFT]
            )
        elif PONG.x + PONG.width == PONG.surface_width and PONG.y == 0:
            player_one_score += 1
            reset_game_state()
        elif PONG.x + PONG.width == PONG.surface_width:
            player_one_score += 1
            reset_game_state()
        elif PONG.y == 0:
            PONG_DIRECTION = random.choice(
                [Direction.DOWN_AND_LEFT, Direction.DOWN, Direction.DOWN_AND_RIGHT]
            )
        else:
            PONG.move_up(MOVE_DISTANCE)
            PONG.move_right(MOVE_DISTANCE)
    #move down
    elif PONG_DIRECTION == Direction.DOWN:
        if PONG.y + PONG.height == PONG.surface_height:
            PONG_DIRECTION = random.choice(
                [Direction.UP_AND_LEFT, Direction.UP_AND_RIGHT, Direction.UP]
            )
        else:
            PONG.move_down(MOVE_DISTANCE)
    #move up
    elif PONG_DIRECTION ==  Direction.UP:
        if PONG.y == 0:
            PONG_DIRECTION = random.choice(
                [Direction.DOWN_AND_LEFT, Direction.DOWN, Direction.DOWN_AND_RIGHT]
            )
        else:
            PONG.move_up(MOVE_DISTANCE)

   

    SCREEN.fill(BLACK)
    GAME_AREA.fill(BLUE)


    print(player_one_score, player_two_score)
    PONG.tick()
    PLAYER_ONE.tick()
    PLAYER_TWO.tick()
    

    SCREEN.blit(GAME_AREA, (0, 0))


    fpsClock.tick(FPS)
    pygame.display.update()
