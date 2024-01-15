from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def w_high_score(self):
        with open("my_file.txt", mode="w") as file:
            file.write(f"{self.high_score}")

    def update_scoreboard(self):
        self.clear()
        with open("my_file.txt") as file:
            h_score = file.read()
        self.write(f"Score: {self.score}  High Score:{h_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.score = 0
            self.w_high_score()
            self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
