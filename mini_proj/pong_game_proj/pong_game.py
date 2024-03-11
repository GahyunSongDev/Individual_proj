import turtle, time

# Create a player bar - left side
player_1 = turtle.Turtle()
player_1.shape("square")
player_1.shapesize(stretch_wid = 4, stretch_len = 1)
player_1.color("white")
player_1.shapesize()
player_1.penup()    # there's no line to be drawn whenever the turtle moves
player_1.goto(-330, 0)

# Create a player bar = right side
player_2 = turtle.Turtle()
player_2.shape("square")
player_2.shapesize(stretch_wid = 4, stretch_len = 1)
player_2.color("white")
player_2.shapesize()
player_2.penup()    # there's no line to be drawn whenever the turtle moves
player_2.goto(320, 0)

# Create a ball to pong
ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()    # there's no line to be drawn whenever the turtle moves
ball.goto(0, 0)
ball.dx = 2
ball.dy = -2

# Initialize scores and time
score_player_1 = 0
score_player_2 = 0
start_time = time.time()
speed_increase_time = start_time + 60  # Increase speed every 1 minute

# Create a screen 
def __init_game__():
    turtle.Screen()
    turtle.bgcolor("dark blue")
    turtle.setup(height = 800, width = 700)
    turtle.title("pong game - mini project by gahyun song")
    turtle.tracer(0)

# function for moving a bar up and down for player 1 and 2
def bar_up_p1():
    up = player_1.ycor() + 25
    if up < 350:
        player_1.sety(up)
def bar_down_p1():
    down = player_1.ycor() - 25
    if down > -350:
        player_1.sety(down)
def bar_up_p2():
    up = player_2.ycor() + 25
    if up < 350:
        player_2.sety(up)
def bar_down_p2():
    down = player_2.ycor() - 25
    if down > -350:
        player_2.sety(down)
        
def exit_game():
    turtle.clear()  # Clear the existing text
    turtle.hideturtle()
    turtle.bgcolor("white")
    turtle.color("grey")

    # Display the winner and scores
    if score_player_1 > score_player_2:
        turtle.goto(0, 100)
        turtle.write("Player 1 Wins!", align="center", font=("Courier", 36, "normal"))
        turtle.goto(0, 0)
        turtle.write(f"Player 1: {score_player_1}", align="center", font=("Courier", 24, "normal"))
        turtle.goto(0, -50)
        turtle.write(f"Player 2: {score_player_2}", align="center", font=("Courier", 24, "normal"))
        turtle.goto(0, -300)
        turtle.write(f"Time: {int(elapsed_time)} seconds", align="center", font=("Courier", 18, "normal"))
    elif score_player_1 < score_player_2:
        turtle.goto(0, 100)
        turtle.write("Player 2 Wins!", align="center", font=("Courier", 36, "normal"))
        turtle.goto(0, 0)
        turtle.write(f"Player 1: {score_player_1}", align="center", font=("Courier", 24, "normal"))
        turtle.goto(0, -50)
        turtle.write(f"Player 2: {score_player_2}", align="center", font=("Courier", 24, "normal"))
        turtle.goto(0, -300)
        turtle.write(f"Time: {int(elapsed_time)} seconds", align="center", font=("Courier", 18, "normal"))
    else:
        turtle.goto(0, 0)
        turtle.write("It's a Tie!", align="center", font=("Courier", 36, "normal"))
        turtle.goto(0, -50)
        turtle.write(f"Player 1: {score_player_1}", align="center", font=("Courier", 24, "normal"))
        turtle.goto(0, -100)
        turtle.write(f"Player 2: {score_player_2}", align="center", font=("Courier", 24, "normal"))
        turtle.goto(0, -300)
        turtle.write(f"Time: {int(elapsed_time)} seconds", align="center", font=("Courier", 18, "normal"))

    # Display option to play again or quit
    turtle.goto(0, 300)  # Adjust the y-coordinate as needed
    turtle.color("gray")
    turtle.write("Enter 'y' for Play Again or 'p' for Stop playing", align="center", font=("Courier", 18, "normal"))

    # Wait for user input
    turtle.listen()
    turtle.onkeypress(turtle.bye, "p")
    turtle.onkeypress(play_game, "y")  # Press 'y' to play again
    turtle.mainloop()
                                                                                 
def play_game():

    global score_player_1, score_player_2, speed_increase_time, elapsed_time

    while True:

        __init_game__()

        turtle.listen()
        turtle.onkeypress(bar_up_p1, "w")
        turtle.onkeypress(bar_down_p1, "s")
        turtle.onkeypress(bar_up_p2, "Up")
        turtle.onkeypress(bar_down_p2, "Down")
        turtle.onkeypress(exit_game, "q")  # Press 'q' to exit the game
        turtle.onkeypress(turtle.bye, "p")

        # Set the boundary for the ball to move
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        if ball.ycor() > 340:
            ball.sety(340)
            ball.dy *= -1

        if ball.ycor() < -340:
            ball.sety(-340)
            ball.dy *= -1

        if ball.xcor() > 335:
            ball.setx(335)
            ball.dx *= -1
            score_player_1 += 1

        if ball.xcor() < -340:
            ball.setx(-340)
            ball.dx *= -1
            score_player_2 += 1

        if (player_1.xcor() - 20 < ball.xcor() < player_1.xcor() + 20) and (player_1.ycor() + 50 > ball.ycor() > player_1.ycor() - 50):
            ball.setx(player_1.xcor() + 20)
            ball.dx *= -1

        if (player_2.xcor() - 20 < ball.xcor() < player_2.xcor() + 20) and (player_2.ycor() + 50 > ball.ycor() > player_2.ycor() - 50):
            ball.setx(player_2.xcor() - 20)
            ball.dx *= -1

        # Display the score and elapsed time
        elapsed_time = time.time() - start_time
        turtle.clear()
        turtle.penup()
        turtle.hideturtle()
        turtle.goto(0, 300)

        # Set text color to light gray
        turtle.color("yellow")

        turtle.write(f"Player 1: {score_player_1}  Player 2: {score_player_2}", align="center", font=("Courier", 24, "normal"))
        turtle.goto(0, -350)
        turtle.write(f"Time: {int(elapsed_time)} seconds", align="center", font=("Courier", 18, "normal"))

        # Increase ball speed every 1 minute
        if time.time() > speed_increase_time:
            ball.dx *= 1.5  # Increase x-axis speed by 1.5 times
            ball.dy *= 1.5  # Increase y-axis speed by 1.5 times
            speed_increase_time += 60  # Set the next speed increase time

        # Optional: Set the game speed by adjusting the sleep time
        time.sleep(0.01)


play_game()
