import pygame
import time
import random
import numpy as np
import threading

def Food_generate(list1):
    while True:
        list2 = np.array([random.randrange(0, 481, step=20), random.randrange(0, 481, step=20), 20, 20])
        a = list2 == list1
        for i in a:
            if all(i):
                return Food_generate(list1)
        return list2
    return


def next_move(snake, food, direction):
    if snake[-1][1] < food[1] and direction[1] != -20 and snake[-1][1]+20 < 500:
        return 'down'
    elif snake[-1][1] > food[1] and direction[1] != 20 and snake[-1][1]-20 > -20:
        return 'up'
    elif snake[-1][0] < food[0] and direction[0] != -20 and snake[-1][0]+20 < 500:
        return 'right'
    elif snake[-1][0] > food[0] and direction[0] != 20 and snake[-1][0]-20 > -20:
        return 'left'
    #survival
    elif direction[1] != 20 and snake[-1][1]-20 > -20:
        return 'up'
    elif direction[0] != -20 and snake[-1][0]+20 < 500:
        return 'right'
    elif direction[1] != -20 and snake[-1][1] + 20 < 500:
        return 'down'
    elif direction[0] != 20 and snake[-1][0]-20 > -20:
        return 'left'


def snake():
    pygame.init()
    DISPLAY = pygame.display.set_mode([500, 500])
    pygame.display.set_caption('Snake')
    WHITE, RED, GREEN = [255, 255, 255], [255, 0, 0], [0, 255, 0]
    OPEN = True
    DIRECTION = np.array([20, 0, 0, 0])
    SNAKE = np.array([[240, 240, 20, 20], [260, 240, 20, 20]])
    FOOD = Food_generate(SNAKE)
    SCORE = 1

    while OPEN:
        move=next_move(SNAKE, FOOD, DIRECTION)
        print(move)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                OPEN = False
                pass
        if move == 'up' and DIRECTION[1] != 20:
            DIRECTION = np.array([0, -20, 0, 0])
        elif move == 'down' and DIRECTION[1] != -20:
            DIRECTION = np.array([0, 20, 0, 0])
        elif move == 'left' and DIRECTION[0] != 20:
            DIRECTION = np.array([-20, 0, 0, 0])
        elif move == 'right' and DIRECTION[0] != -20:
            DIRECTION = np.array([20, 0, 0, 0])
        # snake and foo3
        if all(FOOD == SNAKE[-1]):
            SNAKE = np.append(SNAKE[1:], SNAKE[-1] + DIRECTION).reshape((SCORE + 1), 4)
            SCORE += 1
            SNAKE = np.append(SNAKE[:], SNAKE[-1] + DIRECTION).reshape((SCORE + 1), 4)
            if SNAKE.shape[0]==625:
                print('You won')
                return SCORE
            FOOD=Food_generate(SNAKE)
            pass
        else:
            SNAKE = np.append(SNAKE[1:], SNAKE[-1] + DIRECTION).reshape((SCORE + 1), 4)
        # border
        if not (-20 < SNAKE[-1][0] < 500 and -20 < SNAKE[-1][1] < 500):
            break
        # snake blocked by its own body
        for i in SNAKE[-1]==SNAKE[:-1]:
            if all(i):
                OPEN=False
        # drawing display
        DISPLAY.fill(WHITE)
        # food
        if type(FOOD) != str: pygame.draw.rect(DISPLAY, RED, FOOD)
        #snake
        for i in SNAKE: pygame.draw.rect(DISPLAY, GREEN, i)
        pygame.display.update()
        pygame.time.Clock().tick(20)
        continue
        pygame.quit()
        return SCORE

if __name__ == '__main__':
    snake()