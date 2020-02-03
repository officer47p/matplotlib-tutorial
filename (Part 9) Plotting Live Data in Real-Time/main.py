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
    if len(xs) > 20 and len(ys) > 20:
        xs = xs[-20:]
        ys = ys[-20:]
    plt.plot(xs, ys)


animation = FuncAnimation(plt.gcf(), draw, interval=100)
plt.show()
