# MoralesJohnLab04b.py
# John Morales
# Class: CSCI 1411-001
# Due Date: June 20, 2023

from graphics import *
import time


def main():
    winName = "Lab 4 - MoralesJohn"
    win = GraphWin(winName, 500, 500)

    color1 = input("What color would you like the circle to be? ")
    x1, y1 = eval(
        input("Please enter the x and y coordinates for the center of the cirlce:")
    )
    radius1 = eval(input("What radius would you like: "))

    center1 = Point(x1, y1)
    circ1 = Circle(center1, radius1)
    circ1.setFill(color1)
    circ1.draw(win)

    color2 = "green"
    radius2 = radius1 / 2
    center2 = Point(x1, (y1 - (2 * radius1)))
    circ2 = Circle(center2, radius2)
    circ2.setFill(color2)
    circ2.draw(win)

    line = Line(center1, center2)
    line.setFill("red")
    line.draw(win)

    p1 = win.getMouse()
    circ2.undraw()
    line.undraw()
    p1 = Point((x1 + (2 * radius1)), y1)
    circ2 = Circle(p1, radius2)
    circ2.setFill(color2)
    circ2.draw(win)
    line = Line(center1, p1)
    line.setFill("red")
    line.draw(win)

    p2 = win.getMouse()
    circ2.undraw()
    line.undraw()
    p2 = Point(x1, (y1 + (2 * radius1)))
    circ2 = Circle(p2, radius2)
    circ2.setFill(color2)
    circ2.draw(win)
    line = Line(center1, p2)
    line.setFill("red")
    line.draw(win)

    p3 = win.getMouse()
    circ2.undraw()
    line.undraw()
    p3 = Point((x1 - (2 * radius1)), y1)
    circ2 = Circle(p3, radius2)
    circ2.setFill(color2)
    circ2.draw(win)
    line = Line(center1, p3)
    line.setFill("red")
    line.draw(win)

    p4 = win.getMouse()
    circ2.undraw()
    line.undraw()
    center2 = Point(x1, (y1 - (2 * radius1)))
    circ2 = Circle(center2, radius2)
    circ2.setFill(color2)
    circ2.draw(win)

    line = Line(center1, center2)
    line.setFill("red")
    line.draw(win)
