from turtle import *

t = Turtle()
# changes the speed of the cursor
t.speed(0)

# position the cursor
t.penup()
# define the x, y coordinates
t.goto(-200, -100)
t.pendown()

side_length = 30


# create a square
def create_square(t, side_length, colour):
    """This is a function that creates a square"""
    t.color(colour)
    t.begin_fill()
    for num in range(4):
        t.forward(side_length)
        t.right(90)
    t.end_fill()
    # add this to move the cursor to place a square next to it
    t.forward(side_length)

def new_row(t, side_length, colours_list):
    """This is a function that creates a new row"""
    t.penup()
    t.left(90)
    t.forward(side_length)
    t.left(90)
    t.forward(side_length * (len(colours_list)))
    # t.forward(side_length * (len(colours_list)-1))
    t.right(180) # back to the starting point
    t.pendown()

# specify the number of rows you want to create
number_rows = 10
# specify the colours you want your squares to have
colours_list = ["red", "blue", "orange", "pink", "yellow"]

# declare i and the number of iterations for your while loop
i = 0
number_iterations = len(colours_list) * number_rows

while i < number_iterations:
    for c in colours_list:
        # when i reaches the length of the colours list create a new row
        if i % len(colours_list) == 0:
            new_row(t, side_length, colours_list)
        create_square(t, side_length, c)
        i += 1

# view the turtle screen
done()
