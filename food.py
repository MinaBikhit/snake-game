from turtle import Turtle
from random import randint


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")                                 # choosing the turtle shape as circle
        self.penup()                                         # penup to avoid line drawing by turtle
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)     # resizing the food object
        self.color("blue")                                   # choosing color for the food object
        self.speed(0)                                        # adjusting the speed to zero (fastest) for loading food
        x = randint(-280, 280)                            # generating a random x-coordinate
        y = randint(-280, 280)                            # generating a random y-coordinate
        self.setposition(x, y)                               # using the random coordinates to relocate the food object

    def refresh(self):
        """method that changes the position of the food element after collision"""
        x = randint(-280, 280)
        y = randint(-280, 280)
        self.setposition(x, y)
