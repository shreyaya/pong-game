from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, pos):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid= 5, stretch_len= 1)
        self.goto(pos)
        self.color("white")

    def up(self):
        y = self.ycor() + 30
        self.goto(self.xcor(), y)

    def down(self):
        y = self.ycor() - 30
        self.goto(self.xcor(),y)
