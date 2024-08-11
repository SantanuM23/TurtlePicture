# from turtle import Turtle, Screen
import random
import turtle as t

tim = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

# Draw Random Walk
# directions = [0, 90, 180, 270]
#
#
# tim.pensize(10)
tim.speed("fastest")
# for _ in range(200):
#     tim.color(random_color())
#     tim.forward(20)
#     tim.setheading(random.choice(directions))


# Draw Multiple Shapes
# for l in range(3, 9):
#     angle = 360/l
#     for _ in range(l):
#         tim.forward(100)
#         tim.right(angle)

separate = 1
for _ in range(int(360/separate)):
    tim.color(random_color())
    tim.circle(100)
    tim.setheading(tim.heading() + separate)


screen = t.Screen()
screen.exitonclick()
