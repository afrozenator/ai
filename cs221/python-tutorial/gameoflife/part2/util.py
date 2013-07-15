import cell

# util.py
# Jeff Jacobs, for CS221

def loadBoard(filename):
  with open("board.csv") as f:
      content = f.readlines()
      
  rows = len(content)
  cols = len(content[0].strip().split(","))
  board = [[None for x in range(rows)] for y in range(cols)]

  for r in range(rows):
    curRow = content[r].strip().split(",")
    for c in range(cols):
      curCellInt = int(curRow[c])
      if curCellInt == 0:
        board[r][c] = cell.Cell(False)
      else:
        board[r][c] = cell.Cell(True)
  return board

def printBoard(life):
  board = ""
  for i in range(life.getNumRows()):
    for j in range(life.getNumCols()):
      board = board + str(life.isAlive(i,j))
    board = board + "\n"
  print board
  
def createEmptyGrid(rows, cols):
  newGrid = [[cell.Cell(False) for x in range(rows)] for y in range(cols)]
  return newGrid
  
def getNumLiveNeighbors(life, row, col):
  numLive = 0
  # Look left
  if row >= 1:
    if life.isAlive(row - 1, col):
      numLive = numLive + 1
  # Look right
  if row <= (life.getNumRows() - 2):
    if life.isAlive(row + 1, col):
      numLive = numLive + 1
  # Look up
  if col >= 1:
    if life.isAlive(row, col - 1):
      numLive = numLive + 1
  # Look down
  if col <= (life.getNumCols() - 2):
    if life.isAlive(row, col + 1):
      numLive = numLive + 1
  # Look up and left
  if row >= 1 and col >= 1:
    if life.isAlive(row - 1, col - 1):
      numLive = numLive + 1
  # Look up and right
  if row >= 1 and col <= (life.getNumCols() - 2):
    if life.isAlive(row - 1, col + 1):
      numLive = numLive + 1
  # Look down and left
  if row <= (life.getNumRows() - 2) and col >= 1:
    if life.isAlive(row + 1, col - 1):
      numLive = numLive + 1
  # Look down and right
  if row <= (life.getNumRows() - 2) and col <= (life.getNumCols() - 2):
    if life.isAlive(row + 1, col + 1):
      numLive = numLive + 1
  return numLive