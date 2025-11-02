import numpy as np
import random

def generate_maze(size=20):
    maze = np.zeros((size,size))
    for i in range(size):
        for j in range(size):
            maze[i, j] = 1 if random.random() < 0.3 else 0
    maze[0, 0] = 0
    maze[-1, -1] = 0
    return maze