import time
from turtle import Turtle, Screen
from random import randint

SIZE: int = 15
SPEED: int = 2
TOPLEFTX = TOPLEFTY = 115

# Position the Ant
ANT_ROW: int = randint(5, 10)
ANT_COL: int = randint(5, 10)
ANT_DIRECTION: int = randint(0, 3) * 90


def main():

    global SIZE, SPEED
    global ANT_ROW, ANT_COL, ANT_DIRECTION
    # the width of each square on the grid
    grid_dimension: int = 25

    grid = emptyGrid()

    # Start animating the grid
    while SIZE > ANT_ROW >= 0 and SIZE > ANT_COL >= 0:
        # Change the direction of the ant based on
        # the colour of the cell it's on
        if grid[ANT_ROW][ANT_COL] == 0:
            ANT_DIRECTION -= 90
            if ANT_DIRECTION < 0:
                ANT_DIRECTION += 360
        else:
            ANT_DIRECTION += 90
            if ANT_DIRECTION >= 360:
                ANT_DIRECTION -= 360

        draw_grid(grid, grid_dimension)

        myPen.getscreen().update()
        time.sleep(1 / SPEED)

        # Apply Langton's Ant rules
        # Change the colour of the cell the ant was on
        if grid[ANT_ROW][ANT_COL] == 0:
            grid[ANT_ROW][ANT_COL] = 1
        else:
            grid[ANT_ROW][ANT_COL] = 0

        # Move ant by 1 cell in the new direction
        if ANT_DIRECTION == 0:
            ANT_COL += 1
        elif ANT_DIRECTION == 90:
            ANT_ROW -= 1
        elif ANT_DIRECTION == 180:
            ANT_COL -= 1
        elif ANT_DIRECTION == 270:
            ANT_ROW += 1


myPen = Turtle()
myPen.shape('turtle')
myPen.speed(0)
myPen.color("grey")
myPen.pencolor("grey")


def draw_grid(grid: list, dim: int):
    global SIZE
    global ANT_ROW, ANT_COL, ANT_DIRECTION

    myPen.clear()

    # myPen.setpos(0, 0)
    for i in range(SIZE + 1):
        myPen.penup()
        myPen.goto(TOPLEFTX,
                   TOPLEFTY - i * dim)
        myPen.pendown()
        myPen.goto(TOPLEFTX + SIZE * dim,
                   TOPLEFTY - i * dim)

    for i in range(SIZE + 1):
        myPen.penup()
        myPen.goto(TOPLEFTX + i * dim,
                   TOPLEFTY)
        myPen.pendown()
        myPen.goto(TOPLEFTX + i * dim,
                   TOPLEFTY - SIZE * dim)

    for i in range(SIZE):
        myPen.penup()
        myPen.goto(TOPLEFTX + i * dim + 10,
                   TOPLEFTY + 10)
        myPen.write(chr(65 + i))

    for i in range(1, SIZE + 1):
        myPen.penup()
        myPen.goto(TOPLEFTX - 15,
                   TOPLEFTY - i * dim + 10)
        myPen.write(str(i))

    myPen.setheading(0)
    myPen.goto(TOPLEFTX, TOPLEFTY - dim)

    for row in range(SIZE):
        for col in range(SIZE):
            if grid[row][col] > 0:
                box(dim)
            myPen.penup()

            if row == ANT_ROW and col == ANT_COL:
                myPen.color("red")
                x = myPen.xcor()
                y = myPen.ycor()
                myPen.goto(x+12, y+12)
                myPen.setheading(ANT_DIRECTION)
                myPen.stamp()
                myPen.goto(x, y)
                myPen.color("black")
                myPen.setheading(0)

            myPen.forward(dim)
            myPen.pendown()

        myPen.setheading(270)
        myPen.penup()
        myPen.forward(dim)
        myPen.setheading(180)
        myPen.forward(dim * SIZE)
        myPen.setheading(0)
        myPen.pendown()


def box(dim):
    myPen.begin_fill()

    for _ in range(3):
        myPen.forward(dim)
        myPen.left(90)
    myPen.forward(dim)

    myPen.end_fill()
    myPen.setheading(0)


def randomGrid():
    """
    Randomely populate the grid
    """
    global SIZE
    grid = list()
    for row in range(SIZE):
        grid.append([])
        for col in range(SIZE):
            grid[row].append(randint(0, 1))
    return grid


def emptyGrid():
    """
    Create an empty grid
    """
    global SIZE
    grid = list()
    for row in range(SIZE):
        grid.append([])
        for col in range(SIZE):
            grid[row].append(0)
    return grid


if __name__ == "__main__":
    screen = Screen()
    screen.tracer(0)  # is instance of Screen, not Turtle
    main()
    screen.exitonclick()
