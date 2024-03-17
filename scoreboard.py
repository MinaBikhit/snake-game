from turtle import Turtle,Screen
ALIGNMENT = "center"
FONT = ("Courier", 24, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")      # defining text color as white
        self.penup()             # using penup to avoid drawing lines by the turtle
        self.hideturtle()        # hiding the turtle symbol
        self.score = 0           # score variable initialized at zero
        self.again = ''

    def print_score(self):
        """method that writes the score in the screen"""
        self.clear()
        self.setposition(0, 240)
        self.write(f"Score: {self.score}", True, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """method that increases the score """
        self.score += 1

    def game_over(self):
        """method that displays Game Over when the user loses and asks if the user wants to play again"""
        self.home()
        self.write("Game Over", True, align=ALIGNMENT, font=FONT)
        screen2 = Screen()
        self.again = screen2.textinput(title="Game Over!!",
                                  prompt="Do you want to play again?: \ny: yes\nn:no")
