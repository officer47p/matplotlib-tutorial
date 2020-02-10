import random
from itertools import count
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import pandas as pd

c = count()

xs = []
ys = []


def draw(i):
    global xs
    global ys
    xs.append(next(c))
    ys.append(random.randint(0, 10))
    plt.cla()
    if len(xs) > 5 and len(ys) > 5:
        xs = xs[-5:]
        ys = ys[-5:]
    plt.plot(xs, ys)
    # print(len(xs), len(ys))


animation = FuncAnimation(plt.gcf(), draw, interval=1000)
plt.show()
