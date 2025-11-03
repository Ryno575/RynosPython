import random as rand
import matplotlib.pyplot as plt
from numpy import *

def sortList(origList):           # Sorts the original list from least to greatest
  sortedList = []                 # Print(sorted(numbers)) - Same thing as this
  for i in range(len(origList)): 
    minNum = origList[0]
    for j in range(len(origList)):
      if minNum >= origList[j]:
        minNumIndex = j
        minNum = origList[j]
    currNum = origList.pop(minNumIndex)
    sortedList.append(currNum)
  return sortedList
  
def reverseList(origList):                # Reverses the list
  reversedList = []                     
  for i in range(1, len(origList) + 1):   # Goes through the list from right-end to left-end
    reversedList.append(origList[-i])     # Adds every iteration of original list into new list
  return reversedList                  
  
def sumList(origList):                    # Returns the total sum of the list
  total = 0
  for i in range(len(origList)):
    total = total + origList[i]
  return total
  
def rangeList(origList):                  # Returns the range of the list (Max - Min)
  return(origList[-1] - origList[0])
  
def averageList(origList, total):         # Returns the average dividing the sum by  
  average = float(total) / len(origList)  # the length of the list
  return round(average, 3)
  
def medianList(origList):                 # Returns the median of the list
  origList = sorted(origList)             # The list given MUST be sorted                                   # Once sorted the function can find median
  if (len(origList) % 2 == 0):
    medianIndex1 = int(len(origList) / 2)  # IF length is even it finds 2 median
    medianIndex2 = medianIndex1 - 1        # indexes and then takes avg of both
    median1 = origList[medianIndex1]
    median2 = origList[medianIndex2]
    median = (median2 + median1) / 2
  else:
    medianIndex = int(len(origList) / 2)   # ELSE length is odd it divides the
    median = origList[medianIndex]         # length in 2 and thats the median
  return(median)

def modeList(origList):              # This function first creates a linked list between
  listedNums = []                    # the original list and a frequency list where it
  numFrequency = []                  # will add 1 to the frequency list if there are
  maxFrequency = 1                   # multiple copies of a number
  for i in range(len(origList)):
    currNum = origList[i]
    if (currNum not in listedNums):
      listedNums.append(currNum)
      numFrequency.append(1)
    else:
      for i in range(len(listedNums)):
        if currNum == listedNums[i]:
          tempNum = numFrequency[i]
          tempNum += 1
          numFrequency[i] = tempNum
  
  for i in range(len(numFrequency)):  # When the frequency list is finished, it finds the
    currFrequency = numFrequency[i]   # number with the highest frequency and then pairs
    if maxFrequency < currFrequency:  # it with the number list
      maxFrequency = currFrequency
      frequencyIndex = i
  if maxFrequency == 1:               # IF the max frequency is 1, then there is no mode
    return "NONE"
  else:                               # Else -> returns the number and how many times it appears
    return (str(listedNums[frequencyIndex]) + " appearing " + str(maxFrequency) + " times")

def drawGraph(origList):
  ylist = []
  for i in range(len(origList)):
    y = numbers[i]
    ylist.append(y)
  
  plt.xlabel('x')
  plt.ylabel('y')
  plt.plot(ylist)
  plt.show()
  
numbers = []

for i in range(rand.randint(1, 10)):                             # Change these numbers to decide how big the list is
  numbers.append(rand.randint(-100, 100))
print("Original list: " + str(numbers))

numbers = sortList(numbers)
print("Sorted list: " + str(numbers))

numbers = reverseList(numbers)
print("Reversed list: " + str(numbers))
numbers = reverseList(numbers)

total = sumList(numbers)
print("Sum: " + str(total))

listRange = rangeList(numbers)
print("Range: " + str(listRange))

average = averageList(numbers, total)
print("Average (Mean): " + str(average))

median = medianList(numbers)
print("Median: " + str(median))

mode = modeList(numbers)
print("Mode: " + str(mode))

drawGraph(numbers)
