import random
import turtle
import time

# Draws the first row's squares
def draw_square(length):
  for line in range(4):
    turtle.forward(length)
    turtle.right(90)
  turtle.forward(length)
  return length

# Draws the rectangle if the turtle is at the bottom left of the above rectangle/square  
def draw_rectangleBL(length, width):
  turtle.pd()
  for line in range(2):
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(width)
    turtle.right(90)
  turtle.forward(length)
  turtle.pu()
  
# Draws the rectangle if the turtle is at the bottom right of the above rectangle/square
def draw_rectangleBR(length, width):
  turtle.pd()
  for line in range(2):
    turtle.right(90)
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(length)
  turtle.pu()

# Returns the sizes within the column chosen, excluding all the 0s  
def get_column_sizes(column, randomSet):
  global randSetIndex
  # The turtle highlights the current column in black
  column = int(column) - 1
  highlighter.pu()
  highlighter.color("Black")
  highlighter.clear()
  
  # Highlights the column based on user input
  if column == 0:
    highlighter.goto(-200, 200)
    highlighter.pd()
    highlighter.goto(-200, -200)
    highlighter.goto(-200 + randomSet[0], -200)
    highlighter.goto(-200 + randomSet[0], 200)
    highlighter.goto(-200, 200)
  elif column == (randSetIndex - 1):
    highlighter.goto(-200 + randomSet[column - 1], 200)
    highlighter.pd()
    highlighter.goto(-200 + randomSet[column - 1], -200)
    highlighter.goto(200, -200)
    highlighter.goto(200, 200)
    highlighter.goto(-200 + randomSet[column - 1], 200)
  else:
    highlighter.goto(-200 + randomSet[column - 1], 200)
    highlighter.pd()
    highlighter.goto(-200 + randomSet[column - 1], -200)
    highlighter.goto(-200 + randomSet[column], -200)
    highlighter.goto(-200 + randomSet[column], 200)
    highlighter.goto(-200 + randomSet[column - 1], 200)
      
  # Gets the sizes of each shape in the column that user has chosen
  columnSizes = []
  try:  
    columnSizes.append(Lengths[column])
    columnSizes.append(rowTwoWidths[column])
    columnSizes.append(rowThreeWidths[column])
    columnSizes.append(rowFourWidths[column])
    columnSizes.append(rowFiveWidths[column])
    columnSizes.append(rowSixWidths[column])
    columnSizes.append(rowSevenWidths[column])
    columnSizes.append(rowEightWidths[column])
    columnSizes.append(rowNineWidths[column])
    columnSizes.append(rowTenWidths[column])
  except:
    for i in range(len(columnSizes)):  
      if 0 in columnSizes:
        columnSizes.remove(0)
    return columnSizes

## Highlights the bottom column whenever it is done
def highlight_column_done(rectLength, rectWidth):
  global userSizeBig
  
  ### IF the user enters 'hacker mode' and enters a number less than 20 it will NOT
  ### show the green highlighter bar whenever it reaches the bottom
  if (userSizeBig >= 20):
    highlighter.color("Lime")
    highlighter.pd()
    for i in range(2):
      highlighter.forward(rectLength)
      highlighter.right(90)
      highlighter.forward(rectWidth)
      highlighter.right(90)
    highlighter.pu()
  
# Intializes the startup turtle, goes to top left of screen
turtle.hideturtle()  
turtle.speed(0)
turtle.penup()  
turtle.goto(-200, 200)
turtle.pd()

# Intializes main variables
randSet = []
Lengths = []
columnDone = []
randSetSum = 0
allcolumnsDone = False

# Sets the highlighter turtle in get_column_sums and highlight_column_done function
highlighter = turtle.Turtle()
highlighter.clear()
highlighter.ht()
highlighter.speed(0)
highlighter.pensize(5)
highlighter.pu()

### Allows the user to choose a number for all squares in the first row or enter
### the random menus (or the hack menu)
while True:
  print("How big would you like your 1st row squares? (Between 20 and 150)")
  print("r = random between 2 user chosen numbers,")
  userSize = input("Enter = default random [random between 25 - 100]:")
  try:
    if (int(userSize) >= 20 and int(userSize) <= 150):
      userSizeSmall = int(userSize)
      userSizeBig = int(userSize)
      break
    else:
      print("It must be a positive number between 20 and 150!")
      print("")
      time.sleep(1.5)
  except:
    # Breaks into the random menus (r = user random, enter = default random, hack = hacker mode)
    if (userSize == "r" or userSize == "" or userSize == "hack"):
      print("")
      numIterated = 0
      break
    else:
      print("It must be a positive number between 20 and 150!")
      print("")
      time.sleep(1.5)

