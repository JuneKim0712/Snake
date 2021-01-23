import pygame
import threading
import random
import numpy as np
import matplotlib.pyplot as plt



def dplace(move):
    if move == 'up':
        DIRECTION = np.array([0, -20, 0, 0])
    elif move == 'down':
        DIRECTION = np.array([0, 20, 0, 0])
    elif move == 'left':
        DIRECTION = np.array([-20, 0, 0, 0])
    elif move == 'right':
        DIRECTION = np.array([20, 0, 0, 0])
    return DIRECTION


def Food_generate(list1):
    while True:
        list2 = np.array([random.randrange(0, 481, step=20), random.randrange(0, 481, step=20), 20, 20])
        a = list2 == list1
        for i in a:
            if all(i):
                return Food_generate(list1)
        return list2
    return


def survival(snake, direction):
    ans = []
    ao = np.array([[0, 20], [0, -20], [20, 0], [-20, 0]])
    bin = np.array([True])
    for n in ao:
        bin2 = True
        for i in snake.copy():
            a = all((snake.copy()[-1][:2] + n == i[:2]))
            if a:
                bin = np.append(bin, False)
                bin2 = False
                break
        if bin2:
            bin = np.append(bin, True)
            pass
    point=0
    if direction[1] != -20 and snake[-1][1] + 20 < 500 and bin[1]:
        point += 1
    elif direction[1] != 20 and snake[-1][1] - 20 > -20 and bin[2]:
        point += 1
    elif direction[0] != -20 and snake[-1][0] + 20 < 500 and bin[3]:
        point += 1
    elif direction[0] != 20 and snake[-1][0] - 20 > -20 and bin[4]:
        point += 1
    return point



def next_move(snake, food, direction, score):
    ans = []
    ao = np.array([[0, 20], [0, -20], [20, 0], [-20, 0]])
    bin = np.array([True])
    for n in ao:
        bin2 = True
        for i in snake.copy():
            a = all((snake.copy()[-1][:2] + n == i[:2]))
            if a:
                bin = np.append(bin, False)
                bin2 = False
                break
        if bin2:
            bin = np.append(bin, True)
            pass

    if snake[-1][1] < food[1] and direction[1] != -20 and snake[-1][1] + 20 < 500 and bin[1]:
        ans = 'down'
    elif snake[-1][1] > food[1] and direction[1] != 20 and snake[-1][1] - 20 > -20 and bin[2]:
        ans = 'up'
    elif snake[-1][0] < food[0] and direction[0] != -20 and snake[-1][0] + 20 < 500 and bin[3]:
        ans = 'right'
    elif snake[-1][0] > food[0] and direction[0] != 20 and snake[-1][0] - 20 > -20 and bin[4]:
        ans = 'left'
    # survival

    if not ans:
        down, up, right, left = [0, 'down'], [0, 'up'], [0, 'right'], [0, 'left']
        if direction[1] != -20 and snake[-1][1] + 20 < 500 and bin[1]:
            down=[survival(np.append(snake[1:], snake[-1] + np.array([0, 20, 0, 0])).reshape((score + 1), 4), np.array([0, 20, 0, 0])), 'down']
        if direction[1] != 20 and snake[-1][1] - 20 > -20 and bin[2]:
            up=[survival(np.append(snake[1:], snake[-1] + np.array([0, -20, 0, 0])).reshape((score + 1), 4), np.array([0, -20, 0, 0])), 'up']
        if direction[0] != -20 and snake[-1][0] + 20 < 500 and bin[3]:
            right=[survival(np.append(snake[1:], snake[-1] + np.array([20, 0, 0, 0])).reshape((score + 1), 4), np.array([20, 0, 0, 0])), 'right']
        if direction[0] != 20 and snake[-1][0] - 20 > -20 and bin[4]:
            left=[survival(np.append(snake[1:], snake[-1] + np.array([-20, 0, 0, 0])).reshape((score + 1), 4), np.array([-20, 0, 0, 0])), 'left']
        ans=[down, up, right, left]
        ans.sort()
        if ans[-1][0] == ans[-2][0]:
            return random.choice([ans[-1][1], ans[-2][1]])
        else:
            return str(ans[-1][1])
    else:
        return ans


def snake():
    pygame.init()
    DISPLAY = pygame.display.set_mode([500, 500])
    pygame.display.set_caption('Snake')
    WHITE, RED, GREEN = [255, 255, 255], [255, 0, 0], [0, 255, 0]
    OPEN = True
    move = np.array([20, 0, 0, 0])
    SNAKE = np.array([[220, 240, 20, 20], [240, 240, 20, 20], [260, 240, 20, 20], [280, 240, 20, 20]])
    FOOD = Food_generate(SNAKE)
    SCORE = 3

    while OPEN:
        move = dplace(str(next_move(SNAKE[1:], FOOD, move, SCORE-1)))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                OPEN = False
                pass
        # snake and foo3
        if all(FOOD == SNAKE[-1]):
            SNAKE = np.append(SNAKE[1:], SNAKE[-1] + move).reshape((SCORE + 1), 4)
            move = dplace(str(next_move(SNAKE[1:], FOOD, move, SCORE-1)))
            SCORE += 1
            SNAKE = np.append(SNAKE[:], SNAKE[-1] + move).reshape((SCORE + 1), 4)
            if SNAKE.shape[0] == 625:
                print('You won')
                return SCORE
            FOOD = Food_generate(SNAKE)
            pass
        else:
            SNAKE = np.append(SNAKE[1:], SNAKE[-1] + move).reshape((SCORE + 1), 4)
        # border
        if not (-20 < SNAKE[-1][0] < 500 and -20 < SNAKE[-1][1] < 500):
            OPEN = False
        # snake blocked by its own body
        for i in SNAKE[-1] == SNAKE[:-1]:
            if all(i):
                OPEN = False
        # drawing display
        DISPLAY.fill(WHITE)
        # food
        if type(FOOD) != str: pygame.draw.rect(DISPLAY, RED, FOOD)
        # snake
        for i in SNAKE: pygame.draw.rect(DISPLAY, GREEN, i)
        pygame.display.update()
        pygame.time.Clock().tick(20)
        continue
    snake()
    return [SCORE]


if __name__ == '__main__':
    snake()
