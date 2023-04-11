import turtle
import random
import time

def right():
    if player.xcor() < 200:
        player.forward(50)
def left():
    if player.xcor() > -200:
        player.backward(50)

turtle.bgcolor("DarkSeaGreen3")
turtle.setup(500, 700)

player=turtle.Turtle()
player.shape("square")
player.shapesize(1, 5)
player.up()
player.speed(0)
player.goto(0, -270)
player.color("DarkSlateGray")

ball = turtle.Turtle()
ball.shape("circle")
ball.shapesize(1,1)
ball.up()
ball.speed(0)
ball.color("aquamarine4")

turtle.listen()
turtle.onkeypress(right, "Right")
turtle.onkeypress(left, "Left")

ball_xspeed = 6
ball_yspeed = 7
game_on = True
life = 3

turtle.up()
turtle.ht()
turtle.goto(0, 300)
turtle.write(f"life : {life}", False, "center", ("", 20))

while game_on:
    new_x = ball.xcor() + ball_xspeed
    new_y = ball.ycor() + ball_yspeed
    ball.goto(new_x, new_y)

    if ball.xcor() > 240 or ball.xcor() < -240:
        ball_xspeed *= -1
    if ball.ycor() > 340:
        ball_yspeed *= -1
    if ball.ycor() < -340:
        life -= 1
        turtle.clear()
        turtle.write(f"life : {life}", False, "center", ("", 20))
        time.sleep(1)
        ball.goto(0,0)
        ball_xspeed = 6
        ball_yspeed = 7
    if ball_xspeed**2 < 0.25:
        life += 1
        turtle.clear()
        turtle.write(f"life : {life}", False, "center", ("", 20))
        time.sleep(1)
        ball.goto(0,0)
        ball_xspeed = 7
        ball_yspeed = 7 
    ball_yspeed -= 0.1
    ball_xspeed *= 0.9995
    if player.distance(ball) < 50 and -260 < ball.ycor() < -245:
        ball_yspeed *= -1
    if life == 0:
        game_on = False
        turtle.goto(0,0)
        turtle.write("Game Over",False, "center",("", 20))
        time.sleep(2)
