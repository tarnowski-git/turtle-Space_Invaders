from turtle import Turtle, Screen
from random import randint
from math import sqrt, pow
import winsound


def is_collision(obj_1, obj_2):
    """ Global funcion.
    Uses the Pythagorean Theorem to measure the distance between two objects:
    d = sqrt(pow(x2-x1) + pow(y2-y1))
    """
    if isinstance(obj_1, Turtle) and isinstance(obj_2, Turtle):
        distance = sqrt(pow(obj_2.xcor() - obj_1.xcor(), 2) +
                        pow(obj_2.ycor() - obj_1.ycor(), 2))
        if distance < 15:
            return True
        else:
            return False


class Bullet(Turtle):

    def __init__(self, player):
        Turtle.__init__(self)
        self.color("yellow")
        self.shape("triangle")
        self.penup()
        self.speed(0)
        self.setheading(90)
        self.shapesize(0.5, 0.5)
        self.hideturtle()
        # init
        self.bullet_speed = 20
        self.state = "ready"
        self.player = player

    def fire_bullet(self):
        if self.state == "ready":
            self.play_sound("laser.wav")
            self.state = "fire"
            # Move the bullet to the just above the player
            x = self.player.xcor()
            y = self.player.ycor() + 10
            self.setposition(x, y)
            self.showturtle()

    def reset_positon(self):
        self.hideturtle()
        self.state = "ready"
        self.setposition(0, -400)

    def move_up(self):
        y = self.ycor()
        y += self.bullet_speed
        self.sety(y)

    def play_sound(self, filename):
        winsound.PlaySound("assets\\sounds\\{}".format(
            filename), winsound.SND_ASYNC)


class Invader(Turtle):

    def __init__(self):
        Turtle.__init__(self)
        self.color("red")
        self.shape("assets\\sprites\\invader.gif")
        self.penup()
        self.speed(0)
        # init
        self.invader_speed = 2
        self.reset_positon()

    def move_left_right(self):
        x = self.xcor()
        x += self.invader_speed
        self.setx(x)

    def move_down(self):
        y = self.ycor()
        y -= 40
        self.sety(y)

    def reset_positon(self):
        x = randint(-200, 200)
        y = randint(100, 250)
        self.setposition(x, y)


class Player(Turtle):

    def __init__(self):
        Turtle.__init__(self)
        self.penup()
        self.speed(0)
        self.shape("assets\\sprites\\player.gif")
        self.color("blue")
        self.setposition(0, -250)
        self.setheading(90)
        # init
        self.player_speed = 15

    def move_left(self):
        x = self.xcor()
        x -= self.player_speed
        if x < -280:
            x = -280
        self.setx(x)

    def move_right(self):
        x = self.xcor()
        x += self.player_speed
        if x > 280:
            x = 280
        self.setx(x)


class Border(Turtle):

    def __init__(self):
        Turtle.__init__(self)
        self.penup()
        self.hideturtle()
        self.speed(0)
        self.color("white")
        self.pensize(3)
        # drawing border
        self.draw_border()

    def draw_border(self):
        self.penup()
        self.goto(-300, -300)
        self.pendown()
        self.goto(-300, 300)
        self.goto(300, 300)
        self.goto(300, -300)
        self.goto(-300, -300)


class Score(Turtle):

    def __init__(self):
        Turtle.__init__(self)
        self.speed(0)
        self.color("white")
        self.penup()
        self.setposition(-290, 280)
        self.score = 0
        self.write("Score: {}".format(self.score), False,
                   align="left", font=("Arial", 14, "normal"))
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.write("Score: {}".format(self.score), False,
                   align="left", font=("Arial", 14, "normal"))

    def change_score(self, points):
        self.score += points
        self.update_score()


class Game():
    """Make the game loop into a class.
    Responsible for drawing and updating all our objects"""

    def __init__(self):
        # Set up the screen
        self.screen = Screen()
        self.screen.bgcolor("black")
        self.screen.setup(width=650, height=700)
        self.screen.title("Space Invaders")
        self.screen.bgpic("assets\\sprites\\space_invaders_background.gif")

        # Register the shapes
        self.screen.register_shape("assets\\sprites\\invader.gif")
        self.screen.register_shape("assets\\sprites\\player.gif")

        # initial objects
        self.player = Player()
        self.bullet = Bullet(self.player)
        self.score = Score()
        self.border = Border()
        self.game_over = False

        # Create invaders
        self.number_of_enemies = 5
        self.enemies = []
        for i in range(self.number_of_enemies):
            self.enemies.append(Invader())

        # Create keyboard bindings
        self.screen.listen()
        self.screen.onkey(self.player.move_left, "Left")
        self.screen.onkey(self.player.move_right, "Right")
        self.screen.onkey(self.bullet.fire_bullet, "space")

    def play_sound(self, filename):
        winsound.PlaySound("assets\\sounds\\{}".format(
            filename), winsound.SND_ASYNC)

    def run(self):
        """Make the game loop a function."""
        
        while True:
            # When game_over is set, stop updating objects
            if not self.game_over:

                # for each enemy
                for invader in self.enemies:

                    # Move the enemy left/right
                    invader.move_left_right()

                    # get the enemy back and down
                    if (invader.xcor() < -280 or invader.xcor() > 280):
                        # Move all enemies down
                        for enemy in self.enemies:
                            enemy.move_down()
                            # Change enemy direction
                            enemy.invader_speed *= -1

                    if invader.ycor() < -250:
                        self.game_over = True
                        print("Game Over")

                    if is_collision(self.bullet, invader) == True:
                        self.play_sound("explosion.wav")
                        self.bullet.reset_positon()
                        self.score.change_score(10)
                        invader.reset_positon()

                    if is_collision(self.player, invader) == True:
                        self.player.hideturtle()
                        invader.hideturtle()
                        self.game_over = True
                        print("Game Over")

                # Move the bullet
                if self.bullet.state == "fire":
                    self.bullet.move_up()

                # Check to see if bullet has gone to the top
                if self.bullet.ycor() > 275:
                    self.bullet.reset_positon()

                # Display the screen.
                self.screen.update()

            else:
                break
        # pause game
        input("Press enter to finish")


if __name__ == "__main__":
    Game().run()