### IF the user clicks r -> enters the 'user random menu' where the user chooses 2 integers
### and the program will choose random numbers for the size of the squares 
### between the 2 integers the user chooses 
while (userSize == "r"):
  try:  
    userSizeSmall = int(input("How small would you like your 1st random positive number to be (Between 20 and 150):"))
    print("")
    if (userSizeSmall < 20 or userSizeSmall > 150):
      print("The 1st number must be between 20 and 150!")
      print("")
      continue
    print("How big would you like your 2nd random positive number to be? ")
    userSizeBig = int(input("Must be between " + str(userSizeSmall) + " and 150:"))
    print("")
    if ((userSizeSmall < userSizeBig) and (userSizeSmall >= 20 and userSizeBig > 20)
    and (userSizeSmall < 150 and userSizeBig <= 150)):
      break
    else:
      print("The second input must be larger than the first!")
      print("Both must be positive, between 20 and 150 too!")
      print("")
      continue
  except:
    print("Both inputs must be a number between 20 and 150!")
    print("")

### IF the user clicks enter -> enters the 'default random menu' where it chooses
### a number between 25 and 100 for the first row squares
if (userSize == ""):
  userSizeSmall = 25
  userSizeBig = 100

### IF the user enters the phrase "hack" it will enter 'hacker mode'
### In this mode the user can enter any number above 0 but it may 
### lead to some unpredictable outcomes
while (userSize == "hack"):
  if numIterated == 0:      # Only says it is entering Hacker Mode upon entering
    print("*** ENTERING HACKER MODE ***")
    print("This mode is designed for the user to enter ANY number above 0")
    print("This mode will not allow the user to enter a number below 0")
    print("Be warned this may lead to unpredictable outcomes")
    time.sleep(5)
    print("")
    numIterated = 1
  try:  
    userSizeSmall = int(input("How small would you like your 1st random positive number to be:"))
    print("")
    if (userSizeSmall < 0):
      print("The 1st number must be positive!")
      print("")
      continue
    print("How big would you like your 2nd random positive number to be? ")
    userSizeBig = int(input("Must be bigger than or equal to " + str(userSizeSmall) + ":"))
    print("") 
    if ((userSizeSmall <= userSizeBig) and (userSizeSmall > 0 and userSizeBig > 0)):
      break
    else:
      print("The second input must be larger than the first!")
      print("")
      continue
  except:
      print("Both inputs must be a number larger than 0!")
      print("")

# Builds the squares up until it hits x cor = +200         (Row 1)
turtle.color('#%06x' % random.randint(0, 2**24 - 1))
start = time.time()
while (turtle.xcor() <= 200):
  randLength = random.randint(userSizeSmall, userSizeBig)
  Lengths.append(randLength)
  randSetSum = randLength + randSetSum
  randSet.append(randSetSum)
  # If x cor > +175 then it makes sure that there is at least a 25 length square there
  if (randSetSum > 375):               
    xcor = int(turtle.xcor())
    draw_square(200 - xcor)
    Lengths.pop()
    Lengths.append(200 - xcor)
    break
  else:
    draw_square(randLength)

# Gets the randSet's length
randSetIndex = int(len(randSet))
print("Row 1 Complete")
print("")

# Sets up Row 2
turtle.color('#%06x' % random.randint(0, 2**24 - 1))
turtle.pu()
turtle.goto(-200, (200 - randSet[0]))
turtle.pd()
rowTwoWidths = []

rectWidth = random.randint(25, 100)
draw_rectangleBL(Lengths[0], rectWidth)
rowTwoWidths.append(rectWidth)

### For each square in randSet it will go to the bottom left corner of the square
### Then it will draw a new rectangle with same length as the square above it
### but the rectangle has a random width

for i in range(randSetIndex):
  rectLength = Lengths[i]
  rectWidth = random.randint(25, 100)
  if i == 0:    # Skips 1st square since it was already drawn before the for statement
    continue
  rowTwoWidths.append(rectWidth)
  turtle.goto(-200 + randSet[i - 1], 200 - Lengths[i])
  draw_rectangleBL(rectLength, rectWidth)

