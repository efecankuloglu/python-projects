from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

with open("data.txt", "r") as f:
    data = int(f.read())


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = data
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)


    def increase_score(self):
        self.score += 1 
        self.update_scoreboard()

#    def game_over(self):
#        self.goto(0, 0)
#        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()
        self.save_highscore()

    def save_highscore(self):
        with open("data.txt", "w") as f:
            f.write(str(self.high_score))