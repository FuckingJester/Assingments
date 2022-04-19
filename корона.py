from turtle import *

color("green")
bgcolor("black")
speed(800)
hideturtle()
b = 0
while b < 200:
    right(b)
    forward(b * 3)
    b = b + 1
done()
# Task 1
a, b, c, d, e = map(int, input("Введіть ціле число:\n").split())
M = max(a, b, c, d, e)
