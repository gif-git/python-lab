import pygame as pg
from random import randrange

WINDOW = 600
TILE_SIZE = 30  # size of snake
RANGE = (TILE_SIZE // 2, WINDOW - TILE_SIZE // 2, TILE_SIZE)
get_random_position = lambda: [randrange(*RANGE), randrange(*RANGE)]
snake = pg.rect.Rect([0, 0, TILE_SIZE - 2, TILE_SIZE - 2])
snake.center = get_random_position()
length = 1
segments = [snake.copy()]
snake_dir = (0, 0)
time, time_step = 0, 180 # time of move
food = snake.copy()
food.center = get_random_position()
screen = pg.display.set_mode([WINDOW] * 2)
clock = pg.time.Clock()
#dirs = {pg.K_w:1, pg.K_s: 1, pg.K_a: 1, pg.K_d: 1}

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_i:
                snake_dir = (0, -TILE_SIZE)
            if event.key == pg.K_k:
                snake_dir = (0, TILE_SIZE)
            if event.key == pg.K_j:
                snake_dir = (-TILE_SIZE, 0)
            if event.key == pg.K_l:
                snake_dir = (TILE_SIZE, 0)
    screen.fill('black') # background colour
    # check borders and selfeating
    self_eating = pg.Rect.collidelist(snake, segments[:-1]) !=-1
    if snake.left < 0 or snake.right > WINDOW or snake.top < 0 or snake.bottom > WINDOW or self_eating:
        snake.center, food.center = get_random_position(), get_random_position()
        length, snake_dir = 1, (0,0)
        segments = [snake.copy()]
    # check food
    if snake.center == food.center:
        food.center = get_random_position()
        length += 1
    pg.draw.rect(screen, 'red', food) # food colour
    # draw snake
    [pg.draw.rect(screen, 'green', segment) for segment in segments] # snake colour
    # move snake
    time_now = pg.time.get_ticks()
    if time_now - time > time_step:
        time = time_now
        snake.move_ip(snake_dir)
        segments.append(snake.copy())
        segments = segments[-length:]
    pg.display.flip()
    clock.tick(60)
