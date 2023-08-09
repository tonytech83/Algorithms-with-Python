**Algorithms with Python: Exam**

Please submit your solutions (source code) to all below-described problems
in [Judge](https://judge.softuni.org/Contests/3592).

**2. Guards**

The Ankh Morpork guards need your help there has been a flood in the city and some outposts can no longer be reached
from a specific starting point your task is to report those.
You will be given the map of the outposts, as a graph from the console with a given start node, print all the
unreachable nodes in order by their number ascending.

## **Input**

- The input will come from the console on multiple lines:
    - first line: **N** single integer – the number of nodes
    - second line: **M** single integer –** the number of edges
    - **M** lines describing the edges connections in the format: **{from} {to}**
    - **S** single integer – the start node

## **Output**

- The output is a sequence of integers that represents the unreachable outposts.

## **Constraints**

- The input graph will not contain more than 30 nodes or edges.

## **Examples**

| **Input**                                                                  | **Output** |
|:---------------------------------------------------------------------------|:-----------|
| <p>6</p><p>5</p><p>1 2</p><p>2 4</p><p>3 4</p><p>6 5</p><p>6 4</p><p>1</p> | 3 5 6      |
| <p>4</p><p>4</p><p>1 4</p><p>2 3</p><p>3 4</p><p>4 1</p><p>3</p>           | 2          |