print("Row 2 Complete")
print("")

# Sets up the 3rd row
turtle.color('#%06x' % random.randint(0, 2**24 - 1))
rowThreeWidths = []
turtle.goto(-200, (200 - (randSet[0] + rowTwoWidths[0])))
turtle.pd()
rectWidth = random.randint(25, 100)
draw_rectangleBL(Lengths[0], rectWidth)
rowThreeWidths.append(rectWidth)

for i in range(randSetIndex):
  rectLength = Lengths[i]
  rectWidth = random.randint(25, 100)
  if i == 0:   # Skips 1st square since it was already drawn before the for statement
    continue
  rowThreeWidths.append(rectWidth)
  turtle.goto(-200 + (randSet[i - 1]), (200 - (Lengths[i] + rowTwoWidths[i])))
  draw_rectangleBL(rectLength, rectWidth)

print("Row 3 Complete")
print("")

# Sets up the 4th row
turtle.color('#%06x' % random.randint(0, 2**24 - 1))
rowFourWidths = []
turtle.goto(-200, (200 - (randSet[0] + rowTwoWidths[0] + rowThreeWidths[0])))
turtle.pd()
rectWidth = random.randint(25, 100)
rowFourWidths.append(rectWidth)

### 4 - 10th rows it finds the sum of the column of squares and rectangles
### This is to make sure that the entire column always hits the bottom at the same
### line as the rest of the rectangles, when y cor = -200
columnSum = Lengths[0] + rowTwoWidths[0] + rowThreeWidths[0] + rowFourWidths[0]

### If the sum of column > 350 then it makes a rectangle with the length of 1st
### row square and a width that will make the sum add up to 400
### IF the column sum < 350, draws with random rectangle width instead
if (columnSum > 350):
  columnSum = Lengths[0] + rowTwoWidths[0] + rowThreeWidths[0]
  definedRectWidth = 400 - columnSum
  rowFourWidths[0] = definedRectWidth
  draw_rectangleBL(Lengths[0], definedRectWidth)
  highlighter.goto(-200, (200 - (randSet[0] + rowTwoWidths[0] + rowThreeWidths[0])))
  highlight_column_done(rectLength, definedRectWidth)
  if (1) not in columnDone:
      columnDone.append(1)
else:
  draw_rectangleBL(Lengths[0], rectWidth)

for i in range(randSetIndex):
  rectLength = Lengths[i]
  rectWidth = random.randint(25, 100)
  if i == 0:    # Skips 1st square since it was already drawn before the for statement
    continue
  rowFourWidths.append(rectWidth)
  turtle.goto(-200 + (randSet[i - 1]), (200 - (Lengths[i] + rowTwoWidths[i] 
  + rowThreeWidths[i])))
  
  ### Gets the column sum and checks if it is more than 350
  ### Otherwise draws with random rectangle width instead
  columnSum = Lengths[i] + rowTwoWidths[i] + rowThreeWidths[i] + rowFourWidths[i]
  if (columnSum > 350):
    columnSum = Lengths[i] + rowTwoWidths[i] + rowThreeWidths[i]
    definedRectWidth = 400 - columnSum
    rowFourWidths[i] = definedRectWidth + 1
    draw_rectangleBL(rectLength, definedRectWidth)
    highlighter.goto(-200 + randSet[i - 1], (200 - (Lengths[i] + rowTwoWidths[i] 
    + rowThreeWidths[i])))
    highlight_column_done(rectLength, definedRectWidth)
    if (i + 1) not in columnDone:
      columnDone.append(i + 1)
  else:
    draw_rectangleBL(rectLength, rectWidth)

if columnDone != []:
  print("Columns done: " + str(columnDone))
  print(str(len(columnDone)) + "/" + str(randSetIndex) + " columns done")
print("Row 4 Complete")
print("")

if int(len(columnDone)) == randSetIndex:
  print("All columns done!")
  allCollumsDone = True
  
