import turtle as t
t.hideturtle()

t.screensize(640, 380)


def drawCircle(x, y, color):
    t.penup()
    t.setpos(x, y)
    t.pendown()
    t.color(color)
    t.pensize(5)
    t.circle(40)


drawCircle(0, 30, 'black')
drawCircle(-100, 30, 'blue')
drawCircle(-50, -30, 'yellow')
drawCircle(50, -30, 'green')
drawCircle(100, 30, 'red')

t.exitonclick()
