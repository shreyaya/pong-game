from turtle import Turtle

FONT = ("courier", 32, "bold")


class Scoreboard(Turtle):

    def __init__(self, position):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(position)
        self.color("white")
        self.score = 0
        self.write(f"{self.score}", align="center", font=FONT)
    def update(self):
        self.score += 1
        self.clear()
        self.write(f"{self.score}", align="center", font=FONT)