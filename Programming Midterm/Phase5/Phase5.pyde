def setup():
    size(500, 500) # Set the size of canvas
    
def drawObject(x, y, angle):
    rotate(radians(angle))
    fill(0)
    rect(x+60, y+50-25,  90, 80)
    triangle(x+5, y+70-25,  x+60, y+80-25,  x+60, y+130-25)
    triangle(x+60, y+30-25,  x+60, y+50-25,  x+80, y+50-25)  
    triangle(x+150, y+50-25,  x+150, y+30-25,  x+130, y+50-25)
    fill(255, 255, 255, 255) # Set color to white
    ellipse(x+80, y+80-25,  10, 10)
    ellipse(x+130, y+80-25,  10, 10)
    triangle(x+5, y+70-25,  x+15, y+72-25,  x+15, y+80-25)
    
def draw():
    background(100, 100, 100)
    scale(.25)
    columns = 10
    columnwidth = width/columns + columns + 10 * columns
    rows = 10
    rowheight = height/rows + rows + 5 * rows
    angle = frameCount / 10
    for r in range(rows):
        for c in range(columns):
            drawObject(c * columnwidth, r * rowheight, angle)
