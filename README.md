# Pathfinder2D: Your Guide Through Puzzling Terrain

Welcome to Pathfinder2D, a Python solution to navigate through 2-dimensional pathfinding problems. Given a grid-like puzzle consisting of empty and blocked cells (notated as '-' and '#' respectively), Pathfinder2D accurately determines the shortest path between two specified points while cleverly avoiding any obstacles. It effectively employs graph traversal techniques, specifically breadth-first search, to smoothly navigate through the grid.

## The Solution

Pathfinder2D uses the breadth-first search algorithm to solve the pathfinding problem. The algorithm starts at the source node and visits all nodes at an equal distance before proceeding to the next ‘layer’. This approach ensures that when the destination node is found, it was reached via the shortest possible path. 

Additionally, the algorithm utilizes a 'parent' dictionary to store parts of all explored paths. By backtracking through this dictionary from the destination, a shortest path and its corresponding directions can be reconstructed.

Here are the detailed steps of this algorithmic approach:

1. Initialize a visited matrix of the same size as the input board with all values set to false. Blocked cells are immediately set to true. 

2. Initialize an empty parent dictionary with the format {(x1,y1): ((x0,y0, D)),...}, where 'D' represents the direction from the source (U,D,R,L).

3. Initialize the breadth-first search (BFS) queue and enqueue the source node.

4. Mark the source node as visited on the visited matrix.

5. Loop until the destination is found or all possible paths have been explored (i.e., the BFS queue is empty):

   a. Dequeue a node and save its values to variables.

   b. If an adjacent node is visited (which includes blocked cells), skip it.

   c. If an adjacent node is the destination, add a new entry to the parent dictionary and terminate the search.

   d. Otherwise, mark the node as visited, enqueue it, and update paths in the parent dictionary.

6. If the loop concludes without a path found, return 'None'.

7. If a path to the destination was found during BFS, backtrack through the parent dictionary to construct and return the shortest path and its respective directions.

## How to Use 

1. Import the `Puzzle` module:
   ```python
   import Puzzle
   ```

2. Define your board as a list of lists, and your source and destination as tuples. For example:
   ```python
   Puzzle = [
    ['-', '-', '-', '-', '-'],
    ['-', '-', '#', '-', '-'],
    ['-', '-', '-', '-', '-'],
    ['#', '-', '#', '#', '-'],
    ['-', '#', '-', '-', '-']
   ]

   Source = (0, 0)
   Destination = (4, 4)
   ```

3. Call the `solve_puzzle` function with your board, source, and destination as parameters:
   ```python
   print(Puzzle.solve_puzzle(Puzzle, Source, Destination))
   ```

This will print the shortest path and the necessary movements to get from the source to the destination. If no path is found, it will print `None`.

## Complexity

The time complexity of the `solve_puzzle` function is O(MxN), where M and N are the dimensions of the board. This is because in the worst case, the BFS algorithm will traverse through every cell on the board. The space complexity is also O(MxN) as it involves storage of the board and the visited matrix.

## Contact

For any queries or further discussion, feel free to get in touch via GitHub.
