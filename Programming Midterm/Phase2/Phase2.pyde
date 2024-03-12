def setup():
    size(400, 400) # Set the size of canvas
    noStroke() # Disable drawing the stroke
    
def draw():
    
    fill(0) # Set color to black
    rect(60, 50,  90, 80)
    triangle(5, 70,  60, 80,  60, 130)
    triangle(60, 30,  60, 50,  80, 50)
    triangle(150, 50,  150, 30,  130, 50)
    fill(255, 255, 255, 255) # Set color to white
    ellipse(80, 80,  10, 10)
    ellipse(130, 80,  10, 10)
    triangle(5, 70,  15, 72,  15, 80)
