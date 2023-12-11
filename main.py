# Pong Game

# A simple gaming module
import turtle

# Create game window
wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)  # stops the window from updating. Lets us speed up game?

# Paddle A Graphics
paddle_a = turtle.Turtle()
paddle_a.speed(0)  # speed of animation. Set to max speed
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()  # graphical drawing style
paddle_a.goto(-350, 0)  # starting position of paddle_a

# Paddle B Graphics
paddle_b = turtle.Turtle()
paddle_b.speed(0)  # speed of animation. Set to max speed
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()  # graphical drawing style
paddle_b.goto(350, 0)  # starting position of paddle_b

# Ball Graphics
ball = turtle.Turtle()
ball.speed(0)  # speed of animation. Set to max speed
ball.shape("square")
ball.color("white")
ball.penup()  # graphical drawing style
ball.goto(0, 0)  # starting position of paddle_b

# Ball movement speed
ball.dx = 0.075  # move by 2px
ball.dy = -0.075

# Pen object to write score graphic
pen = turtle.Turtle()
pen.speed(0)  # animation speed
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player 1: 0    Player 2: 0", align="center", font=("Courier", 24, "normal"))

# Score logic
score_a = 0
score_b = 0


# Game control functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# Keyboard binding
wn.listen()  # tells window to listen for keyboard inputs
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        score_a += 1
        pen.clear()
        pen.write(f"Player 1: {score_a}    Player 2: {score_b}", align="center", font=("Courier", 24, "normal"))
        ball.dx *= -1  # reverse direction to other player

    if ball.xcor() < -390:
        ball.goto(0, 0)
        score_b += 1
        pen.clear()
        pen.write(f"Player 1: {score_a}    Player 2: {score_b}", align="center", font=("Courier", 24, "normal"))
        ball.dx *= -1  # reverse direction to other player

    # If ball hits paddle_a
    if ball.xcor() < -340 and paddle_a.ycor() - 50 < ball.ycor() < paddle_a.ycor() + 50:
        ball.dx *= -1

    # If ball hits paddle_b
    if ball.xcor() > 340 and paddle_b.ycor() - 50 < ball.ycor() < paddle_b.ycor() + 50:
        ball.dx *= -1