# Begins Row 5+ ONLY IF all rows are not done
if allcolumnsDone == False:
  # Sets up the 5th row
  turtle.color('#%06x' % random.randint(0, 2**24 - 1))
  rowFiveWidths = []
  turtle.goto(-200, (200 - (randSet[0] + rowTwoWidths[0] + rowThreeWidths[0] 
  + rowFourWidths[0])))
  turtle.pd()
  rectWidth = random.randint(25, 100)
  rowFiveWidths.append(rectWidth)
  
  ### Gets the column sum and checks if it is more than 350
  ### Otherwise draws with random rectangle width instead
  columnSum = (Lengths[0] + rowTwoWidths[0] + rowThreeWidths[0] + rowFourWidths[0] 
  + rowFiveWidths[0])
  
  if (columnSum > 350):
    columnSum = Lengths[0] + rowTwoWidths[0] + rowThreeWidths[0] + rowFourWidths[0]
    definedRectWidth = 400 - columnSum
    rowFiveWidths[0] = definedRectWidth
    draw_rectangleBL(Lengths[0], definedRectWidth)
    
    # Highlights the column if it is done
    highlighter.goto(-200, 200 - (Lengths[0] + rowTwoWidths[0] 
    + rowThreeWidths[0] + rowFourWidths[0]))
    highlight_column_done(Lengths[0], definedRectWidth)

    if (1) not in columnDone:
        columnDone.append(1)
  else:
    draw_rectangleBL(Lengths[0], rectWidth)
  
  for i in range(randSetIndex):
    rectLength = Lengths[i]
    rectWidth = random.randint(25, 100)
    if i == 0:       # Skips 1st square since it was already drawn before the for statement
      continue
    rowFiveWidths.append(rectWidth)
    turtle.goto(-200 + (randSet[i - 1]), (200 - (Lengths[i] + rowTwoWidths[i] 
    + rowThreeWidths[i] + rowFourWidths[i])))
    
    ### Gets the column sum and checks if it is more than 350
    ### Otherwise draws with random rectangle width instead
    columnSum = (Lengths[i] + rowTwoWidths[i] + rowThreeWidths[i] + rowFourWidths[i]
    + rowFiveWidths[i])
    if (columnSum > 350):
      columnSum = (Lengths[i] + rowTwoWidths[i] + rowThreeWidths[i] + rowFourWidths[i])
      definedRectWidth = 400 - columnSum
      rowFiveWidths[i] = definedRectWidth + 1
      draw_rectangleBL(rectLength, definedRectWidth)
    
    # Highlights column if it is done
      highlighter.goto(-200 + randSet[i - 1], 200 - (Lengths[i] + rowTwoWidths[i] 
    + rowThreeWidths[i] + rowFourWidths[i]))
      highlight_column_done(rectLength, definedRectWidth)
      
      if (i + 1) not in columnDone:
        columnDone.append(i + 1)
    else:
      draw_rectangleBL(rectLength, rectWidth)
  
  if columnDone != []:
    print("Columns done: " + str(columnDone)) 
    print(str(len(columnDone)) + "/" + str(randSetIndex) + " columns done")
  print("Row 5 Complete")
  print("")
  
  if int(len(columnDone)) == randSetIndex:
    print("All columns done!")
    allcolumnsDone = True

