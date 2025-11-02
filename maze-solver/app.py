import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from maze_generator import generate_maze
from algorithms import bfs, dfs, best_first, a_star

st.set_page_config(page_title="Maze Solver", layout="centered")

st.title("🧭 Random Maze Solver Visualization")

size = st.slider("Select Maze Size", 10, 40, 20)
algorithm = st.selectbox("Choose Algorithm", ["BFS", "DFS", "Best First Search", "A*"])
generate = st.button("Generate & Solve Maze")

if generate:
    maze = generate_maze(size)
    start, goal = (0, 0), (size-1, size-1)

    if algorithm == "BFS":
        path = bfs(maze, start, goal)
    elif algorithm == "DFS":
        path = dfs(maze, start, goal)
    elif algorithm == "Best First Search":
        path = best_first(maze, start, goal)
    else:
        path = a_star(maze, start, goal)

    fig, ax = plt.subplots(figsize=(6,6))
    ax.imshow(maze, cmap='binary')
    if path:
        px, py = zip(*path)
        ax.plot(py, px, color='red')
    ax.scatter([0],[0], c='green', s=100, label='Start')
    ax.scatter([size-1],[size-1], c='blue', s=100, label='Goal')
    ax.legend()
    st.pyplot(fig)
