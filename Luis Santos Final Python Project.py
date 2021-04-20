from graphics import*
import random
import math
win = GraphWin("Find the Hole", 300, 300) 
win.setBackground("black")

x = 0  
y = 0
radius = 0

def hole():
    circle = Circle(Point(x, y), radius)
    circle.setOutline("white")
    circle.draw(win)

def rectangle():
    rectangle = Rectangle(Point(50,200),Point(250, 150))
    rectangle.setFill("black")
    rectangle.setOutline("silver")
    rectangle.draw(win)
    text = Text(Point(150,165), "You win!")
    text.setTextColor("silver")
    text.draw(win)
    text2 = Text(Point(150,185), "Guesses: " + str(guesses))
    text2.setTextColor("silver")
    text2.draw(win)
    
def play():
    global guesses
    global x
    global y
    global radius
    x = random.randrange(0,300)
    y = random.randrange(0,300)
    radius = random.randrange(20,40)
    guesses = 0
    rectangle2 = Rectangle(Point(0,0), Point(300,300))
    rectangle2.setFill("black")
    rectangle2.draw(win)
    while True:
        click = win.getMouse()
        click.setOutline(color_rgb(random.randrange(100, 255), random.randrange(100, 255), random.randrange(100,255)))
        click.draw(win)
        guesses += 1
        if radius >= math.sqrt((x-click.getX())**2 + (y-click.getY())**2):
            hole()
            rectangle()
            break
play()
while True:
    rectangle3 = Rectangle(Point(75,210), Point(225, 235))
    rectangle3.setFill("black")
    rectangle3.setOutline("gold")
    rectangle3.draw(win)
    text3 = Text(Point(150, 223), "Restart?")
    text3.setTextColor("gold")
    text3.draw(win)
    click2 = win.getMouse()
    while click2.getX() < 75 or click2.getX() > 225 or click2.getY() < 210 or click2.getY() > 235:
        click2 = win.getMouse()
    play()
