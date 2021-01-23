import numpy as np
import random


def Food_generate(list1):
    while True:
        list2 = np.array([random.randrange(0, 481, step=20), random.randrange(0, 481, step=20), 20, 20])
        a = list2 == list1
        for i in a:
            if all(i):
                print(list1, list2)
                continue
        return list2
    return


list1 = np.array([[60, 80, 20, 20], [40, 40, 20, 20]])

for i in range(1, 1000):
    a = Food_generate(list1)
# print(list2[:2])
