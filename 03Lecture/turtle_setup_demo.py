from turtle import *

color('blue', 'pink')
begin_fill()

while True:
    forward(200)
    left(170)
    print(pos())
    if abs(pos()) < 1:
        break

end_fill()
done()