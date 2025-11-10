import random as rand
class Game:                             ### This is where the entire game is located
    def __init__(self, board_instance, dice_instance):
        self.board = board_instance
        self.dice = dice_instance

    def createBoard(self):                ### This function accesses the Board class and makes the board and prints it for the user
        self.board.makeBoard(15)
        return self.board.returnBoard()

    def getTotalDice(self):            ### This function accesses the Dice class and prints the dice output to the user
        return self.dice.getTotalDice()
    
    def takeTurn(self, player_instance):                                     ### This function forces the game to move along and forces each player to take their turn
        print("")
        print("Current Player: '" + player_instance.getName() + "'")         # Returns the current player taking their turn
        print("")
        board.resetSpace(player_instance.getCurrentSpace(), player_instance) # This function resets the board to how it previously was before the player reached this current space
        print("***Dice Roll***")
        self.dice.rollDice()                                                 # This rolls the dice for the current player
        moveSpaces = self.dice.getTotalDice()                                # This function stores the dice roll from the previous step into moveSpaces
        print("")
        player_instance.setCurrentSpace(moveSpaces)                          # The player is then moved to this new space based on (the space they currently are on) + (the dice roll they just recieved)
        playerCurrSpace = player_instance.getCurrentSpace()                  # This then stores the new player's current space into playerCurrSpace
        board.movePlayer(playerCurrSpace, player_instance)                   # This final function updates the Board with the current space that the player is on and the current player
        print("Player: '" + player_instance.getName() + "' is currently on space: " + str(player_instance.getCurrentSpace()))
        print("")
        return self.board.returnBoard()                                      # Return the newly set up board with the player on the new space

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
        elif self.spaceType == "Finish":      # If the space type is automatically set to "Finish" -> skip this step
            pass
        else:                                 # Else -> picks a randomly chosen space type
            self.setSpace()
        return self.spaceType, self.spaceNum  # Returns the space type and the number to the board list
    
    def getSpaceType(self):       # Returns the space type of the current Space object
        return self.spaceType
    
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
        if boardSize < 10:                                    # If the user enters a board size smaller than 5
            numOfSpaces = 10                                  # The compiler automaticall makes the board size 5
        else: numOfSpaces = boardSize                        # This number establishes how many spaces are in the board

        for i in range(1, numOfSpaces + 1):
            if i == numOfSpaces:                             # If the iteration equals the last space -> it is automatically set as "Finish"
                newSpace = self.spaces_instance(i, "Finish") 
            else:
                newSpace = self.spaces_instance(i)           # NewSpace = a newly created Space object
            self.spaces.append(newSpace)
            newSpace = newSpace.addSpace()                   # NewSpace then = only the addSpace function from the Space object
            self.board.append(newSpace)                      # The spaces list appends the spaceType and spaceNum from the newly created 
    
    def movePlayer(self, currSpace, player_instance):        ### This function moves the current Player object on the board list that is outputted to the users 
        spaceString = self.spaces[currSpace - 1]             # Stores the current Space object in spaceString
        spaceString = spaceString.getSpaceType(), player_instance.getCurrentSpace(), "Player: " + player_instance.getName()
        self.board[currSpace - 1] = spaceString              # Returns the [spaceType], currentSpace, and name of player to the current space

    def resetSpace(self, currSpace, player_instance):        ### This fucntion resets the board so that it resets the board to look like how it was at the start of the game
        spaceString = self.spaces[currSpace - 1]             # Stores the current Space object in spaceString 
        spaceString = spaceString.getSpaceType(), player_instance.getCurrentSpace() 
        self.board[currSpace - 1] = spaceString              # Returns the [spaceType] and currentSpace to the current space

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
            print(str(self.die1) + " " + self.opDie + " " + str(self.die2) + " = " + str(int(self.die1) + int(self.die2)))
            return (int(self.die1) + int(self.die2))
        
        else:                                # Else if the user rolled a "-" then it subtracts the two dice together
            if (self.die1) > (self.die2):    # If the first die is greater than the second die then it returns Die1 - Die2 
                print(str(self.die1) + " " + self.opDie + " " + str(self.die2) + " = " + str(int(self.die1) - int(self.die2)))
                return (int(self.die1) - int(self.die2))
            else:                            # Else if the second die is greater then it returns Die2 - Die1
                print(str(self.die2) + " " + self.opDie + " " + str(self.die1) + " = " + str(int(self.die2) - int(self.die1)))
                return (int(self.die2) - int(self.die1)) 

class Player:
    def __init__(self, name):
        self.name = name
        self.currSpace = 1                  # Starts the user on the 'Start' space on the board

    def setCurrentSpace(self, spaceChange):           ### This function changes the current space the player is on based on the roll
        self.currSpace = self.currSpace + spaceChange

    def getCurrentSpace(self):                        ### This function returns the current space the player is on
        return self.currSpace

    def getName(self):                                ### This function returns the name of the player
        return self.name

dice = Dice()
board = Board(Spaces)
player1 = Player("A")
player2 = Player("B")
game = Game(board, dice)
print(game.createBoard())

print(game.takeTurn(player1))
print(game.takeTurn(player1))
print(game.takeTurn(player1))
