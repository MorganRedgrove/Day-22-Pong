from turtle import Turtle
class Paddle(Turtle):
    def __init__(self, start_pos):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(1, 5, 1)
        self.setheading(0)
        if start_pos == "left":
            self.setposition(x=-380, y=0)
            self.showturtle()
        elif start_pos == "right":
            self.setposition(x=380, y=0)
            self.showturtle()

    def paddle_up(self):
        if self.ycor() < 250:
            self.forward(10)

    def paddle_down(self):
        if self.ycor() > -250:
            self.backward(10)