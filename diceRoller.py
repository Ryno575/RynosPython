# Dice Rolling
### DESCRIPTION ###
### A program that allows the user to roll two dice as many times as they want while also counting how many dice of each number ###
### This program also uses the turtle function to draw the two dice so that the user can visually see the dice ###
import random
import turtle as trtl
import time
from tkinter import ttk


# Define Variables
dice1 = [1, 2, 3, 4, 5, 6]
dice2 = [1, 2, 3, 4, 5, 6]
die_numb1 = 0
die_numb2 = 0

# Counter Variables
one_counter = 0
two_counter = 0
three_counter = 0
four_counter = 0
five_counter = 0
six_counter = 0

reset = True

# Draws the dice
def drawdice(wn=wn, turtle1=turtle1, turtle2=turtle2):
    wn.clear()
    turtle1 = trtl.Turtle() # Draws dice 1
    turtle1.speed(0)
    turtle1.penup()
    turtle1.goto(200,50)
    turtle1.pendown()
    turtle1.forward(150)
    turtle1.right(90)
    turtle1.forward(300)
    turtle1.right(90)
    turtle1.forward(300)
    turtle1.right(90)
    turtle1.forward(300)
    turtle1.right(90)
    turtle1.forward(150)

    turtle2 = trtl.Turtle() # Draws dice 2
    turtle2.speed(0)
    turtle2.penup()
    turtle2.goto(-200,50)
    turtle2.pendown()
    turtle2.forward(150)
    turtle2.right(90)
    turtle2.forward(300)
    turtle2.right(90)
    turtle2.forward(300)
    turtle2.right(90)
    turtle2.forward(300)
    turtle2.right(90)
    turtle2.forward(150)

wn = trtl.Screen()

