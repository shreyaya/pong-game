from turtle import Screen, Turtle
from Paddle import Paddle
from ball import Ball
from score_board import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.listen()
screen.tracer(0)

line = Turtle()
line.penup()
line.pencolor("white")
line.hideturtle()
line.goto(0, -300)
line.width(5)
line.setheading(90)

for i in range(0, 30):
    line.pendown()
    line.forward(10)
    line.penup()
    line.forward(10)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
r_score = Scoreboard((40, 250))
l_score = Scoreboard((-40, 250))
screen.onkey(fun=r_paddle.up, key="Up")
screen.onkey(fun=r_paddle.down, key="Down")
screen.onkey(fun=l_paddle.up, key="w")
screen.onkey(fun=l_paddle.down, key="s")
is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()

    if (r_paddle.distance(ball) <= 50 and ball.xcor() >= 320) or (
            l_paddle.distance(ball) <= 50 and ball.xcor() <= -320):
        ball.bounce_x()
    if ball.xcor() > 360:
        ball.refresh()
        r_score.update()
    if ball.xcor() < -360:
        ball.refresh()
        l_score.update()

screen.exitonclick()
