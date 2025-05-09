# Used this program for my CS272 [Introduction to Data Structures] class
itemList = ["M&Ms", "Trail Mix", "Lays: Original", "Lays: Barbecue", "Doritos: Nacho Cheese", 
            "Doritos: Cool Ranch", "Kit-Kat", "Snickers", "3 Muskateers", "Water"]
moneyList = [1.50, 0.75, 1.00, 1.00, 1.00, 1.00, 1.25, 1.50, 1.25, 0.50]
reset = True

while reset == True:                   ### Asks the user to enter an amount of money
  userMoney = input("Please enter an amount of money:")
  print("")
  try:                                
    userMoney = float(userMoney)       ### Breaks the loop if the user enters a number
    reset = False
  except:                              ### If the input given is not a number then it asks 
    print("Please enter a number")     ### the user again to enter a number

while reset != "n":
  buyableList = []
  for i in range(len(moneyList)):      ### Goes through the list of items and if the user's
    currMoney = moneyList[i]           ### amount of money is less then currItem, adds it
    if userMoney >= currMoney:         ### to list of buyable items
      buyableList.append(str(i) + ": " + str(itemList[i]))
  print("You can buy: " + str(buyableList))
  print("")
  reset = input("Would you like to add any more money? (y or n)") ### The user can enter more
  if reset == "y":                                                ### money if they enter 'y'
    addedMoney = input("Please enter how much you would like to add:")
    addedMoney = float(addedMoney)
    userMoney += addedMoney   ### New money is added and resets back to line 15
    print("Your new amount of money: $" + str(userMoney))
    print("")

  else:  ### Asks the user what item they would like to buy based off the index
    print("")
    indexBought = input("Which item would you like to buy? (Enter a number 0 - 9)")
    indexBought = int(indexBought) 
    if indexBought > 9 or indexBought < 0:  ### Resets to line 15 if the number given is not
      print("Please choose a number 0 - 9") ### between 0 and 9
      print("")
      reset = "a"

    else: ### Checks to make sure the user has enough money to buy the item
      moneySpent = moneyList[indexBought]
      if moneySpent > userMoney:         ### Resets to line 15 if the user can't buy the item
        print("You do not have enough money to buy this item")
        print("")
        reset = "a"

      else: ### Buys the item for the user, takes away money for the item's worth, returns change
        userMoney = userMoney - moneySpent
        print("")
        print("You have bought: " + itemList[indexBought])
        print("You have been returned: $" + str(userMoney))

print("")
print("Thank you for shopping at the Vending Machine")
