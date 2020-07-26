import turtle

#---------------------------------------------------
# PADDLE A MOVEMENT FUNCTIONS
#---------------------------------------------------
def paddle_a_up(pad_a: turtle.Turtle) -> None:
    """
    Moves paddle a up by 20 pixels each time "w" is pressed.
    """
    y = pad_a.ycor()
    y += 20
    pad_a.sety(y)
    
def paddle_a_down(pad_a: turtle.Turtle) -> None:
    """
    Moves paddle a down by 20 pixels each time "s" is pressed.
    """
    y = pad_a.ycor()
    y -= 20
    pad_a.sety(y)
#---------------------------------------------------

#---------------------------------------------------
# PADDLE B MOVEMENT FUNCTIONS
#---------------------------------------------------
def paddle_b_up(pad_b: turtle.Turtle) -> None:
    """
    Moves paddle a up by 20 pixels each time "w" is pressed.
    """
    y = pad_b.ycor()
    y += 20
    pad_b.sety(y)
    
def paddle_b_down(pad_b: turtle.Turtle) -> None:
    """
    Moves paddle a down by 20 pixels each time "s" is pressed.
    """
    y = pad_b.ycor()
    y -= 20
    pad_b.sety(y)

#---------------------------------------------------