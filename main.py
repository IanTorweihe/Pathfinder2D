def solve_puzzle(Board, Source, Destination):
  import queue

  # Check if the Board is empty
  if not Board or not Board[0]:
    return None

  # Check if Source and Destination are the same
  if Source == Destination:
    return [Source], ''
    
  # Init matrix to track visited cells
  width = len(Board[0])
  height = len(Board)
  visited = []

  for i in range(height):
    row = []
    for j in range(width):
      if Board[i][j] == '#': # Flag blocked cells as visited
        row.append(True)
      else:
        row.append(False)
    visited.append(row)

  # Init dictionary to save all paths
  parent = {} #{(x1,y1): ((x0,y0, Direction)),...}
  # Init queue for BFS
  BFS = queue.Queue()
  # Enqueue source node and mark visited
  BFS.put(Source)
  visited[Source[0]][Source[1]] = True
  parent[Source] = (None)

  # Define directions of movement - left, down, right, up
  directions = [(0, -1, 'L'), (1, 0, 'D'), (0, 1, 'R'), (-1, 0, 'U')]

  # Flag to track found min path
  found = False

  # Final key for parent dict, if there is a path
  final_key = None
  
  # Loop while queue not empty
  while not BFS.empty() and not found:
    # Dequeue node
    curr = BFS.get()
    for direction in directions:
      nx, ny = direction[0] + curr[0], direction[1] + curr[1]
      if 0 <= nx < height and 0 <= ny < width: # Confirm inbound
        if visited[nx][ny] is True: # Adjacent node visited or blocked
          pass # Check next direction
        else: # Continue search. Write partial paths to parent dict
          visited[nx][ny] = True 
          parent[(nx,ny)] = (curr[0],curr[1],direction[2]) # Update parent dict here
          if nx == Destination[0] and ny == Destination[1]: # Found
            final_key = (nx,ny)
            found = True # Set flag
            break # Exit loop min path to destination found
          else:
            BFS.put((nx,ny)) # Enqueue
      
  if not found: # No path exists
      return None
  elif found is True: # Path exists and found. Backtrack and return result
      cells = []
      directions = ''
      curr_key = final_key
      while parent[curr_key]: # While value is Truthy backtrack and append
          curr_cell, curr_direct = curr_key, parent[curr_key][2]
          cells.append(curr_cell)
          directions += curr_direct
          curr_key = (parent[curr_key][0], parent[curr_key][1])
      cells.append(Source) # When curr val is False backtrack to src complete
      cells.reverse()
      directions = directions[::-1]
      return (cells, directions)


#TEST FUNCTION
Puzzle = [
    ['-', '-', '-', '-', '-'],
    ['-', '-', '#', '-', '-'],
    ['-', '-', '-', '-', '-'],
    ['#', '-', '#', '#', '-'],
    ['-', '#', '-', '-', '-']
]

print(solve_puzzle(Puzzle, (0,2), (2,2)))
#expected output: ([(0, 2), (0, 1), (1, 1), (2, 1), (2, 2)], 'LDDR')

print(solve_puzzle(Puzzle, (0,0), (4,4)))
#Output: ([(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 4), (2, 4), (3, 4), (4, 4)], 'RRRRDDDD')

print(solve_puzzle(Puzzle, (0,0), (4,0)))
#Output: None
    
    