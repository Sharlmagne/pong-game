from turtle import Turtle
FONT = "Courier"


class ScoreBoard:
    def __init__(self):
        self.score = Turtle()
        self.player1_score = 0
        self.player2_score = 0
        self.score.hideturtle()
        self.score.color("white")
        self.show_score()

    def show_score(self):
        self.score.goto(y=230, x=0)
        self.score.write(f"{self.player1_score} {self.player2_score}", align="center", font=(FONT, 50, "normal"))

    def refresh(self):
        self.score.clear()
        self.show_score()

    def game_over(self, player):
        self.score.clear()
        self.score.color("blue")
        self.score.goto(y=0, x=0)
        self.score.write(f"{player} wins!", align="center", font=(FONT, 25, "bold"))


