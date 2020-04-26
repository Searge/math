import time
import turtle as t
from random import randint

SIZE = 15
SPEED = 2
TOPLEFTX = 180
TOPLEFTY = 180

myPen = t.Turtle()
myPen.shape('turtle')
myPen.tracer(0)  # (!)
myPen.speed(0)
myPen.color("black")


def main():
    screen = t.Screen()
    sqr("red")
    screen.exitonclick()


def draw_grid(grid, dim: int):
    global SIZE
    global ant_row, ant_col, ant_direction

    myPen.clear()
    for i in range(0, SIZE + 1):
        myPen.penup()
        myPen.goto(TOPLEFTX,
                   TOPLEFTY - i * dim)
        myPen.pendown()
        myPen.goto(TOPLEFTX + SIZE * dim,
                   TOPLEFTY - i * dim)

    for i in range(0, SIZE + 1):
        myPen.penup()
        myPen.goto(TOPLEFTX + i * dim,
                   TOPLEFTY)
        myPen.pendown()
        myPen.goto(TOPLEFTX + i * dim,
                   TOPLEFTY-SIZE*dim)

    for i in range(0, SIZE):
        myPen.penup()
        myPen.goto(TOPLEFTX + i * dim + 10,
                   TOPLEFTY + 10)
        myPen.write(chr(65 + i))

    for i in range(1, SIZE + 1):
        myPen.penup()
        myPen.goto(TOPLEFTX - 15,
                   TOPLEFTY - i * dim + 10)
        myPen.write(str(i))


def sqr(color):
    t.pendown()
    t.color(color)
    for _ in range(4):
        t.forward(10)
        t.right(90)
    t.penup()


if __name__ == "__main__":
    main()
