import turtle
import winsound

# Main Screen
screen = turtle.Screen()
screen.title("Pong kkk")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

# Elements
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
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = 0.2

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
# Keyboard


screen.listen()
screen.onkeypress(paddle_a_up, "w")
screen.onkeypress(paddle_a_down, "s")
screen.onkeypress(paddle_b_up, "Up")
screen.onkeypress(paddle_b_down, "Down")

score_a = 0
score_b = 0
while True:
    screen.update()

    # ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # collision with the upper wall

    if ball.ycor() > 290:
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        ball.sety(290)
        ball.dy *= -1

    # collision with the lower wall

    if ball.ycor() < -290:
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        ball.sety(-290)
        ball.dy *= -1

    # collision with left wall

    if ball.xcor() < -390:
        score_b += 1
        hud.clear()
        hud.write(f"{score_a} : {score_b}", align="center", font=("Comic "
                                                                  "Sans",
                                                                  24,
                                                                  "normal"))
        winsound.PlaySound("258020__kodack__arcade-bleep-sound.wav", winsound.SND_ASYNC)
        ball.goto(0, 0)
        ball.dx *= -1

    # collision with right wall

    if ball.xcor() > 390:
        score_a += 1
        hud.clear()
        hud.write(f"{score_a} : {score_b}", align="center", font=("Comic "
                                                                  "Sans",
                                                                  24,
                                                                  "normal"))
        winsound.PlaySound("258020__kodack__arcade-bleep-sound.wav", winsound.SND_ASYNC)                                                                  
        ball.goto(0, 0)
        ball.dx *= -1
        
    # collision with paddle 1

    #if ball.xcor() < -330 and paddle_a.ycor() + 50 > ball.ycor() > paddle_a.ycor() - 50:
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        ball.dx *= -1

    # collision with paddle 2

    #if ball.xcor() > 330 and paddle_b.ycor()+50 > ball.ycor() > paddle_b.ycor() - 50:
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        ball.dx *= -1


