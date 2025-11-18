### DESCRIPTION ###
### This program allows the user to enter any number between 1 and 999,999) ###
### Once the user enters a valid number then it goes through every number from 2 -> (user's number) ###
### In this loop it checks to see if each number can be divided into the user's number ###
### If the number can be divided [(i / (user's number) == X.0) where X is a double that has at least 1 decimal number followed by it] then it adds it to the factors of the user's number list ###
### Once done with the loop, the compiler will return the list of factors followed by a '|' character for the middle value (ex. [1, 2, | 4, 8] or [1, |3,| 9] for square numbers) 
### There is also a secret Prime/Composite menu if the user enters -1 instead of a number 1 - 999,999 ###
### This menu is used to find every Prime or Composite number between 1 and the number the the user chooses ###

factors = [1]  # Starts with 1 as a factor because all integers have 1 as a factor
prime = True   # All numbers are prime until proven otherwise
prime_composite_mode = False  # A secret mode that returns all prime or composite numbers between 1 and a number the user inputs

while True:
  try:
    userNum = int(input("Enter any positive number (1 - 999,999):"))
    if userNum < -1 or userNum == 0:
      print("Please enter a positive number")
      print("")
    elif userNum >= 1000000:
      print("Please enter a number smaller than 1,000,000")
      print("")
    elif userNum == -1:
      prime_composite_mode = True
      iteration = 0
      break
    else:
      break
  except:
    print("Please enter a positive number between 0 and 1,000,000")
    print("")

print("")

# A secret mode that returns all prime or composite numbers between 1 and a number the user inputs
while prime_composite_mode == True:   # IF user enters -1 then it enters prime/composite mode
  run = False
  storedNumbers = []
  # A specific menu that only pops up while entering Prime/Composite Mode
  if iteration == 0:
    print("Welcome to Prime/Composite Mode!")
    print("In this mode you can enter a number and it will return all prime or composite numbers between 0 and the entered number")
    iteration += 1 # Does not show this menu after this point
  prime_or_composite = input("Please enter 'P' for prime or 'C' for composite")
  print("")
  
  if prime_or_composite.lower() == 'p': # If user enters 'p' -> Enters prime mode
    while run != True:
      try:
        userNum = int(input("Enter any positive number (Between 0 and 1,000,000):"))
        if userNum <= 0:
          print("Please enter a positive number")
          print("")
        elif userNum >= 1000000:
          print("Please enter a number smaller than 1,000,000")
        else:
          break
      except:
        print("Please enter a positive number")
    
    print("")    
    for i in range(2, userNum): # Runs from 2 to the number that the user chose
      prime = True              # Checks for prime numbers during each iteration
      for j in range(2, i):     # Runs each number from 2 -> userNum and checks to see which ones are prime or not
        divisor = str(i / j)
        divisorLastNum = divisor[-1]
        if divisorLastNum == "0":    # If the number has a factor -> not prime
          prime = False
      if prime == True:         # Adds number to a list if it is prime
        storedNumbers.append(i)
    print("Prime Numbers between 2 and " + str(userNum) + ": " + str(storedNumbers))
    print("")                   # Prints all numbers from 2 -> userNum that are prime
    run = True
    prime_composite_mode = False

  elif prime_or_composite.lower() == 'c': # If user enters 'c' -> enters composite mode
    while run != True:
      try:
        userNum = int(input("Enter any positive number (Between 0 and 1,000,000):"))
        if userNum <= 0:
          print("Please enter a positive number")
          print("")
        elif userNum >= 1000000:
          print("Please enter a number smaller than 1,000,000")
        else:
          break
      except:
        print("Please enter a positive number")

    print("")    
    for i in range(2, userNum): # Runs from 2 to the number that the user chose
      prime = True              # Checks for prime numbers during each iteration
      for j in range(2, i):     # Runs each number from 2 -> userNum and checks to see which ones are prime or not
        divisor = str(i / j)
        divisorLastNum = divisor[-1]
        if divisorLastNum == "0":
          prime = False
      if prime == False:        # Adds number to a list if it is composite
        storedNumbers.append(i)
    print("Composite Numbers between 2 and " + str(userNum) + ": " + str(storedNumbers))
    print("")                   # Prints all composite numbers from 2 -> userNum
    run = True
    prime_composite_mode = False
    
for i in range(2, userNum):          # Goes through every number from 2 - userNum
  divisor = str(userNum / i)
  divisorLastNum = divisor[-1]
  if divisorLastNum == "0":          # If the number ends in #.0 then it is a factor
    prime = False                    # and no longer prime
    factors.append(i)

factors.append(userNum)

# Once the factors are found it goes through the list and puts a mirror '|' where the 
# number on the left and right of the mirror multiply together to get the userNum
# (ex. 1,2,|,4,8 -> 1*8, 2*4) (ex. 1,3,9,|,11,33,99 -> 1*99, 3*33, 9*11)
median = False
for i in range(len(factors) - 1):                  
  firstNum, secondNum = factors[i], factors[i + 1]
  if median == False:
    if (firstNum * secondNum == userNum):
      factors.insert(i + 1, "|")
      median = True
    elif (firstNum * firstNum == userNum):  # There is also a double mirror case (| # |)
      factors.insert(i, "|")                # where the number (#) within the two mirrors
      factors.insert(i + 2, "|")            # can be squared to get the userNum
      median = True

if prime == True:
  print(str(userNum) + " is prime")
else:
  print(str(userNum) + " is composite")
  print("Factors: " + str(factors))
