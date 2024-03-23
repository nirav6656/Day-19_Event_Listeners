from turtle import Turtle, Screen

# Made object named Sheru (my dog name)
# sheru = Turtle()
screen = Screen()

# ------------------Etch-A-Sketch App----------------------

# sheru.pencolor("blue")
# sheru.width(3)
# def up():
#     sheru.setheading(90)
#     sheru.forward(20)
#
# def down():
#     sheru.setheading(270)
#     sheru.forward(20)
#
#
# def left():
#     sheru.setheading(180)
#     sheru.forward(20)
#
#
# def right():
#     sheru.setheading(360)
#     sheru.forward(20)
#
#
# screen.listen()
# screen.onkey(key="Up", fun=up)
# screen.onkey(key="Down", fun=down)
# screen.onkey(key="Left", fun=left)
# screen.onkey(key="Right", fun=right)
#
# screen.mainloop()

# --------------------------------------------------------------

# -----------------------Turtle Race----------------------------

screen.setup(width=500,height=400)
# user_bet = screen.textinput(title="Make your bet",prompt="Which tutle win the race ? Enter a Color: ")
colors = ["red","green","yellow","black"]
start_y = -50
for co in colors:
    co = Turtle("turtle")
    co.color("co")
    co.penup()
    co.goto(x=-250,y=start_y)
    start_y+=50






# --------------------------------------------------------------

screen.exitonclick()
