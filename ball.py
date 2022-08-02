from turtle import Turtle
from random import randint


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        self.shapesize(1, 1)
        self.setposition(0, 0)
        self.speed(1)
        last_score = 1

    def serve_1(self):
        self.setheading(randint(25, 155))

    def serve_2(self):
        self.setheading(randint(205, 335))

    def coll_wall(self):
        if self.ycor() >= 300:
            self.setheading(180 - self.heading())
        if self.ycor() <= -300:
            self.setheading(180 - self.heading())

    def coll_paddle_1(self,object):
         if self.distance(object.position()) < 50 and self.xcor() >= 360:
             self.setheading(360 - self.heading())

    def coll_paddle_2(self,object):
         if self.distance(object.position()) < 50 and self.xcor() <= -360:
             self.setheading(360 - self.heading())

    def coll_goal_1(self):
        if self.xcor() >= 400:
            print("player 1 scores")
            self.hideturtle()
            self.goto(0,0)
            self.showturtle()
            self.serve_2()
            return +1

    def coll_goal_2(self):
        if self.xcor() <= -400:
            print("player 2 scores")
            self.hideturtle()
            self.goto(0,0)
            self.showturtle()
            self.serve_1()
            return +1
