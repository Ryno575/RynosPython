# Number Guesser
### DESCRIPTION ###
### This game makes the computer choose a number 1 - 99 (will allow user to choose a number range in future update) ###
### The user then has 10 guesses to guess the number, each guess will use 1 guess and the compiler will return if the number given is higher or lower then the computer's number ###
### After the user makes 2 guesses, then the user can spend 2 guesses to return to the user a random hint ###
### If the user gets the number before the guesses are up then they win the game and it is added to their win and game counters ###
### If they lose a game then it just adds 1 game to the game counter ###
### At the end of each game it will ask the user if they want to play again ###
### If they want to play again then it will repeat the game until they want to quit ###
### If they are done playing then it will return the games played and the amount of games won ###
###
import random as rand

### ALLOWS PROGRAM TO ACCESS A SET OF HINTS ###
# These hints can be used after the 3rd guess and they are randomly chosen
# Using a hint will also take off 2 guesses instead of the normal 1 guess
class Hints: 
### Checks if the computer's number is even or odd
    def evenOrOdd(self, cpuNum):        
        if (cpuNum % 2 == 0):
            print("The computer's number is even")
        else:
            print("The computer's number is odd")

### Checks if the computer's number is higher or lower than a randomly chosen number
    def higherOrLower(self, cpuNum):    
        randNum = rand.randint(1, 99)   # Picks a number 1 - 99
        # If the random number is higher -> prints that computer's number is lower than random number
        if (randNum > cpuNum):          
            print("Computer's number is less than " + str(randNum))

        # If the random number is lower -> prints that computer's number is hugher than random number
        elif (randNum < cpuNum):        
            print("Computer's number is greater than " + str(randNum))

        ## IN RARE CASES (if random number == computer's number) -> reveals the computer's number
        else:                           
            print("The computer's number is " + str(randNum))

### Checks computer's number and returns all factors of that number (excluding itself)
    def factorsOfNum(self, cpuNum):     
        factors = []
        # If the number is 1 or 2 -> reveals the computer's number
        if (cpuNum == 1 or cpuNum == 2):  
            print("The computer's number is " + str(cpuNum))

        # Else it will iterate through from 1 to computer's number - 1 and files all factors into an array
        else:                            
            for i in range(1, cpuNum - 1):
                # If computer's number divides evenly into the current iteration -> it is a factor
                if (cpuNum % i == 0):     
                   factors.append(i) 
        factors.append("computer's number") # Adds the string "computer's number" to the end of the array to hide the real number
        print("Factors of computer's number: " + str(factors))  # Returns the factors of computer's number
    
    ### Checks to see if computer's number is a square or between 2 squares
    def betweenSquare(self, cpuNum):
        # Iterates from 1 to 11 (or squares between 1 and 121  because it is using i * i)
        for i in range(1, 11):  
            # If computer's number is a square -> reveals that it is a square number (does not tell you what square number)
            if (i * i == cpuNum):
                print("The computer's number is a square number")
                break

            # Else if the computer's number is greater than the current square (i * i) -> reveals that computer's number is between
            # ((i - 1) * (i - 1)) [Previous square number] and (i * i) [Current square number]
            elif (i * i > cpuNum):
                print("The computer's number is between " + str((i-1) * (i-1)) + " and " + str(i * i))
                break

### Compares the user's guess with the computer's number
def checkGuess(cpuNum, userGuess, guesses):
    # If the user guesses the computer's number -> returns -1 as guesses to enter the end game dialogue, adds 1 win to total wins 
    if userGuess == cpuNum:
        guesses = -1

    # If userGuess is greater than computer's number -> returns user's guess is too high, takes away 1 guess from remaining guesses
    elif userGuess > cpuNum:
        print("Your guess is too high")
        guesses -= 1

    # If userGuess is less than computer's number -> returns user's guess is too low, takes away 1 guess from remining guesses    
    else:
        print("Your guess is too low")
        guesses -= 1
    return guesses

### Initalizes pre-game variables                
hints = Hints()
reset = "Y"
gamesPlayed = 0
wins = 0
print("Welcome to the Number Guesser Game!")

