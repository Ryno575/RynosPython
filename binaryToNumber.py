# Binary to Number

def toNum(binaryString):                 ### Turns the number from binary to decimal
    total = 0
    for i in range(len(binaryString) + 1):
        if i == 0:
            continue
        if (int(binaryString[-i]) == 1):
            total += 2**(i-1)
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
    validity = validNum(binaryString)
    if validity == True:
        break
    else:
        print("Please make sure you only use 0s and 1s!")
        print("")

print("")
print("Binary Number: " + binaryString)
print("Decimal Number: " + str(toNum(binaryString)))
