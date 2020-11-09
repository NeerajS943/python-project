import tkinter as tk
from random import randint
from random import shuffle
win = tk.Tk()
canvas = tk.Canvas(win, width = 500, height = 500)
canvas.pack()
class Tile(object):
    def __init__(self, x, y, text):
        self.y = y
        self.x = x
        self.text = text
    def drawFaceDown(self):
        canvas.create_rectangle(self.x, self.y, self.x + 70, self.y + 70, fill = "gray")
        self.isFaceUp = False
    def drawFaceUp(self):
        canvas.create_rectangle(self.x, self.y, self.x + 70, self.y + 70, fill = "gray")
        canvas.create_text(self.x + 35, self.y + 35, text = self.text, width = 70,font="Times 12 bold italic")
        self.isFaceUp = True
    def isUnderMouse(self, event):
        if(event.x > self.x and event.x < self.x + 70):
            if(event.y > self.y and event.y < self.y + 70):
                return True

tiles = []
colors = [
    "Red",
    "Orange",
    "Yellow",
    "Green",
    "Blue",
    "Purple",
    "Pink",
    "Brown",
    "Black",
    "Gray",
    "Magenta"
]

selected = []
for i in range(10):
    randomInd = randint(0, len(colors) - 1)
    color = colors[randomInd]
    selected.append(color)
    selected.append(color)
    del colors[randomInd]
shuffle(selected)
canvas.create_rectangle( 300,400,400,500,fill="gray")
canvas.create_text(350,450, text="Score",fill="black", font="Times 28 bold italic")
canvas.create_rectangle(400,400,500,500, fill="gray")
canvas.create_text(450,450, text="0",fill="black", font="Times 28 bold italic")

score = 0
def checkTiles():
    global score
    if(flippedTiles[-1].text == flippedTiles[-2].text):
        score += 1
        canvas.create_rectangle(400,400,500,500, fill="gray")
        canvas.create_text(450,450, text=score,fill="black", font="Times 28 bold italic")
    else:
        flippedTiles[-1].drawFaceDown() 
        flippedTiles[-2].drawFaceDown()
       
NUM_COLS = 5
NUM_ROWS = 4

for x in range(0,NUM_COLS):
    for y in range(0,NUM_ROWS):
            tiles.append(Tile(x * 78 + 10, y * 78 + 40, selected.pop()))

for i in range(len(tiles)):
    tiles[i].drawFaceDown()

flippedThisTurn = 0
flippedTiles=[]
def mouseClicked(event):
    global flippedTiles
    global flippedThisTurn
    for tile in tiles:
        if tile.isUnderMouse(event):
            if (not(tile.isFaceUp)) :
                tile.drawFaceUp()
                flippedTiles.append(tile)
                flippedThisTurn += 1

            if (flippedThisTurn == 2):
                win.after(1000, checkTiles)               
                flippedThisTurn = 0


win.bind("<Button-1>", mouseClicked)