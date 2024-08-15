#ToDo: make the snake body

from turtle import Turtle,Screen
import time
from snake import Snake
from food import Food
from s import Score_board


screen=Screen()
screen.setup(height=600,width=600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)


snake=Snake()
food=Food()
score=Score_board()
screen.listen()
screen.onkey(snake.up,'Up')
screen.onkey(snake.down,'Down')
screen.onkey(snake.left,'Left')
screen.onkey(snake.right,'Right')



is_game_on=True
while is_game_on:
    screen.update()
    time.sleep(.1)

    snake.move()
    if snake.head.distance(food)<15:
         food.refresh()
         snake.extend()
         score.increase_score()
         score.update_scoreboard()

    #detect collosion with wall
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or  snake.head.ycor()<-280:
        is_game_on=False
        score.game_over()

    #detect collosion with  tail
    for segment in snake.segments:
        if segment==snake.head:
            pass
        elif snake.head.distance(segment)<10:
            is_game_on=False
            score.game_over()





screen.exitonclick()
# ToDo: move the snake


#ToDo control the snake