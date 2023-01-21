from turtle import Turtle


class Paddle(Turtle):

    def __init__(self):
        super().__init__()

    def paddle(self):
        self.shape('square')
        self.color('white')
        self.penup()
        self.shapesize(stretch_wid=7, stretch_len=1)

    def right_paddle(self):
        self.paddle()
        self.goto(430, 0)

    def left_paddle(self):
        self.paddle()
        self.goto(-430, 0)

    def move_up(self):
        if self.ycor() < 220:
            y_pos = self.ycor() + 40
            self.sety(y_pos)

    def move_down(self):
        if self.ycor() > -220:
            y_pos = self.ycor() - 40
            self.sety(y_pos)
