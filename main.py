import turtle as t
import random as r

t.colormode(255)
drawer = t.Turtle()
screen = t.Screen()
drawer.speed("fastest")


def random_color():
    red = r.randint(0, 255)
    g = r.randint(0, 255)
    b = r.randint(0, 255)
    drawer.pencolor(red, g, b)


def draw_spirograph(tilt_angle):
    for _ in range(int(360/tilt_angle)):
        drawer.width(1)
        current_heading = drawer.heading()
        random_color()
        drawer.circle(100)
        drawer.setheading(current_heading + tilt_angle)


draw_spirograph(10)
screen.exitonclick()
