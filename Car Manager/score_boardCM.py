from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
class Scoreboard(Turtle,):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.score = 1
        self.write_score()

    def write_score(self):
        self.clear()
        self.color('black')
        self.goto(-260, 260)
        self.write(arg=f"Level: {self.score}", align="left", font=("Arial", 15, "normal"))


    def increase_scoreCM(self):
        self.score += 1
        self.write_score()

    def game_overCM(self):
        self.goto(0, 0)
        self.color('red')
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)