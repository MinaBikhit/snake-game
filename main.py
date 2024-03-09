import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()  # generating a screen object
screen.setup(width=600, height=600)  # adjusting the dimensions of the screen object
screen.bgcolor("black")  # adjusting the color of the screen object
screen.title("Snake")  # choosing the title of the screen object
screen.tracer(0)  # disabling the tracer function for smoother performance

snake = Snake()  # creation of a snake object
food = Food()  # creation of a class object
score_board = ScoreBoard()  # creation of a scoreboard object
screen.listen()  # using the listen method to allow keyboard presses to affect the game
screen.onkey(snake.up, "Up")  # using onkey method to assign snake.up method to the up key
screen.onkey(snake.down, "Down")  # using onkey method to assign snake.down method to the down key
screen.onkey(snake.left, "Left")  # using onkey method to assign snake.left method to the left key
screen.onkey(snake.right, "Right")  # using onkey method to assign snake.right method to the right key

score_board.print_score()  # calling the print_score methode to print the initial score

game_is_on = True  # the game on variable for the while loop

while game_is_on:  # while loop for game continuity
    screen.update()  # calling the update method to refresh the screen in every iteration
    time.sleep(0.1)  # using the sleep methode increase the refresh rate

    snake.move()  # calling the move methode to start snake movement
    # Detect collision with food
    if snake.head.distance(
            food) < 15:  # checking the distance between the food object and snake head for collission detection
        food.refresh()  # calling the refresh method to change food object location
        score_board.increase_score()  # calling the increase score method to increase the score
        score_board.print_score()  # calling the print score method to reprint the score
        snake.extend()  # calling the extend method to add a new segment to the snake

    # Detect collision with walls
    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        game_is_on = False  # checking if the x or y coordinates of the snake head reached the edges of the screen
        score_board.game_over()  # if collision is detected the game_is_on is changed to False to stop the while loop
        # the game over method is called to dislay game over
    # Detect collision with tail
    for segment in snake.segments[1:]:  # checking the distance between the head and other segments to detect collision
        if snake.head.distance(segment) < 10:
            game_is_on = False  # if collision is detected the game_is_on is changed to False to stop the while loop
            score_board.game_over()  # the game over method is called to dislay game over

screen.exitonclick()  # exit on click method is called to avoid closing of the screen
