from turtle import Turtle, Screen


MOVE_DISTANCE = 20  # constant that determines the step distance of the snake


class Snake():

    def __init__(self):
        self.segments = []              # list that contains all the segments of the snake
        self.choose_speed()             # calling the function that allows the user to choose the desired speed
        self.initial_snake()            # calling the function that creates the initial snake
        self.head = self.segments[0]    # defining the head as the first index in the segments list
        self.speed = 0                  # defining the initial speed later to be chosen by the user


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
        segment.speed(self.speed)
        self.segments.append(segment)

    def extend(self):
        """method used to increase the size of the snake when it eats food"""
        self.add_segment(self.segments[-1].xcor(), self.segments[-1].ycor())

    def choose_speed(self):
        """method aimed to allow the user to choose the speed of the snake"""
        screen1 = Screen()
        speed = screen1.textinput(title="Choose the speed of your snake",
                                 prompt="Enter the desired speed? \n1:Slow \n2:Fast \n3:Fastest  ")
        if int(speed) == 1:
            self.speed = 6
        elif int(speed) == 2:
            self.speed = 10
        elif int(speed) == 3:
            self.speed = 0