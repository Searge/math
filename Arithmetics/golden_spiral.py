import turtle

a, b = 0, 1

while b <= 13:
    a, b = b, a + b
    turtle.goto(a, b)
