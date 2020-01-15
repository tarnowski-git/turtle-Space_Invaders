import turtle
import os

# Set up the screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(width=650, height=650)
wn.title("Space Invaders")

# Draw border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.forward(600)
    border_pen.left(90)

# Create the player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

playerSpeed = 15

# Create the enemy
enemy = turtle.Turtle()
enemy.color("red")
enemy.shape("circle")
enemy.penup()
enemy.speed(0)
enemy.setposition(-200, 250)

enemySpeed = 2


def move_left():
    # Move the player left and right
    x = player.xcor()
    x -= playerSpeed
    if x < -280:
        x = -280
    player.setx(x)


def move_right():
    # check current X position
    x = player.xcor()
    # change position
    x += playerSpeed
    # bordery checking
    if x > 280:
        x = 280
    # update the location
    player.setx(x)


# Create keyboard bindings
wn.listen()
wn.onkey(move_left, "Left")
wn.onkey(move_right, "Right")

# Main game loop
while True:

    # Move the enemy
    x = enemy.xcor()
    x += enemySpeed
    enemy.setx(x)

    # get the enemy back and down
    if enemy.xcor() > 280:
        y = enemy.ycor()
        y -= 40
        enemySpeed *= -1
        enemy.sety(y)

    if enemy.xcor() < -280:
        y = enemy.ycor()
        y -= 40
        enemySpeed *= -1
        enemy.sety(y)

delay = input("Press enter to finish")
