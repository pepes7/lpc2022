""" Import the library turtle"""
import turtle


# Screen() method to get screen
screen = turtle.Screen()

# creating tess object
tess = turtle.Turtle()


def triangle(x_axis, y_axis):
    """ it is used to draw out the pen"""
    tess.penup()

    # it is used to move cursor at x_axis
    # and y_axis position
    tess.goto(x_axis, y_axis)

    # it is used to draw in the pen
    tess.pendown()
    for _ in range(3):

        # move cursor 100 unit
        # digit forward
        tess.forward(100)

        # turn cursor 120 degree left
        tess.left(120)

        # Again,move cursor 100 unit
        # digit forward
        tess.forward(100)


# special built in function to send current
# position of cursor to triangle
screen.onscreenclick(triangle, 1)
screen.listen()

# hold the screen
turtle.done()