# Begins Row 6+ ONLY IF all rows are not done
if allcolumnsDone == False:
  # Sets up the 6th row  
  turtle.color('#%06x' % random.randint(0, 2**24 - 1))
  rowSixWidths = []
  turtle.goto(-200, (200 - (randSet[0] + rowTwoWidths[0] + rowThreeWidths[0] 
  + rowFourWidths[0] + rowFiveWidths[0])))
  turtle.pd()
  rectWidth = random.randint(25, 100)
  rowSixWidths.append(rectWidth)
  
  ### Gets the column sum and checks if it is more than 350
  ### Otherwise draws with random rectangle width instead
  columnSum = (Lengths[0] + rowTwoWidths[0] + rowThreeWidths[0] + rowFourWidths[0] 
  + rowFiveWidths[0] + rowSixWidths[0])
  
  if (columnSum > 350):
    columnSum = (Lengths[0] + rowTwoWidths[0] + rowThreeWidths[0] + rowFourWidths[0] 
    + rowFiveWidths[0])
    definedRectWidth = 400 - columnSum
    rowSixWidths[0] = definedRectWidth
    draw_rectangleBL(Lengths[0], definedRectWidth)
    
    # Highlights the column if it is done
    highlighter.goto(-200, (200 - (randSet[0] + rowTwoWidths[0] + rowThreeWidths[0] 
  + rowFourWidths[0] + rowFiveWidths[0])))
    highlight_column_done(Lengths[0], definedRectWidth)
    
    if (1) not in columnDone:
      columnDone.append(1)
  else:
    draw_rectangleBL(Lengths[0], rectWidth)
  
  for i in range(randSetIndex):
    rectLength = Lengths[i]
    rectWidth = random.randint(25, 100)
    if i == 0:  # Skips 1st square since it was already drawn before the for statement
      continue
    rowSixWidths.append(rectWidth)
    turtle.goto(-200 + (randSet[i - 1]), (200 - (Lengths[i] + rowTwoWidths[i] 
    + rowThreeWidths[i] + rowFourWidths[i] + rowFiveWidths[i])))
    
    ### Gets the column sum and checks if it is more than 350
    ### Otherwise draws with random rectangle width instead  
    columnSum = (Lengths[i] + rowTwoWidths[i] + rowThreeWidths[i] + rowFourWidths[i]
    + rowFiveWidths[i] + rowSixWidths[i])
    
    if (columnSum > 350):
      columnSum = (Lengths[i] + rowTwoWidths[i] + rowThreeWidths[i] + rowFourWidths[i] 
      + rowFiveWidths[i])
      definedRectWidth = 400 - columnSum
      rowSixWidths[i] = definedRectWidth + 1
      draw_rectangleBL(rectLength, definedRectWidth)
      
      # Highlights the column if it is complete
      highlighter.goto(-200 + randSet[i - 1], 200 - (Lengths[i] + rowTwoWidths[i] 
    + rowThreeWidths[i] + rowFourWidths[i] + rowFiveWidths[i]))
      highlight_column_done(rectLength, definedRectWidth)
      
      if (i + 1) not in columnDone:
        columnDone.append(i + 1)
    else:
      draw_rectangleBL(rectLength, rectWidth)
  if columnDone != []:
    print("Columns done: " + str(columnDone))
    print(str(len(columnDone)) + "/" + str(randSetIndex) + " columns done")
  print("Row 6 Complete")
  print("")

  if int(len(columnDone)) == randSetIndex:
    print("All columns done!")
    allcolumnsDone = True

# Begins Row 7+ ONLY IF all rows are not done
if allcolumnsDone == False:
  # Sets up Row 7
  turtle.color('#%06x' % random.randint(0, 2**24 - 1))
  rowSevenWidths = []
  turtle.goto(-200, (200 - (randSet[0] + rowTwoWidths[0] + rowThreeWidths[0] 
  + rowFourWidths[0] + rowFiveWidths[0] + rowSixWidths[0])))
  turtle.pd()
  rectWidth = random.randint(25, 100)
  rowSevenWidths.append(rectWidth)
  
  ### Gets the column sum and checks if it is more than 350
  ### Otherwise draws with random rectangle width instead
  columnSum = (Lengths[0] + rowTwoWidths[0] + rowThreeWidths[0] + rowFourWidths[0] 
  + rowFiveWidths[0] + rowSixWidths[0] + rowSevenWidths[0])
  
  if (columnSum > 350):
    columnSum = (Lengths[0] + rowTwoWidths[0] + rowThreeWidths[0] + rowFourWidths[0] 
    + rowFiveWidths[0] + rowSixWidths[0])
    definedRectWidth = 400 - columnSum
    rowSevenWidths[0] = definedRectWidth
    draw_rectangleBL(Lengths[0], definedRectWidth)
    
    # Highlights the column if it is done
    highlighter.goto(-200, (200 - (randSet[0] + rowTwoWidths[0] + rowThreeWidths[0] 
    + rowFourWidths[0] + rowFiveWidths[0] + rowSixWidths[0])))
    highlight_column_done(Lengths[0], definedRectWidth)
    
    if (1) not in columnDone:
      columnDone.append(1)
  else:
    draw_rectangleBL(Lengths[0], rectWidth)
  
  for i in range(randSetIndex):
    rectLength = Lengths[i]
    rectWidth = random.randint(25, 100)
    if i == 0:  # Skips 1st square since it was already drawn before the for statement
      continue
    rowSevenWidths.append(rectWidth)
    turtle.goto(-200 + (randSet[i - 1]), (200 - (Lengths[i] + rowTwoWidths[i] 
    + rowThreeWidths[i] + rowFourWidths[i] + rowFiveWidths[i] + rowSixWidths[i])))
    
    ### Gets the column sum and checks if it is more than 350
    ### Otherwise draws with random rectangle width instead  
    columnSum = (Lengths[i] + rowTwoWidths[i] + rowThreeWidths[i] + rowFourWidths[i]
    + rowFiveWidths[i] + rowSixWidths[i] + rowSevenWidths[i])
    
    if (columnSum > 350):
      columnSum = (Lengths[i] + rowTwoWidths[i] + rowThreeWidths[i] + rowFourWidths[i] 
      + rowFiveWidths[i] + rowSixWidths[i])
      definedRectWidth = 400 - columnSum
      rowSevenWidths[i] = definedRectWidth + 1
      draw_rectangleBL(rectLength, definedRectWidth)
      
      # Highlights column if it is done
      highlighter.goto(-200 + (randSet[i - 1]), (200 - (Lengths[i] + rowTwoWidths[i] 
      + rowThreeWidths[i] + rowFourWidths[i] + rowFiveWidths[i] + rowSixWidths[i])))
      highlight_column_done(rectLength, definedRectWidth)
      
      if (i + 1) not in columnDone:
        columnDone.append(i + 1)
    else:
      draw_rectangleBL(rectLength, rectWidth)
  
  print("Columns done: " + str(columnDone))
  print(str(len(columnDone)) + "/" + str(randSetIndex) + " columns done")
  print("Row 7 Complete")
  print("")
  
  if int(len(columnDone)) == randSetIndex:
    print("All columns done!")
    allcolumnsDone = True


