# Number Guessing
#### DOES NOT WORK CORRECTLY ####
#### NEED TO RESTART PROJECT ####
### Description:
# Asks the user to enter in a number which will be used for the size of an array
# The compiler will then make an array with the numbers from 1 - size
# The user then has 5 guesses to guess the number that was randomly chosen from this array
# The user can then restart once the user either gets the number or fails to get the number
###
import random as rand

# Assigns Variables
reset = True
player_score = 0
games = 0
duplicates = True
x = 1

# Defines how many numbers are in list
def numb_list(player_number, x):
    number_list = []
    for num in range(player_number):
        number_list.append(x)
        x += 1
    return number_list, x


# Starts the game, player picks amount in number list
while reset == True:
    player_number = int(input("How many numbers would you like to guess from: "))
    number_list, x = numb_list(player_number, x)
    print(number_list)
    guess_numbers = []
    turns = 5

# Computer chooses a number from this list
    number_choice = (rand.choice(number_list))
    print("")
    print("The computer has chosen a number")

# Player guesses numbers until they either run out of turns or guesses the right number
    while turns != 0:  
        while duplicates == True:
            player_choice = int(input("What number do you think it is: "))
            if player_choice > 0:
                if player_choice < x:
                    guess_numbers.append(player_choice)
                else:
                    print("Please enter a number in the list!")
                    print("")
                    continue
            else:
                print("Please enter a number in the list!")
                print("")
                continue


# Loops the player's already guessed numbers to see if there are any duplicates
            dupes = []
            for i in guess_numbers:
                if i not in dupes:
                    dupes.append(i)
                    duplicates = False # Escapes the loop if there are no duplicates
                else:
                    duplicates = True
                    print("You have already guessed this: " + str(player_choice))
                    print("Please choose a new number!")
                    print("")
                    guess_numbers.remove(player_choice) # Continues loop, takes out player's guess from list, does not use a turn
            continue
# If the player guesses the right number then they win! (skips to line 83)
        if player_choice == number_choice:
            turns = -1
            break
            
# If they don't guess correctly -> loops back to line 25
        else:
            print("")
            print("Keep Guessing")
            print("You have guessed: " + str(sorted(guess_numbers)))
            turns = turns - 1
            print("Turns Remaining: " + str(turns))
            print("")
            duplicates = True

# If they run out of turns -> player loses
    if turns == 0:
        print("You Lose!!")
        print("The answer was: " + str(number_choice))
        print("")
        games += 1

# If they get it right -> player wins, adds a point to player's score 
    else:
        print("You Win!!")
        print("The answer was: " + str(number_choice))
        print("")
        player_score += 1
        games += 1

# Asks the player if they would like to reset    
    reset = input("Would you like to reset?? Y or N ")
    if reset == "Y":
        reset = True
        duplicates = True
    else:
        reset = False
        print("You won " + str(player_score) + " out of " + str(games) + " games")
