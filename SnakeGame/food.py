import turtle as t
import random

t.colormode(255)
class Food(t.Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.speed('fastest')
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)#strectes the length and width of the turtle
        self.refresh()
    
    def refresh(self):
        R = random.randint(0,255)
        G = random.randint(0,255)
        B = random.randint(0,255)
        X = random.randint(-270,270)
        Y = random.randint(-270,270)
        COLOR_SET = (R,G,B)
        self.color(COLOR_SET)
        self.goto(x=X,y=Y)
ALIGNMENT = "center"
FONT = ("Courier",10,"normal")
class Scoreboard(t.Turtle):
    def __init__(self):
        super().__init__()
        self.pencolor("white")
        self.score = 0
        self.shape('circle')
        self.hideturtle()
        self.penup()
        self.goto(0,280)
        self.printScore()

    def gameOver(self):
        self.goto(0,0)
        self.clear()
        self.write(f"Game Over",False,align=ALIGNMENT,font=("Courier",20,"bold"))

    
    def printScore(self):
        self.clear()
        self.write(f"Score : {self.score}",False,align=ALIGNMENT,font=FONT)
