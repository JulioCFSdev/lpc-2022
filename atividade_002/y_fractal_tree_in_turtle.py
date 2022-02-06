import turtle

turtle.speed('fastest')

# turning the turtle to face upwards
turtle.right(-90)

# the acute angle between
# the base and branch of the Y
angle = 30


# function to plot a fractal tree
def fractal_tree(size_tree, level):
    if level > 0:
        turtle.colormode(255)

        # splitting the rgb range for green
        # into equal intervals for each level
        # setting the colour according
        # to the current level
        turtle.pencolor(0, 255 // level, 0)

        # drawing the base
        turtle.forward(size_tree)

        turtle.right(angle)

        # recursive call for
        # the right subtree
        fractal_tree(0.8 * size_tree, level - 1)

        turtle.pencolor(0, 255 // level, 0)

        turtle.left(2 * angle)

        # recursive call for
        # the left subtree
        fractal_tree(0.8 * size_tree, level - 1)

        turtle.pencolor(0, 255 // level, 0)

        turtle.right(angle)
        turtle.forward(-size_tree)


# tree of size 80 and level 7
fractal_tree(80, 7)
