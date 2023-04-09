##########################################
# CS 1110A - Programming in Python       #
# Module 2 - Exercise 3 - Drunken Pirate #
# Author: Ahmed Lotfey                   #
# Date:   03/25/2023                     #
##########################################

# import turtles library
import turtle

# durnken pirate step angles
drunken_pirate_angles = [
    45,
    -75,
    160,
    -43,
    270,
    -97,
    -43,
    200,
    -940,
    17,
    -86,
    150,
    25,
    75,
    -90,
    20,
    -145,
    30,
    -50,
    -70,
    -105,
]

# create a play ground
wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Drunken Pirate")

# initite the drunken pirate
drunken_pirate = turtle.Turtle()
drunken_pirate.goto(0,45)
# Drunken pirate moves
def drunken_pirate_walk(angles):
    for angle in angles:
        drunken_pirate.stamp()
        drunken_pirate.left(angle)
        drunken_pirate.forward(100)


# call the drunken pirate walk function
drunken_pirate_walk(drunken_pirate_angles)

# wait for user to close the screen
wn.mainloop()
