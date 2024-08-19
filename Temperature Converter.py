# Temperature Converter
f = 0
c = 0
k = 0
reset = True

# Defines the conversion functions
def fahrenheit_conversion():
    global f
    global c
    global k

    c = (f - 32) * (5/9)
    k = c + 273.15

def celcius_conversion():
    global f
    global c
    global k

    f = (c * (9/5)) + 32
    k = c + 273.15

def kelvin_conversion():
    global f
    global c
    global k

    f = (k - 273.15) * (9/5) + 32
    c = k - 273.15

# Begins reset loop    
while reset == True:
# Asks the user what they want to start with
    while True:
        temp_option = input("What temp setting would you like to convert from? F, C, or K: ")
        print("")
        if temp_option == "F":
            print("You have chosen Fahrenheit!")
            break
        elif temp_option == "C":
            print("You have chosen Celcius!")
            break
        elif temp_option == "K":
            print("You have chosen Kelvin!")
            break
        else:
            print("Please enter F, C, or K")

# Asks the user what they want to convert to
    while True:
        print("")
        convert_option = input("What temp setting would you like to convert to? F, C, K, or all: ")
        print("")
        if convert_option == temp_option:
            print("You have already chosen: ", temp_option, " Please choose a different option!")
        elif convert_option == "F":
            print("You have chosen Fahrenheit!")
            break
        elif convert_option == "C":
            print("You have chosen Celcius!")
            break
        elif convert_option == "K":
            print("You have chosen Kelvin!")
            break
        elif convert_option == "all":
            print("You have chosen Fahrenheit, Celcius and Kelvin!")
            break
        else:
            print("Please enter F, C, K, or all")
            break

# Asks the user what the temp is in there chosen option, converts it
    if temp_option == "F":
        f = float(input("What is the degrees in Fahrenheit: "))
        fahrenheit_conversion()

    elif temp_option == "C":
        c = float(input("What is the degrees in Celcius: "))
        celcius_conversion()

    elif temp_option == "K":
        k = float(input("What is the degrees in Kelvin: "))
        kelvin_conversion()

# Takes the users temp option and converts to their convert option
    if temp_option == "F":
        if convert_option == "C":
            print("Fahrenheit: ", f)
            print("Celcius: ", c)

        elif convert_option == "K":
            print("Fahrenheit: ", f)
            print("Kelvin: ", k)
        
        elif convert_option == "all":
            print("Fahrenheit: ", f)
            print("Celcius: ", c)
            print("Kelvin: ", k)

    elif temp_option == "C":
        if convert_option == "F":
            print("Celcius: ", c)
            print("Fahrenheit: ", f)
        
        elif convert_option == "K":
            print("Celcius: ", c)
            print("Kelvin: ", k)

        elif convert_option == "all":
            print("Celcius: ", c)
            print("Fahrenheit: ", f)
            print("Kelvin: ", k)

    elif temp_option == "K":
        if convert_option == "F":
            print("Kelvin: ", k)
            print("Fahrenheit: ", f)

        elif convert_option == "C":
            print("Kelvin: ", k)
            print("Celcius: ", c)

        elif convert_option == "all":
            print("Kelvin: ", k)
            print("Celcius: ", c)
            print("Fahrenheit: ", f)

    reset = input("Would you like to reset? Y or N: ")
    if reset == "Y":
        reset = True
    else:
        reset = False

print("Goodbye!")