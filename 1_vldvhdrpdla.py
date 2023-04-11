import turtle
import random
import time

def right():
    if player.xcor() < 200:
        player.forward(50)
def left():
    if player.xcor() > 200:
        player.backward(50)

turtle.bgcolor("DarkSeaGreen3")
turtle.setup(500, 700)

player=turtle.Turtle()
player.shape("square")
player.shapesize(1, 5)
player.up()
player.speed(0)
player.goto(0, -270)

turtle.listen()
turtle.onkeypress(right, "Right")
turtle.onkeypress(left, "Left")

