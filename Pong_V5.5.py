import turtle  # Main tool we'll need to draw and control the game
import winsound  # We'll use to allow sound to play within the gameplay

# Draw a Screen which we'll use to work in

screen = turtle.Screen()
screen.title("Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)  # no alterations in speed or functioning of turtle

# Elements

# Add paddles and ball before adding movement, control and mechanics
# Add Hud
# Both the paddles and the ball are stationary turtle drawings with a set of
# characteristics, speed(0) = stops all movement from turtle, penup() =
# makes so turtle doesn't draw lines when the object moves

# Draw paddle 1

paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Draw paddle 2

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Draw ball

# we used vel_x and vel_y to simplify the base speed for the change in speed
# within collision functions ahead

vel_x = 0.2
vel_y = 0.2

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = vel_x
ball.dy = vel_y

# Hud

# Use the turtle to get to a position, hide the turtle and write the base
# score

hud = turtle.Turtle()
hud.speed(0)
hud.shape("square")
hud.color("white")
hud.penup()
hud.hideturtle()
hud.goto(0, 250)
hud.write("0 ; 0", align="center", font=("Small Fonts", 24, "normal"))


# Movement

# Paddle 1 Movement upwards


def paddle_a_up():
    """ in this and all functions within Movement, we'll assign a single
    change in
    the y-axis position of the paddles, which we'll trigger by a key press in
    the next implementation
    """
    y = paddle_a.ycor()
    if y < 250:
        y += 30
    else:
        y = 250
    paddle_a.sety(y)


# Paddle 1 Movement downwards


def paddle_a_down():
    """ in this and all functions within Movement, we'll assign a single
    change in
    the y-axis position of the paddles, which we'll trigger by a key press in
    the next implementation
    """
    y = paddle_a.ycor()
    if y > -250:
        y += -30
    else:
        y = -250
    paddle_a.sety(y)


# Paddle 2 Movement upwards


def paddle_b_up():
    """ in this and all functions within Movement, we'll assign a single
    change in
    the y-axis position of the paddles, which we'll trigger by a key press in
    the next implementation
    """
    y = paddle_b.ycor()
    if y < 250:
        y += 30
    else:
        y = 250
    paddle_b.sety(y)


# Paddle 2 Movement downwards


def paddle_b_down():
    """ in this and all functions within Movement, we'll assign a single
    change in
    the y-axis position of the paddles, which we'll trigger by a key press in
    the next implementation
    """
    y = paddle_b.ycor()
    if y > -250:
        y += -30
    else:
        y = -250
    paddle_b.sety(y)


# Songs


def song1():
    """ This functions opem the .wav within the same directory as the .py
    file and make it so only the sound plays, and the winsound.SND_ASYNC allows
    for the code to continue without the sound having to end first
    """
    winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)


def song2():
    """ This functions opem the .wav within the same directory as the .py
    file and make it so only the sound plays, and the winsound.SND_ASYNC allows
    for the code to continue without the sound having to end first
        """
    winsound.PlaySound(
        "258020__kodack__arcade-bleep-sound.wav", winsound.SND_ASYNC
    )


# pause

is_paused = False


def pause_opt():
    """Function used to switch between two states"""
    global is_paused
    if is_paused:
        is_paused = False
    else:
        is_paused = True


# score

# Values we'll use to change the hud depending on collision with the left
# and right wall

score_a = 0
score_b = 0

# Keyboard

# the following methods assign the respective functions to a key press and
# will make sense within the while True structure ahead

screen.listen()
screen.onkeypress(paddle_a_up, "w")
screen.onkeypress(paddle_a_down, "s")
screen.onkeypress(paddle_b_up, "Up")
screen.onkeypress(paddle_b_down, "Down")
screen.onkeypress(pause_opt, "p")

# Gameplay Loop


cont = 0
while True:
    if is_paused:
        # make it so pressing p will stop everything and show
        # "Paused" in the hud, and pressing again will resume the normal
        # functioning of the code, without a change in score.
        hud.clear()
        hud.write("Paused", align="center", font=("Courier", 24, "normal"))
        screen.addshape("icegif-5447.gif")
    else:
        screen.update()

        hud.clear()
        hud.write(
            f"{score_a} : {score_b}",
            align="center",
            font=("Courier", 24, "normal"), )  # Changes the hud to match the
        # score of the game

        # ball movement

        # use the ball.dx-ball.dy to refresh both the axis's at every instance
        # indefinitely(depending on the ball.dx-ball.dy)

        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # Collision

        # the method used to simulate collision with walls here is to check
        # when the ball reaches a certain threshold within the space and
        # play a sound while reverting-changing the relevant axis and
        # returning ball attributes to previous states.

        # collision with the upper wall

        if ball.ycor() > 290:
            song1()
            ball.sety(290)
            ball.dy *= -1

        # collision with the lower wall

        if ball.ycor() < -290:
            song1()
            ball.sety(-290)
            ball.dy *= -1

        # collision with left wall

        if ball.xcor() < -390:
            score_b += 1
            hud.clear()
            hud.write(
                f"{score_a} : {score_b}",
                align="center",
                font=("Courier", 24, "normal"),
            )

            song2()
            ball.goto(0, 0)
            ball.dx = vel_x

        # collision with right wall

        if ball.xcor() > 390:
            score_a += 1
            hud.clear()
            hud.write(
                f"{score_a} : {score_b}",
                align="center", font=("Courier", 24, "normal"), )

            song2()
            ball.goto(0, 0)
            ball.dx = vel_x
            ball.dx *= -1  # Make it so the ball goes to the left if it came
            # from the right

        # collision with paddle 1

        # paddles check whether if the ball hits the space in the middle or
        # the space near the edges and changes directions accordingly

        if (340 < ball.xcor() < 350) and \
                (paddle_b.ycor() + 25 > ball.ycor() > paddle_b.ycor() - 25):
            ball.setx(340)
            ball.dx *= -1  # flip direction first

        if (340 < ball.xcor() < 350) and \
                (((ball.ycor() >= paddle_b.ycor() + 25)
                  and (ball.ycor() < paddle_b.ycor() + 50))
                 or
                 ((ball.ycor() <= paddle_b.ycor() - 25)
                  and (ball.ycor() > paddle_b.ycor() - 50))):
            ball.setx(340)
            ball.dx *= -1  # flip direction first
            ball.dx -= 0.1  # speed it up

        # collision with paddle 2

        if (-340 > ball.xcor() > -350) and \
                (paddle_a.ycor() + 25 > ball.ycor() > paddle_a.ycor() - 25):
            ball.setx(-340)
            ball.dx *= -1
        if (-340 > ball.xcor() > -350) and \
                (((ball.ycor() >= paddle_a.ycor() + 25)
                  and (ball.ycor() < paddle_a.ycor() + 50))
                 or
                 ((ball.ycor() <= paddle_a.ycor() - 25)
                  and (ball.ycor() > paddle_a.ycor() - 50))):
            ball.setx(-340)
            ball.dx *= -1
            ball.dx += 0.1
