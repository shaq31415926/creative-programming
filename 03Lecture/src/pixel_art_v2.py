# reference:
# https://www.youtube.com/watch?v=ZA4SnBWoA5Q

from turtle import *

t = Turtle()
t.speed(0) # fast speed

# position the cursor
t.penup()
# define the x and y coordinates
t.goto(-200,-100)
t.pendown()

# creates a line
# t.forward(100)

# create a variable that will adjust the size of the shapes

side = 30

# create a square - test before continuing
def square(colour):
    # t.color("blue")
    t.color(colour)
    t.begin_fill()
    # loops over 4 times
    for num in range(4):
        t.forward(side)
        t.rt(90)
    t.end_fill()
    # add so that if we create another square it is placed next to the first square
    t.forward(side)

# specify colours between the squares
# square("blue")
# square("red")
# square("yellow")
# square("blue")
# square("red")
# square("yellow")

# position the cursor so we can place the blocks on top of each other
def new_row():
    t.penup()
    t.left(90)
    t.forward(side)
    t.left(90)
    t.forward(side * (len(colours)-1))
    t.right(180) # back to starting positon
    t.pendown()

colours = ["red", "yellow", "green", "#00FFFF", "purple", "orange"]
number_iterations = 10 * len(colours)
i = 0

while i < number_iterations:
    for c in colours:
        # if i is a multiple of the number of columns then create a new row
        if i % len(colours) == 0:
            new_row()
        square(c)
        i += 1


# TODO: CODE TO FLIP THE PIXELS

def test():
    t.penup()
    t.right(90)
    t.forward(side)
    t.left(90)
    t.backward(side * (len(colours)-1))
    # t.left(180) # back to starting positon
    t.pendown()
    t.penup()

i = 0
while i < len(colours) - 1:
    for c in colours[::-1]:
        square(c)
    test()
    i += 1


# add to code to view turtle screen
done()