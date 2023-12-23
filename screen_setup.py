import turtle as t
from turtle import Screen as s
import random

def make_finish():
    finish = t.Turtle(shape="turtle")
    finish.hideturtle()
    finish.penup()
    finish.goto(x=220,y=0)
    finish.pendown()
    finish.width(width=10)
    finish.right(90)
    finish.forward(250)
    finish.backward(510)
    finish.penup()

screen = s()
screen.setup(height=500,width=500)
colors = ["red","green","blue","yellow","purple","orange"]
y_positions = [-90,-60,-30,0,30,60,90]
all_turtles = []

make_finish()

for turtle_index in range(len(colors)-1):
    new_turtle = t.Turtle(shape='turtle')
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-240,y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

user_prediction = screen.textinput(title="Make your bet",prompt="Which turtle is gonna win ?").lower()
race_on = True
while race_on:
    for turtles in all_turtles:
        if turtles.xcor() > 210:
            race_on = False
            winning_color = turtles.pencolor()
            if user_prediction == winning_color:
                print(f"You won! {winning_color} won the race")
            else:
                print(f"You lose! {winning_color} won the race")
        move = random.randint(0,10)
        turtles.forward(move)

print("Over!")


screen.exitonclick()
