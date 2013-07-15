import util, cell

# life.py
# Jeff Jacobs, CS221

class Life:
  
  # THE RULES:
  #
  # Any live cell with fewer than two live neighbours dies, as if caused by under-population.
  # Any live cell with two or three live neighbours lives on to the next generation.
  # Any live cell with more than three live neighbours dies, as if by overcrowding.
  # Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

  def __init__(self, board):
    self.num_rows = len(board)
    self.num_cols = len(board[0])
    self.board = util.createEmptyGrid(self.num_rows, self.num_cols)
    for r in range(self.num_rows):
      for c in range(self.num_cols):
        if board[r][c].isAlive():
          self.board[r][c].setAlive(True)
    
  def isAlive(self, row, col):
    return self.board[row][col].isAlive()
  
  def setAlive(self, row, col, tf):
    return self.board[row][col].setAlive(tf)
    
  def getNumRows(self):
    return self.num_rows
    
  def getNumCols(self):
    return self.num_cols
    
  def runTimeStep(self):
    tmp_board = util.createEmptyGrid(self.num_rows, self.num_cols)
    for r in range(self.num_rows):
      for c in range(self.num_cols):
        tmp_board[r][c].setAlive(self.board[r][c].isAlive())

    for r in range(self.num_rows):
      for c in range(self.num_cols):
        numLiveNeighbours = util.getNumLiveNeighbors(self, r, c) 
        if self.board[r][c].isAlive():
          if numLiveNeighbours < 2:
            tmp_board[r][c].setAlive(False)
          elif numLiveNeighbours == 2 or numLiveNeighbours == 3:
            tmp_board[r][c].setAlive(True)
          else: 
            tmp_board[r][c].setAlive(False)
        elif numLiveNeighbours == 3:
            tmp_board[r][c].setAlive(True)

    self.board = tmp_board
