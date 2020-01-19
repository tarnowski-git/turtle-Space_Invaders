import turtle
import math
import os
import random

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

# Choose a number of enemies
numer_of_enemies = 5
# Create an empty list
enemies = []
# Add enemies to the list
for i in range(numer_of_enemies):
    # Create the enemy
    enemies.append(turtle.Turtle())

for enemy in enemies:
    enemy.color("red")
    enemy.shape("circle")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    enemy.setposition(x, y)


enemySpeed = 2

# Create the player's bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletSpeed = 20

# Define bullet state
# Ready - ready to fire
# fire - bullet is firing
bulletState = "ready"


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


def fire_bullet():
    # Declare bulletState as a global if it needs changed
    global bulletState
    if bulletState == "ready":
        bulletState = "fire"
        # Move the bullet to the just above the player
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x, y)
        bullet.showturtle()


def isCollision(t1, t2):
    # Distance formula
    # d = sqrt(pow(x2-x1) + pow(y2-y1))
    distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) +
                         math.pow(t1.ycor() - t2.ycor(), 2))
    if distance < 15:
        return True
    else:
        return False


# Create keyboard bindings
wn.listen()
wn.onkey(move_left, "Left")
wn.onkey(move_right, "Right")
wn.onkey(fire_bullet, "space")

# Main game loop
while True:

    for enemy in enemies:
        # Move the enemy
        x = enemy.xcor()
        x += enemySpeed
        enemy.setx(x)

        # get the enemy back and down
        if enemy.xcor() > 280:
            # Move all enemies down
            for e in enemies:
                y = enemy.ycor()
                y -= 40
                e.sety(y)
            # Change enemy direction
            enemySpeed *= -1

        if enemy.xcor() < -280:
            # Move all enemies down
            for e in enemies:
                y = enemy.ycor()
                y -= 40
                e.sety(y)
            enemySpeed *= -1

        # Check for a collison between the bullet and the enemy
        if isCollision(bullet, enemy) == True:
            # Reset the bullet
            bullet.hideturtle()
            bulletState = "ready"
            bullet.setposition(0, -400)
            # Reset the enemy
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            enemy.setposition(x, y)

        if isCollision(player, enemy) == True:
            player.hideturtle()
            enemy.hideturtle()
            print("Game Over")
            break

    # Move the bullet
    if bulletState == "fire":
        y = bullet.ycor()
        y += bulletSpeed
        bullet.sety(y)

    # Check to see if bullet has gone to the top
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletState = "ready"


delay = input("Press enter to finish")
