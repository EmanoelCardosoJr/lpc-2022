import turtle
import winsound

# Main Screen
screen = turtle.Screen()
screen.title("Pong kkk")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

# Elements
#
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
hud = turtle.Turtle()
hud.speed(0)
hud.shape("square")
hud.color("white")
hud.penup()
hud.hideturtle()
hud.goto(0, 250)
hud.write("0 ; 0", align="center", font=("Small Fonts", 24, "normal"))


# Movement
#
# Paddle 1 Movement upwards


def paddle_a_up():
    y = paddle_a.ycor()
    if y < 250:
        y += 30
    else:
        y = 250
    paddle_a.sety(y)


# Paddle 1 Movement downwards


def paddle_a_down():
    y = paddle_a.ycor()
    if y > -250:
        y += -30
    else:
        y = -250
    paddle_a.sety(y)


# Paddle 2 Movement upwards


def paddle_b_up():
    y = paddle_b.ycor()
    if y < 250:
        y += 30
    else:
        y = 250
    paddle_b.sety(y)


# Paddle 2 Movement downwards


def paddle_b_down():
    y = paddle_b.ycor()
    if y > -250:
        y += -30
    else:
        y = -250
    paddle_b.sety(y)


# songs


song_1 = "bounce.wav"
song_2 = "258020__kodack__arcade-bleep-sound.wav"


def song1():
    winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)


def song2():
    winsound.PlaySound("258020__kodack__arcade-bleep-sound.wav", winsound.SND_ASYNC)


# pause

is_paused = False


def pause_opt():
    global is_paused
    if is_paused == True:
        is_paused = False
    else:
        is_paused = True


# score

score_a = 0
score_b = 0

# Keyboard

screen.listen()
screen.onkeypress(paddle_a_up, "w")
screen.onkeypress(paddle_a_down, "s")
screen.onkeypress(paddle_b_up, "Up")
screen.onkeypress(paddle_b_down, "Down")
screen.onkeypress(pause_opt, "p")

cont = 0
while True:
    if is_paused:
        hud.clear()
        hud.write("Paused", align="center", font=("Courier", 24, "normal"))
    else:
        screen.update()

        hud.clear()
        hud.write(
            f"{score_a} : {score_b}", align="center", font=("Courier", 24, "normal")
        )

        # ball movement
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # collision with the upper wall

        if ball.ycor() > 290:
            # winsound.PlaySound(song_1, winsound.SND_ASYNC)
            song1()
            ball.sety(290)
            ball.dy *= -1
        # collision with the lower wall

        if ball.ycor() < -290:
            # winsound.PlaySound(song_1, winsound.SND_ASYNC)
            song1()
            ball.sety(-290)
            ball.dy *= -1
        # collision with left wall

        if ball.xcor() < -390:
            score_b += 1
            hud.clear()
            hud.write(
                f"{score_a} : {score_b}", align="center", font=("Courier", 24, "normal")
            )
            # winsound.PlaySound(song_2, winsound.SND_ASYNC)
            song2()
            ball.goto(0, 0)
            ball.dx = vel_x
        # collision with right wall

        if ball.xcor() > 390:
            score_a += 1
            hud.clear()
            hud.write(
                f"{score_a} : {score_b}", align="center", font=("Courier", 24, "normal")
            )
            # winsound.PlaySound(song_2, winsound.SND_ASYNC)
            song2()
            ball.goto(0, 0)
            ball.dx = vel_x
            ball.dx *= -1
        # collision with paddle 1

        # if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
        if (ball.xcor() > 340 and ball.xcor() < 350) and (
            ball.ycor() < paddle_b.ycor() + 25 and ball.ycor() > paddle_b.ycor() - 25
        ):
            ball.setx(340)
            ball.dx *= -1  # flip direction first
        if (ball.xcor() > 340 and ball.xcor() < 350) and (
            (
                (ball.ycor() >= paddle_b.ycor() + 25)
                and (ball.ycor() < paddle_b.ycor() + 50)
            )
            or (
                (ball.ycor() <= paddle_b.ycor() - 25)
                and (ball.ycor() > paddle_b.ycor() - 50)
            )
        ):
            ball.setx(340)
            ball.dx *= -1  # flip direction first
            ball.dx -= 0.1  # speed it up
        # collision with paddle 2

        # if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        if (ball.xcor() < -340 and ball.xcor() > -350) and (
            ball.ycor() < paddle_a.ycor() + 25 and ball.ycor() > paddle_a.ycor() - 25
        ):
            ball.setx(-340)
            ball.dx *= -1
        if (ball.xcor() < -340 and ball.xcor() > -350) and (
            (
                (ball.ycor() >= paddle_a.ycor() + 25)
                and (ball.ycor() < paddle_a.ycor() + 50)
            )
            or (
                (ball.ycor() <= paddle_a.ycor() - 25)
                and (ball.ycor() > paddle_a.ycor() - 50)
            )
        ):
            ball.setx(-340)
            ball.dx *= -1
            ball.dx += 0.1
