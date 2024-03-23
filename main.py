from turtle import Turtle, Screen
import random
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



is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["green","red", "orange", "yellow", "purple", "blue"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

#Create 6 turtles
# for turtle_index in range(0, 6):
#     sheru = Turtle(shape="turtle")
#     sheru.penup()
#     sheru.color(colors[turtle_index])
#     sheru.goto(x=-230, y=y_positions[turtle_index])
#     all_turtles.append(sheru)
#
# if user_bet:
#     is_race_on = True
#
# while is_race_on:
#     for turtle in all_turtles:
#         #230 is 250 - half the width of the turtle.
#         if turtle.xcor() > 230:
#             is_race_on = False
#             winning_color = turtle.pencolor()
#             if winning_color == user_bet:
#                 print(f"You've won! The {winning_color} turtle is the winner!")
#             else:
#                 print(f"You've lost! The {winning_color} turtle is the winner!")
#
#         #Make each turtle move a random amount.
#         rand_distance = random.randint(0, 10)
#         turtle.forward(rand_distance)






# --------------------------------------------------------------

screen.exitonclick()