### Number Guesser Game Loop
while (reset.lower != "n"):
    ### Initalizes new-game variables
    guesses = 10
    hintsRemaining = 3
    cpuNum = rand.randint(1, 99)
    print("I have chosen a number 1 - 99")
    print("You have 10 guesses to guess it")
    print("Good luck!!")
    gamesPlayed += 1     # Counts how many games the user has played

    ### BEGINNING GAME LOOP (Guesses 9 - 10) [No Hints]
    while (guesses <= 10) and (guesses > 8):
        print()
        print("Guesses remaining: " + str(guesses))
        
        # Allows the user to enter in a number 1 - 99
        try:
            guess = int(input("Please enter a number 1 - 99: "))
            # If the number is less than 1 or greater than 99 -> loop resets until user puts in a valid number
            if (guess < 1) or (guess > 99):
                print("Please enter a number 1 - 99")

            # Else it uses the checkGuess function to see if the guess is too high, too low or just right
            # The checkGuess function also uses 1 guess
            else:
                guesses = checkGuess(cpuNum, guess, guesses)

        # If the program runs into an error -> loop resets until user puts in a valid number
        except:
            print("Please enter a number 1 - 99")

    ### MIDDLE GAME LOOP (Guesses 0 - 8) [Hints Allowed]
    while (guesses > 0):
        # If there are less than 2 guesses left -> the user can not use a hint or else it will force a win 
        if (guesses <= 2):
            hintsRemaining = 0
        print()
        print("Guesses remaining: " + str(guesses))

        # Allows user to enter in a number 1 - 99
        try:
            guess = int(input("Please enter a number 1 - 99 (Enter 0 for hint [Hints Remaining: " + str(hintsRemaining) + "]): "))
            # If the number is less than 1 or greater than 99 -> loop resets until user puts in a valid number
            if (guess < 0) or (guess > 99):
                print("Please enter a number 1 - 99")
            
            # If the number == 0 and there are hints available -> randomly chooses one of the hints from the Hints class
            # and returns a hint to the user.
            # Using a hint also costs the user 2 guesses instead of the normal 1 guess 
            elif (guess == 0 and hintsRemaining > 0):
                hintChoice = rand.randint(0, 3)  # Randomly chooses one of the 4 hints available
                if (hintChoice == 0):
                    hints.evenOrOdd(cpuNum)
                elif (hintChoice == 1):
                    hints.higherOrLower(cpuNum)
                elif (hintChoice == 2):
                    hints.factorsOfNum(cpuNum)
                elif (hintChoice == 3):
                    hints.betweenSquare(cpuNum)

                guesses -= 2
                hintsRemaining -= 1
                print("Hints remaining: " + str(hintsRemaining))

            # If the guess == 0 and there are no hints remaining -> returns back to start of loop until a valid guess is inputted
               
            elif (guess == 0 and hintsRemaining == 0):
                print("You have run out of hints")

            # Else it uses the checkGuess function to see if the guess is too high, too low or just right
            # The checkGuess function also uses 1 guess
            else:
                guesses = checkGuess(cpuNum, guess, guesses)
        # If the program runs into an error -> loop resets until user puts in a valid number
        except:
            print("Please enter a number 1 - 99")

### END GAME ###
    # If the user guessed the computer's number -> returns a congratulations statement and adds 1 win to total wins
    if (guesses == -1):
        print("You Win! You guessed the number!")
        wins += 1
    # If the user could not guess the computer's number -> returns a "You Lose!" and says what the computer's number was
    else:
        print("You Lose! You did not guess the number!")
        print("The computer's number was " + str(cpuNum))

### Asks the user if they want to play again
    print()
    reset = str(input("Would you like to play again? 'Y' or 'N' "))
    print()
    if reset.lower() == "n":  # If they decide no -> skips to line 192
        break
    else:                     # If they decide yes -> skips to line 96
        continue

### POST-GAME DIALOGUE ###
# Shows the stats of the games that user played (how many games they played, how many times they won)
print("You played: " + str(gamesPlayed) + " game(s)")
print("You won: " + str(wins) + " game(s)")
