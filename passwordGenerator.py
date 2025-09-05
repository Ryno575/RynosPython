# Password Generator
# Generates a password of character length 15 (can be changed on line 7; [length will always be >= 4]) that has a number, capital letter, and a symbol with characters that are filled in between.
import random
characters = []
symbols = []
letters = []
characterLength = 15  # Change this number to change password length

def passWord_Generator(numOfCharacters):
  if numOfCharacters <= 3:              ## If the user inputs a character length of less than 4:
    numOfCharacters = 4                 ## the program automatically forces it to be 4 to include a number, capital letter and a symbol
  capital = False
  capital_index = 0
  symbol = False
  symbol_index = 0
  number = False
  number_index = 0
  
  ## Sets the index for a required capital letter, symbol, and number
  ## Also makes sure that none of the indexes match before exitting loop
  while (number_index == symbol_index) or (symbol_index == capital_index) or (capital_index == number_index):
    number_index = random.randint(0, numOfCharacters - 1)
    symbol_index = random.randint(0, numOfCharacters - 1)  
    capital_index = random.randint(0, numOfCharacters - 1)
  
  ### Inserts a random number, symbol, and capital at the required indexes
  ### and fills the rest of the password with random characters
  password = ""
  for i in range(numOfCharacters):
    if i == number_index:
      password = password + str(random.randint(0, 9))
    elif i == symbol_index:
      password = password + symbols[(random.randint(0, len(symbols) - 1))]
    elif i == capital_index:
      password = password + letters[random.randint(0, 25)]
    else:
      password = password + characters[random.randint(0, len(characters) - 1)]
  return password

# Adds all symbols and letters (upper/lower) into seperate lists so it is easy to make
# the password
for i in range(ord('!'), ord('z') + 1): 
  if (i >= ord('!') and i < ord('0')) or (i >= ord(':') and i <= ord('@')) or (i > ord('Z') and i < ord('a')):
    symbols.append(chr(i))               # Adds all symbols
  elif i >= ord('0') and i < ord(':'):   
    continue                             # Skips all numbers
  else:
    letters.append(chr(i))               # Adds all letters
  characters.append(chr(i))              # Adds all letters, numbers and symbols to a 
                                         # character list
print(passWord_Generator(characterLength))
