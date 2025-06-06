import pygame
import time
import random

# Ini pygame
pygame.init()

# Screen size
width = 800
height = 600
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake game")

# Color
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 200, 0)
red = (200, 0, 0)

# Snake size
block_size = 20
snake_speed = 10

# Clock
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 35)

def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(win, green, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    text = font.render(msg, True, color)
    text_rect = text.get_rect(center=(width / 2, height / 2))
    win.blit(text, text_rect)


def game_loop():
    game_over = False
    game_close = False

    x = width / 2
    y = height / 2
    dx = 0
    dy = 0

    snake_list = []
    length = 1

    # Food Position
    food_x = round(random.randrange(0, width - block_size) / 20.0) * 20.0
    food_y = round(random.randrange(0, height - block_size) / 20.0) * 20.0

    while not game_over:

        while game_close:
            win.fill(white)
            message("You lost! Press Q to close or C to replay", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and dx == 0:
                    dx = -block_size
                    dy = 0
                elif event.key == pygame.K_RIGHT and dx == 0:
                    dx = block_size
                    dy = 0
                elif event.key == pygame.K_UP and dy == 0:
                    dy = -block_size
                    dx = 0
                elif event.key == pygame.K_DOWN and dy == 0:
                    dy = block_size
                    dx = 0

        x += dx
        y += dy

        # Hit the wall -> will wrap around
        if x >= width:
            x = 0
        elif x < 0:
            x = width - block_size
        if y >= height:
            y = 0
        elif y < 0:
            y = height - block_size


        win.fill(white)
        pygame.draw.rect(win, red, [food_x, food_y, block_size, block_size])

        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_list.append(snake_head)

        if len(snake_list) > length:
            del snake_list[0]

        # Hit itself
        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        draw_snake(block_size, snake_list)

        pygame.display.update()

        # Eat food
        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, width - block_size) / 20.0) * 20.0
            food_y = round(random.randrange(0, height - block_size) / 20.0) * 20.0
            length += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

# Run game
game_loop()