# Begins Row 8+ ONLY IF all rows are not done
if allcolumnsDone == False:  
  # Sets up Row 8
  turtle.color('#%06x' % random.randint(0, 2**24 - 1))
  rowEightWidths = []
  turtle.goto(-200, (200 - (randSet[0] + rowTwoWidths[0] + rowThreeWidths[0] 
  + rowFourWidths[0] + rowFiveWidths[0] + rowSixWidths[0] + rowSevenWidths[0])))
  turtle.pd()
  rectWidth = random.randint(25, 100)
  rowEightWidths.append(rectWidth)
  
  ### Gets the column sum and checks if it is more than 350
  ### Otherwise draws with random rectangle width instead
  columnSum = (Lengths[0] + rowTwoWidths[0] + rowThreeWidths[0] + rowFourWidths[0] 
  + rowFiveWidths[0] + rowSixWidths[0] + rowSevenWidths[0] + rowEightWidths[0])
  
  if (columnSum > 350):
    columnSum = (Lengths[0] + rowTwoWidths[0] + rowThreeWidths[0] + rowFourWidths[0] 
    + rowFiveWidths[0] + rowSixWidths[0] + rowSevenWidths[0])
    definedRectWidth = 400 - columnSum
    rowEightWidths[0] = definedRectWidth
    draw_rectangleBL(Lengths[0], definedRectWidth)
    
    # Highlights column if it is done
    highlighter.goto(-200, (200 - (randSet[0] + rowTwoWidths[0] + rowThreeWidths[0] 
    + rowFourWidths[0] + rowFiveWidths[0] + rowSixWidths[0] + rowSevenWidths[0])))
    highlight_column_done(Lengths[0], definedRectWidth)
    
    if (1) not in columnDone:
      columnDone.append(1)
  else:
    draw_rectangleBL(Lengths[0], rectWidth)
  
  for i in range(randSetIndex):
    rectLength = Lengths[i]
    rectWidth = random.randint(25, 100)
    if i == 0:  # Skips 1st square since it was already drawn before the for statement
      continue
    rowEightWidths.append(rectWidth)
    turtle.goto(-200 + (randSet[i - 1]), (200 - (Lengths[i] + rowTwoWidths[i] 
    + rowThreeWidths[i] + rowFourWidths[i] + rowFiveWidths[i] + rowSixWidths[i] +
    rowSevenWidths[i])))
    
    ### Gets the column sum and checks if it is more than 350
    ### Otherwise draws with random rectangle width instead  
    columnSum = (Lengths[i] + rowTwoWidths[i] + rowThreeWidths[i] + rowFourWidths[i]
    + rowFiveWidths[i] + rowSixWidths[i] + rowSevenWidths[i] + rowEightWidths[i])
    
    if (columnSum > 350):
      columnSum = (Lengths[i] + rowTwoWidths[i] + rowThreeWidths[i] + rowFourWidths[i] 
      + rowFiveWidths[i] + rowSixWidths[i] + rowSevenWidths[i])
      definedRectWidth = 400 - columnSum
      rowEightWidths[i] = definedRectWidth + 1
      draw_rectangleBL(rectLength, definedRectWidth)
      
      # Highlights column if it is done
      highlighter.goto(-200 + (randSet[i - 1]), (200 - (Lengths[i] + rowTwoWidths[i] 
      + rowThreeWidths[i] + rowFourWidths[i] + rowFiveWidths[i] + rowSixWidths[i] +
      rowSevenWidths[i])))
      highlight_column_done(rectLength, definedRectWidth)
      
      if (i + 1) not in columnDone:
        columnDone.append(i + 1)
    else:
      draw_rectangleBL(rectLength, rectWidth)
  print("Columns done: " + str(columnDone))
  print(str(len(columnDone)) + "/" + str(randSetIndex) + " columns done")
  print("Row 8 Complete")
  print("")
  
  if int(len(columnDone)) == randSetIndex:
    print("All columns done!")
    allcolumnsDone = True

