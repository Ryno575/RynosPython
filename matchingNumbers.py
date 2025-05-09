# Number Guessing
import random as rand

# Assigns Variables
reset = True
player_score = 0
games = 0
duplicates = True

# Defines how many numbers are in list
def numb_list():
    global player_number
    global number_list
    global x
    x = 1
    number_list = []
    for num in range(player_number):
        number_list.append(x)
        x += 1
    print(number_list)


# Starts the game, player picks amount in number list
while reset == True:
    player_number = int(input("How many numbers would you like to guess from: "))
    numb_list()
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
            else:
                print("Please enter a number in the list!")


# Loops the player's already guessed numbers to see if there are any duplicates
            dupes = []
            for i in guess_numbers:
                if i not in dupes:
                    dupes.append(i)
                    duplicates = False # Escapes the loop if there are no duplicates
                else:
                    duplicates = True
                    print("You have already guessed this: ", player_choice)
                    print("Please choose a new number!")
                    print("")
                    guess_numbers.remove(player_choice) # Continues loop, takes out player's guess from list, does not use a turn

# If the player guesses the right number then they win! (skips to line 83)
        if player_choice == number_choice:
            turns = -1
            break
            
# If they don't guess correctly -> loops back to line 25
        else:
            print("")
            print("Keep Guessing")
            print("You have guessed: ", sorted(guess_numbers))
            turns = turns - 1
            print("Turns Remaining: ", turns)
            print("")
            duplicates = True

# If they run out of turns -> player loses
    if turns == 0:
        print("You Lose!!")
        print("The answer was: ", number_choice)
        print("")
        games += 1

# If they get it right -> player wins, adds a point to player's score 
    else:
        print("You Win!!")
        print("The answer was: ", number_choice)
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
        print("You won ", player_score, " out of ", games, " games")
