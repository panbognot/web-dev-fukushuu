# Conway's Game of Life
import random, time, copy
WIDTH = 60
HEIGHT = 20


# Function to count the living neightbors based on the input cells and XY coordinates
def countLivingNeighbors(inputCells, inX, inY):
  # Count number of living neighbors:
  neighbors = 0
  global WIDTH
  global HEIGHT
  
  # Get neigboring coordinates:
  # `% WIDTH` ensures leftCoord is always between 0 and WIDTH - 1
  leftCoord = (inX - 1) % WIDTH
  rightCoord = (inX + 1) % WIDTH
  aboveCoord = (inY - 1) % HEIGHT
  belowCoord = (inY + 1) % HEIGHT
  
  if inputCells[leftCoord][aboveCoord] == '#':
    neighbors += 1    # Top-left neighbor is alive
  if inputCells[inX][aboveCoord] == '#':
    neighbors += 1    # Top neighbor is alive  
  if inputCells[rightCoord][aboveCoord] == '#':
    neighbors += 1    # Top-right neighbor is alive
  if inputCells[leftCoord][inY] == '#':
    neighbors += 1    # Left neighbor is alive
  if inputCells[rightCoord][inY] == '#':
    neighbors += 1    # Right neighbor is alive
  if inputCells[leftCoord][belowCoord] == '#':
    neighbors += 1    # Bottom-left neighbor is alive
  if inputCells[inX][belowCoord] == '#':
    neighbors += 1    # Bottom neighbor is alive
  if inputCells[rightCoord][belowCoord] == '#':
    neighbors += 1    # Bottom-right neighbor is alivve

  return neighbors


# Create a list of list for the cells:
nextCells = []
for x in range(WIDTH):
  column = []   # Create a new column.
  for y in range(HEIGHT):
    if random.randint(0, 1) == 0:
      column.append('#')  # Add a living cell.
    else:
      column.append(' ')  # Add a dead cell
  nextCells.append(column)  # nextCells is a list of column lists.


while True:   # Main program loop
  print('\n\n\n\n\n')   # Separate each step with newlines.
  currentCells = copy.deepcopy(nextCells)

  # Print currentCells on the screen:
  for y in range(HEIGHT):
    for x in range(WIDTH):
      print(currentCells[x][y], end='')   # Print the # or space.
    print()   # Print a newline at the end of the row.

  # Calculate the next step's cells based on current step's cells:
  for x in range(WIDTH):
    for y in range(HEIGHT):
      # Count number of living neighbors:
      numNeighbors = countLivingNeighbors(currentCells, x, y)

      # Set cell based on Conway's Game of Life rules:
      if currentCells[x][y] == '#' and (numNeighbors == 2 or numNeighbors == 3):
        # Living cells with 2 or 3 neighbors stay alive:
        nextCells[x][y] = '#'
      elif currentCells[x][y] == ' ' and numNeighbors == 3:
        # Dead cells with 3 neighbors become alive:
        nextCells[x][y] = '#'
      else:
        # Everything else dies or stays dead:
        nextCells[x][y] = ' '

  time.sleep(1)   # Add a 1-second pause to reduce flickering.