# Begins Row 9+ ONLY IF all rows are not done
if allcolumnsDone == False:
  # Sets up Row 9
  turtle.color('#%06x' % random.randint(0, 2**24 - 1))
  rowNineWidths = []
  turtle.goto(-200, (200 - (randSet[0] + rowTwoWidths[0] + rowThreeWidths[0] 
  + rowFourWidths[0] + rowFiveWidths[0] + rowSixWidths[0] + rowSevenWidths[0]+
  rowEightWidths[0])))
  turtle.pd()
  rectWidth = random.randint(25, 100)
  rowNineWidths.append(rectWidth)
  
  ### Gets the column sum and checks if it is more than 350
  ### Otherwise draws with random rectangle width instead
  columnSum = (Lengths[0] + rowTwoWidths[0] + rowThreeWidths[0] + rowFourWidths[0] 
  + rowFiveWidths[0] + rowSixWidths[0] + rowSevenWidths[0] + rowEightWidths[0]
  + rowNineWidths[0])
  
  if (columnSum > 350):
    columnSum = (Lengths[0] + rowTwoWidths[0] + rowThreeWidths[0] + rowFourWidths[0] 
    + rowFiveWidths[0] + rowSixWidths[0] + rowSevenWidths[0] + rowEightWidths[0])
    definedRectWidth = 400 - columnSum
    rowNineWidths[0] = definedRectWidth
    draw_rectangleBL(Lengths[0], definedRectWidth)
    
    # Highlights column if it is done
    highlighter.goto(-200, (200 - (randSet[0] + rowTwoWidths[0] + rowThreeWidths[0] 
    + rowFourWidths[0] + rowFiveWidths[0] + rowSixWidths[0] + rowSevenWidths[0]+
    rowEightWidths[0])))
    highlight_column_done(Lengths[0], definedRectWidth)
    
    if (1) not in columnDone:
      columnDone.append(1)
  else:
    draw_rectangleBL(Lengths[0], rectWidth)
  
  for i in range(randSetIndex):
    rectLength = Lengths[i]
    rectWidth = random.randint(25, 100)
    if i == 0:  # Skips 1st square since it was already drawn before the for statement
      continue
    rowNineWidths.append(rectWidth)
    turtle.goto(-200 + (randSet[i - 1]), (200 - (Lengths[i] + rowTwoWidths[i] 
    + rowThreeWidths[i] + rowFourWidths[i] + rowFiveWidths[i] + rowSixWidths[i] +
    rowSevenWidths[i] + rowEightWidths[i])))
    
    ### Gets the column sum and checks if it is more than 350
    ### Otherwise draws with random rectangle width instead  
    columnSum = (Lengths[i] + rowTwoWidths[i] + rowThreeWidths[i] + rowFourWidths[i]
    + rowFiveWidths[i] + rowSixWidths[i] + rowSevenWidths[i] + rowEightWidths[i] 
    + rowNineWidths[i])
    
    if (columnSum > 350):
      columnSum = (Lengths[i] + rowTwoWidths[i] + rowThreeWidths[i] + rowFourWidths[i] 
      + rowFiveWidths[i] + rowSixWidths[i] + rowSevenWidths[i] + rowEightWidths[i])
      definedRectWidth = 400 - columnSum
      rowNineWidths[i] = definedRectWidth + 1
      draw_rectangleBL(rectLength, definedRectWidth)
      
      # Highlight column if it is done
      highlighter.goto(-200 + (randSet[i - 1]), (200 - (Lengths[i] + rowTwoWidths[i] 
      + rowThreeWidths[i] + rowFourWidths[i] + rowFiveWidths[i] + rowSixWidths[i] +
      rowSevenWidths[i] + rowEightWidths[i])))
      highlight_column_done(rectLength, definedRectWidth)
      
      if (i + 1) not in columnDone:
        columnDone.append(i + 1)
    else:
      draw_rectangleBL(rectLength, rectWidth)
  print("Columns done: " + str(columnDone))
  print(str(len(columnDone)) + "/" + str(randSetIndex) + " columns done")
  print("Row 9 Complete")
  print("")
  
  if int(len(columnDone)) == randSetIndex:
    print("All columns done!")
    allcolumnsDone = True

