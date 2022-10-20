from turtle import Turtle


class Board:
    def __init__(self):
        self.top = Turtle("square")
        self.bottom = Turtle("square")
        self.center = Turtle("square")
        self.top.penup()
        self.bottom.penup()
        self.top.shapesize(stretch_wid=0.1, stretch_len=40)
        self.bottom.shapesize(stretch_wid=0.1, stretch_len=40)
        self.center.shapesize(stretch_wid=30, stretch_len=0.1)
        self.top.goto(0, 299)
        self.bottom.goto(0, -292)
        self.center.color("white")

        # self.top.color("white")
        # self.bottom.color("white")


