import turtle
import random

# screen setup :
wn = turtle.Screen()
wn.title("Snake")
wn.bgcolor("blue")
wn.setup(500, 500)

# snake setup:
snake = turtle.Turtle()
snake.speed(0)
snake.shape("square")
snake.color()
snake.color("white")
snake.penup()
snake.goto(0, 0)
snake.direction = "stop"

# food criation:
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(100, 100)


# snake movement:
def move():
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y + 1)

    if snake.direction == "down":
        y = snake.ycor()
        snake.sety(y - 1)

    if snake.direction == "left":
        x = snake.xcor()
        snake.setx(x - 1)

    if snake.direction == "right":
        x = snake.xcor()
        snake.setx(x + 1)


# changing the dir of the snake :

def goUp():
    snake.direction = "up"


def goDown():
    snake.direction = "down"


def goLeft():
    snake.direction = "left"


def goRight():
    snake.direction = "right"


# listen to the keyBoard
wn.listen()
wn.onkeypress(goUp, "Up")
wn.onkeypress(goDown, "Down")
wn.onkeypress(goLeft, "Left")
wn.onkeypress(goRight, "Right")


# create loop for the game :
while True:
    wn.update()

    if snake.distance(food) < 10:
        x = random.randint(-245, 245)
        y = random.randint(-245, 245)
        food.goto(x, y)
    move()






wn.mainloop()
