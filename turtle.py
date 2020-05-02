import turtle


trute = turtle.Turtle()
trute.speed(40)


def square():
    trute.forward(100)
    trute.right(90)
    trute.forward(100)
    trute.right(90)
    trute.forward(100)
    trute.right(90)
    trute.forward(100)


elephant_weight = 3000
ant_weight = 0.1

for count in range(4):
    square()


