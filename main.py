from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball

screen = Screen()
screen.title("Pong")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.mode("logo")

paddle_1 = Paddle("left")
paddle_2 = Paddle("right")

screen.listen()

screen.onkeypress(fun=paddle_1.paddle_up, key="w")
screen.onkeypress(fun=paddle_1.paddle_down, key="s")

screen.onkeypress(fun=paddle_2.paddle_up, key="Up")
screen.onkeypress(fun=paddle_2.paddle_down, key="Down")

ball = Ball()

score_player_1 = 0
score_player_2 = 0

ball.serve_1()

gameover = False
while gameover == False:
    ball.forward(10)
    ball.coll_wall()
    ball.coll_paddle_1(paddle_2)
    ball.coll_paddle_2(paddle_1)
    score_player_1 = ball.coll_goal_1()
    score_player_2 = ball.coll_goal_2()
    if score_player_1 == 5:
        ball.reset()
        game_over = True
    elif score_player_2 == 5:
        ball.reset()
        game_over = True

screen.exitonclick()
