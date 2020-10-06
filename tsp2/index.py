from tkinter import *
from opt_2 import *
from opt_3 import *
from nearest import *
from sa import *

size = 550

def click(event):
    # draw_point(event.x, event.y)
    points.append((event.x, event.y))

def clear():
    global points
    points = []
    c.delete("point", "good_point", "line")

root = Tk()

root.title("TSP - Visualizer [Nemanja Trifunovic br. ind.:346/2010]")
root.resizable(0,0)

c = Canvas(root, bg="white", width = size, height = size)

c.configure(cursor="crosshair")
c.pack()
c.bind("<Button-1>", click)

Button(root, text = "Clear", command = clear).pack(side = LEFT)
# Button(root, text = "Randomise", command = randomise).pack(side = LEFT)
Button(root, text = "Nearest Neighbour", command = lambda : nearest).pack(side = LEFT)
Button(root, text = "2-OPT", command = lambda : opt_2).pack(side = LEFT)
Button(root, text = "3-OPT", command = lambda : opt_3).pack(side = LEFT)

v = IntVar()
Label(root, textvariable = v).pack(side = RIGHT)
Label(root, text = "dist:").pack(side = RIGHT)

root.mainloop()