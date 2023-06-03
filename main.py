import time
from turtle import  Screen
from snake import Snake
from food import  Food
from scoreborde import Scorebored

screen = Screen()
screen.tracer(0)
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake Game")



food = Food()
scordBored = Scorebored()

screen.listen()
def set_new_game():
    snake = Snake()
    screen.onkey(snake.right,"Right")
    screen.onkey(snake.down,"Down")
    screen.onkey(snake.left,"Left")
    screen.onkey(snake.up,"Up")
    return snake
snake = set_new_game()
while True:
    screen.update()
    time.sleep(0.1)
    snake.go()
    if snake.out_of_screen() or snake.colotion():
        scordBored.reset_borde()

        snake.reset()


    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scordBored.increase_score()



screen.mainloop()