# Begins FINAL ROW ONLY IF all rows are not done
if allcolumnsDone == False:
  # Sets up Row 10 (FINAL ROW)
  turtle.color('#%06x' % random.randint(0, 2**24 - 1))
  rowTenWidths = []
  turtle.goto(-200, (200 - (randSet[0] + rowTwoWidths[0] + rowThreeWidths[0] 
  + rowFourWidths[0] + rowFiveWidths[0] + rowSixWidths[0] + rowSevenWidths[0]+
  rowEightWidths[0] + rowNineWidths[0])))
  turtle.pd()
  
  ### Gets the column sum and gives the final width equal to 400 - columnSum
  columnSum = (Lengths[0] + rowTwoWidths[0] + rowThreeWidths[0] + rowFourWidths[0] 
  + rowFiveWidths[0] + rowSixWidths[0] + rowSevenWidths[0] + rowEightWidths[0]
  + rowNineWidths[0])
  
  rectWidth = 400 - columnSum
  rowTenWidths.append(rectWidth)
  draw_rectangleBL(Lengths[0], rectWidth)
  if (1) not in columnDone:
    columnDone.append(1)
  
  for i in range(randSetIndex):
    rectLength = Lengths[i]
    if i == 0:  # Skips 1st square since it was already drawn before the for statement
      continue
    
    turtle.goto(-200 + (randSet[i - 1]), (200 - (Lengths[i] + rowTwoWidths[i] 
    + rowThreeWidths[i] + rowFourWidths[i] + rowFiveWidths[i] + rowSixWidths[i] +
    rowSevenWidths[i] + rowEightWidths[i] + rowNineWidths[i])))
    
    ### Gets the column sum and checks if it is more than 350
    ### Otherwise draws with random rectangle width instead  
    columnSum = (Lengths[i] + rowTwoWidths[i] + rowThreeWidths[i] + rowFourWidths[i]
    + rowFiveWidths[i] + rowSixWidths[i] + rowSevenWidths[i] + rowEightWidths[i] 
    + rowNineWidths[i])
    rectWidth = 400 - columnSum
    rowTenWidths.append(rectWidth)
    
    if (i + 1) not in columnDone:
      columnDone.append(i + 1)
    draw_rectangleBL(rectLength, rectWidth)
    
  print("Columns done: " + str(columnDone))
  print("FINAL ROW Complete")
  print("")

end = time.time()
elapsedTime = end - start
print("Elapsed time: " + str(elapsedTime) + " seconds")
### Lets the user enter a number for a column and the function get_column_sizes
### will return the column sizes from top to bottom 
### a.nd the turtle will highlight the column in black
highlighter.clear()
reset = "A"
while (reset != ""):
  try:
    print("")
    userColumn = int(input("Choose a column (1 - " + str(randSetIndex) + ") to get the size of all the shapes:"))
    if (userColumn > 0 and userColumn <= int(randSetIndex)):
      columnSize = get_column_sizes(userColumn, randSet)
      print (str(columnSize) + " [Top -> Bottom]")
    
  except:
    print("")
  reset = input("Would you like to reset? Enter to escape: ")
  
highlighter.clear()  
print("Goodbye!")
