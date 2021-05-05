from turtle import *

speed('fastest')

# turning the turtle to face upwards
right(-90)

# the acute angle between
# the base and branch of the Y
angle = 30


# function to plot a Y
def fractal_tree(size, level):
    if level > 0:
        colormode(255)

        # splitting the rgb range for green
        # into equal intervals for each level
        # setting the colour according
        # to the current level
        pencolor(0, 255 // level, 0)

        # drawing the base
        forward(size)

        right(angle)

        # recursive call for
        # the right subtree
        fractal_tree(0.8 * size, level - 1)

        pencolor(0, 255 // level, 0)

        left(2 * angle)

        # recursive call for
        # the left subtree
        fractal_tree(0.8 * size, level - 1)

        pencolor(0, 255 // level, 0)

        right(angle)
        forward(-size)


# tree of size 80 and level 7
fractal_tree(80, 7)
