import pygame
# import time
import random
import numpy as np

pygame.init()
DISPLAY = pygame.display.set_mode([500, 500])
pygame.display.set_caption('Snake')
WHITE, RED, GREEN = [255, 255, 255], [255, 0, 0], [0, 255, 0]
OPEN = True
DIRECTION = np.array([20, 0, 0, 0])
SNAKE = np.array([[240, 240, 20, 20]])
FOOD = np.array([random.randrange(0, 501, step=20), random.randrange(0, 501, step=20), 20, 20])
print(FOOD)
while FOOD.copy() in SNAKE.copy(): FOOD = np.array([random.randrange(0, 501, step=20), random.randrange(0, 501, step=20), 20, 20])
print(FOOD)
SCORE = 0
while OPEN:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            OPEN = False
            pass
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and DIRECTION[1] != 20:
                DIRECTION = np.array([0, -20, 0, 0])
            elif event.key == pygame.K_DOWN and DIRECTION[1] != -20:
                DIRECTION = np.array([0, 20, 0, 0])
            elif event.key == pygame.K_LEFT and DIRECTION[0] != 20:
                DIRECTION = np.array([-20, 0, 0, 0])
            elif event.key == pygame.K_RIGHT and DIRECTION[0] != -20:
                DIRECTION = np.array([20, 0, 0, 0])
            pass
        pass

    # food

    if FOOD == 'eaten':
        FOOD = np.array([random.randrange(0, 501, step=20), random.randrange(0, 501, step=20), 20, 20])
        while FOOD.copy() in SNAKE.copy(): FOOD = np.array([random.randrange(0, 501, step=20), random.randrange(0, 501, step=20), 20, 20])
        SCORE += 1
        SNAKE = np.append(SNAKE[:], SNAKE[-1] + DIRECTION).reshape((SCORE + 1), 4)
        pass
    else:
        SNAKE = np.append(SNAKE[1:], SNAKE[-1] + DIRECTION).reshape((SCORE + 1), 4)
        pass
    print(FOOD)

    if not (-20 < SNAKE[-1][0] < 500 and -20 < SNAKE[-1][1] < 500):
        DISPLAY.fill(RED)
        break
    elif FOOD in SNAKE[-1][:-2]:
        print('Eaten')
        FOOD = 'eaten'
        pass
    # drawing display
    DISPLAY.fill(WHITE)
    if FOOD != 'eaten': pygame.draw.rect(DISPLAY, RED, FOOD)
    for i in SNAKE: pygame.draw.rect(DISPLAY, GREEN, i)
    pygame.display.update()
    pygame.time.Clock().tick(3)
    continue

pygame.quit()
