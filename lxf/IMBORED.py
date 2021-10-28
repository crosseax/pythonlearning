import turtle

turtle.bgcolor('black')
turtle.pensize(2)
turtle.speed(10)


for i in range(1):
    for colors in ['red']:
        turtle.color(colors)
        x, y = 1, 1
        while x < 200:
            x, y = y, x + y
            turtle.circle(x)
            turtle.left(y/2)
        

turtle.hideturtle()

turtle.done()