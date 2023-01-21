import random
from turtle import Screen
from paddle import Paddle
from scoreboard import Scoreboard
from ball import Ball
from time import sleep

game_is_on = True

screen = Screen()

screen.setup(width=900, height=600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

scoreboard = Scoreboard()

paddle1 = Paddle()
paddle1.left_paddle()
paddle2 = Paddle()
paddle2.right_paddle()

ball = Ball()


screen.listen()
screen.onkey(paddle1.move_up, "w")
screen.onkey(paddle1.move_down, "s")
screen.onkey(paddle2.move_up, "Up")
screen.onkey(paddle2.move_down, "Down")

ball.init()

while game_is_on:

    screen.update()
    sleep(0.01)
    ball.move()

    # Detect collision with wall
    if abs(ball.ycor()) > 280:
        ball.wall_bounce()

    # Detect collision with paddles
    if ball.distance(paddle1) < 75 and ball.xcor() < -415:
        ball.ball_speed += 1
        ball.paddle_bounce()
    if ball.distance(paddle2) < 75 and ball.xcor() > 415:
        ball.ball_speed += 1
        ball.paddle_bounce()

    # Detect ball miss
    if ball.xcor() > 445:
        scoreboard.add_point_left()
        ball.goto(0, 0)
        sleep(1)
        ball.setheading(random.randint(135, 215))
        ball.ball_speed = 1

    elif ball.xcor() < -445:
        scoreboard.add_point_right()
        ball.goto(0, 0)
        sleep(1)
        ball.setheading(random.randint(-45, 45))
        ball.ball_speed = 1

    # End the Game
    if scoreboard.score_1 == 5 or scoreboard.score_2 == 5:
        scoreboard.game_over()
        game_is_on = False

screen.exitonclick()
