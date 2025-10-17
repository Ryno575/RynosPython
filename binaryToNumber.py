# Binary to Number
### DESCRIPTION ###
### A short program that turns a user's inputted string of 0s and 1s into decimal format ###

def toNum(binaryString):                 ### Turns the number from binary to decimal
    total = 0
    for i in range(1, len(binaryString) + 1):   ### Goes through the length of string starting at
        if (int(binaryString[-i]) == 1):        ### the end of the string and for every '1' that it finds
            total += 2**(i-1)                   ### the total will increment by 2^(i-1)
    return total

def validNum(binaryString):               ### Makes sure that there is only 1s and 0s in the string
    for i in binaryString:                ### Otherwise returns False, user has to put in new string
        try:
            if int(i) > 1 or int(i) < 0:
                return False
        except:
            return False
    return True

while True:
    binaryString = str(input("Enter a binary number using 0s and 1s: "))
    validity = validNum(binaryString)    ### Checks to see if the user only put in 1s and 0s
    if validity == True:                 ### If the user only put in 1s and 0s -> turns the binary string into decimal form
        break
    else:
        print("Please make sure you only use 0s and 1s!") 
        print("")

print("")
print("Binary Number: " + binaryString)                 ### EXAMPLE: 10000011
print("Decimal Number: " + str(toNum(binaryString)))    ### EXAMPLE: 131
