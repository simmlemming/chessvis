from board import Board
from graphics import *

win = GraphWin("Chess visualizer 5000", Board.size, Board.size)
b = Board()
b.draw(win)

win.mainloop()

