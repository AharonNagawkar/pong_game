from turtle import Turtle
from random import choice


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.create_ball()
        self.ball_speed = 1

    def create_ball(self):
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color('white')

    def init(self):
        init_heading = choice([45, 135, 225, 315])
        self.setheading(init_heading)

    def move(self):
        self.forward(self.ball_speed)

    def wall_bounce(self):
        impact = self.heading()
        self.setheading(360-impact)

    def paddle_bounce(self):
        impact = self.heading()
        self.setheading(180-impact)
