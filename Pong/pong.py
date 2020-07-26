import turtle
import winsound
import mvmnt


# Setting up the window
window = turtle.Screen()
window.title("Pong")  # Changes the name at the top left of the window
window.bgcolor("black") # Changes the background color for the window
window.bgpic("background.png")
window.setup(width=800, height=600) # Sets up the dimensions for the screen
window.tracer(0) # Stops window from updating; forces up to manually update and allows for speeding up the game


# Creating the objects within the game

# Paddle A
pad_a = turtle.Turtle()
pad_a.speed(0) # Speed of animation; Sets to maximum speed
pad_a.shape("square")
pad_a.shapesize(stretch_wid=5, stretch_len=1)
pad_a.color("white")
pad_a.penup()
pad_a.goto(-350, 0)

# Paddle B
pad_b = turtle.Turtle()
pad_b.speed(0) # Speed of animation; Sets to maximum speed
pad_b.shape("square")
pad_b.shapesize(stretch_wid=5, stretch_len=1)
pad_b.color("white")
pad_b.penup()
pad_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0) # Speed of animation; Sets to maximum speed
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx, ball.dy = 0.2, 0.2  # Ball speed

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle() # Hides pen cursor
pen.goto(0, 260)
pen.write("Player A: 0      Player B: 0", align="center", font=("Comic Sans", 25, "normal"))

# Score
score_a, score_b = 0, 0


#---------------------------------------------------
# PADDLE A MOVEMENT FUNCTIONS
#---------------------------------------------------
def paddle_a_up() -> None:
    """
    Moves paddle a up by 20 pixels each time "w" is pressed.
    """
    y = pad_a.ycor()
    y += 20
    pad_a.sety(y)

def paddle_a_down() -> None:
    """
    Moves paddle a down by 20 pixels each time "s" is pressed.
    """
    y = pad_a.ycor()
    y -= 20
    pad_a.sety(y)

#---------------------------------------------------
# PADDLE B MOVEMENT FUNCTIONS
#---------------------------------------------------
def paddle_b_up() -> None:
    """
    Moves paddle a up by 20 pixels each time up arrow is pressed.
    """
    y = pad_b.ycor()
    y += 20
    pad_b.sety(y)

def paddle_b_down() -> None:
    """
    Moves paddle a down by 20 pixels each time the down arrow is pressed.
    """
    y = pad_b.ycor()
    y -= 20
    pad_b.sety(y)


# Keyboard binding
window.listen()
window.onkeypress(paddle_a_up, "w")
window.onkeypress(paddle_a_down, "s")
window.onkeypress(paddle_b_up, "Up")
window.onkeypress(paddle_b_down, "Down")

# Main game loop; Every game has one:
running = True
while running:
    try:
        window.update()
        
        #----------------------------------------------------
        # Moving the ball
        #----------------------------------------------------
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        #----------------------------------------------------
        # BORDER CHECKING
        #----------------------------------------------------
        if ball.ycor() > 290:
            ball.sety(290)
            winsound.PlaySound("sound_files/border.wav", winsound.SND_ASYNC)
            ball.dy *= -1
            
        if ball.ycor() < -290:
            ball.sety(-290)
            winsound.PlaySound("sound_files/border.wav", winsound.SND_ASYNC)
            ball.dy *= -1
        
        if ball.xcor() > 390:
            winsound.PlaySound("sound_files/winsound.wav", winsound.SND_ASYNC)
            ball.goto(0, 0)
            ball.dx *= -1
            score_a += 1
            pen.clear() # Updating Score
            pen.write(f"Player A: {score_a}      Player B: {score_b}", align="center", font=("Comic Sans", 25, "normal"))

        if ball.xcor() < -390:
            winsound.PlaySound("sound_files/winsound.wav", winsound.SND_ASYNC)
            ball.goto(0, 0)
            ball.dx *= -1
            score_b += 1
            pen.clear() # Updating Score
            pen.write(f"Player A: {score_a}      Player B: {score_b}", align="center", font=("Comic Sans", 25, "normal"))

        #----------------------------------------------------
        # COLLISION DETECTION
        #----------------------------------------------------
        if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < pad_b.ycor() + 40 and ball.ycor() > pad_b.ycor() - 40):
            ball.setx(340)
            winsound.PlaySound("sound_files/pad_collision.wav", winsound.SND_ASYNC)
            ball.dx *= -1
        
        if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < pad_a.ycor() + 40 and ball.ycor() > pad_a.ycor() - 40):
            ball.setx(-340)
            winsound.PlaySound("sound_files/pad_collision.wav", winsound.SND_ASYNC)
            ball.dx *= -1
    except:
        running = False

    