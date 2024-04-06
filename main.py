from turtle import *


def draw_line(point1, point2):
    penup()
    goto(point1[0], point1[1])
    pendown()
    goto(point2[0], point2[1])
    penup()


Screen().setup(1200, 1200)

shape("turtle")
penup()

# goto(80,170)
# dot(40,"red")
pensize(5)
draw_line([-400, -250], [-100, -250])
draw_line([-100, -250], [-100, 300])
draw_line([-100, 300], [-300, 300])
draw_line([-300, 300], [-300, 250])
pendown()
circle(-50)
penup()
draw_line([-300, 150], [-300, -50])
draw_line([-300, -50], [-375, -175])
draw_line([-300, -50], [-215, -175])
mainloop()
