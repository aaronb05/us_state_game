from turtle import Turtle
FONT = ("arial", 10, "bold")


class State(Turtle):
    def __init__(self):
        super().__init__()

        self.text = ""
        self.x_cor = 0
        self.y_cor = 0
        self.correct_answers = 0

    def move_to_location(self, u_input, x, y):
        self.text = u_input
        self.x_cor = x
        self.y_cor = y
        self.hideturtle()
        self.penup()
        self.goto(x, y)
        self.write(f"{self.text}", align="center", font=FONT)
        self.correct_answers += 1

    def end_game(self):
        self.text = "GAME OVER, YOU WIN!"
        self.penup()
        self.goto(0, 0)
        self.color("green")
        self.write(f"{self.text}", align="center", font=("Courier", 25, "bold"))


