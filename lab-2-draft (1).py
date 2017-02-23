# lab 2 draft

from turtle import *
bob = Turtle()

screen = bob.getscreen()

rent = screen.numinput("How much for rent?", "How much will you spend on rent?")
utilities = screen.numinput("How much for utilities?", "How much will you spend on utilities?")
food = screen.numinput("How much for food?", "How much will you spend on food?")
fun = screen.numinput("How much for fun?", "How much will you spend on fun?")

# Assume each bar is 20 pixels wide
bar_width = 20


# Move to start point
bob.penup()
bob.goto(-4 * bar_width, -200)
#bob.left(180)
#bob.forward(4 * bar_width)

if rent > utilities and rent > food and rent > fun:
    bob.color('black', 'red')
else:
    bob.color('black', 'blue')

bob.left(90) # face north
bob.pendown()
bob.begin_fill()
bob.forward(rent)
bob.right(90)
bob.forward(bar_width)
bob.right(90)
bob.forward(rent)
bob.right(90)
bob.forward(bar_width)
bob.end_fill()
bob.penup()

bob.goto(-4 * bar_width, -220)
bob.write("Rent")
bob.goto(-4*bar_width, rent - 180)
bob.write("$" + str(rent))

# Move to second bar position
bob.goto(-2 * bar_width, -200)

if utilities > rent and utilities > food and utilities > fun:
    bob.color('black', 'red')
else:
    bob.color('black', 'blue')

bob.right(90) # face north
bob.pendown()
bob.begin_fill()
bob.forward(utilities)
bob.right(90)
bob.forward(bar_width)
bob.right(90)
bob.forward(utilities)
bob.right(90)
bob.forward(bar_width)
bob.end_fill()
bob.penup()

bob.goto(-2 * bar_width, -220)
bob.write("Utilities")
bob.goto(-2*bar_width, utilities-180)
bob.write("$" + str(utilities))

# Move to third bar position
bob.goto(0, -200)

if food > rent and food > utilities and food > fun:
    bob.color('black', 'red')
else:
    bob.color('black', 'blue')

bob.right(90) # face north
bob.pendown()
bob.begin_fill()
bob.forward(food)
bob.right(90)
bob.forward(bar_width)
bob.right(90)
bob.forward(food)
bob.right(90)
bob.forward(bar_width)
bob.end_fill()
bob.penup()

bob.goto(0, -220)
bob.write("Food")
bob.goto(0, food-180)
bob.write("$" + str(food))

# Move to fourth bar position
bob.goto(2 * bar_width, -200)

if fun > rent and fun > food and fun > utilities:
    bob.color('black', 'red')
else:
    bob.color('black', 'blue')

bob.right(90) # face north
bob.pendown()
bob.begin_fill()
bob.forward(fun)
bob.right(90)
bob.forward(bar_width)
bob.right(90)
bob.forward(fun)
bob.right(90)
bob.forward(bar_width)
bob.end_fill()
bob.penup()

bob.goto(2 * bar_width, -220)
bob.write("Fun")
bob.goto(2*bar_width, fun-180)
bob.write("$" + str(fun))

# Add chart title
bob.goto(-50, 350)
bob.write("Monthly Expenses")

bob.hideturtle()

done()
