# Plot townspeople vs. vampires on a graph

from turtle import *

p = Turtle()
v = Turtle()

scr = p.getscreen()

people = int(scr.numinput("Starting population", "Enter the town's starting population"))
vampires = int(scr.numinput("Starting vampires", "Enter the vampire coven size:"))
converted = int(scr.numinput("Infection rate", "Enter the number of people each vampire can convert per day:"))
hunters = int(scr.numinput("Hunting rate", "Enter the number of vampires that can be killed per day:"))

p.penup()
v.penup()

p.color('black')
v.color('red')

day = -200

p.goto(day, people)
p.pendown()
p.right(90)
p.forward(people)
p.left(90)
p.forward(500)
p.penup()
p.goto(day, people)
p.pendown()

v.goto(day, vampires)
v.pendown()


while people > 0 and vampires > 0:
    print("People: " + str(people) + "\t\tVampires: " + str(vampires))
    # First, the vampire hunters strike during the day
    print("Hunters kill up to " + str(hunters) + " vampire(s)")
    vampires = vampires - hunters
    if vampires < 0:
        vampires = 0

    # The vampires retaliate each night
    if vampires > 0:
        turned = vampires * converted
        print("Remaining vampires turn up to " + str(turned) + " townspeople")
        if people < turned:
            vampires = vampires + people
            people = 0
        else:
            people = people - turned
            vampires = vampires + turned
    p.goto(day, people)
    v.goto(day, vampires)
    day = day + 30
    print("\n")

p.write("Human population")
v.write("Vampire population")

done()
