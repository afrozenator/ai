import util

# life.py
# Jeff Jacobs, CS221


def getEmptyBoard(num_rows, num_cols):
  return [[{} for x in range(num_rows)] for y in range(num_cols)]

def duplicateBoard(source, destination, num_rows, num_cols):
  for r in range(num_rows):
    for c in range(num_cols):
      if source[r][c]['alive']:
        destination[r][c]['alive'] = True
      else:
        destination[r][c]['alive'] = False

class Life:
  
  # THE RULES:
  #
  # Any live cell with fewer than two live neighbours dies, as if caused by under-population.
  # Any live cell with two or three live neighbours lives on to the next generation.
  # Any live cell with more than three live neighbours dies, as if by overcrowding.
  # Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

  def __init__(self, board):
    # YOUR CODE HERE
    self.num_rows = len(board)
    self.num_cols = len(board[0])
    # First initialize to all empty dict.
    self.board = getEmptyBoard(self.num_rows, self.num_cols)
    duplicateBoard(board, self.board, self.num_rows, self.num_cols)

  def isAlive(self, row, col):
    # YOUR CODE HERE
    return self.board[row][col]['alive']
  
  def setAlive(self, row, col, tf):
    # YOUR CODE HERE
    self.board[row][col]['alive'] = tf
    
  def getNumRows(self):
    # YOUR CODE HERE
    return self.num_rows
    
  def getNumCols(self):
    # YOUR CODE HERE
    return self.num_cols
    
  def runTimeStep(self):
    # YOUR CODE HERE
    tmp_board = getEmptyBoard(self.num_rows, self.num_cols)
    duplicateBoard(self.board, tmp_board, self.num_rows, self.num_cols)
    for r in range(self.num_rows):
      for c in range(self.num_cols):
        # Get the number of live neighbours
        neighboursAlive = self.numAlive(self.getNeighbours(r, c))
        if self.isAlive(r, c):
          if neighboursAlive < 2:
            tmp_board[r][c]['alive'] = False
          elif neighboursAlive == 2 or neighboursAlive == 3:
            tmp_board[r][c]['alive'] = True
          elif neighboursAlive > 3:
            tmp_board[r][c]['alive'] = False
        elif neighboursAlive == 3:
            tmp_board[r][c]['alive'] = True
    duplicateBoard(tmp_board, self.board, self.num_rows, self.num_cols)

  def numAlive(self, lst):
    num = 0
    for n in lst:
      if self.isAlive(n[0], n[1]):
        num = num + 1
    return num

  def satisfiesBounds(self, row, col):
    return (0 <= row) and (row < self.num_rows) and (0 <= col) and (col < self.num_cols)
  
  def getNeighbours(self, row, col):
   neighbours = []
   if self.satisfiesBounds(row - 1, col):
     neighbours.append((row - 1, col))
   if self.satisfiesBounds(row + 1, col):
     neighbours.append((row + 1, col))
   if self.satisfiesBounds(row, col - 1):
     neighbours.append((row, col - 1))
   if self.satisfiesBounds(row, col + 1):
     neighbours.append((row, col + 1))
   if self.satisfiesBounds(row - 1, col - 1):
     neighbours.append((row - 1, col - 1))
   if self.satisfiesBounds(row - 1, col + 1):
     neighbours.append((row - 1, col + 1))
   if self.satisfiesBounds(row + 1, col - 1):
     neighbours.append((row + 1, col - 1))
   if self.satisfiesBounds(row + 1, col + 1):
     neighbours.append((row + 1, col + 1))
   return neighbours
