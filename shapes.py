import turtle as t 
from turtle import Screen as s
import random
buddy = t.Turtle()
buddy.speed('normal')
# i=0
# while i<4:
#     x = 0
#     while x <5:
#         buddy.forward(10)
#         buddy.penup()
#         buddy.forward(10)
#         buddy.pendown()
#         x+=1
#     buddy.right(90)
#     i += 1
# colors = ["blue3" , "DarkCyan" , "DarkSalmon" , "DarkSeaGreen" , "firebrick" , "gold4" , "LemonChiffon4" , "khaki"]
# t.colormode(255)
t.colormode(255)
def drawSquare(b):
    buddy.color(change_color())
    for i in range(4):
        b.forward(100)
        b.left(90)

def change_color():
    r = random.randint(0,254)
    b = random.randint(0,254)
    g = random.randint(0,254)
    random_color = (r,b,g)
    return random_color

    

def pentagon(b):
    buddy.color(change_color())
    for i in range(5):
        b.forward(100)
        b.left(72)

def hexagon(b):
    buddy.color(change_color())
    for i in range(6):
        b.forward(100)
        b.left(60)

def octagon(b):
    buddy.color(change_color())
    for i in range(8):
        b.forward(100)
        b.left(45)

# drawSquare(buddy)
# pentagon(buddy)
# hexagon(buddy)
# octagon(buddy)

def random_walk(b):
    b.pensize(20)
    for i in range(200):
        buddy.color(change_color())
        b.forward(random.randint(1,100))
        b.setheading(random.choice([90,270,180,360]))

random_walk(buddy)


field = s()
field.exitonclick()