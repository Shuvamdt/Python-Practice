from turtle import Turtle
FONT = ("Courier",24, "normal")
ALIGNMENT = "center"

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0, 260)
        self.score = 0
        with open("data.txt") as file:
            hs = file.read()
            self.high_score = int(hs)
        self.penup()
        self.hideturtle()
        self.color("white")
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, align=ALIGNMENT ,font=FONT)
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, align=ALIGNMENT, font=FONT)
    def score_up(self):
        self.score+=1
        self.update_scoreboard()
        # self.clear()
        # self.write(f"Score: {self.score} High Score: {self.high_score}", False, align=ALIGNMENT, font=FONT)
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", False, align=ALIGNMENT, font=FONT)
    def reset(self):
        if self.score > self.high_score :
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.score))
        self.score = 0
        self.update_scoreboard()