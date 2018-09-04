# Simple Snake Game in Python 3
# By Sander Ruscigno
import turtle
import time
import random

delay = 0.1

# set up the screen
wn = turtle.Screen()
wn.title("Snake Game By @Ruscigno")
wn.bgcolor("green")
wn.setup(width=600, height=600)
wn.tracer(0) #turns off animation

# Snake head
head = turtle.Turtle()
head.speed(0) # animation speed
head.shape("square")
head.color("black")
head.penup() # does not draw anything
head.goto(0,0)
head.direction = "up"

# Snake food
food = turtle.Turtle()
food.speed(0) # animation speed
food.shape("circle")
food.color("red")
food.penup() # does not draw anything
food.goto(0,100)

segments = []

def go_up():
    head.direction = "up"

def go_down():
    head.direction = "down"

def go_left():
    head.direction = "left"

def go_right():
    head.direction = "right"            

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    elif head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    elif head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    elif head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Keyboards bindings
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

# main game loop
while True:
    wn.update()

    # check for a collision with the food
    if head.distance(food) < 20:
        # move the food to a random spot
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("gray")
        new_segment.penup()
        segments.append(new_segment)

    # move the end segment first in reverse order
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    # move segment 0 to the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()
    
    time.sleep(delay)

wn.mainloop()