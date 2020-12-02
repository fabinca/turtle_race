import turtle as t
import random
from numpy import random as r

SCREEN_WIDTH = 500
END = SCREEN_WIDTH / 2 - 50
START = -END


def draw_line(t_obj, x_point):
    t_obj.hideturtle()
    t_obj.penup()
    t_obj.goto(x_point, 200)
    t_obj.pendown()
    t_obj.goto(x_point, -200)


def setup_runners():
    colors = ["yellow", "orange", "red", "purple", "blue", "green"]
    random.shuffle(colors)
    y_point = 120
    for turtle_index in range(0, 6):
        new_turtle = t.Turtle(shape="turtle")
        new_turtle.setheading(90)
        new_turtle.penup()
        new_turtle.color(colors[turtle_index])
        new_turtle.goto(x=-200, y=y_point)
        y_point -= 30
        runners.append(new_turtle)


def step():
    random.shuffle(runners)
    for runner in runners:
        step_size = random.randint(1, 20)
        direction = round((r.normal(1, 0.1)) * 90)
        runner.setheading(direction)
        runner.penup()
        runner.forward(step_size)


def check_over():
    for runner in runners:
        if runner.xcor() >= END:
            return False
    return True


def winner_is(guess):
    x = 0
    output = ""
    for runner in runners:
        if runner.xcor() > x:
            x = runner.xcor()
            a, winner = runner.color()
    if winner == guess:
        output += "You've won!\n"
    else:
        output += "You've lost!\n"
    output += f"The {winner} turtle was the fastest."
    return output

# ------------UI---------------------
screen = t.Screen()
screen.setup(width=SCREEN_WIDTH, height=400)
lines = t.Turtle()
t.mode("logo")

draw_line(lines, START)
draw_line(lines, END)
runners = []
setup_runners()

bet = screen.textinput(
    title="Make your bet",
    prompt=
    "Which color will win?(yellow, orange, red, purple, blue, green or yellow")

game_not_over = True
while game_not_over:
    step()
    game_not_over = check_over()

screen.textinput(title="The winner is", prompt=winner_is(bet))

screen.exitonclick()
