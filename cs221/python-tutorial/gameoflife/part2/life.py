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
    # YOUR CODE HERE
    
  def isAlive(self, row, col):
    # YOUR CODE HERE
  
  def setAlive(self, row, col, tf):
    # YOUR CODE HERE
    
  def getNumRows(self):
    # YOUR CODE HERE
    
  def getNumCols(self):
    # YOUR CODE HERE
    
  def runTimeStep(self):
    # YOUR CODE HERE
