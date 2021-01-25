import pygame
import random
import numpy as np

def Food_generate(list1):
    while True:
        list2 = np.array([random.randrange(0, 481, step=20), random.randrange(0, 481, step=20), 20, 20])
        a = list2 == list1
        for i in a:
            if all(i):
                print(list1, list2)
                return Food_generate(list1)
        return list2
    return

def next_move(snake, food):
    pass

def snake():
    pygame.init()
    DISPLAY = pygame.display.set_mode([500, 500])
    pygame.display.set_caption('Snake')
    WHITE, RED, GREEN = [255, 255, 255], [255, 0, 0], [0, 255, 0]
    OPEN = True
    DIRECTION = np.array([20, 0, 0, 0])
    SNAKE = np.array([[240, 240, 20, 20]])
    FOOD = Food_generate(SNAKE)
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
                print(SNAKE)
        # drawing display
        DISPLAY.fill(WHITE)
        # food
        if type(FOOD) != str: pygame.draw.rect(DISPLAY, RED, FOOD)
        #snake
        for i in SNAKE: pygame.draw.rect(DISPLAY, GREEN, i)
        pygame.display.update()
        pygame.time.Clock().tick(6)
        continue
        pygame.quit()
        return SCORE

if __name__ == '__main__':
    snake()