from turtle import Turtle
UP = 90
DOWN = 270


class Paddle:
    def __init__(self, location):
        self.paddle = Turtle("square")
        self.paddle.penup()
        self.paddle.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle.setposition(location)
        self.paddle.color("white")

    def up(self):
        if self.paddle.ycor() >= 260:
            pass
        else:
            y_position = self.paddle.ycor() + 20
            x_position = self.paddle.xcor()
            self.paddle.goto(x_position, y_position)

    def down(self):
        if self.paddle.ycor() <= -240:
            pass
        else:
            y_position = self.paddle.ycor() - 20
            x_position = self.paddle.xcor()
            self.paddle.goto(x_position, y_position)

    def reset(self, location):
        self.paddle.goto(location)


