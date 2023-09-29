#!/usr/bin/env python3
""" A Python module to draw spirographical images using turtle programming.
History:
01.00 2023-Sep-25 Scott S. Initial release.
01.01 2023-Sep-29 Scott S. Add loop definition.

MIT License

Copyright (c) 2023 TigerPointe Software, LLC

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

Create a custom get_spiro.py file for your design.

#!/usr/bin/env python3
import spirographical as sg
sg.draw(colors=['hotpink', 'hotpink', 'cornflowerblue', 'cornflowerblue'],
        title='Pastel Weave', loops=70, skiploops=2, twist=-10)

#!/usr/bin/env python3
import spirographical as sg
sg.draw(colors=['lightsteelblue', 'cornflowerblue', 'royalblue',
                'blue', 'mediumblue', 'navy', 'midnightblue'],
        title='Blue Spiral', loops=40, skiploops=1, twist=3)

If you enjoy this software, please do something kind for free.

Please consider giving to cancer research.
https://braintumor.org/
https://www.cancer.org/
"""

import math
import importlib
import turtle


def draw(colors=['red', 'purple', 'blue', 'green', 'yellow', 'orange'],
         bgcolor='black', title='Spirographical Rainbow',
         size=450, loops=60, skiploops=0, twist=1, exitonclick=True):
    """Draws a spirographical image using turtle programming.
    PARAMETERS:
    colors      : array of colors, one color per repeating edge
                  the edge count is defined by the array length
    bgcolor     : background color
    title       : window title
    size        : image size in pixels
    loops       : number of full loops over which to iterate
                  on a full loop, each color is used exactly once
    skiploops   : number of starting loops to skip (creates a donut hole)
    twist       : value by which to twist the next edge on each loop
                  positive value produces a clockwise twist
                  negative value produces a counter-clockwise twist
    exitonclick : wait for an image click event before exiting
    """

    # Create the drawing board
    importlib.reload(turtle)  # hack to fix TurtleScreen._RUNNING issue
    turtle.title(title)       # window title
    turtle.setup(size, size)  # width and height in pixels
    turtle.bgcolor(bgcolor)   # background color

    # Configure the pen
    t = turtle.Pen()          # new pen
    t.shapesize(0.5, 0.5, 1)  # reduce the 20x20px turtle by 50% (10x10px)
    t.speed(0)                # speed 0=fastest, or 1=slow to 10=fast

    # Calculate the line width percentage rate of increase
    count = loops * len(colors)
    skipcount = skiploops * len(colors)
    rate = math.floor((size / count) * 100)

    # Loop through each value in the range
    circle = 360  # degrees in a circle
    for x in range(count):
        t.pencolor(colors[x % len(colors)])  # loop number selects pen color
        t.width((x // rate) + 1)             # line width gradually increases
        if (x < skipcount):
            t.penup()    # do not draw lines (loop is skipped)
        else:
            t.pendown()  # draw lines (loop is not skipped)
        t.forward(x)     # move turtle a greater distance on each loop
        t.right((circle // len(colors)) - twist)  # adjust next line by twist
    t.hideturtle()

    # Wait for the click event to exit (optional)
    if (exitonclick):
        turtle.exitonclick()


def loop(colors=['red', 'purple', 'blue', 'green', 'yellow', 'orange'],
         bgcolor='black', title='Looping Rainbow',
         size=450, radius=100, steps=None, pensize=1, sparseness=1,
         exitonclick=True):
    """Draws a looping spirographical image using turtle programming.
    PARAMETERS:
    colors      : array of colors
    bgcolor     : background color
    title       : window title
    size        : image size in pixels
    radius      : radius of each inner circle
    steps       : steps (edge count) of each inner circle
                  None = circle
                  1 = point
                  2 = line
                  3 = triangle
                  4 = square
                  5 = pentagon
                  6 = hexagon, etc.
    sparseness  : multiplier to control the sparseness of the design
                  1 = repeat color array one time, dense
                  2 = repeat color array two times, sparse
                  3 = repeat color array three times, more sparse, etc.
    pensize     : pen size
    exitonclick : wait for an image click event before exiting
    """

    # Create the drawing board
    importlib.reload(turtle)  # hack to fix TurtleScreen._RUNNING issue
    turtle.title(title)       # window title
    turtle.setup(size, size)  # width and height in pixels
    turtle.bgcolor(bgcolor)   # background color

    # Configure the pen
    t = turtle.Pen()    # new pen
    t.pensize(pensize)  # pen size
    t.speed(0)          # speed 0=fastest, or 1=slow to 10=fast
    t.hideturtle()      # hide turtle

    # Repeat the colors array for increased spareseness
    allcolors = (colors * sparseness)

    # Loop through each value in the range
    circle = 360 # degrees in a circle
    arc = circle // len(allcolors)  # size of each color arc 
    for x in range(arc):
        c = ((x * len(allcolors)) // arc)  # loop number selects pen color
        t.pencolor(allcolors[c])
        t.circle(radius=radius, steps=steps)  # draw next circle
        t.left(len(allcolors))  # colors count determines rotation

    # Wait for the click event to exit (optional)
    if (exitonclick):
        turtle.exitonclick()


# Start the program interactively
if __name__ == '__main__':
    try:
        print('Spirographical Python Module')
        print('    Drawing the sample image, please wait ...')
        draw(exitonclick=False)  # do not wait for click
        print('    Image completed.')
        input('Press ENTER to Continue: ')
    except Exception as e:
        print(str(e))
