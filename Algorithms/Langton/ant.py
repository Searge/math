import turtle as t


def sqr(color):
    t.pendown()
    t.color(color)
    for _ in range(4):
        t.forward(10)
        t.right(90)
    t.penup()


sqr("red")

