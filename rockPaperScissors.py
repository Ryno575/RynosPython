# Rock Paper Scissors
import random as rand
import time

robot_score = 0
player_score = 0
reset = True
winner = "None"

while reset == True:
# Decides player's choice, must be Rock or Paper or Scissors
    while True:
        player_choice = input("Rock, Paper or Scissors? ") 
        if player_choice == "Rock" or player_choice == "Paper" or player_choice == "Scissors":
            print("Your choice is " + player_choice)
            break

        else:
            print("Please choose Rock, Paper or Scissors")
            continue

# Decides robot's choice (Based off rand import)
    robot_choice = rand.randint(1, 3)
    print(robot_choice)


    if robot_choice == 1:
        robot_choice = "Rock"
        print("The robot's choice is " + robot_choice)

    elif robot_choice == 2:
        robot_choice = "Paper"
        print("The robot's choice is " + robot_choice)

    else:
        robot_choice = "Scissors"
        print("The robot's choice is " + robot_choice)

# Figures out if it is a tie first
    if robot_choice == player_choice:
        print("It is a Tie!")

# Moves on to robot picking rock
    elif robot_choice == "Rock":
        if player_choice == "Paper":
            print("You Win!")
            player_score += 1
        else:
            print("You Lose!")    
            robot_score += 1
# Then robot picking paper
    elif robot_choice == "Paper":
        if player_choice == "Scissors":
            print("You Win!")
            player_score += 1
        else:
            print("You Lose!")
            robot_score += 1
# Lastly robot picking scissors
    elif robot_choice == "Scissors":
        if player_choice == "Rock":
            print("You Win!")
            player_score += 1
        else:
            print("You Lose!")    
            robot_score += 1


    print("")
    print("PLAYER: " + str(player_score))
    print("ROBOT: " + str(robot_score))
# Asks if the user wants to play again
    reset = input("Would you like to reset?? Y or N ")
    if reset == "Y":
        reset = True
    else:
        reset = False

# Decides the winner
if int(player_score) > int(robot_score):
    winner = "PLAYER"

elif int(player_score) == int(robot_score):
    winner = "NONE"

else:
    winner = "ROBOT"

# Prints the closing statements (Winners and Scoreboard)
print("")
print("---FINAL SCORE---")
print("PLAYER: " + str(player_score))
print("ROBOT: " + str(robot_score))
print("The winner is: " + winner)
time.sleep(2)




