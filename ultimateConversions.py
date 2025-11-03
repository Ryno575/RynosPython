### Number <-> Hex <-> Binary Converter
### DESCRIPTION ###
### This is an ongoing project where one day the user will be able to enter a number, binary, and/or hexadecimal set and ###
### it will take it into this huge conversion machine and return to the user a number, binary and/or hexadecimal set in ###
### relation to the given set ###

import math
class Conversion:
    def __init__(self, binaryString, hexString, numberString):
            self.binaryAndHexDictionary = {"0000": "0", "0001": "1", "0010": "2", "0011": "3", 
                                           "0100": "4", "0101": "5", "0110": "6", "0111": "7", 
                                           "1000": "8", "1001": "9", "1010": "A", "1011": "B",
                                           "1100": "C", "1101": "D", "1110": "E", "1111": "F"}
            self.binaryString = "0b" + str(binaryString)              ## Initalizes overall binaryString that is used in the subclasses
            self.hexString = "0x" + str(hexString)                    ## Initalizes overall hexString that is used in the subclasses
            self.numberString = str(numberString)                     ## Initalizes overall numberString that is used in the subclasses
                                    
            self.binarySets = self.setBinarySets()                    # This is where the sets of binary strings will be stored
            
    def setBinarySets(self):                                          ## Sets the binary sets (the binary string split into groups of 4) based off of the current binary string
        localBinaryString = self.binaryString[2:]                     # Removes the '0b' from the beginning of the binary string to be used as the local string
        binarySets = []
        for i in range(int(math.ceil((len(localBinaryString) / 4)))): # Takes the binary string and divides into sections of 4 (ex. '0bXXXXYYYYZZZZ' -> 'XXXX YYYY ZZZZ')
            if i == 0:
                currSet = localBinaryString[-4*(i+1):]                # Starts from the right end and takes the last 4 numbers
            else:
                 currSet = localBinaryString[-4*(i+1):i*(-4)]         # Continues on until there the loop reaches the left end
            while len(currSet) != 4:                                  ## If any set has less than 4 digits (the leftmost is the most common for this) 
                currSet = '0' + str(currSet)                          ## then it will add 0s to the front of the set so that it can be read through the dictionary
            binarySets.append(currSet)                                # Adds the current set to a list
        
        def reverseList(origList):                           # A local function that reverses the binarySets list (this list needs to be reversed because the setBinarySets function initally has the sets in the opposite order) 
            reversedList = []
            for i in range(1, len(origList) + 1):            # Goes through the list from right-end to left-end
                reversedList.append(origList[-i])            # Adds every iteration of original list into new list
            return reversedList
                          
        return reverseList(binarySets)                       # Returns the reversed list

    def setBinaryString(self, newBinaryString):
        self.binaryString = newBinaryString                         # Allows user to change to a new binary string
        self.binarySets = self.setBinarySets()                      # This is where the sets of binary strings will be reset and restored with the new binary string

    def setHexString(self, newHexString):                           # Allows user to change to a new hexademical string
        self.hexString = "0x" + str(newHexString)
    
    def setNumberString(self, newNumberString):                     # Allows user to change to a new number string
        self.numberString = str(newNumberString)
    
    class ToBinary:
        def __init__(self, outer_instance):
            self.outer = outer_instance                              # Points a reference to the outer class Conversion

        def numToBinary(self):                                        ### NEED TODO ###
            return
        
        def hexToBinary(self):                                        ### NEED TODO ###
            return

    class ToNumber:
        def __init__(self, outer_instance):
            self.outer = outer_instance                              # Points a reference to the outer class Conversion

        def binaryToNum(self):
            total = 0                                                # Total = the binary in decimal form
            localBinaryString = self.outer.binaryString[2:]          # Removes the '0b' from the beginning of the binary string to be used as the local string
            for i in range(1, len(localBinaryString) + 1):     # Loops from the right end of the string until left end of the string {from -1 to -(length of binaryString)}
                if (int(localBinaryString[-i]) == 1):          # If the current index == 1
                    total += 2**(i-1)                                # Add 2 to the power of (the current index - 1) to the current total {it is i - 1 because we started from 1 -> length of string + 1 in the loop}
            return self.outer.binaryString + " -> " + str(total)                                             # Return the decimal total to the user

        def hexToNum(self):                                          ### NEED TODO ###
            return

    class ToHexadecimal:
        def __init__(self, outer_instance):
            self.outer = outer_instance                              # Points a reference to the outer class Conversion

        def binaryToHex(self):
            hexConversion = "0x"                                          # Begins the hex conversion with '0x'
            for i in range( len(self.outer.binarySets)):                  # Reads the binarySets list from left end to right end
                currSet = self.outer.binarySets[i]
                hexConversion += self.outer.binaryAndHexDictionary[currSet]     # Adds the corresponding number (1-9) or letter (A-F) from the binary and hexadecmical dictionary
                
            return self.outer.binaryString + " -> " + str(hexConversion)        # Returns the binary to hexadecimal conversion
        
        def numToHex(self):                                            ### NEED TODO ###
            return
   
conv = Conversion("10110011", "", "")  # Outermost class (Conversion)

toHex = conv.ToHexadecimal(conv)        # Inner class (Hex(pointing to Conversion))
toNum = conv.ToNumber(conv)             # Inner class (Num(pointing to Conversion))

print(toHex.binaryToHex())              # Runs the function binaryToHex from the ToHexadecimal class
conv.setBinaryString("10100101")        # Rewrites binary string as "1010 0101"

print(toNum.binaryToNum())              # Runs the function binaryToNum from the ToNum class
