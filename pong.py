from turtle import Screen
from pong_peddles import Peddles
from pong_ball import Ball
from pong_score_board import  Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("PONG")
screen.tracer(0)

target_score = screen.textinput(title="enter a target score!",prompt= "integer value only , Got it!")
try:
    total_score = int(target_score)
except(ValueError,TypeError):
    total_score = 10

r_peddles = Peddles((350,0))
l_peddles = Peddles((-350,0))
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkey(r_peddles.up,"Up")
screen.onkey(r_peddles.down,"Down")
screen.onkey(l_peddles.up,"w")
screen.onkey(l_peddles.down,"s")


is_game_on = True

while is_game_on:
    time.sleep(ball.movement_speed)
    screen.update()
    ball.move()

    # detecting collision with wall
    if ball.ycor() >= 270 or ball.ycor() <= -270:
        ball.bounce_y()

    # Detecting collision with peddles
    if ball.distance(r_peddles) < 50 and ball.xcor() > 320 or ball.distance(l_peddles) < 50  and  ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 370:
        ball.reset_position()
        score.l_point()


    if ball.xcor() < -370:
        ball.reset_position()
        score.r_point()

    if total_score == score.l_score or target_score == score.r_score:
        is_game_on = False
        score.game_over()


screen.exitonclick()
