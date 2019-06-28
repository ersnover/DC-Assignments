#draws a pyramid with height = x
def DrawPyramid(height):
    bottom_row = height * 2 - 1
    for i in range(1, height + 1):
        row_length = i * 2 -1
        spaces = int((bottom_row - row_length) / 2)
        print(" " * spaces + "*" * row_length + " " * spaces)

DrawPyramid(50)