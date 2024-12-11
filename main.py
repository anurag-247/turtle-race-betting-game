from turtle import Turtle ,Screen
import random

# tim = Turtle(shape="turtle")
screen = Screen()

# def front():
#     tim.forward(10)
#
# def back():
#     tim.backward(10)
#
# def clock():
#     tim.right(5)
#
# def a_clock():
#     tim.left(5)
#
# screen.listen()
# screen.onkey(front, "w")
# screen.onkey(back, "s")
# screen.onkey(clock, "d")
# screen.onkey(a_clock, "a")

screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race?\n red/orange/yellow/green/blue/violet\n Enter a color: ")
# print(user_bet)
l=["red","orange","yellow","green","blue","violet"]
t=["red","orange","yellow","green","blue","violet"]


def create_turtle(y_co, color):
    c = Turtle(shape="turtle")
    c.color(color)
    c.penup()
    x_co = -230
    # y_co = -125
    c.goto(x=x_co, y=y_co)
    # y_co += 50
    c.pendown()
    return c


y = -125
tlist = []
for _ in range(6):
    a = create_turtle(y, l[_])
    tlist.append(a)
    y += 50

not_at_end = True
while not_at_end:
    for _ in range(6):
        tlist[_].forward(random.randint(0, 50))
        # print(tlist[_].xcor())
        if tlist[_].xcor() >= 230:
            not_at_end = False
            winner = tlist[_].color()[0]

if user_bet == winner:
    print(f'Congratulations! {winner} won')
else:
    print(f'You lose, the winner is {winner}')

screen.exitonclick()