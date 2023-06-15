from turtle import Turtle

# Constants
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    """
    For making an updated score and high score appear on the screen.

    Methods:
    update_scoreboard: To update the score on the screen while the game is running.
    game_over: To reset the score and high score on the screen.
    increase_score: To increase the score on the screen.    
    """

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("high_score.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score} | HighScore: {self.high_score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.clear()
        if self.score > self.high_score:
            with open("high_score.txt",mode='w') as data:
                data.write(f"{self.score}")
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
