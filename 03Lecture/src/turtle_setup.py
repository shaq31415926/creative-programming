# reference: https://docs.python.org/3/library/turtle.html

from turtle import *

color('red', 'yellow')
begin_fill()

forward(200)
left(170)

while True:
    forward(200)
    left(170)
    print(pos())
    if abs(pos()) < 1:
        break

end_fill()
done()