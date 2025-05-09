import random as rand

user = "A" 
names = []


while (user != ""):
  user = input("Please enter a name for Secret Santa (Enter to esc): ")
  if (user == "" and len(names) < 2):
    print("You must enter at least 2 names")
    print("")
    user = "A"
    continue
  elif (user == ""):
    break
  elif (user in names):
    print("You have already entered this name")
    print("")
  else:
    names.append(user)
    print("")

originalNames = names[:] # Copies list to be seperate from its original
origNames = names[:]
i = 0
reset = ""

while (reset == ""):
  names = originalNames[:]
  i = 0
  while (names != []):
    for name in names:
      print("")
      i += 1
      while True:
        currName = rand.choice(names)
        if ((currName == name) and i == len(origNames)):
          names = origNames
          i = 0
          name = names[0]
          print("***RESETTING***")
          print("")
          break
        elif (currName == name):
          continue
        else:
          print(name + ": " + currName)
          names.remove(currName)
          break
      if i == len(origNames):
        break
  print("")
  reset = input("Would you like to reset? Enter for yes: ")
