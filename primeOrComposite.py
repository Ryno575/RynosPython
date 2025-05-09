factors = [1]
prime = True

while True:
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

print("")
for i in range(userNum):             # Goes through every number from 2 - userNum
  if (i == 0 or i == 1):             # (Skips 0 and 1) and finds all the factors 
    continue                         # of the userNum
  divisor = str(userNum / i)
  divisorLastNum = divisor[-1]
  if divisorLastNum == "0":          # If the number ends in #.0 then it is a factor
    prime = False                    # and no longer prime
    factors.append(i)

factors.append(userNum)

for i in range(len(factors) - 1):        # Once the factors are found it goes through
  firstNum = factors[i]                  # the list and puts a mirror '|' where the 
  secondNum = factors[i + 1]             # number on the left and right of the mirror
  if (firstNum * secondNum == userNum):  # multiply together to get the userNum
    factors.insert(i + 1, "|")           # (ex. 1,2,|,4,8) (ex. 1,3,9,|,11,33,99)

if prime == True:
  print(str(userNum) + " is prime")
else:
  print(str(userNum) + " is composite")
  print("Factors: " + str(factors))
print("")
