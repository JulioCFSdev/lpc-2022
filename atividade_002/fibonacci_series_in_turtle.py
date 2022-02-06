# Python program for Plotting Fibonacci
# spiral fractal using Turtle
import turtle
import math


def fibo_plot(int_number):
    a = 0
    b = 1
    square_a = a
    square_b = b

    # Setting the colour of the plotting pen to blue
    x.pencolor("blue")

    # Drawing the first square
    x.forward(b * factor)
    x.left(90)
    x.forward(b * factor)
    x.left(90)
    x.forward(b * factor)
    x.left(90)
    x.forward(b * factor)

    # Proceeding in the Fibonacci Series
    temp = square_b
    square_b = square_b + square_a
    square_a = temp

    # Drawing the rest of the squares
    for i in range(1, int_number):
        x.backward(square_a * factor)
        x.right(90)
        for j in range(3):
            x.forward(square_b * factor)
            if j == 2:
                pass
            x.left(90)

        # Proceeding in the Fibonacci Series
        temp = square_b
        square_b = square_b + square_a
        square_a = temp

    # Bringing the pen to starting point of the spiral plot
    x.penup()
    x.setposition(factor, 0)
    x.seth(0)
    x.pendown()

    # Setting the colour of the plotting pen to red
    x.pencolor("red")

    # Fibonacci Spiral Plot
    x.left(90)
    for i in range(number_iterations):
        print(b)
        fibo_equation = math.pi * b * factor / 2
        fibo_equation /= 90
        for j in range(90):
            x.forward(fibo_equation)
            x.left(1)
        temp = a
        a = b
        b = temp + b


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
    x = turtle.Turtle()
    x.speed(100)
    fibo_plot(number_iterations)
    turtle.done()

else:
    print("Number of iterations must be > 0")
