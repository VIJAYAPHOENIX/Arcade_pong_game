from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.r_score = 0
        self.l_score =0
        self.update()
        self.game_over()

    def update(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.l_score,align="center",font=("courier",80,"normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("courier", 80, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update()

    def r_point(self):
        self.r_score += 1
        self.update()

    def game_over(self):
        self.goto(0, 0)
        self.write("game over!", align="center", font=("Arial", 34, "normal"))