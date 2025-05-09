def stringLength(origString):           # Returns the length of the given string
  return len(origString)
  
def findChar(origString, char):         # Finds a specific character in the given string
  indexes = []
  for i in range(len(origString)):
    currChar = origString[i]
    if (char == currChar):              # Adds the index of the character in string if in string
      indexes.append(i)
  if indexes == []:                     # If there is no character then it'll print "N/A"
    indexes.append("N/A")
  return indexes

def findWord(origString, word):         # Finds the given word in the given string
  print
  
def charFrequency(origString):          # Takes every single character in the string and
  charInString = []                     # puts it into a list
  numChars = []
  maxChar = 0
  for i in range(len(origString)):      
    currChar = origString[i]
    if (currChar not in charInString):  # If char is not in string -> adds it to 
      charInString.append(currChar)     # charInString, also adds a 1 to numChars
      numChars.append(1)                # to match with the character position
    else:
      for i in range(len(charInString)):
        if currChar == charInString[i]: # If char is already in charInString then it
          tempNum = numChars[i]         # finds where the character is located and adds
          tempNum += 1                  # 1 to the same position in numChars
          numChars[i] = tempNum         # (ex. String = "Hello"; ['H', 'e', 'l', 'o'])
                                        # (ex. cont.             ['1', '1', '2', '1'])
                                        
  for i in range(len(numChars)):                            # Goes through 
    if (numChars[i] > maxChar and charInString[i] != ' '):  # numChars to find 
      maxChar = numChars[i]                                 # the one that appears 
      mostCommonChar = charInString[i]                      # the most in the string
                                                            # (excludes spaces)
  print("Characters in string: " + str(charInString))       
  print("")
  print("Number of characters: " + str(numChars))
  print("")
  print("Most common character: '" + str(mostCommonChar) + "' appearing " + str(maxChar) + " times")

### PRIMARY STRING ###
string = "Is it okay if I just start putting a bunch of random words to make the length of the string really long? Apple Banana Purple Black Green and Pink"

print("Length of string: " + str(stringLength(string)))

userChar = 'a'
print("")
print("The character '" + userChar + "' appears in the phrase '" + string + "' at: " + str(findChar(string, userChar)))
print("")
charFrequency(string)
