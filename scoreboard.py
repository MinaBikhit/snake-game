from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, 'normal')
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")      # defining text color as white
        self.penup()             # using penup to avoid drawing lines by the turtle
        self.hideturtle()        # hiding the turtle symbol
        self.score = 0           # score variable initialized at zero

    def print_score(self):
        """method that writes the score in the screen"""
        self.clear()
        self.setposition(0, 240)
        self.write(f"Score: {self.score}", True, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """method that increases the score """
        self.score += 1

    def game_over(self):
        """method that displays Game Over when the user loses"""
        self.home()
        self.write("Game Over", True, align=ALIGNMENT, font=FONT)