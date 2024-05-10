import turtle

import random
import time

# creating screen
screen = turtle.Screen()
screen.title("snake")
screen.setup(width=700, height=700)
screen.tracer(0)
screen.bgcolor("#1d1d1d")
# creating border
turtle.speed(5)
turtle.pensize(4)
turtle.penup()
turtle.goto(-300, 250)
turtle.pendown()
turtle.color("red")
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.right(90)
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.right(90)
turtle.penup()
turtle.hideturtle()


# scores
score = 0
delay = 0.1

# snake
snake = turtle.Turtle()
snake.speed()
snake.shape("square")
snake.color('GREEN')
snake.penup()
snake.goto(0, 0)
snake.direction = 'stop'

# food
fruit = turtle.Turtle()
fruit.speed(0)
fruit.shape("circle")
fruit.color("white")
fruit.penup()
fruit.goto(30, 30)

old_fruit = []

# scoring
scoring = turtle.Turtle()
scoring.speed(0)
scoring.color("white")
scoring.penup()
scoring.hideturtle()
scoring.goto(0, 300)
scoring.write("score", align="center", font=("courier", 24, "bold"))


# defining movements
def snake_go_up():
    if snake.direction != "down":
        snake.direction = "up"


def snake_go_down():
    if snake.direction != "up":
        snake.direction = "down"


def snake_go_left():
    if snake.direction != "right":
        snake.direction = "left"


def snake_go_right():
    if snake.direction != "left":
        snake.direction = "right"


def snake_move():
    if snake.direction == "up":
        c = snake.ycor()
        snake.sety(c + 20)

    if snake.direction == "down":
        c = snake.ycor()
        snake.sety(c - 20)

    if snake.direction == "left":
        d = snake.xcor()
        snake.setx(d - 20)

    if snake.direction == "right":
        d = snake.xcor()
        snake.setx(d + 20)


# defining keyboards
screen.listen()
screen.onkeypress(snake_go_up, "Up")
screen.onkeypress(snake_go_down, "Down")
screen.onkeypress(snake_go_left, "Left")
screen.onkeypress(snake_go_right, "Right")

# main loop
while True:
    screen.update()

    # snake and food  collision
    if snake.distance(fruit) < 20:
        x = random.randint(-290, 270)
        y = random.randint(-240, 240)
        fruit.goto(x, y)
        scoring.clear()
        score += 1
        scoring.write("score {}".format(score), align="center", font=("courier", 24, "bold"))
        delay -= 0.001
        # creating new fruits
        new_fruit = turtle.Turtle()
        new_fruit.speed(0)
        new_fruit.shape("square")
        new_fruit.color("red")
        new_fruit.penup()
        old_fruit.append(new_fruit)
    # adding ball
    for index in range(len(old_fruit), -1, 1):
        a = old_fruit[index - 1].xcor()
        b = old_fruit[index - 1].ycor()

        old_fruit[index].goto(a, b)

    if len(old_fruit) > 0:
        a = snake.xcor()
        b = snake.ycor()
        old_fruit[0].goto(a, b)

    snake_move()

    # snake and border collision
    if snake.xcor() > 200 or snake.xcor() < -300 or snake.ycor() > 240 or snake.ycor() < -240:
        time.sleep(1)
        screen.clear()
        screen.bgcolor("turquoise")
        scoring.goto(0, 0)
        scoring.write("  Game over \n Your score is {}:".format(score), align="center", font=("courier", 30, "bold"))

    # snake collision
    for food in old_fruit:
        if food.distance(snake) < 20:
            time.sleep(1)
            screen.clear()
            screen.bgcolor("turquoise")
            scoring.goto(0, 0)
            scoring.write("  Game over \n Your score is {}:".format(score), align="center",
                          font=("courier", 30, "bold"))

    time.sleep(delay)

    turtle.Terminator()


