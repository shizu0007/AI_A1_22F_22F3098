AI 2002 -- Assignment 1\
Uninformed Search in a Grid Environment

Student Name: Shahzad Ahmed\
Roll No: 22F3098

------------------------------------------------------------------------

Project Description:

In this assignment, I implemented an AI pathfinding system that
demonstrates six uninformed search algorithms in a grid-based
environment using Pygame.

The objective of this project is to visualize how each algorithm
explores nodes step-by-step while finding a path from a Start node (S)
to a Target node (T).

The system also handles dynamic obstacles that may appear randomly
during execution.

------------------------------------------------------------------------

Algorithms Implemented:

1.  Breadth-First Search (BFS)
2.  Depth-First Search (DFS)
3.  Uniform Cost Search (UCS)
4.  Depth-Limited Search (DLS)
5.  Iterative Deepening DFS (IDDFS)
6.  Bidirectional Search

------------------------------------------------------------------------

Visualization Details:

Green → Start node\
Red → Target node\
Blue → Frontier nodes\
Yellow → Explored nodes\
Purple → Final path\
Black → Obstacles

The GUI shows step-by-step animation of how each algorithm expands
nodes.

------------------------------------------------------------------------

Dynamic Obstacles:

During execution, obstacles may appear randomly in empty cells. This
simulates a dynamic environment and allows observation of how the
algorithms behave under changing conditions.

------------------------------------------------------------------------

How to Run the Project:

1.  Install Python (if not installed)

2.  Install pygame:

    pip install pygame

3.  Run the program:

    python main.py

------------------------------------------------------------------------

Keyboard Controls:

R → Reset grid\
B → Best case scenario\
W → Worst case scenario

1 → Run BFS\
2 → Run DFS\
3 → Run UCS\
4 → Run DLS\
5 → Run IDDFS\
6 → Run Bidirectional Search

------------------------------------------------------------------------

Conclusion:

This project helped me understand how uninformed search algorithms
differ in terms of exploration strategy, optimality, memory usage, and
performance in both static and dynamic environments.
