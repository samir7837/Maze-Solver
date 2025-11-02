# 🧭 Streamlit Maze Solver

A visual **maze-solving app** built using **Streamlit**, where a random maze is generated and solved using classical pathfinding algorithms — **BFS**, **DFS**, **Best First Search**, and **A\***.

---

## 🚀 Features

- 🎲 **Random Maze Generation**
- 🧩 Choose between multiple algorithms:
  - Breadth-First Search (BFS)
  - Depth-First Search (DFS)
  - Best First Search
  - A* (A-Star)
- 🧠 **Visualize** the solution path directly on the maze
- ⚙️ Adjustable maze size (10x10 to 40x40)
- Simple, interactive Streamlit UI

---

## 📂 Project Structure

maze-solver/
│
├── app.py # Main Streamlit app
├── maze_generator.py # Random maze generation logic
├── algorithms.py # BFS, DFS, Best First, A* algorithms
└── README.md # Documentation

---

## 🧮 How It Works

A maze grid is generated using random 0s (open) and 1s (walls).

You choose an algorithm from the dropdown.

The chosen algorithm tries to find a path from Start (0,0) to Goal (n-1,n-1).

The path is visualized in red, with green and blue dots marking the start and goal.

---

## 🧠 Algorithms Overview

| Algorithm             | Type       | Characteristics                                     |
| --------------------- | ---------- | --------------------------------------------------- |
| **BFS**               | Uninformed | Finds the shortest path (if exists)                 |
| **DFS**               | Uninformed | Explores deeply, may not find shortest path         |
| **Best First Search** | Informed   | Greedy — uses heuristic for faster exploration      |
| **A***                | Informed   | Combines cost and heuristic — optimal and efficient |

---

## 💻 Tech Stack

Python 3.9+

Streamlit

NumPy

MatplotliB

---
