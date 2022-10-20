from turtle import Turtle
import time


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.speed("slowest")

    def move(self, angle, speed):
        self.setheading(angle)
        self.forward(speed)

    def reset(self):
        self.goto(0, 0)
        time.sleep(3)
