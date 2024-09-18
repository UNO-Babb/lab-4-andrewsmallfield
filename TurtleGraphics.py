#TurtleGraphics.py
#Name: Andrew Smallfield
#Date: 9/18/24
#Assignment: Turtle Graphics

import turtle 
hideturtle() 

def drawSquare(myTurtle, size):
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)


def drawPolygon(myTurtle, sides):
    for i in range(sides):
        myTurtle.forward(50)
        myTurtle.right(360/sides)



def fillCorner(myTurtle, Corner):
    drawSquare(myTurtle, 100) #Square size 100)
    
    if Corner==1:
        myTurtle.goto(0,0)
        myTurtle.begin_fill()
        drawSquare(myTurtle, 50)
        myTurtle.end_fill()
        
    if Corner==2:
        myTurtle.goto(50,0)
        myTurtle.begin_fill()
        drawSquare(myTurtle, 50)
        myTurtle.end_fill()
        
    if Corner==3:
        myTurtle.goto(0,-50)
        myTurtle.begin_fill()
        drawSquare(myTurtle, 50)
        myTurtle.end_fill()
        
    if Corner==4:
        myTurtle.up()
        myTurtle.goto(50,-50)
        myTurtle.down()
        myTurtle.begin_fill()
        drawSquare(myTurtle, 50)
        myTurtle.end_fill()

    if Corner== 5:
        myTurtle.begin_fill()
        drawSquare(myTurtle, 100)
        myTurtle.end_fill()



def squaresInSquares(myTurtle, num):
    size = 10
    for i in range(num):
        drawSquare(myTurtle, size)
        myTurtle.up()
        myTurtle.left(90)
        myTurtle.forward(10)
        myTurtle.left(90)
        myTurtle.forward(10)
        myTurtle.left(180)
        myTurtle.down()
        size = size + 20
        

def main():
    myTurtle = turtle.Turtle()

    #drawSquare(myTurtle, 100) #draws a square

    #drawPolygon(myTurtle, 5) #draws a pentagon
    #drawPolygon(myTurtle, 8) #draws an octogon

    #fillCorner(myTurtle, 2) #draws a square with top right corner filled in.
    #fillCorner(myTurtle, 3) #draws a square bottom left corner filled in.

    #squaresInSquares(myTurtle, 5) #draws 5 concentric squares
    #squaresInSquares(myTurtle, 3) #draws 3 concentric squares


main()
