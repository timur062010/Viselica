from turtle import *


def draw_line(point1, point2, size=10, p_color='black'):
    oldPenSize = pen()['pensize']
    oldColor = pen()['pencolor']

    penup()
    goto(point1[0], point1[1])
    pendown()
    goto(point2[0], point2[1])
    penup()

    pensize(oldPenSize)
    pencolor(oldColor)

def draw_cirle(rad, size=10, p_color='black'):
    oldPensize = pen()['pensize']
    oldColor = pen()['pencolor']

    pensize(size)
    pencolor(p_color)

    pendown()
    circle(rad)
    penup()

    pensize(oldPensize)
    pencolor(oldColor)

Screen().setup(1200, 1200)

shape("turtle")
penup()

# goto(80,170)
# dot(40,"red")

draw_line([-400, -250], [-100, -250])
draw_line([-100, -250], [-100, 300])
draw_line([-100, 300], [-300, 300])
draw_line([-300, 300], [-300, 250])
draw_cirle(-50)
draw_line([-300, 150], [-300, -50])
draw_line([-300, 50], [-375, 125])
draw_line([-300, 50], [-215, 125])
draw_line([-300, -50], [-375, -175])
draw_line([-300, -50], [-215, -175])
mainloop()
