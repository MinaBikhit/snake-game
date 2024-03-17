from turtle import Turtle, Screen


MOVE_DISTANCE = 20  # constant that determines the step distance of the snake


class Snake:

    def __init__(self):
        self.segments = []              # list that contains all the segments of the snake
        self.speed = 0.1                # defining the initial speed later to be chosen by the user
        self.choose_difficulty()             # calling the function that allows the user to choose the desired speed
        self.initial_snake()            # calling the function that creates the initial snake
        self.head = self.segments[0]    # defining the head as the first index in the segments list

    def initial_snake(self):
        """method that creates the initial snake"""
        x = 0
        y = 0
        for _ in range(3):

            self.add_segment(x, y)
            x -= 20

    def move(self):
        """method that allows the snake to move across the screen"""
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        """method that allows the snake to go up"""
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)

    def down(self):
        """method that allows the snake to go down"""
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)

    def left(self):
        """method that allows the snake to go left"""
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)

    def right(self):
        """method that allows the snake to go right"""
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)

    def add_segment(self, x, y):
        """method that is used to add a segment to the snake"""
        segment = Turtle()
        segment.color("white")
        segment.shape("square")
        segment.penup()
        segment.setposition(x, y)
        self.segments.append(segment)

    def extend(self):
        """method used to increase the size of the snake when it eats food"""
        self.add_segment(self.segments[-1].xcor(), self.segments[-1].ycor())

    def choose_difficulty(self):
        """method aimed to allow the user to choose the speed of the snake"""
        global MOVE_DISTANCE
        screen1 = Screen()
        speed = screen1.textinput(title="Choose Difficulty",
                                 prompt="Choose Difficulty: \n1:Easy \n2:Normal \n3:Hard  ")

        try:
            if speed == "1":
                MOVE_DISTANCE = 10
                self.speed = 0.1
            elif speed == "2":
                MOVE_DISTANCE = 20
                self.speed = 0.1
            elif speed == "3":
                MOVE_DISTANCE = 20
                self.speed = 0.05
            else:
                MOVE_DISTANCE = 20
                self.speed = 0.1
        except TypeError:
            MOVE_DISTANCE = 20
            self.speed = 0.1

    def pass_through_wall(self):
        """Method to let the snake pass through walls"""
        if self.head.xcor() > 300:
            self.head.goto(-300, self.head.ycor())
        elif self.head.xcor() < -300:
            self.head.goto(300, self.head.ycor())
        elif self.head.ycor() > 300:
            self.head.goto(self.head.xcor(), -300)
        elif self.head.ycor() < -300:
            self.head.goto(self.head.xcor(), 300)

    def reset(self):
        """Reset the snake to its initial state."""
        # Clear existing segments
        for segment in self.segments:
            segment.goto(1000, 1000)  # Move segment out of the screen
            segment.clear()           # Clear the segment
        self.segments.clear()         # Clear the segments list

        # Recreate the initial snake
        self.initial_snake()
        self.head = self.segments[0]  # Update the head reference
