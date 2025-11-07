import random as rand
class Game:                             ### This is where the entire game is located
    def __init__(self, board_instance, dice_instance, player_instance):
        ### TODO ###
        ### Inherit Board, Dice, and Player Classes
        pass
    ### TODO ###
    ### Make functions that make the game run ###
    pass

class Spaces:                           ### A class that gets the spaces that will be inputted into the board
    def __init__(self, spaceNum, spaceType=None):
        self.spaceType = spaceType      # Space Type initally equals None/Null
        self.spaceNum = spaceNum        # Space number starts at 1

    def setSpace(self):                       ### This function sets the randomly chosen space type
        spaceChoices = ['Normal', 'Loop', 'Number', 'Exit', 'Skip Start']
        self.spaceType = (rand.choices(spaceChoices))

    def addSpace(self):                       ### This function adds the Space object to the board
        if self.spaceNum == 1:                # If it is the first space -> the space type is automaticall "Start"
            self.spaceType = "Start"
        elif self.spaceType == "Finish":
            pass
        else:                                 # Else -> picks a randomly chosen space type
            self.setSpace()
        return self.spaceType, self.spaceNum  # Returns the space type and the number to the board list
    
    class NormalSpace:        ### This subclass controls what the user does on the Normal Space
        pass

    class LoopSpace:          ### This subclass controls what the user does on the Loop Space
        pass

    class SkipSpace:          ### This subclass controls what the user does on the Skip Space
        pass

    class ExitSpace:          ### This subclass controls what the user does on the Exit Space
        pass

class Board:
    def __init__(self, spaces_instance=Spaces):      ### Makes the Board class that inherits spaces form Spaces class
        self.spaces_instance = spaces_instance
        self.board = []                              # This is the list that will store the board's spaces
        self.spaces = []                             # This is a list that will store the space's locations so that they can be accessed later

    def makeBoard(self, boardSize):                          ### This function makes the board
        if boardSize < 5:                                    # If the user enters a board size smaller than 5
            numOfSpaces = 5                                  # The compiler automaticall makes the board size 5
        else: numOfSpaces = boardSize                        # This number establishes how many spaces are in the board

        for i in range(1, numOfSpaces + 1):
            if i == numOfSpaces:                             # If the iteration equals the last space -> it is automatically set as "Finish"
                newSpace = self.spaces_instance(i, "Finish") 
            else:
                newSpace = self.spaces_instance(i)           # NewSpace = a newly created Space object
            self.spaces.append(newSpace)
            newSpace = newSpace.addSpace()                   # NewSpace then = only the addSpace function from the Space object
            self.board.append(newSpace)                      # The spaces list appends the spaceType and spaceNum from the newly created 
    
    def returnSpaces(self):                          # This function returns the spaces location in memory                     
        return self.spaces
    
    def returnBoard(self):                           # This function returns the board to the user
        return self.board

class Dice:
    def __init__(self):
        self.die1 = rand.randint(1, 6)       # Rolls the first dice -> randomly lands on a number 1-6
        self.die2 = rand.randint(1, 6)       # Rolls the second dice -> randomly lands on a number 1-6
        self.opDie = rand.choice(["-", "+"]) # Rolls the operation dice -> randomly lands on either "+" or "-"
    
    def rollDice(self):                                          ### This function will be used to take each player's turns
        self.die1 = rand.randint(1, 6)                           # Rolls the first dice -> randomly lands on a number 1-6
        self.die2 = rand.randint(1, 6)                           # Rolls the second dice -> randomly lands on a number 1-6
        self.opDie = rand.choice(["-", "+", "-", "+", "-", "+"]) # Rolls the operation dice -> randomly lands on either "+" or "-"

    def getTotalDice(self):                  ### This function gets the total amount of dice and decides how the player moves
        print("Die 1: " + str(self.die1))    # Prints to the user what they randomly rolled for Die 1
        print("Die 2: " + str(self.die2))    # Prints to the user what they randomly rolled for Die 2

        if (self.opDie == "+"):              # If the user rolled a "+" on the operation die then it adds the 2 dice together
            print(str(self.die1) + self.opDie + str(self.die2))
            return (int(self.die1) + int(self.die2))
        
        else:                                # Else if the user rolled a "-" then it subtracts the two dice together
            if (self.die1) > (self.die2):    # If the first die is greater than the second die then it returns Die1 - Die2 
                print(str(self.die1) + self.opDie + str(self.die2))
                return (int(self.die1) - int(self.die2))
            else:                            # Else if the second die is greater then it returns Die2 - Die1
                print(str(self.die2) + self.opDie + str(self.die1))
                return (int(self.die2) - int(self.die1)) 
                    
dice = Dice()
board = Board(Spaces)
print(dice.getTotalDice())

print("")
board.makeBoard(0)
print(board.returnBoard())
