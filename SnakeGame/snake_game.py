from turtle import Screen as s
from snake import Snake
from food import Food
from food import Scoreboard
import turtle
import time
screen = s()
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.title("SNAKE GAME")
screen.tracer(0)#will remove the animation from the screen

snake_obj = Snake()
food_obj = Food()
scorecard = Scoreboard()

screen.listen()
screen.onkey(snake_obj.up,'Up')
screen.onkey(snake_obj.down,'Down')
screen.onkey(snake_obj.right,'Right')
screen.onkey(snake_obj.left,'Left')
score_ = 0
game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake_obj.move()

    #collision with food
    if snake_obj.head.distance(food_obj) < 20:
        # print("YEah")
        food_obj.refresh()
        scorecard.score = scorecard.score + 1
        # print(scorecard.score)
        snake_obj.extend()
        scorecard.printScore()
    
    #collision with the wall
    if snake_obj.head.xcor() > 280 or snake_obj.head.xcor() < -280 or snake_obj.head.ycor() > 280 or snake_obj.head.ycor() < -280 :
        game_on = False
        print(f"Your final score is {scorecard.score}")
        scorecard.gameOver()

    #collision with body
    for block in snake_obj.blocks:
        if block == snake_obj.head:
            pass
        elif snake_obj.head.distance(block) < 15:
            game_on = False
            print(f"Your final score is {scorecard.score}")
            scorecard.gameOver()



screen.exitonclick()
