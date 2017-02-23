from turtle import *
import random

# Global variables

t = Turtle()
t.speed(5)
t.hideturtle()
scr = t.getscreen()

# Functions

def drawDie(x, y, value):
    global t
    oldSpeed = t.speed()
    t.speed(0)
    t.pu()
    t.goto(x,y)
    t.seth(0)
    t.width(2)
    side = 50
    t.pd()
    t.color("black", "white")
    t.begin_fill()
    for i in range(4):
        t.forward(side)
        t.left(90)
    t.end_fill()
    t.pu()

    t.goto(x+15, y+2)    
        
    if value-1 in range(6):
        t.write(str(value), font=("Arial", 28, "normal"))
    else:
        print("The value parameter must be in the range 1 through 6.")
    t.speed(oldSpeed)

def printScore(score):
    global t
    oldSpeed = t.speed()
    t.speed(0)
    t.pu()
    t.goto(-20, 100)
    t.seth(0)
    t.pd()
    t.color("white")
    t.begin_fill()
    for i in range(2):
        t.forward(150)
        t.left(90)
        t.forward(40)
        t.left(90)
    t.end_fill()
    
    t.color("black")
    t.write("Score: " + str(score), font=("Arial", 18, "normal"))
    t.speed(oldSpeed)

def gameLost():
    global t
    t.pu()
    t.goto(-100, -100)
    t.seth(0)
    t.write("Game over! You lost!", font=("Arial", 28, "normal"))

def gameWon(score):
    global t
    t.pu()
    t.goto(-120, -100)
    t.seth(0)
    t.write("Game over! You won! Final score: " + str(score), font=("Arial", 18, "normal"))

# Main function
def main():
    global t
    global scr

    t.pu()
    t.goto(-100, 180)
    t.write("Welcome to Oink!", font=("Arial", 28, "normal"))

    target = random.randint(50, 75)
    t.goto(-100, 140)
    t.write("Target score: "+str(target), font=("Arial", 18, "normal"))

    score = 0
    printScore(score)
    
    again = "y"
    while again == "y" and score <= target-5:
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        drawDie(-50, 0, die1)
        drawDie(50, 0, die2)

        if die1 == 1 and die2 == 1:
            score = 0
            again = "n"
        else:
            if die1 == die2: # score points but must roll again
                score += die1 + die2
            elif die1 != 1 and die2 != 1: # points scored
                score += die1 + die2
            if score <= target-5 and die1 != die2:
                again = scr.textinput("Roll again?", "Do you want to roll again?")
        printScore(score)
        
    if score == 0 or score > target or score < target-5:
        gameLost()
    elif die1 != 1 or die2 != 1:
        gameWon(score)
        
   

# Program start
main()
