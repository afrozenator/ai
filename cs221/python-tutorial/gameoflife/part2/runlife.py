import Tkinter, sys, life, util

# runlife.py
# Jeff Jacobs, for CS221

boardFile = sys.argv[1]

game = life.Life(util.loadBoard(boardFile))

root = Tkinter.Tk()

cells = [[0 for x in range(game.getNumRows())] for y in range(game.getNumCols())]

for r in range(game.getNumRows()):
  for c in range(game.getNumCols()):
    alive = game.isAlive(r,c)
    color = ""
    if alive:
      color = "white"
    else:
      color = "black"
    cells[r][c] = Tkinter.Canvas(root, background=color, width=12, height=12, borderwidth=0)
    cells[r][c].grid(row=r,column=c)
            
def animate():
  updateBoard()
  game.runTimeStep()
  root.after(500, animate)
  
def updateBoard():
  for r in range(game.getNumRows()):
    for c in range(game.getNumCols()):
        alive = game.isAlive(r,c)
        color = ""
        if alive:
          color = "white"
        else:
          color = "black"
        cells[r][c].configure(background=color)
  
animate()
root.mainloop()