import numpy as np
import random

def Food_generate(list1):
    list2=np.array([random.randrange(0, 481, step=20), random.randrange(0, 481, step=20), 20, 20])
    while True:
        a=list2==list1
        list2 = np.array([random.randrange(0, 481, step=20), random.randrange(0, 481, step=20), 20, 20])
        for i in a:
            if all(i):
                continue
        return list2

list1=np.array([[60, 80, 20, 20]])

for i in range(1, 10000):
    print(Food_generate(list1))
#print(list2[:2])