# Temperature Converter
reset = True

# Defines the conversion functions
def fahrenheit_conversion(f, c=0, k=0):
    c = (f - 32) * (5/9)
    k = c + 273.15
    return c,k

def celcius_conversion(c, f=0, k=0):
    f = (c * (9/5)) + 32
    k = c + 273.15
    return f,k

def kelvin_conversion(k, f=0, c=0):
    f = (k - 273.15) * (9/5) + 32
    c = k - 273.15
    return f,c

# Begins reset loop    
while reset == True:
# Asks the user what they want to start with
    while True:
        temp_option = input("What temp setting would you like to convert from? F, C, or K: ")
        print("")
        if temp_option.lower() == "f":
            print("You have chosen Fahrenheit!")
            break
        elif temp_option.lower() == "c":
            print("You have chosen Celcius!")
            break
        elif temp_option.lower() == "k":
            print("You have chosen Kelvin!")
            break
        else:
            print("Please enter F, C, or K")

# Asks the user what they want to convert to
    while True:
        print("")
        convert_option = input("What temp setting would you like to convert to? F, C, K, or all: ")
        print("")
        if convert_option.lower() == temp_option.lower():
            print("You have already chosen: ", temp_option.upper(), " Please choose a different option!")
        elif convert_option.lower() == "f":
            print("You have chosen Fahrenheit!")
            break
        elif convert_option.lower() == "c":
            print("You have chosen Celcius!")
            break
        elif convert_option.lower() == "k":
            print("You have chosen Kelvin!")
            break
        elif convert_option.lower() == "all":
            print("You have chosen Fahrenheit, Celcius and Kelvin!")
            break
        else:
            print("Please enter F, C, K, or all")
            break

# Asks the user what the temp is in there chosen option, converts it
    if temp_option.lower() == "f":
        f = float(input("What is the degrees in Fahrenheit: "))
        c,k = fahrenheit_conversion(f)

    elif temp_option.lower() == "c":
        c = float(input("What is the degrees in Celcius: "))
        f,k = celcius_conversion(c)

    elif temp_option.lower() == "k":
        k = float(input("What is the degrees in Kelvin: "))
        f,c = kelvin_conversion(k)

# Takes the users temp option and converts to their convert option
    if temp_option.lower() == "f":
        if convert_option.lower() == "c":
            print("Fahrenheit: ", f)
            print("Celcius: ", c)

        elif convert_option.lower() == "k":
            print("Fahrenheit: ", f)
            print("Kelvin: ", k)
        
        elif convert_option.lower() == "all":
            print("Fahrenheit: ", f)
            print("Celcius: ", c)
            print("Kelvin: ", k)

    elif temp_option.lower() == "c":
        if convert_option.lower() == "f":
            print("Celcius: ", c)
            print("Fahrenheit: ", f)
        
        elif convert_option.lower() == "k":
            print("Celcius: ", c)
            print("Kelvin: ", k)

        elif convert_option.lower() == "all":
            print("Celcius: ", c)
            print("Fahrenheit: ", f)
            print("Kelvin: ", k)

    elif temp_option.lower() == "k":
        if convert_option.lower() == "f":
            print("Kelvin: ", k)
            print("Fahrenheit: ", f)

        elif convert_option.lower() == "c":
            print("Kelvin: ", k)
            print("Celcius: ", c)

        elif convert_option.lower() == "all":
            print("Kelvin: ", k)
            print("Celcius: ", c)
            print("Fahrenheit: ", f)

    reset = input("Would you like to reset? Y or N: ")
    if reset.lower() == "y":
        reset = True
    else:
        reset = False

print("Goodbye!")
