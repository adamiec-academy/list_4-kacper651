# Remove this comment to confirm that this task is done

from turtle import *


BLOCK_SIZE = ...                 # Set size of a single block (square) on grid [in pixels]
GRID_TOP_LEFT_CORNER = ..., ...  # Set the starting position of grid [in pixels]


def get_image_data_from_file(file):
    data = []

    for x in open(file, encoding="utf-8"):
        data.append(x.strip().split(4 * " "))

    for y in range(len(data)):
        for x in range(len(data[0])):
            data[y][x] = tuple(map(int, data[y][x].split(",")))

    return data


def to_pixels(x, y):  # Get pixel position of x, y grid position (function returns a pair of coordinates)
    # TODO
    return ..., ...


def square(x, y, colour):  # Draw a rectangle filled with colour in position x, y (grid position)
    # TODO
    pass


tracer(0, 1)
colormode(255)

data = get_image_data_from_file("image_data_1.txt")

# Make a code to draw specific squares from data matrix
# TODO


update()
exitonclick()
