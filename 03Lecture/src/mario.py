# reference: https://www.youtube.com/watch?v=idFwiKdBeU8
from turtle import *

t = Turtle()
t.speed(0)

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

# create 5 small squares on the first line
num_squares = 5
side_length = 10
colour = "red"

for num in range(num_squares):
    create_square(t, side_length, colour)

def new_row(t, side_length, num, shift):
    # TO DO: TIDY THIS CODE - NOT SURE WHAT THE BEST WAY TO WRITE THIS IS
    t.penup()
    t.right(90)
    t.forward(side_length)
    t.left(90)
    t.backward(side_length * (num + shift))
    # t.left(180) # back to starting positon
    t.pendown()
    t.penup()

# create second row
new_row(t, side_length, num_squares, shift=1)
num_squares = 10
for num in range(num_squares):
    create_square(t, side_length, colour)

# create new row
new_row(t, side_length, num_squares, shift=0)
num_squares = 3
for num in range(num_squares):
    create_square(t, side_length, colour="brown")
for num in range(num_squares):
    create_square(t, side_length, colour="#ffd987")
num_squares = 1
for num in range(num_squares):
    create_square(t, side_length, colour="black")
for num in range(num_squares):
    create_square(t, side_length, colour="#ffd987")

# create new row
num_squares = 8
new_row(t, side_length, num_squares, shift=1)

num_squares = 1
for num in range(num_squares):
    create_square(t, side_length, colour="brown")
for num in range(num_squares):
    create_square(t, side_length, colour="#ffd987")
for num in range(num_squares):
    create_square(t, side_length, colour="brown")
num_squares = 4
for num in range(num_squares):
    create_square(t, side_length, colour="#ffd987")
num_squares = 1
for num in range(num_squares):
    create_square(t, side_length, colour="black")
num_squares = 3
for num in range(num_squares):
    create_square(t, side_length, colour="#ffd987")

# create new row
num_squares = 11
new_row(t, side_length, num_squares, shift=0)
num_squares = 1
for num in range(num_squares):
    create_square(t, side_length, colour="brown")
for num in range(num_squares):
    create_square(t, side_length, colour="#ffd987")
num_squares = 2
for num in range(num_squares):
    create_square(t, side_length, colour="brown")
num_squares = 4
for num in range(num_squares):
    create_square(t, side_length, colour="#ffd987")
num_squares = 1
for num in range(num_squares):
    create_square(t, side_length, colour="black")
num_squares = 3
for num in range(num_squares):
    create_square(t, side_length, colour="#ffd987")

# new row
num_squares = 12
new_row(t, side_length, num_squares, shift=0)
num_squares = 2
for num in range(num_squares):
    create_square(t, side_length, colour="brown")
num_squares = 5
for num in range(num_squares):
    create_square(t, side_length, colour="#ffd987")
num_squares = 4
for num in range(num_squares):
    create_square(t, side_length, colour="black")

# new row
num_squares = 9
new_row(t, side_length, num_squares, shift=0)
num_squares = 8
for num in range(num_squares):
    create_square(t, side_length, colour="#ffd987")

# new row
new_row(t, side_length, num_squares, shift=1)
num_squares = 2
for num in range(num_squares):
    create_square(t, side_length, colour="red")
num_squares = 1
for num in range(num_squares):
    create_square(t, side_length, colour="blue")
num_squares = 2
for num in range(num_squares):
    create_square(t, side_length, colour="red")
num_squares = 1
for num in range(num_squares):
    create_square(t, side_length, colour="blue")
for num in range(num_squares):
    create_square(t, side_length, colour="red")

# new row
num_squares = 8
new_row(t, side_length, num_squares, shift=0)
num_squares = 3
for num in range(num_squares):
    create_square(t, side_length, colour="red")
num_squares = 1
for num in range(num_squares):
    create_square(t, side_length, colour="blue")
num_squares = 2
for num in range(num_squares):
    create_square(t, side_length, colour="red")
num_squares = 1
for num in range(num_squares):
    create_square(t, side_length, colour="blue")
num_squares = 3
for num in range(num_squares):
    create_square(t, side_length, colour="red")

# new row
num_squares = 11
new_row(t, side_length, num_squares, shift=0)
num_squares = 4
for num in range(num_squares):
    create_square(t, side_length, colour="red")
num_squares = 4
for num in range(num_squares):
    create_square(t, side_length, colour="blue")
num_squares = 4
for num in range(num_squares):
    create_square(t, side_length, colour="red")

# new row
num_squares = 12
new_row(t, side_length, num_squares, shift=0)
num_squares = 2
for num in range(num_squares):
    create_square(t, side_length, colour="#ffd987")
colour_list = ["red", "blue", "yellow", "blue", "blue",
            "yellow", "blue", "red"]
for c in colour_list:
    create_square(t, side_length, colour=c)
num_squares = 2
for num in range(num_squares):
    create_square(t, side_length, colour="#ffd987")

# new row
num_squares = 12
new_row(t, side_length, num_squares, shift=0)
num_squares = 3
for num in range(num_squares):
    create_square(t, side_length, colour="#ffd987")
num_squares = 6
for num in range(num_squares):
    create_square(t, side_length, colour="blue")
num_squares = 3
for num in range(num_squares):
    create_square(t, side_length, colour="#ffd987")

# new row
num_squares = 12
new_row(t, side_length, num_squares, shift=0)
num_squares = 2
for num in range(num_squares):
    create_square(t, side_length, colour="#ffd987")
num_squares = 8
for num in range(num_squares):
    create_square(t, side_length, colour="blue")
num_squares = 2
for num in range(num_squares):
    create_square(t, side_length, colour="#ffd987")

done()