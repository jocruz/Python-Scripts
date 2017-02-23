from turtle import *

bob = Turtle()
bob.speed(0)
screen = bob.getscreen()

bob.pencolor("black")

rows = int(screen.numinput("How many rows?", "How many rows?", 5, 1, 10))
cols = int(screen.numinput("How many columns?", "How many columns?", 7, 1, 10))
length = int(screen.numinput("How long is each square's side?",
                         "How long is each square's side?", 25, 10, 50))
color1 = screen.textinput("What's the first color?", "What's the first color?")
color2 = screen.textinput("What's the second color?", "What's the second color?")
color3 = screen.textinput("What's the third color?", "What's the third color?")

startX = -(cols*length)//2
startY = -(rows*length)//2

bob.penup()
bob.goto(startX, startY)
bob.pendown()

for row in range(rows):
    if row % 3 == 0:
        startColor = color1
    elif row % 3 == 1:
        startColor = color2
    else:
        startColor = color3

    color = startColor
    for col in range(cols):
        bob.fillcolor(color)
        bob.begin_fill()
        for side in range(4):
            bob.forward(length)
            bob.left(90)
        bob.end_fill()

        bob.forward(length)

        if (row + col) % 3 == 0: 
            color = color2
        elif (row + col) % 3 == 1:
            color = color3
        else:
            color = color1

    bob.penup()
    bob.left(180)
    bob.forward(cols*length)
    bob.right(90)
    bob.forward(length)
    bob.right(90)
    bob.pendown()

bob.hideturtle()
done()
