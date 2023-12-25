import turtle as t

STARTING_POSITION = [ (0,0) , (-20,0) , (-40,0) ]
MOVING_DISTANCE = 20
TURNING_ANGLE = 90
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.blocks = []
        self.createSnake()
        self.head = self.blocks[0]
    def createSnake(self):
        for coordinates in STARTING_POSITION:
            new_block = t.Turtle("square")
            new_block.color("white")
            new_block.penup()
            new_block.goto(coordinates)
            self.blocks.append(new_block)
    
    def extend(self):
        self.addBlock(self.blocks[-1].position())


    def addBlock(self,position):
            new_block = t.Turtle("square")
            new_block.color("white")
            new_block.penup()
            new_block.goto(position)
            self.blocks.append(new_block)

    def move(self):
        for i in range (len(self.blocks)-1, 0, -1):
            x_coordinates = self.blocks[i-1].xcor()
            y_coordinates = self.blocks[i-1].ycor()
            self.blocks[i].goto(x_coordinates, y_coordinates)
        self.blocks[0].forward(MOVING_DISTANCE)

    def left(self):
        self.blocks[0].setheading(LEFT)
    def down(self):
        self.blocks[0].setheading(DOWN)
    def right(self):
        self.blocks[0].setheading(RIGHT)
    def up(self):
        self.blocks[0].setheading(UP)