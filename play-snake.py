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

    if head.distance(food) < 20:
        # move the food to a random spot
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

    move()
    
    time.sleep(delay)

wn.mainloop()