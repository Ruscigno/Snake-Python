# Simple Snake Game in Python 3
# By Sander Ruscigno
import turtle
import time

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

# main game loop
while True:
    wn.update()

    move()
    
    time.sleep(delay)

wn.mainloop()