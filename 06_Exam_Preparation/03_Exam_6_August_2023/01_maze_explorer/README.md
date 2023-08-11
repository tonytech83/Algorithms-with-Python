
# **Algorithms Fundamentals with Python: Exam**
Please submit your solutions (source code) to all the below-described problems in [Judge](https://judge.softuni.org/Contests/4044).

## **1. Maze Explorer**

You are tasked with finding the **shortest path in a maze** that is represented by a **two-dimensional grid**. The maze contains walls denoted by the character **'#'**, and open paths denoted by the character **'.'**. 

You can move in any of the four main directions (**up**, **down**, **left**, or **right**), but **cannot move through walls**. 

You must start at the position (**0, 0**) and find the shortest path to the destination position (denoted with **'E'**).

The output of the program should be the shortest path from the starting position to the destination position.
### **Input**
- The first line of the input contains a single integer n, which represents the size of the square maze.
- The next n lines of the input contain n characters each, representing the symbols in each row of the maze:
  - A "**#**" character denotes a wall.
  - A "**.**" character denotes an open path.
  - A "**S**" character denotes the starting position.
  - An "**E**" character denotes the end of the maze.
### **Output**
- The output should be a single integer representing the number of steps required to follow the shortest path from the starting position to the destination position.
### **Constraints**
- **1 <= n <= 20**, where n is an integer representing the **size of the square maze**.
- The symbols in the maze will be limited to "**S**" (representing the starting position), "**E**" (representing the destination position), "**#**" (representing a wall), and "**.**" (representing an open path).
- There will always be **at least one** valid path from the starting position to the destination position.
### **Examples**

| **Input**|**Output**|
|:----| :-: |
| <p>4</p><p>S.#.</p><p>.##E</p><p>.##.</p><p>....</p>|8|
| <p>4</p><p>S...</p><p>.##E</p><p>.##.</p><p>....</p>|4|
