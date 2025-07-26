from turtle import Turtle, Screen
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard   
import time

screen = Screen()
screen.title("Ping Pong game")
screen.bgcolor("darkblue")
screen.setup(width=1000, height=600)
screen.tracer(0)

right_paddle = Paddle((450, 0))
left_paddle = Paddle((-450, 0))
ball = Ball()
scoreboard = Scoreboard()
# Control paddles
screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s") 

game_is_on = True
while game_is_on:
    screen.update()
    ball.move()
    time.sleep(ball.speed)  # Control the speed of the ball

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddles
    if (ball.distance(right_paddle) < 50 and ball.xcor() > 420) or (ball.distance(left_paddle) < 50 and ball.xcor() < -420):
        ball.bounce_x()

    # Detect when ball goes out of bounds
    if ball.xcor() > 480:
        ball.reset_position()
        scoreboard.l_point()
    elif ball.xcor() < -480:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()