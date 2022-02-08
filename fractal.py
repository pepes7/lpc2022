""" Import the library turtle"""
import turtle

tess = turtle.Turtle()
screen = turtle.Screen()
tess.speed('fastest')

# turning the turtle to face upwards
tess.rt(-90)

# the acute ANGLE between
# the base and branch of the Y
ANGLE = 30

# function to plot a Y


def draw_fractal_tree(base, level):
    """ Requires that the level greater than 0"""
    if level > 0:
        screen.colormode(255)

        # splitting the rgb range for green
        # into equal intervals for each level
        # setting the colour according
        # to the current level
        tess.pencolor(0, 255//level, 0)

        # drawing the base
        tess.fd(base)

        tess.rt(ANGLE)

        # recursive call for
        # the right subtree
        draw_fractal_tree(0.8 * base, level-1)

        tess.pencolor(0, 255//level, 0)

        tess.lt(2 * ANGLE)

        # recursive call for
        # the left subtree
        draw_fractal_tree(0.8 * base, level-1)

        tess.pencolor(0, 255//level, 0)

        tess.rt(ANGLE)
        tess.fd(-base)


# tree of size 80 and level 7
draw_fractal_tree(80, 7)
