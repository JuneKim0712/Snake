import random
import numpy as np
import tensorflow as tf
import tensorflow_probability as tfp
import matplotlib.pyplot as plt
import pygame


class snake_game:
    def __init__(self):
        pygame.init()
        self.DISPLAY = pygame.display.set_mode([500, 500])
        self.OPEN = True
        self.DIRECTION = ['right', np.array([1, 0])]
        self.snake = np.array([[15, 13], [14, 13], [13, 13], [14, 13]])
        self.food = self.Food_generate()
        self.score = 4
        pygame.display.set_caption('Snake')
        return

    def Food_generate(self):
        while True:
            random_food = [random.randrange(0, 24, step=1), 
            random.randrange(0, 24, step=1)]
            if random_food in self.snake:
                continue
            else:
                return random_food

    def next_move(self):
        pass

    def preprocess(self):

        pass

    def main(self):
        while self.OPEN:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.OPEN = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.DIRECTION = ['up', np.array([[0, -1]])]
                    elif event.key == pygame.K_DOWN:
                        self.DIRECTION = ['down', np.array([[0, 1]])]
                    elif event.key == pygame.K_LEFT:
                        self.DIRECTION = ['left', np.array([[-1, 0]])]
                    elif event.key == pygame.K_RIGHT:
                        self.DIRECTION = ['right', np.array([[1, 0]])]
                    pass
                pass

            #snake body movement
            if all(self.food == self.snake[-1]):
                self.score += 1
                self.snake = np.append(self.snake[:], self.snake[-1] + self.DIRECTION[1]).reshape(self.score, 2)
                self.food = self.Food_generate()
            else:
                self.snake = np.append(self.snake[1:], self.snake[-1] + self.DIRECTION[1]).reshape(self.score, 2)

            # border
            if not (-1 < self.snake[-1][0] < 25 and -1 < self.snake[-1][1] < 25):
                self.OPEN=False
            # snake blocked by its own body
            for i in self.snake[-1] == self.snake[:-1]:
                if all(i):
                    self.OPEN = False
            #won or not
            if self.snake.shape[0]==625:
                print('You won')
                return self.score
            #displaying
            self.DISPLAY.fill([0, 0, 0])
            for i in self.snake:
                pygame.draw.rect(self.DISPLAY, [0, 255, 0], [i[0]*20, i[1]*20, 20, 20])
            pygame.draw.rect(self.DISPLAY, [255, 0, 0], [self.food[0]*20, self.food[1]*20, 20, 20])
            pygame.display.update()
            pygame.time.Clock().tick(5)
            continue
        return self.score



if __name__ == '__main__':
    a=snake_game()
    a.main()
    