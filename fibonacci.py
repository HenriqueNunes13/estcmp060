# Python program for Plotting Fibonacci
# spiral fractal using Turtle
import turtle
import math


def fibonacci_plot(iteration):
    a = 0
    b = 1
    square_a = a
    square_b = b

    # Setting the colour of the plotting pen to blue
    draw_pen.pencolor("blue")

    # Drawing the first square
    draw_pen.forward(b * factor)
    draw_pen.left(90)
    draw_pen.forward(b * factor)
    draw_pen.left(90)
    draw_pen.forward(b * factor)
    draw_pen.left(90)
    draw_pen.forward(b * factor)

    # Proceeding in the Fibonacci Series
    assistant_variable = square_b
    square_b = square_b + square_a
    square_a = assistant_variable

    # Drawing the rest of the squares
    for count in range(1, iteration):
        draw_pen.backward(square_a * factor)
        draw_pen.right(90)
        for c in range(2):
            draw_pen.forward(square_b * factor)
            draw_pen.left(90)
        draw_pen.forward(square_b * factor)

        # Proceeding in the Fibonacci Series
        assistant_variable = square_b
        square_b = square_b + square_a
        square_a = assistant_variable

    # Bringing the pen to starting point of the spiral plot
    draw_pen.penup()
    draw_pen.setposition(factor, 0)
    draw_pen.seth(0)
    draw_pen.pendown()

    # Setting the colour of the plotting pen to red
    draw_pen.pencolor("red")

    # Fibonacci Spiral Plot
    draw_pen.left(90)
    for i in range(iteration):
        print(b)
        forward_width = math.pi * b * factor / 2
        forward_width /= 90
        for j in range(90):
            draw_pen.forward(forward_width)
            draw_pen.left(1)
        assistant_variable = a
        a = b
        b = assistant_variable + b


# Here 'factor' signifies the multiplicative
# factor which expands or shrinks the scale
# of the plot by a certain factor.
factor = 1

# Taking Input for the number of
# Iterations our Algorithm will run
number_iterations = int(input('Enter the number of iterations (must be > 1): '))

# Plotting the Fibonacci Spiral Fractal
# and printing the corresponding Fibonacci Number
if number_iterations > 0:
    print("Fibonacci series for", number_iterations, "elements :")
    draw_pen = turtle.Turtle()
    draw_pen.speed(100)
    fibonacci_plot(number_iterations)
    turtle.done()
else:
    print("Number of iterations must be > 0")
