from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from board import Board
from scoreboard import ScoreBoard
import random


SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800
STARTING_ANGLES = [60, 330, 150, 240]
STARTING_SPEED = 0.2
SPEED_MULTIPLIER = [1, 1.1, 0.9, 1, 1.3, 1, 0.9, 1.2, 1.1]
NUMBER_OF_GAMES = 5

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


# initial positions for each player
position_2 = (SCREEN_WIDTH/2) - 50
position_1 = (SCREEN_WIDTH/-2) + 40


score = ScoreBoard()
board = Board()
player2 = Paddle((position_2, 0))
player1 = Paddle((position_1, 0))
ball = Ball()

screen.listen()
screen.onkeypress(player2.up, "Up")
screen.onkeypress(player2.down, "Down")
screen.onkeypress(player1.up, "w")
screen.onkeypress(player1.down, "s")

angle = random.choice(STARTING_ANGLES)
speed = STARTING_SPEED


def game_restart():
    score.refresh()
    ball.reset()
    player1.reset((position_1, 0))
    player2.reset((position_2, 0))


game_is_on = True
while game_is_on:
    # Detect who wins the game
    if score.player1_score == NUMBER_OF_GAMES:
        board.center.color("black")
        ball.color("black")
        screen.update()
        score.game_over("Player 1")
        game_is_on = False

    elif score.player2_score == NUMBER_OF_GAMES:
        board.center.color("black")
        ball.color("black")
        screen.update()
        score.game_over("Player 2")
        game_is_on = False

    else:
        screen.update()
        ball.move(angle, speed)

        # Detect collision with walls
        if ball.ycor() > 290 or ball.ycor() < -290:
            angle *= -1
            ball.move(angle, speed)

        # Detect collision with right paddle
        if ball.xcor() > 338 and ball.distance(player2.paddle) < 45:
            angle += 45
            speed *= random.choice(SPEED_MULTIPLIER)
            ball.move(angle, speed)

        if ball.xcor() < -350 and ball.distance(player1.paddle) < 45:
            angle += 45
            speed *= random.choice(SPEED_MULTIPLIER)
            ball.move(angle, speed)

        # Detect when the ball goes out
        if ball.xcor() > 400:
            score.player1_score += 1
            game_restart()
            speed = STARTING_SPEED
            angle = random.choice(STARTING_ANGLES[2:])

        if ball.xcor() < -400:
            score.player2_score += 1
            game_restart()
            speed = STARTING_SPEED
            angle = random.choice(STARTING_ANGLES[0:2])

screen.exitonclick()
