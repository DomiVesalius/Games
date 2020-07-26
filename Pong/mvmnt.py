import turtle

def paddle_a_up(paddle_a: turtle.Turtle) -> int:
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)
    
