"""Python program for Plotting Fibonacci
 spiral fractal using Turtle"""
import turtle
import math


def draw_fibo(number):
    """Declare auxiliary variables to draw"""
    aux_one = 0
    aux_two = 1
    square_a = aux_one
    square_b = aux_two

    x.pencolor("blue")

    # Drawing the first square
    x.forward(aux_two * FACTOR)
    x.left(90)
    x.forward(aux_two * FACTOR)
    x.left(90)
    x.forward(aux_two * FACTOR)
    x.left(90)
    x.forward(aux_two * FACTOR)

    # Proceeding in the Fibonacci Series
    temp = square_b
    square_b = square_b + square_a
    square_a = temp

    # Drawing the rest of the squares
    for _ in range(1, number):
        x.backward(square_a * FACTOR)
        x.right(90)
        x.forward(square_b * FACTOR)
        x.left(90)
        x.forward(square_b * FACTOR)
        x.left(90)
        x.forward(square_b * FACTOR)

        # Proceeding in the Fibonacci Series
        temp = square_b
        square_b = square_b + square_a
        square_a = temp

    # Bringing the pen to starting point of the spiral plot
    x.penup()
    x.setposition(FACTOR, 0)
    x.seth(0)
    x.pendown()

    # Setting the colour of the plotting pen to red
    x.pencolor("red")

    # Fibonacci Spiral Plot
    x.left(90)
    for _ in range(number):
        print(aux_two)
        fdwd = math.pi * aux_two * FACTOR / 2
        fdwd /= 90
        for _ in range(90):
            x.forward(fdwd)
            x.left(1)
        temp = aux_one
        aux_one = aux_two
        aux_two = temp + aux_two


# Here 'factor' signifies the multiplicative
# factor which expands or shrinks the scale
# of the plot by a certain factor.
FACTOR = 1

# Taking Input for the number of
# Iterations our Algorithm will run
number_element = int(input('Enter the number of iterations (must be > 1): '))

# Plotting the Fibonacci Spiral Fractal
# and printing the corresponding Fibonacci Number
if number_element > 0:
    print("Fibonacci series for", number_element, "elements :")
    x = turtle.Turtle()
    x.speed(100)
    draw_fibo(number_element)
    turtle.done()
else:
    print("Number of iterations must be > 0")
