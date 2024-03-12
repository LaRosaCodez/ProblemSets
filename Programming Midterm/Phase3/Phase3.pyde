def setup():
    size(400, 400) # Set the size of canvas
    noStroke() # Disable drawing the stroke
    
def drawObject(x, y, s):
    pushMatrix()
    
    offset = -10 # Offset for even tiling
    y += offset
    
    translate(x,y) # Set parameters
    scale(s)
    
    fill(0) # Set color to black
    rect(x+60, y+50,  90, 80)
    triangle(x+5, y+70,  x+60, y+80,  x+60, y+130)
    triangle(x+60, y+30,  x+60, y+50,  x+80, y+50)
    triangle(x+150, y+50,  x+150, y+30,  x+130, y+50)
    fill(255, 255, 255, 255) # Set color to white
    ellipse(x+80, y+80,  10, 10)
    ellipse(x+130, y+80,  10, 10)
    triangle(x+5, y+70,  x+15, y+72,  x+15, y+80)
    
    popMatrix()
    
def draw():
    drawObject(0, 0, 1)
    drawObject(10, 10, 1)
