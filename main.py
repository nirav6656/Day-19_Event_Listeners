from turtle import Turtle, Screen

# Made object named Sheru (my dog name)
sheru = Turtle()
screen = Screen()


sheru.pencolor("blue")
sheru.width(3)
def up():
    sheru.setheading(90)
    sheru.forward(20)

def down():
    sheru.setheading(270)
    sheru.forward(20)


def left():
    sheru.setheading(180)
    sheru.forward(20)


def right():
    sheru.setheading(360)
    sheru.forward(20)


screen.listen()
screen.onkey(key="Up", fun=up)
screen.onkey(key="Down", fun=down)
screen.onkey(key="Left", fun=left)
screen.onkey(key="Right", fun=right)

screen.mainloop()
screen.exitonclick()
