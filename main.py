import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()  # generating a screen object
screen.setup(width=600, height=600)  # adjusting the dimensions of the screen object
screen.bgcolor("olivedrab")  # adjusting the color of the screen object
screen.title("Snake")  # choosing the title of the screen object
screen.tracer(0)  # disabling the tracer function for smoother performance

snake = Snake()  # creation of a snake object
food = Food()  # creation of a food object
score_board = ScoreBoard()  # creation of a scoreboard object
score_board.print_score()  # calling the print_score methode to print the initial score
reset_game = False

def close_game():
    """function that closes the game window"""
    screen.bye()  # Close the screen

def reset_game_func():
    """Function that resets the game."""
    global reset_game
    reset_game = True


def game():
    """function that contains the game code to be recalled whenever the game needs to start"""

    global reset_game
    game_is_on = True  # the game on variable for the while loop

    screen.listen()  # using the listen method to allow keyboard presses to affect the game
    screen.onkey(snake.up, "Up")  # using onkey method to assign snake.up method to the up key
    screen.onkey(snake.down, "Down")  # using onkey method to assign snake.down method to the down key
    screen.onkey(snake.left, "Left")  # using onkey method to assign snake.left method to the left key
    screen.onkey(snake.right, "Right")  # using onkey method to assign snake.right method to the right key
    screen.onkeypress(close_game, "Escape")  # using onkey method to assign close_game method to the Escape key
    screen.onkeypress(reset_game_func, "r")  # using onkey method to assign reset game method to the r key
    screen.onkeypress(reset_game_func, "R")  # using onkey method to assign reset game method to the R key
    while game_is_on:  # while loop for game continuity
        screen.update()  # calling the update method to refresh the screen in every iteration
        time.sleep(snake.speed)  # using the sleep method to control increase the refresh rate

        snake.move()  # calling the move method to start snake movement

        # Detect collision with food
        if snake.head.distance(
                food) < 15:  # checking the distance between the food object and snake head for collision detection
            food.refresh()  # calling the refresh method to change food object location
            score_board.increase_score()  # calling the increase score method to increase the score
            score_board.print_score()  # calling the print score method to reprint the score
            snake.extend()  # calling the extend method to add a new segment to the snake

        # Detect collision with walls
        if abs(snake.head.xcor()) > 290 or abs(snake.head.ycor()) > 290:
            snake.pass_through_wall()  # if collision is detected the pass_through_wall method will be called

        # Detect collision with tail
        for segment in snake.segments[1:] or reset_game:  # checking the distance between the head and other segments to detect collision
            if snake.head.distance(segment) < 10:
                game_is_on = False  # if collision is detected the game_is_on equals False to stop the while loop
                score_board.game_over()  # the game over method is called to display game over
                try:                        # using try except in case user clicks cancel
                    if score_board.again.lower() == "y": # checking if the user wants to play again
                        score_board.score = 0            # resetting the score to zero
                        score_board.print_score()        # calling the print_score methode to print the initial score
                        snake.reset()                    # resetting the snake to the initial size
                        snake.choose_difficulty()        # asking the user to choose difficulty
                        game()
                except AttributeError:
                    pass
            elif reset_game:
                game_is_on = False                      # game_is_on as False to stop the while loop
                reset_game = False                      # reset_game as False to stop the while loop
                score_board.score = 0                   # resetting the score to zero
                score_board.print_score()               # calling the print_score methode to print the initial score
                snake.reset()                           # resetting the snake to the initial size
                snake.choose_difficulty()               # asking the user to choose difficulty
                game()                                  # calling the game function to restart the game

# try except expression to prevent errors on closing the game window
try:
    game()
except:
    pass

