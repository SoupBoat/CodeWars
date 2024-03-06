import turtle
import random
import time

delay = 0.1

# Set up the screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "left"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []

# Functions
def go_up():
    head.direction = "up"

def go_down():
    head.direction = "down"

def go_left():
    head.direction = "left"

def go_right():
    head.direction = "right"

def stop():
    head.direction = "stop"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Keyboard bindings
wn.listen()
wn.onkeypress(stop, "space")

# Main game loop
while True:
    wn.update()
    print(head.xcor(), head.ycor())
    # Check for collision with the border
    if head.ycor() < -200:
        y = head.ycor()
        head.sety(y + 20)
        go_left()
    print(head.xcor(), head.ycor())

    if head.ycor() > 200:
        y = head.ycor()
        head.sety(y - 20)
        go_right()
    print(head.xcor(), head.ycor())

    if head.xcor() > 200:
        x = head.xcor()
        head.setx(x - 20)
        go_down()
    print(head.xcor(), head.ycor())

    if head.xcor() < -200:
        x = head.xcor()
        head.setx(x + 20)
        go_up()
    print(head.xcor(), head.ycor())

    # Hide the segments
    for segment in segments:
        segment.goto(1000, 1000)
    segments.clear()

    # Check for collision with food
    if head.distance(food) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x, y)

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

    # Move the end segments first in reverse order
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # Check for head collisions with the body segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            # Hide the segments
            for seg in segments:
                seg.goto(1000, 1000)
            segments.clear()

    time.sleep(delay)

wn.mainloop()