# Begins reset function
while reset == True:
    drawdice()

    die_numb1 = random.choice(dice1)
    if die_numb1 == 1:            # Draws 1 on dice
        turtle1.penup()
        turtle1.goto(200,-115)
        turtle1.pendown()
        turtle1.begin_fill()
        turtle1.circle(20)
        turtle1.end_fill()

        one_counter += 1

    elif die_numb1 == 2:             # Draws 2 on dice
        turtle1.penup()
        turtle1.goto(115,-15)
        turtle1.pendown()
        turtle1.begin_fill()
        turtle1.circle(20)
        turtle1.end_fill()

        turtle1.penup()
        turtle1.goto(275,-195)
        turtle1.pendown()
        turtle1.begin_fill()
        turtle1.circle(20)
        turtle1.end_fill()
        
        two_counter += 1

    elif die_numb1 == 3:          # Draws 3 on dice
        turtle1.penup()
        turtle1.goto(125,-15)
        turtle1.pendown()
        turtle1.begin_fill()
        turtle1.circle(20)
        turtle1.end_fill()

        turtle1.penup()
        turtle1.goto(200,-115)
        turtle1.pendown()
        turtle1.begin_fill()
        turtle1.circle(20)
        turtle1.end_fill()

        turtle1.penup()
        turtle1.goto(275,-195)
        turtle1.pendown()
        turtle1.begin_fill()
        turtle1.circle(20)
        turtle1.end_fill()

        three_counter += 1  

    elif die_numb1 == 4:            # Draws 4 on dice
        turtle1.penup()
        turtle1.goto(125,-15)
        turtle1.pendown()
        turtle1.begin_fill()
        turtle1.circle(20)
        turtle1.end_fill()

        turtle1.penup()
        turtle1.goto(275,-15)
        turtle1.pendown()
        turtle1.begin_fill()
        turtle1.circle(20)
        turtle1.end_fill()

        turtle1.penup()
        turtle1.goto(275,-195)
        turtle1.pendown()
        turtle1.begin_fill()
        turtle1.circle(20)
        turtle1.end_fill()   

        turtle1.penup()
        turtle1.goto(125,-195)
        turtle1.pendown()
        turtle1.begin_fill()
        turtle1.circle(20)
        turtle1.end_fill()

        four_counter += 1   

    elif die_numb1 == 5:             # Draws 5 on dice
        turtle1.penup()
        turtle1.goto(125,-15)
        turtle1.pendown()
        turtle1.begin_fill()
        turtle1.circle(20)
        turtle1.end_fill()

        turtle1.penup()
        turtle1.goto(275,-15)
        turtle1.pendown()
        turtle1.begin_fill()
        turtle1.circle(20)
        turtle1.end_fill()

        turtle1.penup()
        turtle1.goto(275,-195)
        turtle1.pendown()
        turtle1.begin_fill()
        turtle1.circle(20)
        turtle1.end_fill()   

        turtle1.penup()
        turtle1.goto(125,-195)
        turtle1.pendown()
        turtle1.begin_fill()
        turtle1.circle(20)
        turtle1.end_fill() 

        turtle1.penup()
        turtle1.goto(200,-115)
        turtle1.pendown()
        turtle1.begin_fill()
        turtle1.circle(20)
        turtle1.end_fill()

        five_counter += 1

    else:                               # Draws 6 on dice
        turtle1.penup()
        turtle1.goto(125,-15)
        turtle1.pendown()
        turtle1.begin_fill()
        turtle1.circle(20)
        turtle1.end_fill()

        turtle1.penup()
        turtle1.goto(275,-15)
        turtle1.pendown()
        turtle1.begin_fill()
        turtle1.circle(20)
        turtle1.end_fill()

        turtle1.penup()
        turtle1.goto(275,-115)
        turtle1.pendown()
        turtle1.begin_fill()
        turtle1.circle(20)
        turtle1.end_fill()

        turtle1.penup()
        turtle1.goto(275,-195)
        turtle1.pendown()
        turtle1.begin_fill()
        turtle1.circle(20)
        turtle1.end_fill()   

        turtle1.penup()
        turtle1.goto(125,-195)
        turtle1.pendown()
        turtle1.begin_fill()
        turtle1.circle(20)
        turtle1.end_fill()

        turtle1.penup()
        turtle1.goto(125,-115)
        turtle1.pendown()
        turtle1.begin_fill()
        turtle1.circle(20)
        turtle1.end_fill()

        six_counter += 1

    die_numb2 = random.choice(dice2)
    if die_numb2 == 1:
        turtle2.penup()
        turtle2.goto(-200,-115)
        turtle2.pendown()
        turtle2.begin_fill()
        turtle2.circle(20)
        turtle2.end_fill()
        
        one_counter += 1

    elif die_numb2 == 2:             # Draws 2 on dice
        turtle2.penup()
        turtle2.goto(-275,-15)
        turtle2.pendown()
        turtle2.begin_fill()
        turtle2.circle(20)
        turtle2.end_fill()

        turtle2.penup()
        turtle2.goto(-125,-195)
        turtle2.pendown()
        turtle2.begin_fill()
        turtle2.circle(20)
        turtle2.end_fill()

        two_counter += 1

    elif die_numb2 == 3:          # Draws 3 on dice
        turtle2.penup()
        turtle2.goto(-275,-15)
        turtle2.pendown()
        turtle2.begin_fill()
        turtle2.circle(20)
        turtle2.end_fill()

        turtle2.penup()
        turtle2.goto(-200,-115)
        turtle2.pendown()
        turtle2.begin_fill()
        turtle2.circle(20)
        turtle2.end_fill()

        turtle2.penup()
        turtle2.goto(-125,-195)
        turtle2.pendown()
        turtle2.begin_fill()
        turtle2.circle(20)
        turtle2.end_fill()

        three_counter += 1

    elif die_numb2 == 4:            # Draws 4 on dice
        turtle2.penup()
        turtle2.goto(-275,-15)
        turtle2.pendown()
        turtle2.begin_fill()
        turtle2.circle(20)
        turtle2.end_fill()

        turtle2.penup()
        turtle2.goto(-125,-15)
        turtle2.pendown()
        turtle2.begin_fill()
        turtle2.circle(20)
        turtle2.end_fill()

        turtle2.penup()
        turtle2.goto(-125,-195)
        turtle2.pendown()
        turtle2.begin_fill()
        turtle2.circle(20)
        turtle2.end_fill()   

        turtle2.penup()
        turtle2.goto(-275,-195)
        turtle2.pendown()
        turtle2.begin_fill()
        turtle2.circle(20)
        turtle2.end_fill()

        four_counter += 1  

    elif die_numb2 == 5:             # Draws 5 on dice
        turtle2.penup()
        turtle2.goto(-275,-15)
        turtle2.pendown()
        turtle2.begin_fill()
        turtle2.circle(20)
        turtle2.end_fill()

        turtle2.penup()
        turtle2.goto(-125,-15)
        turtle2.pendown()
        turtle2.begin_fill()
        turtle2.circle(20)
        turtle2.end_fill()

        turtle2.penup()
        turtle2.goto(-125,-195)
        turtle2.pendown()
        turtle2.begin_fill()
        turtle2.circle(20)
        turtle2.end_fill()   

        turtle2.penup()
        turtle2.goto(-275,-195)
        turtle2.pendown()
        turtle2.begin_fill()
        turtle2.circle(20)
        turtle2.end_fill() 

        turtle2.penup()
        turtle2.goto(-200,-115)
        turtle2.pendown()
        turtle2.begin_fill()
        turtle2.circle(20)
        turtle2.end_fill()
        
        five_counter += 1

    else:                               # Draws 6 on dice
        turtle2.penup()
        turtle2.goto(-275,-15)
        turtle2.pendown()
        turtle2.begin_fill()
        turtle2.circle(20)
        turtle2.end_fill()

        turtle2.penup()
        turtle2.goto(-125,-15)
        turtle2.pendown()
        turtle2.begin_fill()
        turtle2.circle(20)
        turtle2.end_fill()

        turtle2.penup()
        turtle2.goto(-125,-115)
        turtle2.pendown()
        turtle2.begin_fill()
        turtle2.circle(20)
        turtle2.end_fill()

        turtle2.penup()
        turtle2.goto(-125,-195)
        turtle2.pendown()
        turtle2.begin_fill()
        turtle2.circle(20)
        turtle2.end_fill()

        turtle2.penup()
        turtle2.goto(-275,-195)
        turtle2.pendown()
        turtle2.begin_fill()
        turtle2.circle(20)
        turtle2.end_fill()

        turtle2.penup()
        turtle2.goto(-275,-115)
        turtle2.pendown()
        turtle2.begin_fill()
        turtle2.circle(20)
        turtle2.end_fill()

        six_counter += 1

    print("Dice 1: " + str(die_numb2))
    print("Dice 2: " + str(die_numb1))

    print("")
    reset = input("Would you like to reset? Y or N: ")

    if reset == "Y":
        reset = True

    else:
        reset = False

# Prints how many of each number the player got
print("You had: ", one_counter, " ones!")
print("You had: ", two_counter, " twos!")
print("You had: ", three_counter, " threes!")
print("You had: ", four_counter, " fours!")
print("You had: ", five_counter, " fives!")
print("You had: ", six_counter, " sixes!")

# Kills the program
time.sleep(5)
print("Goodbye!")
wn.bye()

