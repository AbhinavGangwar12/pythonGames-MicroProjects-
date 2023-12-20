import random
import turtle as t
from turtle import Screen as s

lak = t.Turtle()
t.colormode(255)
lak.speed('fastest')
lak.pensize(3)

head = 5

def change_color():
    r = random.randint(0,255)
    b = random.randint(0,255)
    g = random.randint(0,255)
    return (r,b,g)

def draw(buddy):
    global head
    buddy.color(change_color())
    buddy.circle(100)
    buddy.setheading(head)
    head+=5

def draw_spirograph(t):
    for i in range(int(360/5)):
        draw(t)

draw_spirograph(lak)

screen = s()
screen.exitonclick()