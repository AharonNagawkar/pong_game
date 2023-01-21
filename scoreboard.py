from turtle import Turtle
FONT = ("Courier", 40, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.penup()
        self.score_1 = 0
        self.score_2 = 0
        self.players_score()

    def separation(self):
        self.goto(0, -425)
        self.setheading(90)
        self.pensize(5)
        while self.ycor() < 430:
            self.pendown()
            self.forward(25)
            self.penup()
            self.forward(25)

    def players_score(self):
        self.separation()
        self.goto(-100, 230)
        self.write(f"{self.score_1}", font=FONT)
        self.goto(80, 230)
        self.write(f"{self.score_2}", font=FONT)

    def add_point_left(self):
        self.score_1 += 1
        self.clear()
        self.players_score()

    def add_point_right(self):
        self.score_2 += 1
        self.clear()
        self.players_score()

    def game_over(self):
        self.goto(-140, 0)
        self.write(f"Game Over", font=FONT)
